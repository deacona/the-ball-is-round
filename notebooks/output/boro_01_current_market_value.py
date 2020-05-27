#!/usr/bin/env python
# coding: utf-8

# # Boro Player Predictions - Current Market Value

# ## 0. Setup

# In[4]:


## standard library
import os
import re
import pickle
import shutil


# In[7]:


## data wrangling
import numpy as np
import pandas as pd


# In[8]:


## visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns
sns.set()


# In[9]:


## machine learning
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.utils import resample


# In[10]:


## project src


# In[11]:


## global constants
RANDOM_STATE = 4


# ## 1. Problem Definition
# 
# * Determine Busines Objectives
# * Situation Assessment
# * Determine Data Mining Goal
# * Produce Project Plan

# The aim of this project is to see if we can use data on players at Middlesbrough Football Club to make preditions about the player's and the team's current and future performance.
# 
# We have player data from Transfermarkt, ESPN, WhoScored and Fly Me To The Moon (fanzine).
# 
# "Performance" could be measured in many different ways: Results on the pitch, market value, fan popularity, churn, ...

# ## 2. Data Understanding
# 
# * Collect Initial Data
# * Describe Data
# * Explore Data
# * Verify Data Quality

# The first part of the data we'll look at is some general information on players, including their market value, as taken from Transfermarkt

# In[12]:


def extract_season(file_name):
    """
    INPUT:
        file_name - String containing name of the data source file
        
    OUTPUT:
        season_out - String containing the formated label for the season
    """
    
    season_part = file_name.split(".")[0].split("_")[-1]
    season_out = season_part[:2] + "/" + season_part[-2:]
    
    return season_out

# extract_season?


# In[13]:


extract_season("tmk_cnt_mbr_all_0910.csv")


# In[14]:


def clean_data(source_name):
    """
    INPUT:
        source_name - String containing name of the data source
        
    OUTPUT:
        tmk_df - Dataframe containing the cleaned data
    """

    dir_tmk_cnt = "../data/raw/tmk/tmk_cnt/"
    data_list = []
    for file in os.listdir(dir_tmk_cnt):
        filepath = os.path.join(dir_tmk_cnt, file)
        print(filepath)
        tmp = pd.read_csv(filepath, encoding='latin-1', header=0, 
                          names=["Shirt number", "Position", "Name", "Date of birth", "Nationality",
                                "Height", "Foot", "Joined", "Signed from", "Contract expires",
                                "Market value"])
        tmp["Season"] = extract_season(file)
        data_list.append(tmp)

    tmk_df = pd.concat(data_list, axis=0, sort=False, ignore_index=True)

    tmk_df["Name"].fillna(method="bfill", inplace=True)

    tmk_df["Position"] = tmk_df.Name.shift(-1)
    tmk_df.loc[tmk_df.Position == tmk_df.Name, "Position"] = tmk_df.Name.shift(-2)

    tmk_df.drop(axis=1, columns=["Nationality", "Signed from"], inplace=True)

    tmk_df.dropna(subset=["Market value"], inplace=True)

    tmk_df = tmk_df.replace('-', np.nan)

    tmk_df["Shirt number"] = pd.to_numeric(tmk_df["Shirt number"], downcast='integer')

    tmk_df["Position group"] = None
    tmk_df.loc[(tmk_df.Position.str.upper().str.contains("KEEPER"))
            | (tmk_df.Position.str.upper().str.contains("GOAL")), 
           "Position group"] = "G"
    tmk_df.loc[(tmk_df.Position.str.upper().str.contains("BACK"))
            | (tmk_df.Position.str.upper().str.contains("DEF")), 
           "Position group"] = "D"
    tmk_df.loc[(tmk_df.Position.str.upper().str.contains("MID"))
            | (tmk_df.Position.str.upper().str.contains("MIT"))
            | (tmk_df.Position.str.upper().str.contains("WING")), 
           "Position group"] = "M"
    tmk_df.loc[(tmk_df.Position.str.upper().str.contains("STRIKER"))
            | (tmk_df.Position.str.upper().str.contains("FORW")), 
           "Position group"] = "F"

    tmk_df["Age"] = tmk_df["Date of birth"].str.extract(r".*([0-9]{2})", expand=False).astype("int")

    tmk_df["Date of birth"] = pd.to_datetime(
        tmk_df["Date of birth"].str.extract(r"(.*) \([0-9]{2}\)", expand=False), 
        format="%b %d, %Y")

    tmk_df["Joined"] = pd.to_datetime(tmk_df.Joined, format="%b %d, %Y")

    tmk_df["Contract expires"] = pd.to_datetime(tmk_df["Contract expires"], format="%d.%m.%Y")

    tmk_df["Height"] = (tmk_df["Height"]                               .str.strip()                               .str.replace(' ', '')                               .str.replace(',', '')                               .str.replace('m', '')                               .replace({'-':np.nan, '':np.nan})                               .astype(float))
    tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Height.notna()].Name.values)
           & tmk_df.Name.isin(tmk_df[tmk_df.Height.isna()].Name.values), "Height"] = \
    tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Height.notna()].Name.values)
           & tmk_df.Name.isin(tmk_df[tmk_df.Height.isna()].Name.values)] \
        .sort_values(by=["Name", "Season"]).Height.fillna(method="bfill")
    
    tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Foot.notna()].Name.values)
           & tmk_df.Name.isin(tmk_df[tmk_df.Foot.isna()].Name.values), "Foot"] = \
    tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Foot.notna()].Name.values)
           & tmk_df.Name.isin(tmk_df[tmk_df.Foot.isna()].Name.values)] \
        .sort_values(by=["Name", "Season"]).Foot.fillna(method="bfill")

    tmk_df["Market value"] = (tmk_df["Market value"]                               .str.strip()                               .replace({'-':np.nan})                               .replace(r'[£km]', '', regex=True)                               .astype(float) *                 tmk_df["Market value"].str.extract(r'[\d\.]+([km]+)', expand=False)
                    .fillna(1)
                    .replace(['k','m'], [10**3, 10**6]).astype(int) / 10**6)

    return tmk_df

# clean_data?


# In[15]:


tmk_df = clean_data("tmk_cnt")
# tmk_df.info()


# In[16]:


tmk_df.sample(8, random_state=RANDOM_STATE)


# In[17]:


tmk_df.describe(include="all")


# **ANALYSIS** So the data is looking broadly in good shape, but there are a few missing values to consider...

# In[18]:


tmk_df.count() / tmk_df.shape[0]


# **ANALYSIS** Only `Joined` has large gaps. Let's look at it in more detail...

# In[19]:


tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Joined.notna()].Name.values)
       & tmk_df.Name.isin(tmk_df[tmk_df.Joined.isna()].Name.values)].sort_values(by=["Name", "Season"])


# **ANALYSIS** _Possibly_ we could back fill some missing `Joined` dates but this might have some downstream consequences because the date will be at the end of that season. We'll leave them as Nulls for now.

# Next we'll look at the distributions of single fields with bar charts for categorical variables and histograms for numeric and date variables

# In[20]:


tmk_df["Position group"].value_counts().plot(kind='bar')


# In[21]:


tmk_df.Foot.fillna("unknown").value_counts().plot(kind='bar')


# In[22]:


tmk_df.Season.value_counts().sort_index().plot(kind='bar')


# In[23]:


tmk_df["Shirt number"].hist(bins=42)


# In[24]:


tmk_df["Age"].hist(bins=25)


# In[25]:


tmk_df["Height"].hist()


# In[26]:


tmk_df["Date of birth"].hist()


# In[27]:


tmk_df["Joined"].hist()


# In[28]:


tmk_df["Contract expires"].hist()


# In[29]:


tmk_df["Market value"].hist()


# We can explore simple relationships between variables using pairplots and histogram facet grids

# In[30]:


sns.pairplot(tmk_df)


# In[31]:


sns.pairplot(tmk_df, hue="Position group")


# In[32]:


sns.pairplot(tmk_df, hue="Foot")


# In[33]:


grid = sns.FacetGrid(tmk_df, row="Position group", col="Foot", margin_titles=True)
grid.map(plt.hist, "Market value", bins=20)


# In[ ]:





# ## 3. Data Preperation
# 
# * Select Data
# * Clean Data
# * Construct Data
# * Integrate Data
# * Format Data

# In[34]:


df = tmk_df.copy()
df.shape


# In[35]:


df["Player key"] = df.Name + " (" + df.Season + ")"
df.set_index(df["Player key"], drop=True, inplace=True, verify_integrity=True)
df.drop(columns=["Player key"], inplace=True)
df.info()


# We can derive some new numeric features to express relationships between dates

# In[36]:


df["Age when joined"] = (df["Joined"] - df["Date of birth"])/ np.timedelta64(1, 'Y')
df["Age when joined"].hist()


# **ANALYSIS** Most players join in their teens or mid-twenties.

# In[37]:


df["Years in team"] = (pd.to_datetime("1st July 20"+df.Season.str[-2:]) - df["Joined"])/ np.timedelta64(1, 'Y')
df["Years in team"].hist()


# **ANALYSIS** I'm going to leave out `Shirt number`, `Position`, `Name`, `Date of birth`, `Joined`, `Season` and `Contract expires` from the model for now. `Contract expires` is populated in less than half of records. The others can be discarded for simplicity of model.

# In[38]:


df.drop(columns=["Shirt number", "Position", "Name", "Date of birth", "Joined", "Season", "Contract expires"], inplace=True)
df.shape


# `Foot` and `Position group` will be one-hot encoded 

# In[39]:


for var in ["Foot", "Position group"]:
    df = pd.concat(
        [
            df.drop(var, axis=1),
            pd.get_dummies(
                df[var], prefix=var, prefix_sep="=", drop_first=False
            ),
        ],
        axis=1,
    )

# df.describe()
df.shape


# In[40]:


df.sample(5, random_state=RANDOM_STATE)


# In[41]:


df.describe()


# In[42]:


df[df.Height.isna() | df["Age when joined"].isna() | df["Years in team"].isna()].shape


# ~~Discard a handful of rows which don't have `Height` and/or `Age when joined` and/or `Years in team`~~

# In[43]:


# df = df[df.Height.notna() & df["Age when joined"].notna() & df["Years in team"].notna()]
# df.shape


# In[44]:


# df.describe()


# In[111]:


# pd.plotting.scatter_matrix(df[["Height", "Age", "Age when joined", "Years in team", "Market value"]], figsize=(15,15));


# In[110]:


sns.pairplot(df[["Height", "Age", "Age when joined", "Years in team", "Market value"]])


# In[46]:


df.columns


# In[ ]:





# ## 4. Modelling
# 
# * Select Modelling Technique
# * Generate Test Design
# * Build Model
# * Assess Model

# In[47]:


feature_names = ['Height', 'Age', 'Age when joined', 'Years in team', 'Foot=both',
       'Foot=left', 'Foot=right', 'Position group=D', 'Position group=F',
       'Position group=G', 'Position group=M']
feature_names


# In[48]:


drop_nulls = True
drop_nulls


# In[49]:


if drop_nulls:
    X = df[df.notna().all(axis=1)][feature_names]
    y = df[df.notna().all(axis=1)]["Market value"]
else:
    X = df[feature_names]
    y = df["Market value"]
    
X.shape, y.shape


# In[50]:


X.shape[0] / (X.shape[1] ** 2)


# **ANALYSIS** 3 seems a good starting point for number of cross-validation folds

# In[51]:


number_of_folds = 3
number_of_folds


# In[52]:


X.columns


# https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

# In[53]:


model = LinearRegression() #normalize=True)
# model = LinearRegression(fit_intercept=False)
model


# In[54]:


param_grid = {"fit_intercept": [True, False],
             "normalize": [True, False],}
param_grid


# In[55]:


grid = GridSearchCV(model, param_grid, cv=number_of_folds)
grid


# In[56]:


grid.fit(X, y)


# In[57]:


grid.best_params_


# In[58]:


model = grid.best_estimator_
model


# In[59]:


for scoring in ['neg_mean_absolute_error', 'neg_mean_squared_error', 'r2']:
    results = cross_val_score(model, X, y, cv=number_of_folds, scoring=scoring)
    print("{0}: {1} ({2})".format(scoring, results.mean(), results.std()))


# In[60]:


# Create CV training and test scores for various training set sizes
train_sizes, train_scores, test_scores = learning_curve(model, 
                                                        X, 
                                                        y,
                                                        # Number of folds in cross-validation
                                                        cv=number_of_folds,
                                                        # Evaluation metric
#                                                         scoring='accuracy',
                                                        # Use all computer cores
                                                        n_jobs=-1, 
                                                        # 50 different sizes of the training set
                                                        train_sizes=np.linspace(0.1, 1.0, 50))

# Create means and standard deviations of training set scores
train_mean = np.mean(train_scores, axis=1)
train_std = np.std(train_scores, axis=1)

# Create means and standard deviations of test set scores
test_mean = np.mean(test_scores, axis=1)
test_std = np.std(test_scores, axis=1)

# Draw lines
plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

# Draw bands
plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

# Create plot
plt.title("Learning Curve")
plt.xlabel("Training Set Size"), plt.ylabel("R2 Score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()


# **ANALYSIS** The model seems pretty weak in general but we can say that 120 training samples is enough to maximise the score.

# In[61]:


optimum_training_size = 120
optimum_training_size


# In[62]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=RANDOM_STATE, train_size=optimum_training_size)
X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[63]:


model.fit(X_train, y_train)


# In[64]:


model.score(X_train, y_train)


# **ANALYSIS** An R^2 score of 0.244 isn't great - especially just on the training data - but it's a baseline. The only way is up (I Hope!) :)

# In[65]:


# Model selection - LinearRegression, Lasso, ElasticNet, RidgeRegression, SVR(kernel="linear")
# Learning curves 
# Test/train split and Cross validation
# Validation (Grid Search)
# Pipeline
# Feature scaling


# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression

# In[ ]:





# ## 5. Evaluation
# 
# * Evaluate Results
# * Review Process
# * Determine Next Steps

# In[66]:


# MSE, RMSE
# MAE
# R squared
# https://machinelearningmastery.com/metrics-evaluate-machine-learning-algorithms-python/


# In[68]:


model.score(X_test, y_test)


# **ANALYSIS** As per the training score, the test data returns a pretty poor R^2 of 0.144. Plenty to work on

# In[69]:


# model.coef_


# In[70]:


# model.intercept_


# In[71]:


sns.scatterplot(y_train, model.predict(X_train))
sns.scatterplot(y_test, model.predict(X_test))


# **ANALYSIS** Confirming our scoring visually, it looks pretty weak correlation between actual and predicted values. Note also the model is not able to predict anything much above £4m even though some of the data exceeded £10m.

# In[72]:


params = pd.Series(model.coef_, index=X.columns)
# params

np.random.seed(1)
err = np.std([model.fit(*resample(X, y)).coef_ for i in range(1000)], 0)
# err

pd.DataFrame({"effect": params.round(2), "error": err.round(2)})


# **ANALYSIS** The individual features which appear to have most effect are `Age`, `Age when joined`, `Years in team` and `Position group=G`. Perhaps the most we can say is old goalkeepers aren't worth much.

# In[ ]:





# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.PolynomialFeatures.html

# In[73]:


# def PolynomialRegression(degree=2, **kwargs):
#     return make_pipeline(PolynomialFeatures(degree),
#                         LinearRegression(**kwargs))


# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.validation_curve.html?highlight=validation_curve#sklearn.model_selection.validation_curve

# In[ ]:





# In[74]:


# degree = np.arange(0,10)
# train_score, val_score = validation_curve(PolynomialRegression(), X, y,
#                                          'polynomialfeatures__degree',
#                                          degree, cv=5)

# plt.plot(degree, np.median(train_score, 1), color="blue", label="training score")
# plt.plot(degree, np.median(val_score, 1), color="red", label="validation score")
# plt.legend(loc="best")
# plt.ylim(0, 1)
# plt.xlabel("degree")
# plt.ylabel("score");


# In[75]:


# # Create range of values for parameter
# param_range = np.arange(1, 250, 2)

# # Calculate accuracy on training and test set using range of parameter values
# train_scores, test_scores = validation_curve(RandomForestClassifier(), 
#                                              X, 
#                                              y, 
#                                              param_name="n_estimators", 
#                                              param_range=param_range,
#                                              cv=3, 
#                                              scoring="accuracy", 
#                                              n_jobs=-1)


# # Calculate mean and standard deviation for training set scores
# train_mean = np.mean(train_scores, axis=1)
# train_std = np.std(train_scores, axis=1)

# # Calculate mean and standard deviation for test set scores
# test_mean = np.mean(test_scores, axis=1)
# test_std = np.std(test_scores, axis=1)

# # Plot mean accuracy scores for training and test sets
# plt.plot(param_range, train_mean, label="Training score", color="black")
# plt.plot(param_range, test_mean, label="Cross-validation score", color="dimgrey")

# # Plot accurancy bands for training and test sets
# plt.fill_between(param_range, train_mean - train_std, train_mean + train_std, color="gray")
# plt.fill_between(param_range, test_mean - test_std, test_mean + test_std, color="gainsboro")

# # Create plot
# plt.title("Validation Curve With Random Forest")
# plt.xlabel("Number Of Trees")
# plt.ylabel("Accuracy Score")
# plt.tight_layout()
# plt.legend(loc="best")
# plt.show()


# In[76]:


# train_score


# In[77]:


# val_score


# https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.learning_curve.html

# In[78]:


# fig, ax = plt.subplots(1, 2, figsize=(16, 6))
# fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

# for i, degree in enumerate([2, 4]):
#     N, train_lc, val_lc = learning_curve(PolynomialRegression(degree),
#                                          X, y, cv=5,
#                                          train_sizes=np.linspace(0.3, 1, 25))

#     ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
#     ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
#     ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1],
#                  color='gray', linestyle='dashed')

#     ax[i].set_ylim(-0.1, 1.1)
#     ax[i].set_xlim(N[0], N[-1])
#     ax[i].set_xlabel('training size')
#     ax[i].set_ylabel('score')
#     ax[i].set_title('degree = {0}'.format(degree), size=14)
#     ax[i].legend(loc='best')


# In[ ]:





# ## 6. Deployment
# 
# * Plan Deployment
# * Plan Monitoring and Maintenance
# * Produce Final Report
# * Review Project

# In[79]:


# Fill missing values
# Any conclusions on predictions


# In[114]:


df_out = df.copy()
df_out.shape


# In[128]:


if drop_nulls:
    df_out["Market value (prediction)"] = np.NaN
    df_out.loc[df_out.notna()[feature_names].all(axis=1), "Market value (prediction)"] = model.predict(df_out[df_out.notna()[feature_names].all(axis=1)][feature_names])
else:
    df_out["Market value (prediction)"] = model.predict(df_out[feature_names])

df_out.shape


# In[129]:


df_out.describe()


# In[131]:


sns.pairplot(df_out[["Height", "Age", "Age when joined", "Years in team", "Market value", "Market value (prediction)"]])


# **ANALYSIS** As we saw during data preperation there's no clear correlations with continuous features at work. Further our predictions don't even particularly correlate with the actual values.

# In[132]:


df_unseen = df_out[df_out["Market value"].isna()]
df_unseen.shape


# In[136]:


df_unseen[df_unseen["Market value (prediction)"].notna()].describe()


# In[135]:


df_unseen[df_unseen["Market value (prediction)"].notna()]


# **ANALYSIS** The player's missing actual Market values are all young players (17-21). The predictions are typically quite small which is as expected at least. Poor Connor Ripley (11/12) gets a negative value!

# In[140]:


df_out.to_csv("../data/interim/boro_01_dataset.csv")


# In[141]:


clf_file = "../models/boro_01_model.pkl" 
with open(clf_file, "wb") as clf_outfile:
    pickle.dump(model, clf_outfile)


# In[142]:


ftn_file = "../models/boro_01_feature_names.pkl" 
with open(ftn_file, "wb") as ftn_outfile:
    pickle.dump(feature_names, ftn_outfile)


# In[ ]:


## save notebook before running `nbconvert`


# In[3]:


imageFolder = './output'
for filename in os.listdir(imageFolder):
    file_path = os.path.join(imageFolder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


# In[1]:


get_ipython().system("jupyter nbconvert --no-input --output-dir='./output' --to markdown boro_01_current_market_value.ipynb")


# In[144]:


get_ipython().system("jupyter nbconvert --output-dir='./output' --to python boro_01_current_market_value.ipynb")


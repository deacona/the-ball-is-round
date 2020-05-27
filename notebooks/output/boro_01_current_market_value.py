#!/usr/bin/env python
# coding: utf-8

# # Boro Player Predictions - Current Market Value

# ## 0. Setup

# In[1]:


## standard library
import os
import re
import pickle
import shutil


# In[2]:


## data wrangling
import numpy as np
import pandas as pd


# In[3]:


## visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")

import seaborn as sns
sns.set()


# In[4]:


## machine learning
from sklearn.model_selection import train_test_split
from sklearn.model_selection import validation_curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.utils import resample
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# In[5]:


## project src


# In[6]:


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

# In[7]:


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


# In[8]:


extract_season("tmk_cnt_mbr_all_0910.csv")


# In[9]:


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

    ## Name and Position are mis-aligned in the source files
    
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


# In[10]:


tmk_df = clean_data("tmk_cnt")
# tmk_df.info()


# In[11]:


tmk_df.sample(8, random_state=RANDOM_STATE)


# In[12]:


tmk_df.describe(include="all")


# **ANALYSIS** So the data is looking broadly in good shape, but there are a few missing values to consider...

# In[13]:


tmk_df.count() / tmk_df.shape[0]


# **ANALYSIS** Only `Joined` has large gaps. Let's look at it in more detail...

# In[14]:


tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Joined.notna()].Name.values)
       & tmk_df.Name.isin(tmk_df[tmk_df.Joined.isna()].Name.values)].sort_values(by=["Name", "Season"])


# **ANALYSIS** _Possibly_ we could back fill some missing `Joined` dates but this might have some downstream consequences because the date _might_ exceed the end of that season. We'll leave them as Nulls for now.

# Next we'll look at the distributions of single fields with bar charts for categorical variables and histograms for numeric and date variables

# In[15]:


tmk_df["Position group"].value_counts().plot(kind='bar')


# In[16]:


tmk_df.Foot.fillna("unknown").value_counts().plot(kind='bar')


# In[17]:


tmk_df.Season.value_counts().sort_index().plot(kind='bar')


# In[18]:


tmk_df["Shirt number"].hist(bins=42)


# In[19]:


tmk_df["Age"].hist(bins=25)


# In[20]:


tmk_df["Height"].hist()


# In[21]:


tmk_df["Date of birth"].hist()


# In[22]:


tmk_df["Joined"].hist()


# In[23]:


tmk_df["Contract expires"].hist()


# In[24]:


tmk_df["Market value"].hist()


# We can explore simple relationships between variables using pairplots and histogram facet grids

# In[25]:


sns.pairplot(tmk_df)


# In[26]:


sns.pairplot(tmk_df, hue="Position group")


# In[27]:


sns.pairplot(tmk_df, hue="Foot")


# In[28]:


facet_grid = sns.FacetGrid(tmk_df, row="Position group", col="Foot", margin_titles=True)
facet_grid.map(plt.hist, "Market value", bins=20)


# In[ ]:





# ## 3. Data Preperation
# 
# * Select Data
# * Clean Data
# * Construct Data
# * Integrate Data
# * Format Data

# In[29]:


df = tmk_df.copy()
df.shape


# In[30]:


df["Player key"] = df.Name + " (" + df.Season + ")"
df.set_index(df["Player key"], drop=True, inplace=True, verify_integrity=True)
df.drop(columns=["Player key"], inplace=True)
df.info()


# We can derive some new numeric features to express relationships between dates

# In[31]:


df["Age when joined"] = (df["Joined"] - df["Date of birth"])/ np.timedelta64(1, 'Y')
df["Age when joined"].hist()


# **ANALYSIS** Most players join in their teens or mid-twenties.

# In[32]:


df["Years in team"] = (pd.to_datetime("1st July 20"+df.Season.str[-2:]) - df["Joined"])/ np.timedelta64(1, 'Y')
df["Years in team"].hist()


# **ANALYSIS** I'm going to leave out `Shirt number`, `Position`, `Name`, `Date of birth`, `Joined`, `Season` and `Contract expires` from the model for now. `Contract expires` is populated in less than half of records. The others can be discarded for simplicity of model.

# In[33]:


df.drop(columns=["Shirt number", "Position", "Name", "Date of birth", "Joined", "Season", "Contract expires"], inplace=True)
df.shape


# `Foot` and `Position group` will be one-hot encoded 

# In[34]:


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


# In[35]:


df.sample(5, random_state=RANDOM_STATE)


# In[36]:


df.describe()


# In[37]:


sns.pairplot(df[["Height", "Age", "Age when joined", "Years in team", "Market value"]])


# In[38]:


df.columns


# In[ ]:





# ## 4. Modelling
# 
# * Select Modelling Technique
# * Generate Test Design
# * Build Model
# * Assess Model

# In[39]:


feature_names = ['Height', 'Age', 'Age when joined', 'Years in team', 'Foot=both',
       'Foot=left', 'Foot=right', 'Position group=D', 'Position group=F',
       'Position group=G', 'Position group=M']
feature_names


# In[40]:


drop_nulls = True
drop_nulls


# In[41]:


if drop_nulls:
    X = df[df.notna().all(axis=1)][feature_names]
    y = df[df.notna().all(axis=1)]["Market value"]
else:
    X = df[feature_names]
    y = df["Market value"]
    
X.shape, y.shape


# In[42]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=RANDOM_STATE, train_size=0.9)
X_train.shape, X_test.shape, y_train.shape, y_test.shape


# In[43]:


number_of_folds = 10
number_of_folds


# In[44]:


kfold = KFold(n_splits=number_of_folds, shuffle=True, random_state=RANDOM_STATE)
kfold


# In[45]:


model = LinearRegression()
model


# In[46]:


param_grid = {"fit_intercept": [True, False],
             "normalize": [True, False],}
param_grid


# In[47]:


grid = GridSearchCV(model, param_grid, cv=kfold)
grid


# In[48]:


grid.fit(X_train, y_train)


# In[49]:


grid.best_params_


# In[50]:


grid.score(X_train, y_train)


# **ANALYSIS** 0.223 isn't great - especially just on the training data - but it's a baseline. The only way is up (I Hope!) :)

# In[51]:


final_model = grid.best_estimator_
final_model


# In[52]:


final_model.fit(X_train, y_train)


# In[53]:


final_model.score(X_train, y_train)


# **ANALYSIS** 

# In[54]:


median_absolute_error(y_train, final_model.predict(X_train))


# In[55]:


mean_squared_error(y_train, final_model.predict(X_train), squared=False)


# In[56]:


r2_score(y_train, final_model.predict(X_train))


# **ANALYSIS** Baseline some other useful metrics

# In[57]:


# Create CV training and test scores for various training set sizes
train_sizes, train_scores, test_scores = learning_curve(final_model, 
                                                        X_train, 
                                                        y_train,
                                                        cv=kfold,
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
plt.xlabel("Training Set Size"), plt.ylabel("Score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()


# **ANALYSIS** The model seems pretty weak in general but we can say the learning curves have largely converged so adding extra training samples is unlikely to improve the model.

# In[ ]:





# ## 5. Evaluation
# 
# * Evaluate Results
# * Review Process
# * Determine Next Steps

# In[58]:


final_model.score(X_test, y_test)


# **ANALYSIS** As per the training score, the test data returns a pretty poor score of 0.01. Plenty to work on

# In[59]:


median_absolute_error(y_test, final_model.predict(X_test))


# In[60]:


mean_squared_error(y_test, final_model.predict(X_test), squared=False)


# In[61]:


r2_score(y_test, final_model.predict(X_test))


# **ANALYSIS** 

# In[62]:


sns.scatterplot(y_train, final_model.predict(X_train))
sns.scatterplot(y_test, final_model.predict(X_test))


# **ANALYSIS** Confirming our scoring visually, it looks pretty weak correlation between actual and predicted values. Note also the model is not able to predict anything much above £4m even though some of the data exceeded £10m.

# In[63]:


params = pd.Series(final_model.coef_, index=X.columns)
# params

np.random.seed(1)
err = np.std([final_model.fit(*resample(X, y)).coef_ for i in range(1000)], 0)
# err

pd.DataFrame({"effect": params.round(2), "error": err.round(2)})


# **ANALYSIS** The individual features which appear to have most effect are `Age`, `Age when joined`, `Years in team` and `Position group=G`. Perhaps the most we can say is old goalkeepers aren't worth much.

# In[ ]:





# ## 6. Deployment
# 
# * Plan Deployment
# * Plan Monitoring and Maintenance
# * Produce Final Report
# * Review Project

# In[64]:


df_out = df.copy()
df_out.shape


# In[65]:


if drop_nulls:
    df_out["Market value (prediction)"] = np.NaN
    df_out.loc[df_out.notna()[feature_names].all(axis=1), "Market value (prediction)"] = final_model.predict(df_out[df_out.notna()[feature_names].all(axis=1)][feature_names])
else:
    df_out["Market value (prediction)"] = final_model.predict(df_out[feature_names])

df_out.shape


# In[66]:


df_out.describe()


# In[67]:


sns.pairplot(df_out[["Height", "Age", "Age when joined", "Years in team", "Market value", "Market value (prediction)"]])


# **ANALYSIS** As we saw during data preperation there's no clear correlations with continuous features at work. Further our predictions don't even particularly correlate with the actual values.

# In[68]:


df_unseen = df_out[df_out["Market value"].isna()]
df_unseen.shape


# In[69]:


df_unseen[df_unseen["Market value (prediction)"].notna()].describe()


# In[70]:


df_unseen[df_unseen["Market value (prediction)"].notna()]


# **ANALYSIS** The player's missing actual Market values are all young players (17-21). The predictions are typically quite small which is as expected at least. Poor Connor Ripley (11/12) gets a negative value!

# In[71]:


df_out.to_csv("../data/interim/boro_01_dataset.csv")


# In[72]:


clf_file = "../models/boro_01_model.pkl" 
with open(clf_file, "wb") as clf_outfile:
    pickle.dump(final_model, clf_outfile)


# In[73]:


ftn_file = "../models/boro_01_feature_names.pkl" 
with open(ftn_file, "wb") as ftn_outfile:
    pickle.dump(feature_names, ftn_outfile)


# In[74]:


## save notebook before running `nbconvert`


# In[75]:


outFolder = './output'
for filename in os.listdir(outFolder):
    file_path = os.path.join(outFolder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


# In[76]:


get_ipython().system("jupyter nbconvert --no-input --output-dir='./output' --to markdown boro_01_current_market_value.ipynb")


# In[199]:


get_ipython().system("jupyter nbconvert --output-dir='./output' --to python boro_01_current_market_value.ipynb")


# In[ ]:





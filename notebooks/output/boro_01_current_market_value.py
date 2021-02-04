#!/usr/bin/env python
# coding: utf-8

# # Boro Player Predictions - Current Market Value
# 
# Written report for this analysis can be found [here](../reports/boro_01_market_value.md)

# In[1]:


## standard library
import os
import sys
import re
import pickle
import shutil


# In[2]:


## data wrangling
import numpy as np
import pandas as pd

pd.set_option("display.latex.repr", True)
pd.set_option('precision', 3)


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
# from sklearn.feature_selection import SelectKBest, f_regression
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import Ridge
# from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.svm import SVR
# from sklearn.utils import resample
from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.inspection import permutation_importance


# In[5]:


## project src
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../src'))
# sys.path

get_ipython().run_line_magic('load_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

# import utilities
import players


# In[6]:


## global constants
RANDOM_STATE = 4


# ## 1. Business Understanding
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

# A number of key performance metrics will be investigated in turn, looking at how predictable each is...
# 
# 1) Current market value
# 
# 2) Current fan popularity
# 
# 3) Current performance rating
# 
# ... and more TBC ...
# 

# In[ ]:





# ## 2. Data Understanding
# 
# * Collect Initial Data
# * Describe Data
# * Explore Data
# * Verify Data Quality

# In[7]:


print("Loading Transfermarkt general information...")

tmk_df = players.clean_data("tmk_cnt")
# tmk_df.info()


# In[8]:


print("Random sample of records...")

tmk_df.sample(8, random_state=RANDOM_STATE)


# In[9]:


print("Summary of whole data source...")

tmk_df.describe(include="all")


# **ANALYSIS:** So the data is looking broadly in good shape, but there are a few missing values to consider...

# In[10]:


# print("% populated...")

pd.DataFrame(100 * tmk_df.count() / tmk_df.shape[0], columns=["% populated"])


# In[11]:


print("Players with missing Joined dates...")

tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df.Joined.notna()].Name.values)
       & tmk_df.Name.isin(tmk_df[tmk_df.Joined.isna()].Name.values)].sort_values(by=["Name", "Season"])[["Name", "Season", "Joined"]].T


# In[12]:


print("Players with missing Contract expires dates...")

tmk_df.loc[tmk_df.Name.isin(tmk_df[tmk_df["Contract expires"].notna()].Name.values)
       & tmk_df.Name.isin(tmk_df[tmk_df["Contract expires"].isna()].Name.values)].sort_values(by=["Name", "Season"])[["Name", "Season", "Contract expires"]].T


# **ANALYSIS:** _Possibly_ we could back fill some missing `Joined` and `Contract expires` dates but this might have some undesired consequences because the date _might_ not be valid for that particular season. We'll leave them as Nulls for now.

# In[13]:


tmk_df["Position group"].value_counts().plot(kind='bar')
plt.title('Position group of Players')
plt.xlabel('Position group')
plt.ylabel('Number of players');


# In[14]:


tmk_df.Foot.fillna("unknown").value_counts().plot(kind='bar')
plt.title('Footedness of Players')
plt.xlabel('Foot')
plt.ylabel('Number of players');


# In[15]:


tmk_df.Season.value_counts().sort_index().plot(kind='bar')
plt.title('Players per Season')
plt.xlabel('Season')
plt.ylabel('Number of players');


# In[16]:


tmk_df["Shirt number"].hist(bins=42)
plt.title('Shirt number of Players')
plt.xlabel('Shirt number')
plt.ylabel('Number of players');


# In[17]:


tmk_df["Age"].hist(bins=25)
plt.title('Age of Players')
plt.xlabel('Age')
plt.ylabel('Number of players');


# In[18]:


tmk_df["Height"].hist()
plt.title('Height of Players')
plt.xlabel('Height')
plt.ylabel('Number of players');


# In[19]:


tmk_df["Date of birth"].hist()
plt.title('Date of birth of Players')
plt.xlabel('Date of birth')
plt.ylabel('Number of players');


# In[20]:


tmk_df["Joined"].hist()
plt.title("Players' Joined date")
plt.xlabel('Joined date')
plt.ylabel('Number of players');


# In[21]:


tmk_df["Contract expires"].hist()
plt.title("Players' Contract expiry date")
plt.xlabel('Contract expires')
plt.ylabel('Number of players');


# In[22]:


tmk_df["Market value"].hist()
plt.title("Market value of Players")
plt.xlabel('Market value')
plt.ylabel('Number of players');


# In[23]:


g = sns.pairplot(tmk_df)
g.fig.suptitle("Pair plots of Shirt number, Height, Market value and Age", y=1.08);


# In[24]:


g = sns.pairplot(tmk_df, hue="Position group")
g.fig.suptitle("Pair plots of Shirt number, Height, Market value and Age grouped by Position group", y=1.08);


# In[25]:


g = sns.pairplot(tmk_df, hue="Foot")
g.fig.suptitle("Pair plots of Shirt number, Height, Market value and Age grouped by Foot", y=1.08);


# In[ ]:





# In[ ]:





# In[ ]:





# In[26]:


print("Loading Transfermarkt performance summary...")

# import players
# psm_df = utilities.folder_loader("tmk_psm", ["Shirt number", "Position", "Name", "Age", "Nationality",
#                                 "In squad", "Appearances", "Goals", "Assists", 
#                                     "Yellow cards", "Second yellow cards", "Red cards",
#                                    "Substitutions on", "Substitutions off", "PPG", "Minutes played"])

psm_df = players.clean_data("tmk_psm")
# psm_df.info()


# In[27]:


print("Random sample of records...")

psm_df.sample(8, random_state=RANDOM_STATE)


# In[28]:


print("Summary of whole data source...")

psm_df.describe(include="all")


# **ANALYSIS:** So the data is looking broadly in good shape

# In[29]:


psm_df["Position group"].value_counts().plot(kind='bar')
plt.title('Position group of Players')
plt.xlabel('Position group')
plt.ylabel('Number of players');


# In[30]:


psm_df.Competition.value_counts().plot(kind='bar')
plt.title('Players per Competition')
plt.xlabel('Competition')
plt.ylabel('Number of players');


# In[31]:


psm_df.Season.value_counts().sort_index().plot(kind='bar')
plt.title('Players per Season')
plt.xlabel('Season')
plt.ylabel('Number of players');


# In[32]:


psm_df["Shirt number"].hist(bins=42)
plt.title('Shirt number of Players')
plt.xlabel('Shirt number')
plt.ylabel('Number of players');


# In[33]:


psm_df["Age"].hist(bins=25)
plt.title('Age of Players')
plt.xlabel('Age')
plt.ylabel('Number of players');


# In[34]:


g = sns.pairplot(psm_df[["In squad", "Goals", "Assists", 
            "Yellow cards", #"Second yellow cards", "Red cards",
            "PPG", "Minutes played"]])
g.fig.suptitle("Pair plots of usage, goals, assists, yellow cards, PPG", y=1.08);


# In[35]:


g = sns.pairplot(psm_df[["In squad", "Goals", "Assists", 
            "Yellow cards", #"Second yellow cards", "Red cards",
            "PPG", "Minutes played", "Position group"]], hue="Position group")
g.fig.suptitle("Pair plots of usage, goals, assists, yellow cards, PPG by Position group", y=1.08);


# In[36]:


g = sns.pairplot(psm_df[["In squad", "Goals", "Assists", 
            "Yellow cards", #"Second yellow cards", "Red cards",
            "PPG", "Minutes played", "Competition"]], hue="Competition")
g.fig.suptitle("Pair plots of usage, goals, assists, yellow cards, PPG by Competition", y=1.08);


# In[ ]:





# In[ ]:





# ## 3. Data Preperation
# 
# * Select Data
# * Clean Data
# * Construct Data
# * Integrate Data
# * Format Data

# In[37]:


df = tmk_df.copy()
# df.shape

df["Player key"] = df.Name + " (" + df.Season + ")"
df.set_index(df["Player key"], drop=True, inplace=True, verify_integrity=True)
df.drop(columns=["Player key"], inplace=True)

print("Final dataset created with index from {0} to {1}.".format(df.index[0], df.index[-1]))


# In[38]:


df["Age when joined"] = (df["Joined"] - df["Date of birth"])/ np.timedelta64(1, 'Y')
df["Age when joined"].hist()
plt.title("Players' Age when joined")
plt.xlabel('Age when joined')
plt.ylabel('Number of players');


# **ANALYSIS:** Most players join in their teens or mid-twenties.

# In[39]:


df["Years in team"] = (pd.to_datetime("1st July 20"+df.Season.str[-2:]) - df["Joined"])/ np.timedelta64(1, 'Y')
df["Years in team"].hist()
plt.title("Players' Years in team")
plt.xlabel('Years in team')
plt.ylabel('Number of players');


# **ANALYSIS:** I'm going to leave out `Position`, `Date of birth`, `Joined`, and `Contract expires` from the model for now. `Contract expires` is populated in less than half of records. The others are encoded in derived features now.

# In[40]:


df.drop(columns=["Position", "Name", "Date of birth", "Joined", "Season", "Contract expires"], inplace=True)
# df.shape


# <s>**ANALYSIS:** `Foot` and `Position group` will be one-hot encoded</s>

# In[41]:


# for var in ["Foot", "Position group"]:
#     df = pd.concat(
#         [
#             df.drop(var, axis=1),
#             pd.get_dummies(
#                 df[var], prefix=var, prefix_sep="=", drop_first=False
#             ),
#         ],
#         axis=1,
#     )

# df.describe()
# df.shape


# In[42]:


psm_df.columns


# In[43]:


def psm_agg(x):
    d = {}
    
    d["Shirt number"] = x["Shirt number"].max()
    d["Age"] = x["Age"].max()
    d["Position group"] = x["Position group"].max()
    
    d["Competition"] = x["Competition"].agg(lambda a: ', '.join(a.sort_values()))
    
    d["In squad"] = x["In squad"].sum()
    d["Games started"] = x["Games started"].sum()
    d["Goals"] = x["Goals"].sum()
    d["Assists"] = x["Assists"].sum()
    d["Yellow cards"] = x["Yellow cards"].sum()
    d["Second yellow cards"] = x["Second yellow cards"].sum()
    d["Red cards"] = x["Red cards"].sum()
    d["Substitutions on"] = x["Substitutions on"].sum()
    d["Substitutions off"] = x["Substitutions off"].sum()
    d["Minutes played"] = x["Minutes played"].sum()
    
    x["Appearances"] = x["Games started"] + x["Substitutions on"]
    d["Appearances"] = x["Appearances"].sum()
    
    d["PPG"] = ((x["PPG"] * x["Appearances"]).sum() / x["Appearances"].sum())
    
    d["Goals p90"] = x["Goals"].sum() * 90 / x["Minutes played"].sum()
    d["Assists p90"] = x["Assists"].sum() * 90 / x["Minutes played"].sum()
    d["Yellow cards p90"] = x["Yellow cards"].sum() * 90 / x["Minutes played"].sum()
    
    return pd.Series(d, index=["Shirt number", "Age", "Position group", "Competition",
                                "In squad", "Appearances", "Games started", 
                               "Goals", "Assists", 
                                    "Yellow cards", "Second yellow cards", "Red cards",
                                   "Substitutions on", "Substitutions off", "PPG", "Minutes played",
                              "Goals p90", "Assists p90", "Yellow cards p90"])

get_ipython().run_line_magic('pinfo', 'psm_agg')


# In[44]:


df2 = psm_df.groupby(["Name", "Season"]).apply(psm_agg).fillna(0)
df2.reset_index(inplace=True)
df2["Player key"] = df2.Name + " (" + df2.Season + ")"
df2.set_index(df2["Player key"], drop=True, inplace=True, verify_integrity=True)
df2.drop(columns=["Player key", "Name", "Season"], inplace=True)

# df = pd.concat([df, df2], axis=1)
df = df.combine_first(df2)


# In[ ]:





# In[45]:


print("Random sample of records...")

df.sample(5, random_state=RANDOM_STATE)


# In[46]:


print("Summary of whole dataset...")

df.describe(include="all")


# In[47]:


df.Competition.value_counts().plot(kind="bar")
plt.title("Players' Competitions involved in")
plt.xlabel('Competitions involved in')
plt.ylabel('Number of players');


# In[48]:


# g = sns.pairplot(df[["Shirt number", "Height", "Age", "Age when joined", "Years in team", "Market value"]])
# g.fig.suptitle("Pair plots of Shirt number, Height, Age, Age when joined, Years in team and Market value", y=1.08);

df.corr().style.background_gradient(cmap='coolwarm')

# sns.heatmap(df.corr(), 
#             xticklabels=df.columns.values,
#             yticklabels=df.columns.values)


# **ANALYSIS**: I'll remove `Games started` and `Age when joined` as they are closely correlated with other features.

# In[49]:


df.columns


# In[50]:


df.shape


# In[ ]:





# ## 4. Modelling
# 
# * Select Modelling Technique
# * Generate Test Design
# * Build Model
# * Assess Model

# In[51]:


numeric_features = ['Shirt number', 
                'Height', 'Age', #'Age when joined', 
                    'Years in team', 
                    'In squad', 'Appearances', #'Games started', 
                    'Substitutions on', 'Substitutions off', 
                    'Goals', 'Assists', 
                    'Yellow cards', 'Second yellow cards', 'Red cards', 
                    'PPG', 'Minutes played',
                   'Goals p90', 'Assists p90', 'Yellow cards p90']

print("\n")
print("Selected numeric features are: {0}".format(numeric_features))


# In[52]:


categorical_features = ['Foot', 'Position group', 'Competition']

print("\n")
print("Selected categorical features are: {0}".format(categorical_features))


# In[53]:


feature_names = numeric_features + categorical_features

# print("\n")
# print("Selected features are: {0}".format(feature_names))


# In[54]:


drop_nulls = False

print("\n")
print("Dropping nulls during data preparation: {0}".format(drop_nulls))


# In[55]:


if drop_nulls:
    X = df[df.notna().all(axis=1)][feature_names]
    y = df[df.notna().all(axis=1)]["Market value"]
else:
    X = df[df["Market value"].notna()][feature_names]
    y = df[df["Market value"].notna()]["Market value"]
    
# X.shape, y.shape


# In[56]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=RANDOM_STATE, train_size=0.9)

# X_train.shape, X_test.shape, y_train.shape, y_test.shape
print("\n")
print("Train data has shape: {0}".format(X_train.shape))
print("Test data has shape: {0}".format(X_test.shape))


# In[57]:


number_of_folds = 10
# number_of_folds


# In[58]:


kfold = KFold(n_splits=number_of_folds, shuffle=True, random_state=RANDOM_STATE)
# kfold


# In[ ]:





# In[59]:


numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', MinMaxScaler())])

categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

model = Pipeline(steps=[('preprocessor', preprocessor),
#                         ('basis', PolynomialFeatures()),
#                         ('reduction', SelectKBest(f_regression)),
                      ('estimator', GradientBoostingRegressor())])


# In[60]:


param_grid = {
#             "reduction__k": [5, 10, 15],
#             "estimator__n_estimators": [10, 20, 30],
#              "estimator__max_depth": [1, 3, 5],
#              "estimator__min_samples_split": [0.1, 0.2, 0.3],
#               "estimator__max_features": ["auto", "sqrt", "log2"],
              "estimator__random_state": [RANDOM_STATE],
#             "estimator__kernel": ['linear'] #, 'poly', 'rbf', 'sigmoid', 'precomputed']
#             "estimator__gamma": ["scale", "auto"]
             }
# param_grid


# In[61]:


grid = GridSearchCV(model, param_grid, cv=kfold)
# grid


# In[62]:


print("\n")
print("Full model grid-space to tune hyperparameters across...")
grid.fit(X_train, y_train)


# In[63]:


# grid.best_params_


# In[64]:


final_model = grid.best_estimator_
# final_model


# In[65]:


print("\n")
print("Final tuned model...")
final_model.fit(X_train, y_train)


# In[ ]:





# ## 5. Evaluation
# 
# * Evaluate Results
# * Review Process
# * Determine Next Steps

# In[66]:


def model_scores(y_act, y_pred):
    """
    INPUT:
        y_act - Actual values from target vector
        y_pred - Predicted values from target vector
        
    OUTPUT:
        Dictionary containing multiple scoring metrics with nice labels as keys
    """
    
    return {"MedAE": median_absolute_error(y_act, y_pred),
            "RMSE": mean_squared_error(y_act, y_pred, squared=False),
            "R^2": r2_score(y_act, y_pred),
           }

# model_scores?


# In[67]:


print("Model scores")

pd.DataFrame(
    [model_scores(y_train, final_model.predict(X_train)), 
    model_scores(y_test, final_model.predict(X_test))], 
    index=["Train", "Test"]
    ).T


# **ANALYSIS:** Switching from random forest to gradient boost has improved the training scores further... but the test scores are (arguably) slightly worse.

# In[68]:


# Create CV training and test scores for various training set sizes
train_sizes, train_scores, test_scores = learning_curve(final_model, 
                                                        X, 
                                                        y,
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
plt.title("Learning curve")
plt.xlabel("Training set size"), plt.ylabel("R^2 score"), plt.legend(loc="best")
plt.tight_layout()
plt.show()


# **ANALYSIS:** Scores are converging slowly now so more data could well help.

# In[69]:


sns.scatterplot(y_train, final_model.predict(X_train))
sns.scatterplot(y_test, final_model.predict(X_test))

mv_range = [y.min(), y.max()]
plt.plot(mv_range, mv_range, '--r')
plt.title('Actual vs Predicted Market value')
plt.xlabel('Market value (actual)')
plt.ylabel('Market value (predicted)');


# **ANALYSIS:** Our predictions are still undershooting in general but the training data is getting very close (overfitting?)

# In[70]:


# transformed_features = list(numeric_features) \
#     + final_model['preprocessor'].transformers_[1][1]['onehot']\
#                          .get_feature_names(categorical_features).tolist()
# transformed_features


# In[71]:


def show_significant_features(features, labels):
    r = permutation_importance(final_model, features, labels,
                            n_repeats=30,
                            random_state=RANDOM_STATE)

    for i in r.importances_mean.argsort()[::-1]:
        if r.importances_mean[i] - 2 * r.importances_std[i] > 0:
            print("{0} {1:.3f} +/- {2:.3f}".format(feature_names[i].ljust(20), 
#                                                 transformed_features[i].ljust(20), 
                                                    r.importances_mean[i],
                                                    r.importances_std[i]))

get_ipython().run_line_magic('pinfo', 'show_significant_features')


# In[72]:


print("\nSignificant training features:")
show_significant_features(X_train, y_train)

print("\nSignificant testing features:")
show_significant_features(X_test, y_test)


# **ANALYSIS:** `Minutes played`, `Goals`, `Appearances`, `Age`, `Position group` and `In squad` are particularly influencing the model. Of those, only `In squad` - along with `Yellow cards` and `Assists` - are generalising to new predictions.

# In[ ]:





# ## 6. Deployment
# 
# * Plan Deployment
# * Plan Monitoring and Maintenance
# * Produce Final Report
# * Review Project

# In[73]:


df_out = df.copy()
# df_out.shape


# In[74]:


if drop_nulls:
    df_out["Market value (prediction)"] = np.NaN
    df_out.loc[df_out.notna()[feature_names].all(axis=1), "Market value (prediction)"] = final_model.predict(df_out[df_out.notna()[feature_names].all(axis=1)][feature_names])
else:
    df_out["Market value (prediction)"] = final_model.predict(df_out[feature_names])

# df_out.shape


# In[75]:


print("Summary of whole dataset (with predictions)...")

df_out.describe(include="all")


# In[76]:


df_unseen = df_out[df_out["Market value"].isna()]
# df_unseen.shape


# In[77]:


print("Summary of unseen records in dataset (no labels)...")

df_unseen[df_unseen["Market value (prediction)"].notna()].describe(include="all")


# **ANALYSIS:** The player's missing actual Market values are mostly young players who haven't been used much.

# In[78]:


print("Predictions below zero")

df_unseen[df_unseen["Market value (prediction)"] < 0.0].describe(include="all")
# pd.DataFrame(df_unseen.loc['Connor Ripley (11/12)'])


# **ANALYSIS:** The model seems to particularly struggle with young players who we don't have much information about.

# In[79]:


df_out.to_csv("../data/interim/boro_01_dataset.csv")


# In[80]:


clf_file = "../models/boro_01_model.pkl" 
with open(clf_file, "wb") as clf_outfile:
    pickle.dump(final_model, clf_outfile)


# In[81]:


ftn_file = "../models/boro_01_feature_names.pkl" 
with open(ftn_file, "wb") as ftn_outfile:
    pickle.dump(feature_names, ftn_outfile)


# In[82]:


## save notebook before running `nbconvert`


# In[83]:


# outFolder = './output'
# for filename in os.listdir(outFolder):
#     file_path = os.path.join(outFolder, filename)
#     try:
#         if os.path.isfile(file_path) or os.path.islink(file_path):
#             os.unlink(file_path)
#         elif os.path.isdir(file_path):
#             shutil.rmtree(file_path)
#     except Exception as e:
#         print('Failed to delete %s. Reason: %s' % (file_path, e))


# In[84]:


# !jupyter nbconvert --no-input --output-dir='./output' --to markdown boro_01_current_market_value.ipynb


# In[85]:


# !jupyter nbconvert --output-dir='./output' --to python boro_01_current_market_value.ipynb


# In[ ]:





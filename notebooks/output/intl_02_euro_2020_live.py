#!/usr/bin/env python
# coding: utf-8

# # Euro 2020 (2021) Predictions
# 
# <!-- Written report for this analysis can be found [here](../reports/boro_01_market_value.md) -->

# ## 1. Business Understanding
# 
# * Determine Busines Objectives
# * Situation Assessment
# * Determine Data Mining Goal
# * Produce Project Plan

# ```
# # 1. Predict results of every match at Euro 2020
# # 2. Make predictions before each round of competition
# # 3. Ideally, at each round, use the predictions to simulate remainder of competition
# # 4. Check against other predictions and actual results
# # 5. Write up process (report/blog)
# ```

# ## 2. Data Understanding
# 
# * Collect Initial Data
# * Describe Data
# * Explore Data
# * Verify Data Quality

# In[1]:


import pandas as pd
import os
import numpy as np
import pickle

import matplotlib.pyplot as plt
plt.style.use("seaborn-whitegrid")
import seaborn as sns
sns.set()

import src.utilities as utilities


# In[2]:


match = utilities.get_master("nations_matches")
# match.info()

match = match[['Round', 'Day', 'Date', 'Time', 'Team_1', 'Team_2',
       'Year', 'Goals_1', 'Goals_2',
       'Goal_diff', 'Venue', 'Venue_country', 'Venue_city', 'Home_1',
       'Home_2']]

match["Goal_total"] = match.Goals_1 + match.Goals_2
match["Result"] = None
match.loc[match.Goals_1 == match.Goals_2, "Result"] = "Draw"
match.loc[match.Goals_1 > match.Goals_2, "Result"] = "Win"
match.loc[match.Goals_1 < match.Goals_2, "Result"] = "Loss"

match.describe(include="all").T


# In[3]:


def metric_histograms(df, metrics, discrete=False):
#     df = df_in.dropna(subset=[metric]).fillna("NULL")
    for metric in metrics:
        print("\n{0}\n".format(metric))
#         df[metric].hist()
        sns.histplot(data=df, x=metric, kde=True, discrete=discrete)
        plt.show()
#         sns.boxplot(x=df[metric])
#         plt.show()
        print("\n--------------------")

metric_histograms(match, ["Goals_1", "Goals_2", "Goal_diff", "Goal_total"], discrete=True)


# In[4]:


def group_boxplots(df_in, cols, metric):
    df = df_in.dropna(subset=[metric]).fillna("NULL")
    for col in cols:
        print("\n{0}\n".format(col))
        print(df[col].value_counts())
        sns.boxplot(x=col, y=metric, data=df.sort_values(by=col), 
                    showmeans=True, width=0.6)
        plt.xticks(rotation=90)

    #     plt.savefig("../reports/figures/club_01_boxplot_{0}.PNG".format(col))
        plt.show()
        print("\n--------------------")
        
col_list = ["Round", "Day", "Time", "Year", "Venue_country", "Result"]

group_boxplots(match, col_list, "Goal_total")


# In[ ]:





# In[5]:


summary = utilities.get_master("nations_summaries")
# summary.info()

summary = summary[['Rank Local', 'Rank Global', 'Team', 'Rating',
       'Average Rank', 'Average Rating', '1 Year Change Rank',
       '1 Year Change Rating', 'Matches Total', 'Matches Home', 'Matches Away',
       'Matches Neutral', 'Matches Wins', 'Matches Losses', 'Matches Draws',
       'Goals For', 'Goals Against', 'Year', 'Country',
       'Data Year', 'GDP (PPP)', 'Population']]

summary["GDP (PPP) Per Capita"] = summary['GDP (PPP)'] / summary['Population']

summary.describe(include="all").T


# In[6]:


metric_histograms(summary, ['Rating', 'Average Rank',
       'Average Rating', '1 Year Change Rank', '1 Year Change Rating',
       'Matches Total', 'Matches Home', 'Matches Away', 'Matches Neutral',
       'Matches Wins', 'Matches Losses', 'Matches Draws', 'Goals For',
       'Goals Against', 'GDP (PPP)',
       'Population', 'GDP (PPP) Per Capita'])


# In[ ]:





# ## 3. Data Preperation
# 
# * Select Data
# * Clean Data
# * Construct Data
# * Integrate Data
# * Format Data

# In[7]:


data = match.merge(summary, left_on=["Team_1", "Year"], right_on=["Team", "Year"]) #, suffixes=["", "_1"])
data = data.merge(summary, left_on=["Team_2", "Year"], right_on=["Team", "Year"], suffixes=["", " (2)"])
data.sort_values(by=["Date"], inplace=True)
data.reset_index(drop=True, inplace=True)

data["Elo_rating_diff"] = data["Rating"] - data["Rating (2)"]
data["Home_advantage"] = data["Home_1"] - data["Home_2"]
# data["Win_expectency_1"] = ((10**((-(data.Elo_rating_diff + (100 * data.Home_advantage)))/400))+1)**-1
data["Relative_experience"] = data["Matches Total"] / data["Matches Total (2)"]
data["Relative_population"] = data["Population"] / data["Population (2)"]
data["Relative_GDP_per_capita"] = data["GDP (PPP) Per Capita"] / data["GDP (PPP) Per Capita (2)"]
data["Relative_ELO_rating"] = data["Rating"] / data["Rating (2)"]
# data["Relative_ELO_rank_1yr_change"] = data["1 Year Change Rank"] / data["1 Year Change Rank (2)"]
# data["Relative_ELO_rating_1yr_change"] = data["1 Year Change Rating"] / data["1 Year Change Rating (2)"]
# data["Combined_ELO_rating_1yr_change"] = data["1 Year Change Rating"].abs() + data["1 Year Change Rating (2)"].abs()

# model_years = [2000, 2004, 2008, 2012, 2016]
live_years = [2021]
data["Usage"] = "Training"
data.loc[data.Year.isin(live_years), "Usage"] = "Live"

# data = data[["Date", "Year", "Team_1", "Team_2", "Goal_diff", "Goal_total", "Elo_rating_diff", "Home_advantage", "Win_expectency_1",
#              "Relative_experience", "Relative_population", "Relative_GDP_per_capita",
#             "Relative_ELO_rating"]] #, "Relative_ELO_rank_1yr_change", "Relative_ELO_rating_1yr_change"
# ]]

# data.columns
data.describe().T


# In[8]:


skip_cols = [x+" (2)" for x in summary.columns]
# print(skip_cols)
skip_cols = summary.columns.tolist() + skip_cols
# print(skip_cols)
skip_cols = [x for x in skip_cols if x in data.columns ]
# print(skip_cols)

data.drop(columns=skip_cols).corr().style.background_gradient(cmap='coolwarm')


# In[9]:


# data_lim.corr().style.background_gradient(cmap='coolwarm')


# In[ ]:





# ## 4. Modelling
# 
# * Select Modelling Technique
# * Generate Test Design
# * Build Model
# * Assess Model

# In[10]:


# from sklearn.dummy import DummyRegressor
# from sklearn.linear_model import LinearRegression
# from sklearn.linear_model import Lasso
# from sklearn.linear_model import Ridge
# # from sklearn.linear_model import BayesianRidge
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.ensemble import GradientBoostingRegressor
# # from sklearn.ensemble import VotingRegressor
# # from sklearn.neighbors import KNeighborsRegressor
# from sklearn.svm import SVR
# # from sklearn.compose import TransformedTargetRegressor
from sklearn.base import BaseEstimator, RegressorMixin

# from sklearn.metrics import median_absolute_error
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import r2_score

# # from sklearn.utils import resample
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# # from sklearn.model_selection import learning_curve
# # from sklearn.model_selection import KFold
# from sklearn.model_selection import train_test_split

# # np.random.seed(1)


# In[11]:


class EloRegressor(BaseEstimator, RegressorMixin):
    def __init__(self): #, yType="Diff", goalWeight=4., goalBoost=16.):
        self.yType = "Diff"
        self.goalWeight = 4.
        self.goalBoost = 1.
    
    def _show_params(self):
        print("_show_params...")
        print("yType:", self.yType)
        print("goalWeight:", self.goalWeight)
        print("goalBoost:", self.goalBoost)
        
        return
    
    def _calc_output(self, X):
        X_tmp = X.copy(deep=True)
        X_tmp["EloRatingDiffWithHomeAdv"] = X_tmp["Elo_rating_diff"] + (100 * X_tmp.Home_advantage)
        X_tmp["WinExpectency1Square"] = (10**((-X_tmp.EloRatingDiffWithHomeAdv)/400))+1
        X_tmp["WinExpectency1"] = X_tmp["WinExpectency1Square"]**-1
        X_tmp["RawGoalDiff"] = (self.goalWeight * (X_tmp.WinExpectency1 - 0.5)).round(0)
        X_tmp["RawGoalDiffAbs"] = X_tmp["RawGoalDiff"].abs()
        X_tmp["EitherWins"] = 0
        X_tmp.loc[X_tmp.RawGoalDiffAbs > 0, "EitherWins"] = 1
#         X_tmp["QualifyGoalsRankAvg"] = (X_tmp["QualifyGoalsRank1"] + X_tmp["QualifyGoalsRank2"]) / 2
        X_tmp["ApplyGoalBoost"] = 0
#         X_tmp.loc[X_tmp.QualifyGoalsRankAvg <= self.goalBoost, "ApplyGoalBoost"] = 1
        X_tmp["Goals1"] = X_tmp["ApplyGoalBoost"]
        X_tmp.loc[X_tmp.RawGoalDiff > 0, "Goals1"] = X_tmp.RawGoalDiff + X_tmp.ApplyGoalBoost
        X_tmp["Goals2"] = X_tmp["ApplyGoalBoost"]
        X_tmp.loc[X_tmp.RawGoalDiff <= 0, "Goals2"] = X_tmp.ApplyGoalBoost - X_tmp.RawGoalDiff
        X_tmp["GoalDiff"] = X_tmp.Goals1 - X_tmp.Goals2
        X_tmp["GoalDiffAbs"] = X_tmp.GoalDiff.abs()
        X_tmp["GoalTotal"] = X_tmp.Goals1 + X_tmp.Goals2
        
        return X_tmp["Goal"+self.yType].values

    def fit(self, X, y=None):
        if y.name == "Goal_total":
            self.yType = "Total"
#         else:
#             self.yType = "Diff"
        y_tmp = self._calc_output(X).mean()
        y_low = y.quantile(q=0.2)
        y_high = y.quantile(q=0.8)
        while y_tmp < y_low:
            self.goalWeight += 0.05
            y_tmp = self._calc_output(X).mean()
        while y_tmp > y_high:
            self.goalWeight -= 0.05
            y_tmp = self._calc_output(X).mean()
        self._show_params()
        
        return self

    def predict(self, X, y=None):
        self._show_params()
        return self._calc_output(X)


# ## 5. Evaluation
# 
# * Evaluate Results
# * Review Process
# * Determine Next Steps

# ## 6. Deployment
# 
# * Plan Deployment
# * Plan Monitoring and Maintenance
# * Produce Final Report
# * Review Project

# In[12]:


pickle_base = "../models/intl_02_{0}.pkl"

print("Un-Pickling files...")

with open(pickle_base.format("gd_model"), "rb") as pkl_1:
    selected_gd_model = pickle.load(pkl_1)
with open(pickle_base.format("gd_features"), "rb") as pkl_2:
    gd_features = pickle.load(pkl_2)
with open(pickle_base.format("gt_model"), "rb") as pkl_3:
    selected_gt_model = pickle.load(pkl_3)
with open(pickle_base.format("gt_features"), "rb") as pkl_4:
    gt_features = pickle.load(pkl_4)

selected_gd_model, gd_features, selected_gt_model, gt_features


# In[13]:


output_prev = pd.read_csv("../data/interim/intl_02_predictions.csv")
output_prev["Year"] = output_prev.Year.astype(str)
output_prev.info()


# In[14]:


output_new = data.copy(deep=True)[["Date", "Year", "Round", "Team_1", "Team_2", "Usage", "Goals_1", "Goals_2", "Goal_diff", "Goal_total", "Result"]]
output_new.columns = ["Date", "Year", "Round", "Team_1", "Team_2", "Usage", "Actual_score_1", "Actual_score_2", "Actual_goal_diff", "Actual_goal_total", "Actual_result"]
# output.loc[output.index.isin(gd_y_test.index), "Usage"] = "Testing"

gd_pred = selected_gd_model.predict(data[gd_features])
gt_pred = selected_gt_model.predict(data[gt_features])

gd_weight = 1 #.05
gt_weight = 1 #.15

## add weights?
output_new["Predicted_score_1"] = (gd_weight * (gt_pred + gd_pred) / 2).round()
output_new["Predicted_score_2"] = (gt_weight * (gt_pred - gd_pred) / 2).round()

## use earlier predictions where available
output = output_prev.combine_first(output_new)
output = output[output_prev.columns]
# print(output.shape)

output["Predicted_goal_diff"] = output.Predicted_score_1 - output.Predicted_score_2
output["Predicted_goal_total"] = output.Predicted_score_1 + output.Predicted_score_2
output["Predicted_result"] = None
output.loc[output.Predicted_score_1 == output.Predicted_score_2, "Predicted_result"] = "Draw"
output.loc[output.Predicted_score_1 > output.Predicted_score_2, "Predicted_result"] = "Win"
output.loc[output.Predicted_score_1 < output.Predicted_score_2, "Predicted_result"] = "Loss"

output["Correct_result"] = (output.Actual_result == output.Predicted_result).astype(int)
output["Correct_goal_diff"] = (output.Actual_goal_diff == output.Predicted_goal_diff).astype(int)
output["Correct_score"] = ((output.Actual_score_1 == output.Predicted_score_1) & (output.Actual_score_2 == output.Predicted_score_2)).astype(int)
output["Points"] = output.Correct_result + output.Correct_goal_diff + output.Correct_score

for col in ["Correct_result", "Correct_goal_diff", "Correct_score", "Points"]:
    output.loc[pd.isnull(output.Actual_result), col] = np.nan

output.to_csv("../data/interim/intl_02_predictions_live.csv", index=False)
output.describe(include="all").T


# In[15]:


def agg_by_col(df, col, asc=True):
    """
    INPUT:
        df - Match-level output dataframe
        col - Column to aggregate by
        asc - Sort ascending (True) or descending (False)
        
    OUTPUT:
        agg - Aggregated dataframe
    """
    agg = pd.concat([
        df[pd.notnull(df.Actual_result)][col].value_counts().sort_index(),
        df[pd.notnull(df.Actual_result)].groupby(col)[["Points", "Correct_result", "Correct_goal_diff", "Correct_score",
                                                                  "Predicted_goal_total", "Actual_goal_total"]].mean(),
        df[pd.notnull(df.Actual_result) & (df.Predicted_result != "Draw")][col].value_counts() / df[pd.notnull(df.Actual_result)][col].value_counts(),
        df[pd.notnull(df.Actual_result) & (df.Actual_result != "Draw")][col].value_counts() / df[pd.notnull(df.Actual_result)][col].value_counts(),
    ], axis=1)
    agg.sort_index(ascending=asc, inplace=True)
    agg.columns = ['Matches played', 'Points per game', '% correct result',
       '% correct goal diff', '% correct score', 'Goals per game (predicted)',
       'Goals per game (actual)', '% games won (predicted)',
       '% games won (actual)']
#     print(agg.columns)
    
    return agg

overall = pd.DataFrame({
    "Matches played": output[pd.notnull(output.Actual_result)].shape[0],
    "Points per game": output[pd.notnull(output.Actual_result)].Points.mean(),
    "% correct result": output[pd.notnull(output.Actual_result)].Correct_result.mean(),
    "% correct goal diff": output[pd.notnull(output.Actual_result)].Correct_goal_diff.mean(),
    "% correct score": output[pd.notnull(output.Actual_result)].Correct_score.mean(),
    "Goals per game (predicted)": output[pd.notnull(output.Actual_result)].Predicted_goal_total.mean(),
    "Goals per game (actual)": output[pd.notnull(output.Actual_result)].Actual_goal_total.mean(),
    "% games won (predicted)": output[pd.notnull(output.Actual_result) & (output.Predicted_result != "Draw")].shape[0] / output[pd.notnull(output.Actual_result)].shape[0],
    "% games won (actual)": output[pd.notnull(output.Actual_result) & (output.Actual_result != "Draw")].shape[0] / output[pd.notnull(output.Actual_result)].shape[0],
}, index=["Overall"])
# print(overall.columns)

summary = pd.concat([agg_by_col(output, "Year"), agg_by_col(output, "Usage", asc=False), overall], axis=0)
summary = summary.round(2)
pct_cols = []
for col in summary.columns:
    if col.startswith("%"):
        pct_cols.append(col)
summary[pct_cols] = (100 * summary[pct_cols]).astype(int).astype(str) + "%"

summary


# In[16]:


output.loc[output.Usage == "Live"].describe().dropna(axis=1, how="any").T


# In[ ]:





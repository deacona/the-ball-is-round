#!/usr/bin/env python
# coding: utf-8

# # International data - World Cup 2018 predictions
# 
# Ported from Excel - see original [here](models/World cup 2018 CALC.xlsx)

# ### 1. Input data on team fixtures and performance

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


HOME_TEAMS = ["Russia"]
HOME_TEAMS


# In[3]:


fixtures = pd.read_csv("../data/raw/whs/whs_fix/whs_fix_wcm_2018.csv")
fixtures.columns = ["Date", "Time", "ignore_1", "Team1", "ignore_2", "Team2", "ignore_3"]
fixtures.drop(columns=["ignore_1", "ignore_2", "ignore_3"], inplace=True)
fixtures.Date.fillna(method="ffill", inplace=True)
fixtures.dropna(axis="index", subset=["Team1"], inplace=True)
fixtures.info()


# In[4]:


fixtures["HomeAdv1"] = 0
fixtures["HomeAdv2"] = 0
fixtures.loc[fixtures.Team1.isin(HOME_TEAMS), "HomeAdv1"] = 1
fixtures.loc[fixtures.Team2.isin(HOME_TEAMS), "HomeAdv2"] = 1

fixtures.head(5)


# In[5]:


elo = pd.read_csv("../data/raw/wkp/wkp_elo/World_Football_Elo_Ratings.csv")
elo.columns = ["Team", "EloRank", "ignore_1", "ignore_2", "ignore_3", "EloRating", "FIFARank", "ignore_4", "ignore_5"]
elo.drop(columns=["ignore_1", "ignore_2", "ignore_3", "ignore_4", "ignore_5"], inplace=True)
elo.info()


# In[6]:


elo.head(5)


# In[7]:


qualifying = pd.read_csv("../data/raw/fif/Qualifying_goals.csv")
qualifying = qualifying[["Team", "Rank"]]
qualifying.columns = ["Team", "QualifyGoalsRank"]
qualifying.info()


# In[8]:


qualifying.head(5)


# In[9]:


inputData = fixtures.merge(elo, how="inner", left_on="Team1", right_on="Team", suffixes=["","1"])    .drop(columns=["Team"])    .merge(elo, how="inner", left_on="Team2", right_on="Team", suffixes=["1","2"])    .merge(qualifying, how="inner", left_on="Team1", right_on="Team")    .drop(columns=["Team_x", "Team_y"])    .merge(qualifying, how="inner", left_on="Team2", right_on="Team")    .drop(columns=["Team"])    .rename(columns={"QualifyGoalsRank_x": "QualifyGoalsRank1", "QualifyGoalsRank_y": "QualifyGoalsRank2"})
inputData
inputData.info()


# ### 2. Build model and make predictions

# In[10]:


def make_predictions(X_input, p_goal_weight, p_goal_boost):
    """Take input data and parameters and make predictions

    Args:
        X_input: Input dataframe with columns
            ['Date', 'Time', 'Team1', 'Team2', 'HomeAdv1', 'HomeAdv2', 'EloRank1', 'EloRating1', 
            'FIFARank1', 'EloRank2', 'EloRating2', 'FIFARank2', 'QualifyGoalsRank1', 'QualifyGoalsRank2']
        p_goal_weight: Float value weight to apply to calculate raw goal differences
        p_goal_boost: Float value rank threshold for applying goal boost

    Returns:
        X_full: Output dataframe with columns
            ['Date', 'Time', 'Team1', 'Team2', 'HomeAdv1', 'HomeAdv2', 'EloRank1', 'EloRating1', 
            'FIFARank1', 'EloRank2', 'EloRating2', 'FIFARank2', 'QualifyGoalsRank1', 'QualifyGoalsRank2', 
            'EloRatingDiff', 'EloRatingDiffWithHomeAdv', 'WinExpectency1Square', 'WinExpectency1',
            'RawGoalDiff', 'RawGoalDiffAbs', 'EitherWins', 'QualifyGoalsRankAvg', 'ApplyGoalBoost', 
            'Goals1', 'Goals2', 'GoalDiff', 'GoalDiffAbs', 'GoalTotal']
    """
    X_full = X_input.copy()
    X_full["EloRatingDiff"] = X_full["EloRating1"] - X_full["EloRating2"]
    X_full["EloRatingDiffWithHomeAdv"] = X_full["EloRatingDiff"] + (100 * X_full.HomeAdv1) - (100 * X_full.HomeAdv2)
    X_full["WinExpectency1Square"] = (10**((-X_full.EloRatingDiffWithHomeAdv)/400))+1
    X_full["WinExpectency1"] = X_full["WinExpectency1Square"]**-1
    X_full["RawGoalDiff"] = (p_goal_weight * (X_full.WinExpectency1 - 0.5)).round(0)
    X_full["RawGoalDiffAbs"] = X_full["RawGoalDiff"].abs()
    X_full["EitherWins"] = 0
    X_full.loc[X_full.RawGoalDiffAbs > 0, "EitherWins"] = 1
    X_full["QualifyGoalsRankAvg"] = (X_full["QualifyGoalsRank1"] + X_full["QualifyGoalsRank2"]) / 2
    X_full["ApplyGoalBoost"] = 0
    X_full.loc[X_full.QualifyGoalsRankAvg <= p_goal_boost, "ApplyGoalBoost"] = 1
    X_full["Goals1"] = X_full["ApplyGoalBoost"]
    X_full.loc[X_full.RawGoalDiff > 0, "Goals1"] = X_full.RawGoalDiff + X_full.ApplyGoalBoost
    X_full["Goals2"] = X_full["ApplyGoalBoost"]
    X_full.loc[X_full.RawGoalDiff <= 0, "Goals2"] = X_full.ApplyGoalBoost - X_full.RawGoalDiff
    X_full["GoalDiff"] = X_full.Goals1 - X_full.Goals2
    X_full["GoalDiffAbs"] = X_full.GoalDiff.abs()
    X_full["GoalTotal"] = X_full.Goals1 + X_full.Goals2
    
    return X_full

# make_predictions?


# In[11]:


EXCEL_GOAL_WEIGHT = 4.
EXCEL_GOAL_BOOST = 19.
EXCEL_GOAL_WEIGHT, EXCEL_GOAL_BOOST


# In[12]:


data = make_predictions(inputData, EXCEL_GOAL_WEIGHT, EXCEL_GOAL_BOOST)

# data.iloc[:, -14:].head(5)
data.describe(include="all").T


# In[13]:


data[["Date", "Time", "Team1", "Team2", "Goals1", "Goals2"]].to_csv("../data/interim/intl_01_predictions.csv", index=False)


# ### 3. Evaluate predictions against historic trends

# In[14]:


def compare_to_historic(X_full, show_comparison=True):
    """Take input data and parameters and make predictions

    Args:
        X_full: Full dataframe with columns
            ['Date', 'Time', 'Team1', 'Team2', 'HomeAdv1', 'HomeAdv2', 'EloRank1', 'EloRating1', 
            'FIFARank1', 'EloRank2', 'EloRating2', 'FIFARank2', 'QualifyGoalsRank1', 'QualifyGoalsRank2', 
            'EloRatingDiff', 'EloRatingDiffWithHomeAdv', 'WinExpectency1Square', 'WinExpectency1',
            'RawGoalDiff', 'RawGoalDiffAbs', 'EitherWins', 'QualifyGoalsRankAvg', 'ApplyGoalBoost', 
            'Goals1', 'Goals2', 'GoalDiff', 'GoalDiffAbs', 'GoalTotal']
        show_comparison: Boolean whether to display historic comparison

    Returns:
        None
    """
    
    poisson = pd.read_csv("../data/raw/wkp/wkp_pds/Poisson_goals_World_Cup.csv")
    poisson.columns = ["k", "P_of_k_goals", "ignore_1", "ignore_2"]
    poisson.drop(columns=["ignore_1", "ignore_2"], inplace=True)
    poisson["label"] = "% games "+poisson.k.astype(str)+" goals"
    poisson.set_index("label", inplace=True)
#     poisson.info()
    
    totals = pd.read_csv("../data/raw/fif/World_Cup_goals.csv")
    totals.columns = ["Tournament", "NoOfTeams", "MatchesPlayed", "GoalsScored", "AverageGoals", "AverageAttendance",
                     "Rolling", "ignore_1", "ignore_2"]
    totals.drop(columns=["ignore_1", "ignore_2"], inplace=True)
    totals.dropna(axis="index", subset=["Tournament"], inplace=True)
#     totals.info()

    historic = pd.concat([poisson.P_of_k_goals.T, totals.iloc[10, -1:]])
    historic.rename({"Rolling": "AverageGoalsPerGame"}, inplace=True)
    historic["% games drawn"] = 314 / 1416
    historic["% games won"] = 1 - historic["% games drawn"]
#     historic
    
    predictions = pd.DataFrame([{
        "AverageGoalsPerGame": X_full.GoalTotal.sum() / X_full.shape[0],
        "% games drawn": X_full[X_full.EitherWins == 0].shape[0] / X_full.shape[0],
        "% games won": X_full[X_full.EitherWins == 1].shape[0] / X_full.shape[0],
    }])
    for g in range(8):
        predictions["% games "+str(g)+" goals"] = X_full[X_full.GoalTotal == g].shape[0] / X_full.shape[0]
#     predictions.info()

    hist_vs_pred = pd.concat([pd.DataFrame(historic).T, predictions]).T
    hist_vs_pred.columns = ["Historic", "Predictions"]
    hist_vs_pred["%Diff"] = 1.0
    hist_vs_pred.loc[hist_vs_pred.Predictions > 0, "%Diff"] =         1 - (hist_vs_pred.loc[hist_vs_pred.Predictions > 0, "Historic"]            / hist_vs_pred.loc[hist_vs_pred.Predictions > 0, "Predictions"])
    if show_comparison:
        print(hist_vs_pred)
    
    return None

# compare_to_historic?


# In[15]:


compare_to_historic(data)


# ### 4. Compare predictions to actual results

# In[16]:


results = pd.read_excel("../models/World cup 2018 CALC.xlsx", sheet_name="Fixtures_and_calcs")
results = results.iloc[:, [0,1,3,5,32,33]]
results.columns = ["Date", "Time", "Team1", "Team2", "Actual1", "Actual2"]
results.Date.fillna(method="ffill", inplace=True)
results["Time"] = results["Time"].astype(str).str[:5]
results.dropna(axis="index", subset=["Team1"], inplace=True)

# results.info()
results.head(5)


# In[17]:


def compare_to_actual(X_full, X_results, show_comparison=True):
    """Takes full data with predictions and actual results to compare

    Args:
        X_full: Full dataframe with columns
            ['Date', 'Time', 'Team1', 'Team2', 'HomeAdv1', 'HomeAdv2', 'EloRank1', 'EloRating1', 
            'FIFARank1', 'EloRank2', 'EloRating2', 'FIFARank2', 'QualifyGoalsRank1', 'QualifyGoalsRank2', 
            'EloRatingDiff', 'EloRatingDiffWithHomeAdv', 'WinExpectency1Square', 'WinExpectency1',
            'RawGoalDiff', 'RawGoalDiffAbs', 'EitherWins', 'QualifyGoalsRankAvg', 'ApplyGoalBoost', 
            'Goals1', 'Goals2', 'GoalDiff', 'GoalDiffAbs', 'GoalTotal']
        X_results: Results dataframe with columns
            ['Date', 'Time', 'Team1', 'Team2', 'Actual1', 'Actual2']
        show_comparison: Boolean whether to display historic comparison

    Returns:
        percentage_points: Float value percentage of available points achieved by predictions
    """
    
    compare = X_full[["Date", "Time", "Team1", "Team2", "Goals1", "Goals2"]]        .merge(X_results, how="inner", on=["Date", "Time", "Team1", "Team2"])
    compare.rename(columns={"Goals1": "Prediction1", "Goals2": "Prediction2"}, inplace=True)

    compare["Prediction2"] = compare.Prediction2.astype(float)

    compare["CorrectResult"] = 0
    compare.loc[((compare.Prediction1 > compare.Prediction2) & (compare.Actual1 > compare.Actual2))
                | ((compare.Prediction1 == compare.Prediction2) & (compare.Actual1 == compare.Actual2))
                | ((compare.Prediction1 < compare.Prediction2) & (compare.Actual1 < compare.Actual2))
                , "CorrectResult"] = 1

    compare["CorrectGoalDiff"] = 0
    compare.loc[(compare.Prediction1 - compare.Prediction2 == compare.Actual1 - compare.Actual2), "CorrectGoalDiff"] = 1

    compare["CorrectScore"] = 0
    compare.loc[(compare.Prediction1 == compare.Actual1) & (compare.Prediction2 == compare.Actual2), "CorrectScore"] = 1

    compare["PointsScored"] = compare.CorrectResult + compare.CorrectGoalDiff + compare.CorrectScore

#     compare.tail(10)

    compare[["CorrectResult", "CorrectGoalDiff", "CorrectScore", "PointsScored"]].sum()

    matches_played = compare.shape[0]
#     matches_played

    pred_vs_actual = pd.concat([compare[["CorrectResult", "CorrectGoalDiff", "CorrectScore", "PointsScored"]].sum(),
              pd.Series({"CorrectResult": matches_played, "CorrectGoalDiff": matches_played, "CorrectScore": matches_played, "PointsScored": 3 * matches_played})
              ], axis=1)
    pred_vs_actual.columns = ["Predictions", "Maximum"]
    pred_vs_actual["% of Maximum"] = pred_vs_actual.Predictions / pred_vs_actual.Maximum
    if show_comparison:
        print(pred_vs_actual)
    
    percentage_points = pred_vs_actual.loc["PointsScored" , "% of Maximum"]
    
    return percentage_points

# compare_to_actual?


# In[18]:


compare_to_actual(data, results)


# ### 5. Improve the model?

# In[19]:


import itertools


# In[20]:


weight_options = [1., 2., 3., 4., 5., 6., 7., 8., 9.]
boost_options = [14., 15., 16., 17., 18., 19., 20., 21., 22., 23., 24.]

param_grid = list(itertools.product(weight_options, boost_options))
len(param_grid)


# In[21]:


scoring = []
for params in param_grid:
    df = make_predictions(inputData, params[0], params[1])
    compare_to_historic(df, show_comparison=False)
    pp = compare_to_actual(df, results, show_comparison=False)
    scoring.append({
        "Parameters": params,
        "%PointsScored": pp,
    })

pd.DataFrame(scoring).sort_values(by="%PointsScored", ascending=False).head(10)


# In[22]:


data2 = make_predictions(inputData, 4., 16.)
compare_to_historic(data2)
compare_to_actual(data2, results)


# In[23]:


data2[["Date", "Time", "Team1", "Team2", "Goals1", "Goals2"]].to_csv("../data/interim/intl_01_predictions_2.csv", index=False)


# In[ ]:





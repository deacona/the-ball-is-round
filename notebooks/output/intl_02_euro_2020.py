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

# ### EURO 2020 fixtures/results
# * https://en.wikipedia.org/wiki/UEFA_Euro_2020
# * https://www.whoscored.com/Regions/247/Tournaments/124/Seasons/7329/Stages/16297/Show/International-European-Championship-2020
# * https://www.uefa.com/uefaeuro-2020/fixtures-results/#/md/33673
# * https://fbref.com/en/comps/676/schedule/UEFA-Euro-Scores-and-Fixtures
# 
# ### Historic results
# * https://www.staff.city.ac.uk/r.j.gerrard/football/aifrform.html (1871-2001)
# * https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017/data (1872-)
# * https://fbref.com/en/comps/676/history/European-Championship-Seasons (2000-)
# * https://en.wikipedia.org/wiki/UEFA_Euro_2020_qualifying (qualifying)
# * https://fbref.com/en/comps/678/Euro-Qualifying-Stats (qualifying)
# 
# ### ELO ratings
# * https://en.m.wikipedia.org/wiki/World_Football_Elo_Ratings
# * https://www.eloratings.net/2021_European_Championship
# * http://eloratings.net/2016_European_Championship_start
# * https://www.eloratings.net/about
# 
# ### Historic trends
# * https://blog.annabet.com/soccer-goal-probabilities-poisson-vs-actual-distribution/
# * https://en.wikipedia.org/wiki/Poisson_distribution
# 
# ### GDP
# * https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)
# * https://en.wikipedia.org/wiki/List_of_countries_by_past_and_projected_GDP_(nominal)
# * https://www.rug.nl/ggdc/productivity/pwt/
# 
# ### Prediction competitions
# * https://www.squawka.com/en/euro-2020-predictions-odds-outright-group-winner-final/
# * https://www.telegraph.co.uk/football/euro-2020-wallchart-predictor/
# * https://gaming.uefa.com/en/uefaeuro2020tournamentpredictor/main
# * https://www.uefa.com/uefaeuro-2020/news/0269-1232cabf40a1-47e385aa9131-1000--euro-2020-tournament-predictor-rules/

# In[1]:


import pandas as pd
import os
import numpy as np

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


def metric_histograms(df, metrics):
#     df = df_in.dropna(subset=[metric]).fillna("NULL")
    for metric in metrics:
        print("\n{0}\n".format(metric))
#         df[metric].hist()
        sns.histplot(data=df, x=metric, kde=True)
        plt.show()
#         sns.boxplot(x=df[metric])
#         plt.show()
        print("\n--------------------")

metric_histograms(match, ["Goals_1", "Goals_2", "Goal_diff", "Goal_total"])


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


# ## fix data mismatch

# for col in ["Team_1", "Team_2"]:
#     print("\n")
#     print(match[~match[col].isin(summary.Team.values)][col].value_counts())
#     print("\n")
#     print(summary[~summary.Team.isin(match[col].values)].Team.value_counts())


# In[8]:


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


# In[9]:


data.corr().style.background_gradient(cmap='coolwarm')


# In[10]:


# # Computing IQR
# Q1 = data.quantile(0.25)
# Q3 = data.quantile(0.75)
# IQR = Q3 - Q1

# # Filtering Values between Q1-1.5IQR and Q3+1.5IQR
# lower_limit = Q1 - (1.5 * IQR)
# upper_limit = Q3 + (1.5 * IQR)

# lower_limit, upper_limit
# # data[(data < lower_limit) | (data > upper_limit)].dropna(how="all")


# In[11]:


# data_lim = data.copy(deep=True)

# for col in data_lim.columns:
#     if col == "Home_advantage":
#         continue
#     data_lim.loc[data_lim[col] < lower_limit[col], col] = lower_limit[col]
#     data_lim.loc[data_lim[col] > upper_limit[col], col] = upper_limit[col]
    
# data_lim = pd.DataFrame(MinMaxScaler().fit_transform(data_lim), columns=data_lim.columns)
    
# data_lim.describe().T


# In[12]:


# data_lim.corr().style.background_gradient(cmap='coolwarm')


# In[13]:


# sns.pairplot(data_lim, size = 2.5)
# plt.show();


# In[ ]:





# ## 4. Modelling
# 
# * Select Modelling Technique
# * Generate Test Design
# * Build Model
# * Assess Model

# ### Updated WC model
# * https://github.com/deacona/the-ball-is-round/blob/master/reports/intl_01_world_cup_2018.md
# * https://github.com/deacona/the-ball-is-round/blob/master/notebooks/intl_01_world_cup_2018.ipynb
# 
# ### "Soccernomics"
# * goal diff = (0.6666 * home adv) + (0.5 * relative experience) + (0.1 * relative population) + (0.1 * relative gdp/head) + ...
# * e.g. England vs Germany at Euro 96
#     * Home = England = 1
#     * Exp = 84k v 84k = 0
#     * Pop = 57 v 81 = -0.4
#     * GDP/h = 1627492 / 57 v 2633828 / 81 = -0.1
#     * GD = (0.6666 * 1) + (0.5 * 0) + (0.1 * -0.4) + (0.1 * -0.1) = 0.6
# * http://www.soccernomics-agency.com/wordpress/wp-content/uploads/2017/10/soccer-convergence-1.pdf
# 
# ### Dixon-Coles (and other probability models)
# * https://dashee87.github.io/football/python/predicting-football-results-with-statistical-modelling-dixon-coles-and-time-weighting/
# * http://www.statsandsnakeoil.com/2018/06/05/modelling-the-world-cup-with-regista/
# * http://opisthokonta.net/?cat=48

# In[14]:


from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
# from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import GradientBoostingRegressor
# from sklearn.ensemble import VotingRegressor
# from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
# from sklearn.compose import TransformedTargetRegressor
from sklearn.base import BaseEstimator, RegressorMixin

from sklearn.metrics import median_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

# from sklearn.utils import resample
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
# from sklearn.model_selection import learning_curve
# from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split

# np.random.seed(1)


# In[15]:


gd_features = ["Home_advantage", "Relative_experience", "Relative_population", "Relative_GDP_per_capita", "Elo_rating_diff"]
gt_features = ["Home_advantage", "Relative_experience", "Relative_population", "Relative_GDP_per_capita", "Elo_rating_diff"]

gd_target = "Goal_diff"
gt_target = "Goal_total"

gd_X = data.loc[~data.Year.isin(live_years), gd_features]
gd_y = data.loc[~data.Year.isin(live_years), gd_target]
gt_X = data.loc[~data.Year.isin(live_years), gt_features]
gt_y = data.loc[~data.Year.isin(live_years), gt_target]

gd_X_train, gd_X_test, gd_y_train, gd_y_test = train_test_split(gd_X, gd_y, random_state=42, train_size=0.8)
gt_X_train, gt_X_test, gt_y_train, gt_y_test = train_test_split(gt_X, gt_y, random_state=42, train_size=0.8)

print("GD Train data has shape: {0}".format(gd_X_train.shape))
print("GD Test data has shape: {0}".format(gd_X_test.shape))
print("------")
print("GT Train data has shape: {0}".format(gt_X_train.shape))
print("GT Test data has shape: {0}".format(gt_X_test.shape))


# In[16]:


# # model = LinearRegression(fit_intercept=False, normalize=True)
# model = EloRegressor()
# model.fit(gd_X_train, gd_y_train)

# y_pred = model.predict(gd_X_test)

# {"MedAE": median_absolute_error(gd_y_test, y_pred),
#             "RMSE": mean_squared_error(gd_y_test, y_pred, squared=False),
#             "R^2": r2_score(gd_y_test, y_pred),
#            }


# In[17]:


# params = pd.Series(model.coef_, index=X_train.columns)
# # params
# err = np.std([model.fit(*resample(X_train, y_train)).coef_ for i in range(1000)], 0)

# pd.DataFrame({"effect": params.round(2), "error": err.round(2)})


# In[18]:


get_ipython().run_cell_magic('time', '', '\n## add ELO model?\nclass EloRegressor(BaseEstimator, RegressorMixin):\n    def __init__(self): #, yType="Diff", goalWeight=4., goalBoost=16.):\n        self.yType = "Diff"\n        self.goalWeight = 4.\n        self.goalBoost = 1.\n    \n    def _show_params(self):\n        print("_show_params...")\n        print("yType:", self.yType)\n        print("goalWeight:", self.goalWeight)\n        print("goalBoost:", self.goalBoost)\n        \n        return\n    \n    def _calc_output(self, X):\n        X_tmp = X.copy(deep=True)\n        X_tmp["EloRatingDiffWithHomeAdv"] = X_tmp["Elo_rating_diff"] + (100 * X_tmp.Home_advantage)\n        X_tmp["WinExpectency1Square"] = (10**((-X_tmp.EloRatingDiffWithHomeAdv)/400))+1\n        X_tmp["WinExpectency1"] = X_tmp["WinExpectency1Square"]**-1\n        X_tmp["RawGoalDiff"] = (self.goalWeight * (X_tmp.WinExpectency1 - 0.5)).round(0)\n        X_tmp["RawGoalDiffAbs"] = X_tmp["RawGoalDiff"].abs()\n        X_tmp["EitherWins"] = 0\n        X_tmp.loc[X_tmp.RawGoalDiffAbs > 0, "EitherWins"] = 1\n#         X_tmp["QualifyGoalsRankAvg"] = (X_tmp["QualifyGoalsRank1"] + X_tmp["QualifyGoalsRank2"]) / 2\n        X_tmp["ApplyGoalBoost"] = 0\n#         X_tmp.loc[X_tmp.QualifyGoalsRankAvg <= self.goalBoost, "ApplyGoalBoost"] = 1\n        X_tmp["Goals1"] = X_tmp["ApplyGoalBoost"]\n        X_tmp.loc[X_tmp.RawGoalDiff > 0, "Goals1"] = X_tmp.RawGoalDiff + X_tmp.ApplyGoalBoost\n        X_tmp["Goals2"] = X_tmp["ApplyGoalBoost"]\n        X_tmp.loc[X_tmp.RawGoalDiff <= 0, "Goals2"] = X_tmp.ApplyGoalBoost - X_tmp.RawGoalDiff\n        X_tmp["GoalDiff"] = X_tmp.Goals1 - X_tmp.Goals2\n        X_tmp["GoalDiffAbs"] = X_tmp.GoalDiff.abs()\n        X_tmp["GoalTotal"] = X_tmp.Goals1 + X_tmp.Goals2\n        \n        return X_tmp["Goal"+self.yType].values\n\n    def fit(self, X, y=None):\n        if y.name == "Goal_total":\n            self.yType = "Total"\n#         else:\n#             self.yType = "Diff"\n        y_tmp = self._calc_output(X).mean()\n        y_low = y.quantile(q=0.2)\n        y_high = y.quantile(q=0.8)\n        while y_tmp < y_low:\n            self.goalWeight += 0.05\n            y_tmp = self._calc_output(X).mean()\n        while y_tmp > y_high:\n            self.goalWeight -= 0.05\n            y_tmp = self._calc_output(X).mean()\n        self._show_params()\n        \n        return self\n\n    def predict(self, X, y=None):\n        self._show_params()\n        return self._calc_output(X)\n\ndef model_pipe(model, X_train, y_train):\n    """\n    INPUT:\n        model: Untrained regression model\n        X_train: Training features\n        y_train: Training target\n        \n    OUTPUT:\n        model: Trained model\n    """\n    \n#     model = TransformedTargetRegressor(regressor=model, transformer=MinMaxScaler())\n    model = Pipeline(steps=[(\'standardizer\', StandardScaler()),\n#                             (\'normalizer\', MinMaxScaler()),\n                      (\'estimator\', model)])\n    model.fit(X_train, y_train)\n    \n    return model\n\ndef get_trained_models(X_train, y_train):\n    """\n    INPUT:\n        X_train: Training features\n        y_train: Training target\n        \n    OUTPUT:\n        model_list: List of trained models\n    """\n    model_list = [\n        {"Name": "Dummy (mean)", "Reg": model_pipe(DummyRegressor(strategy="mean"), X_train, y_train)},\n        {"Name": "Dummy (median)", "Reg": model_pipe(DummyRegressor(strategy="median"), X_train, y_train)},\n        {"Name": "Linear Reg", "Reg": model_pipe(LinearRegression(), X_train, y_train)}, #sometimes skews results table\n        {"Name": "Lasso", "Reg": model_pipe(Lasso(), X_train, y_train)},\n        {"Name": "Ridge", "Reg": model_pipe(Ridge(), X_train, y_train)},\n    #     {"Name": "Bayesian Ridge", "Reg": model_pipe(BayesianRidge(), X_train, y_train)},\n        {"Name": "Random Forest", "Reg": model_pipe(RandomForestRegressor(random_state=42), X_train, y_train)},\n    #     {"Name": "Random Forest (tuned)", "Reg": rf_tuned(X_train, y_train)},\n        {"Name": "Gradient Boost", "Reg": model_pipe(GradientBoostingRegressor(), X_train, y_train)},\n    #     {"Name": "K Neighbors", "Reg": model_pipe(KNeighborsRegressor(), X_train, y_train)},\n        {"Name": "SVM (linear)", "Reg": model_pipe(SVR(kernel="linear"), X_train, y_train)},\n        {"Name": "SVM (rbf)", "Reg": model_pipe(SVR(kernel="rbf"), X_train, y_train)},\n    #     {"Name": "Voting (RF+KNN)", "Reg": model_pipe(VotingRegressor([(\'rf\', RandomForestRegressor(random_state=42)), \n    #                                                             (\'knn\', KNeighborsRegressor())]), X_train, y_train)},\n    #     {"Name": "Voting (LR+RF+KNN)", "Reg": model_pipe(VotingRegressor([(\'lr\', LinearRegression()),\n    #                                                             (\'rf\', RandomForestRegressor(random_state=42)),\n    #                                                             (\'knn\', KNeighborsRegressor())]), X_train, y_train)},\n        {"Name": "Elo", "Reg": EloRegressor().fit(X_train, y_train)}\n    ]\n\n    return model_list\n\ngd_model_list = get_trained_models(gd_X_train, gd_y_train)\ngt_model_list = get_trained_models(gt_X_train, gt_y_train)\n\nlen(gd_model_list), len(gt_model_list)')


# In[ ]:





# ## 5. Evaluation
# 
# * Evaluate Results
# * Review Process
# * Determine Next Steps

# ```
# # % correct score, goal diff, result, points
# # vs historic trends (goals, W/D/L)
# ```

# In[19]:


def get_model_scores(y_act, y_pred):
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

def evaluate_models(model_list, X_test, y_test, show_plots=True):
    """
    INPUT:
        y_act - Actual values from target vector
        y_pred - Predicted values from target vector
        show_plots: True/False to display any plots
        
    OUTPUT:
        Dictionary containing multiple scoring metrics with nice labels as keys
    """

    eval_list = []
    for model in model_list:
        print("\nEvaluating {0}...\n".format(model["Name"]))

        y_pred = model["Reg"].predict(X_test)
        eval_dict = get_model_scores(y_test, y_pred)
        eval_dict["Name"] = model["Name"]
        print(eval_dict)
        eval_list.append(eval_dict)

        if show_plots:
    #         residuals = y_test - y_pred
        #     plt.scatter(residuals,y_pred)
            sns.residplot(x=y_test, y=y_pred)
        #     sns.regplot(x=y_test, y=residuals, ci=99)
            plt.title("Residuals plot for {0}".format(model["Name"]))
            plt.show()

        #     plt.hist(residuals, bins=20)
        # #     plt.xlim(-40,50)
        #     plt.xlabel('Residuals')
        #     plt.title("Residuals histogram for {0}".format(model["Name"]))
        #     plt.show()

        print("\n--------------------")

    print("\n{0} models evaluated".format(len(eval_list)))

    eval_df = pd.DataFrame(eval_list)
    # eval_df.columns

    return eval_df

show_eval_plots = True

print("Goal difference model")
gd_eval = evaluate_models(gd_model_list, gd_X_test, gd_y_test, show_plots=show_eval_plots)
print("==============")
print("==============")
print("Goal total model")
gt_eval = evaluate_models(gt_model_list, gt_X_test, gt_y_test, show_plots=show_eval_plots)


# In[20]:


gd_eval[['Name', 'R^2', 'RMSE', 'MedAE']]        .style        .background_gradient(cmap='Reds', subset=['RMSE', 'MedAE'])        .background_gradient(cmap='Greens', subset=['R^2'])


# In[21]:


gt_eval[['Name', 'R^2', 'RMSE', 'MedAE']]        .style        .background_gradient(cmap='Reds', subset=['RMSE', 'MedAE'])        .background_gradient(cmap='Greens', subset=['R^2'])


# In[22]:


# kfold = KFold(n_splits=10, shuffle=True, random_state=42)

# # Create CV training and test scores for various training set sizes
# train_sizes, train_scores, test_scores = learning_curve(model_list[2]["Reg"], 
#                                                         X_train, 
#                                                         y_train,
#                                                         cv=kfold,
#                                                         # 50 different sizes of the training set
#                                                         train_sizes=np.linspace(0.1, 1.0, 50))

# # Create means and standard deviations of training set scores
# train_mean = np.mean(train_scores, axis=1)
# train_std = np.std(train_scores, axis=1)

# # Create means and standard deviations of test set scores
# test_mean = np.mean(test_scores, axis=1)
# test_std = np.std(test_scores, axis=1)

# # Draw lines
# plt.plot(train_sizes, train_mean, '--', color="#111111",  label="Training score")
# plt.plot(train_sizes, test_mean, color="#111111", label="Cross-validation score")

# # Draw bands
# plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, color="#DDDDDD")
# plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, color="#DDDDDD")

# # Create plot
# plt.title("Learning curve")
# plt.xlabel("Training set size"), plt.ylabel("R^2 score"), plt.legend(loc="best")
# plt.tight_layout()
# plt.show()


# In[23]:


selected_gd_model = gd_model_list[9]["Reg"]
selected_gt_model = gt_model_list[3]["Reg"]

selected_gd_model, selected_gt_model


# In[ ]:





# ## 6. Deployment
# 
# * Plan Deployment
# * Plan Monitoring and Maintenance
# * Produce Final Report
# * Review Project

# In[24]:


output = data.copy(deep=True)[["Date", "Year", "Team_1", "Team_2", "Usage", "Goals_1", "Goals_2", "Goal_diff", "Goal_total", "Result"]]
output.columns = ["Date", "Year", "Team_1", "Team_2", "Usage", "Actual_score_1", "Actual_score_2", "Actual_goal_diff", "Actual_goal_total", "Actual_result"]
output.loc[output.index.isin(gd_y_test.index), "Usage"] = "Testing"

gd_pred = selected_gd_model.predict(data[gd_features])
gt_pred = selected_gt_model.predict(data[gt_features])

gd_weight = 1 #.05
gt_weight = 1 #.15

## add weights?
output["Predicted_score_1"] = (gd_weight * (gt_pred + gd_pred) / 2).round()
output["Predicted_score_2"] = (gt_weight * (gt_pred - gd_pred) / 2).round()
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

output.to_csv("../data/interim/intl_02_predictions.csv", index=False)
output.describe(include="all").T


# In[25]:


output.loc[output.Usage == "Live", ["Predicted_score_1", "Predicted_score_2", "Predicted_goal_diff", "Predicted_goal_total"]].describe()#.T


# In[26]:


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


# In[ ]:





# In[ ]:





#!/usr/bin/python -tt
"""
Created on Mon Feb 06 16:49:37 2017

@author: adeacon
"""

import pandas as pd
from scipy.spatial import distance
import math
from numpy.random import permutation
import logging
# from pandas.tools.plotting import scatter_matrix
# import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import utilities

pd.set_option('display.max_columns', 500)
pd.set_option('display.expand_frame_repr', False)


def func_score(x):
    #Result,Points,PointsOpp,Win,WinDraw,Draw,DrawLoss,Loss,WinShare
    if x > 0:
        return 'Win', 3, 0, 1, 1, 0, 0, 0, 1.0
    elif x < 0:
        return 'Loss', 0, 3, 0, 0, 0, 1, 1, 0.5
    else:
        return 'Draw', 1, 1, 0, 1, 1, 1, 0, 0.0


def func_nogoal(x):
    if x == 0:
        return 1
    else:
        return 0


def build_fulldata():
    logging.info("Building fulldata dataframe from results, stadiums, managers ...")
    
    home_renames = {
            'HomeTeam': 'Team'
            , 'AwayTeam': 'TeamOpp'
            , 'FTHG': 'Goals'
            , 'FTAG': 'GoalsOpp'
            , 'HTHG': 'Goals1stHalf'
            , 'HTAG': 'Goals1stHalfOpp'
            , 'HS': 'Shots'
            , 'AS': 'ShotsOpp'
            , 'HST': 'ShotsOnTarget'
            , 'AST': 'ShotsOnTargetOpp'
            , 'HHW': 'ShotsHitWoodwork'
            , 'AHW': 'ShotsHitWoodworkOpp'
            , 'HC': 'Corners'
            , 'AC': 'CornersOpp'
            , 'HF': 'Fouls'
            , 'AF': 'FoulsOpp'
            , 'HO': 'Offsides'
            , 'AO': 'OffsidesOpp'
            , 'HY': 'YellowCards'
            , 'AY': 'YellowCardsOpp'
            , 'HR': 'RedCards'
            , 'AR': 'RedCardsOpp'
            , 'HBP': 'BookingPoints'
            , 'ABP': 'BookingPointsOpp'
            }
    away_renames = {}
    for key,val in home_renames.items():
        if val.endswith('Opp'):
            away_renames[key] = val[:-3]
        else:
            away_renames[key] = val+'Opp'
    stat_to_diff = ['Goals','Goals1stHalf','Shots','ShotsOnTarget','ShotsHitWoodwork','Corners','Fouls','Offsides','YellowCards','RedCards','BookingPoints']
    #logging.debug(list(away_renames))
    #logging.debug(list(home_renames))

    logging.info("Process results")
    results = utilities.get_master("results")
    
    homeresults = results.rename(columns=home_renames)
    homeresults['HomeAway'] = 'Home'
    #homeresults.info()
    #logging.debug(homeresults.describe(include="all"))

    awayresults = results.rename(columns=away_renames)
    awayresults['HomeAway'] = 'Away'
    #awayresults.info()
    #logging.debug(homeresults.describe(include="all"))
    
    allresults = pd.concat([homeresults,awayresults], ignore_index=True)
    allresults.drop(['FTR','HTR','Unnamed: 0'], axis=1, inplace=True)

    # logging.debug(allresults[(allresults['Team']=="Middlesbrough")&(allresults['Season']=="2006-2007")]["Date"].min())

    for stat in stat_to_diff:
        allresults[stat+'Diff'] = allresults[stat] - allresults[stat+'Opp']
        allresults['Total'+stat] = allresults[stat] + allresults[stat+'Opp']

    allresults['Saves'] = allresults['ShotsOnTargetOpp'] - allresults['GoalsOpp']
    allresults['SavesOpp'] = allresults['ShotsOnTarget'] - allresults['Goals']
    allresults['SavesDiff'] = allresults['Saves'] - allresults['SavesOpp']
    allresults['Goals2ndHalf'] = allresults['Goals'] - allresults['Goals1stHalf']
    allresults['Goals2ndHalfOpp'] = allresults['GoalsOpp'] - allresults['Goals1stHalfOpp']
    allresults['Goals2ndHalfDiff'] = allresults['GoalsDiff'] - allresults['Goals1stHalfDiff']
    #Result,Points,PointsOpp,Win,WinDraw,Draw,DrawLoss,Loss,CleanSheet,CleanSheetOpp
    allresults['Result'], allresults['Points'], allresults['PointsOpp'], allresults['Win'], allresults['WinDraw'], allresults['Draw'], allresults['DrawLoss'], allresults['Loss'], allresults['WinShare'] = zip(*allresults['GoalsDiff'].map(func_score))
    allresults['CleanSheet'] = allresults['Goals'].map(func_nogoal)
    allresults['CleanSheetOpp'] = allresults['GoalsOpp'].map(func_nogoal)
    
    #allresults['Date'] = pd.to_datetime(allresults['Date'], format="%d/%m/%y")
    
    allresults['GameWeek'] = allresults.sort_values('Date').groupby(['Season','Div','Team']).cumcount() + 1

    logging.info("Process stadiums")
    stadiums = utilities.get_master("stadiums")
    stadiums.drop(['Country','TeamFull'], axis=1, inplace=True)

    fulldata = pd.merge(allresults, stadiums, on='Team', how='left')
    #fulldata.drop(['Unnamed: 0'], axis=1, inplace=True)
    stadiums.rename(columns={'Team': 'TeamOpp'}, inplace=True)
    fulldata = pd.merge(fulldata, stadiums, on='TeamOpp', how='left', suffixes=('', 'Opp'))
    fulldata.drop(['Unnamed: 0','Unnamed: 0Opp'], axis=1, inplace=True)
    
    fulldata['EuclideanDistance'] = ( (fulldata.Latitude-fulldata.LatitudeOpp)**2 + (fulldata.Longitude-fulldata.LongitudeOpp)**2 )**0.5
    #logging.debug(100000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))

    logging.info("Process managers")
    managers = utilities.get_master("managers")
    managers.dropna(subset=["Manager"], inplace=True)

    fulldata = pd.merge(fulldata, managers, on='Team', how='left')
    #logging.debug(200000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))
    fulldata = fulldata[((fulldata['Date'] >= fulldata['DateFrom']) & (fulldata['Date'] <= fulldata['DateTo'])) | (fulldata['Manager'].isnull())]
    #logging.debug(300000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))
    fulldata.drop(['Unnamed: 0','DateFrom','DateTo','Duration','YearRange'], axis=1, inplace=True)
    fulldata = fulldata.drop_duplicates()
    #fulldata.info()
    #logging.debug(400000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))

    managers.rename(columns={'Team': 'TeamOpp'}, inplace=True)
    fulldata = pd.merge(fulldata, managers, on='TeamOpp', how='left', suffixes=('', 'Opp'))
    #logging.debug(500000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')])
    fulldata = fulldata[((fulldata['Date'] >= fulldata['DateFrom']) & (fulldata['Date'] <= fulldata['DateTo'])) | (fulldata['ManagerOpp'].isnull())]
    #logging.debug(600000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))
    fulldata.drop(['Unnamed: 0','DateFrom','DateTo','Duration','YearRange'], axis=1, inplace=True)
    fulldata = fulldata.drop_duplicates()
    #fulldata.info()
    #logging.debug(700000+len(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['TeamOpp']=="Chelsea")&(fulldata['Season']=="2016-2017")&(fulldata['HomeAway']=='Home')]))
    
    #fulldata.info()
    #logging.debug(fulldata.describe(include="all"))
    # logging.debug(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['Season']=="2006-2007")]["Date"].min()#.describe(include="all"))
    
    utilities.save_master(fulldata, "fulldata")
    #return fulldata


def fulldata_analysis():

    fulldata = utilities.get_master("fulldata")

    #logging.debug(pd.show_versions())
    fulldata.info()
    #logging.debug(fulldata.describe(include="all"))
    #logging.debug(fulldata["Div"].value_counts())
    #logging.debug(fulldata["Tier"].value_counts())
    #logging.debug(fulldata["Country"].value_counts())
    #logging.debug(fulldata["Season"].value_counts())
    #logging.debug(fulldata["Goals"].value_counts())
    #logging.debug(fulldata["Stadium"].value_counts())
    #logging.debug(fulldata["City"].value_counts())
    #logging.debug(fulldata["Manager"].value_counts())
    #logging.debug(fulldata[(fulldata['Team']=="Middlesbrough")&(fulldata['Season']=="2017-2018")].describe(include="all"))
    #logging.debug(fulldata[(fulldata['EuclideanDistance']==0)] #.head())

    buckets = ['Div','Season','Team']
    stats = 'Shots','ShotsOnTarget','Goals','Corners','Points','Win'
    filteron = 'Div'
    values = ['E0']
    aggfunc = 'mean'
    pseudocode = "SELECT "+aggfunc+" OF "+str(stats)+" WHERE "+filteron+" IS "+str(values)+" GROUPED BY "+str(buckets)
    logging.info("Analysis pseudocode: {0}".format(pseudocode))
    selected = fulldata[fulldata[filteron].isin(values)].groupby(buckets)[stats].agg([aggfunc])

    print(selected.describe(include="all"))
    # pd.scatter_matrix(selected, diagonal='kde')


def get_summary(group_key, df=None, agg_method="mean", base_filters={}, metric_mins={}, output_metrics=[]):

    if df is None:
        #fetch from master csv
        df = utilities.get_master("fulldata")
    #logging.debug(list(df.columns.values))
    
    #filter unwanted records
    #df = df[(df['Team']=="Chelsea")]
    #df = df[(df['Country']=="England")]
    #df = df[(df['Tier']==1)]
    for field, vals in base_filters.items():
        df = df[(df[field].isin(vals))]
        
#    selected_columns = [group_key]+metrics
#    df = df[selected_columns]
    df.dropna(subset=[group_key], inplace=True)
    
    #aggregate data
#   df_avg = df[[group_key]+metrics].groupby(group_key).mean()
    df_avg = df.groupby(group_key).agg(agg_method)
    #df_avg.info()
    df_cnt = df[group_key].value_counts()
    #df_cnt.columns = ['NumberOfMatches']
    #logging.debug(df_cnt)
    df = pd.concat([df_cnt, df_avg], axis=1)
    df.rename(columns = {group_key:'NumberOfMatches'}, inplace = True)
    df.drop(['Unnamed: 0'], axis=1, inplace=True)
    
    #add derived metrics
    df["ShotAccuracy"] = df["ShotsOnTarget"] / df["Shots"]
    df["ShotAccuracyOpp"] = df["ShotsOnTargetOpp"] / df["ShotsOpp"]
    df["ShotPercent"] = df["Goals"] / df["ShotsOnTarget"]
    df["ShotPercentOpp"] = df["GoalsOpp"] / df["ShotsOnTargetOpp"]
    df["SavePercent"] = df["Saves"] / df["ShotsOnTargetOpp"]
    df["SavePercentOpp"] = df["SavesOpp"] / df["ShotsOnTarget"]
    df["ShotConversion"] = df["Goals"] / df["Shots"]
    df["ShotConversionOpp"] = df["GoalsOpp"] / df["ShotsOpp"]
    df["TSR"] = df["Shots"] / df["TotalShots"]
    df["TSROpp"] = df["ShotsOpp"] / df["TotalShots"]
    df["ShotOnTargetRatio"] = df["ShotsOnTarget"] / df["TotalShotsOnTarget"]
    df["ShotOnTargetRatioOpp"] = df["ShotsOnTargetOpp"] / df["TotalShotsOnTarget"]
    df["ShotDominance"] = df["Shots"] / df["ShotsOpp"]
    df["ShotPace"] = df["TotalShots"]
    df["PDO"] = 1000 * (df["ShotPercent"] + df["SavePercent"])
    df["PDOOpp"] = 1000 * (df["ShotPercentOpp"] + df["SavePercentOpp"])
    df["%TSoTt"] = df["ShotAccuracy"] + (1 - df["ShotAccuracyOpp"])
    df["%TSoTtOpp"] = df["ShotAccuracyOpp"] + (1 - df["ShotAccuracy"])
    df["GraysonRating"] = (0.5+(df["TSR"]-0.5)*0.732**0.5)*(1.0+(df["%TSoTt"]-1.0)*0.166**0.5)*(1000+(df["PDO"]-1000)*0.176**0.5)
    df["GraysonRatingOpp"] = (0.5+(df["TSROpp"]-0.5)*0.732**0.5)*(1.0+(df["%TSoTtOpp"]-1.0)*0.166**0.5)*(1000+(df["PDOOpp"]-1000)*0.176**0.5)
    df["GraysonScore"] = 10 * (df["GraysonRating"]-363) / (695-363)
    df["GraysonScoreOpp"] = 10 * (df["GraysonRatingOpp"]-363) / (695-363)
    
    #filter unwanted aggregate data
    #df = df[(df["NumberOfMatches"] >= 50)]
    for field, val in metric_mins.items():
        df = df[(df[field] >= val)]
    
    if output_metrics:
        df = df[output_metrics]
    #df.info()
    #logging.debug(df)
    return df


def find_similar():

    group_key = "Manager"
    base_filters = {
            "Tier": [1]
            , "Country": ["England", "Spain", "Italy", "Germany"]
            }
    metric_mins = {
            "NumberOfMatches": 100
            }

    items = get_summary(group_key, base_filters=base_filters, metric_mins=metric_mins)
    items.info()

    #logging.debug(players)
    logging.debug("\nNumber of items included: "+str(len(items)))

    # Normalize all of the numeric columns
    items_normalized = (items - items.mean()) / items.std()
    items_normalized.fillna(0, inplace=True)
    #items_normalized.info()
    #logging.debug(items_normalized.describe(include="all")

    #logging.debug(players_normalized.index.values
    for item in items_normalized.index.values:
        #logging.debug("\n###############################"
        logging.debug("\n"+item)

        #selected_player = players.loc[name]
        #logging.debug(selected_player.name
        #logging.debug(selected_player.to_frame().T #.name

        # Normalize all of the numeric columns
        selected_normalized = items_normalized.loc[item]
        #logging.debug(selected_normalized

        # Find the distance between select player and everyone else.
        euclidean_distances = items_normalized.apply(lambda row: distance.euclidean(row, selected_normalized), axis=1)

        # Create a new dataframe with distances.
        distance_frame = pd.DataFrame(data={"dist": euclidean_distances, "idx": euclidean_distances.index})
        distance_frame.sort_values("dist", inplace=True)

        most_similar = distance_frame.iloc[1:4]["idx"]
        #most_similar = items.loc[nearest_neighbours]
        #logging.debug(most_similar
        logging.debug("... is similar to... ")
        logging.debug(list(most_similar.index.values))


def make_prediction():

    group_key = "Team"
    base_filters = {
            "Div":["E0"]
            }
    pred_col = 'Points'

    items = get_summary(group_key, base_filters=base_filters)

    x_columns = list(items.columns.values)
    x_columns.remove(pred_col)
    y_column = [pred_col]

    ###Generating training and testing sets

    # Randomly shuffle the index of nba.
    random_indices = permutation(items.index)
    # Set a cutoff for how many items we want in the test set (in this case 1/3 of the items)
    test_cutoff = math.floor(len(items)/3)
    # Generate the test set by taking the first 1/3 of the randomly shuffled indices.
    test = items.loc[random_indices[1:test_cutoff]]
    test.fillna(0, inplace=True)
    #test.info()
    #logging.debug(test.describe(include="all"))
    # Generate the train set with the rest of the data.
    train = items.loc[random_indices[test_cutoff:]]
    train.fillna(0, inplace=True)
    #train.info()
    #logging.debug(train.describe(include="all"))

    ###Using sklearn for k nearest neighbors
    #logging.debug("Using sklearn for k nearest neighbors...")

    from sklearn.neighbors import KNeighborsRegressor
    # Create the knn model.
    # Look at the five closest neighbors.
    knn = KNeighborsRegressor(n_neighbors=5)
    #logging.debug(knn)
    # Fit the model on the training data.
    knn.fit(train[x_columns], train[y_column])
    #logging.debug(knn)
    # Make point predictions on the test set using the fit model.
    predictions = knn.predict(test[x_columns])
    #logging.debug("\nPredicted PointsPGm:")
    #logging.debug(predictions.shape)

    ###Computing error

    # Get the actual values for the test set.
    actual = test[y_column].copy()

    # Compute the mean squared error of our predictions.
    mse = (((predictions - actual) ** 2).sum()) / len(predictions)
    logging.debug("\nMean Squared Error:")
    logging.debug(mse)

    actual["Predicted"+pred_col] = predictions
    actual["Diff"] = actual[pred_col] - actual["Predicted"+pred_col]
    logging.debug("\nActual and Predicted "+pred_col+":")
    logging.debug(actual.sort_values(["Diff"], ascending=False))


def do_classification():
    # Load dataset
    #url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    dataset = utilities.get_master("fulldata")

    #filter unwanted records and columns
    dataset = dataset[(dataset['Div']=="E0")]
    #dataset.info()
    dataset = dataset[["ShotsOnTarget", "ShotsOnTargetOpp", "Saves", "SavesOpp", "Result"]]
    dataset.dropna(subset=["ShotsOnTarget", "ShotsOnTargetOpp", "Saves", "SavesOpp", "Result"], inplace=True)
    #logging.debug(list(dataset.columns.values))

    # shape
    logging.debug(dataset.shape)

    # head
    logging.debug(dataset.head(20))

    # descriptions
    logging.debug(dataset.describe())

    # class distribution
    logging.debug(dataset.groupby('Result').size())

    # box and whisker plots
    dataset.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
    plt.show()

    # histograms
    dataset.hist()
    plt.show()

    # scatter plot matrix
    scatter_matrix(dataset)
    plt.show()

    # Split-out validation dataset
    array = dataset.values
    X = array[:,0:4]
    Y = array[:,4]
    validation_size = 0.20
    seed = 7
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

    logging.debug(X_train[:5])
    logging.debug(X_validation[:5])
    logging.debug(Y_train[:5])
    logging.debug(Y_validation[:5])

    # Test options and evaluation metric
    seed = 7
    scoring = 'accuracy'

    # Spot Check Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))
    # evaluate each model in turn
    results = []
    names = []
    for name, model in models:
    	kfold = model_selection.KFold(n_splits=10, random_state=seed)
    	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    	results.append(cv_results)
    	names.append(name)
    	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    	logging.debug(msg)

    # Compare Algorithms
    fig = plt.figure()
    fig.suptitle('Algorithm Comparison')
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

    # Make predictions on validation dataset
    logging.debug("\nPrediction using K Nearest Neighbours algorithm...")
    knn = KNeighborsClassifier()
    knn.fit(X_train, Y_train)
    predictions = knn.predict(X_validation)
    logging.debug(accuracy_score(Y_validation, predictions))
    logging.debug(confusion_matrix(Y_validation, predictions))
    logging.debug(classification_report(Y_validation, predictions))

    logging.debug("\nPrediction using Support Vector Clustering algorithm...")
    svc = SVC()
    svc.fit(X_train, Y_train)
    predictions = svc.predict(X_validation)
    logging.debug(accuracy_score(Y_validation, predictions))
    logging.debug(confusion_matrix(Y_validation, predictions))
    logging.debug(classification_report(Y_validation, predictions))


def test_soccernomics():
    pass
#        ## Soccernomics (* need financial/economic data)
#            *Avg lge pos Vs Relative wage spend
#                EPL+Champ 98-07 R^2 = 0.8872
#                40 English clubs 78-97 R^2 = 0.92
#            *Change in lge pos Vs Pre-tax profits
#            Change in lge pos Vs Change in attendance
#            Win% Vs Experience, Population, Wealth
#                International teams 1872-2001
#                    Home adv = 2/3 GoalsPG
#                    Int experience (matches) = 1/2GoalsPG
#                    *Population = 1/10 GoalsPG
#                    *GDP = 1/10 GoalsPG


def test_numbers_game():

#        ## Numbers Game (* need betting data)
#            Corners Vs Shots, Goals
#                EPL 2001/02-2010/11
    group_key = "Corners"
    base_filters = {
            "Div": ["E0"]
            , "Season": ["2001-2002", "2002-2003", "2003-2004", "2004-2005", "2005-2006", "2006-2007", "2007-2008", "2008-2009", "2009-2010", "2010-2011"]
            }
    output_metrics = ["NumberOfMatches", "Shots","ShotsOnTarget", "Goals", "Win", "WinDraw", "Points", "GraysonScore"]
    corners = get_summary(group_key, base_filters=base_filters, output_metrics=output_metrics)
    corners.info()
    logging.debug(corners)
#            Actual goal freq Vs Predicted (Poisson dist)
#                England, Germany, Spain, Italy, France 1993-2011
#            Home goals Vs Away goals (%)
#                EPL 2011/02-2010/11
#                Serie A
#                La Liga
#                Bundesliga
#            *% favourite wins Vs % gap in odds


def test_footballintheclouds():
    ### Various Shot Metrics - Premier League 2016/17
    #http://footballintheclouds.blogspot.co.uk/p/various-shot-metrics-premier-league.html
    #https://jameswgrayson.wordpress.com/2014/08/11/methodology-and-validation-of-the-team-ratings/
    group_key = "Team"
    base_filters = {
            "Div": ["E0"]
            , "Season": ["2016-2017"] #["2009-2010"]
            }
    output_metrics = ["NumberOfMatches", 'Shots', 'ShotsOpp', 'TSR', 'ShotPercent'	, 'SavePercent', 'PDO', '%TSoTt', 'GraysonRating', 'GraysonScore']
    teams = get_summary(group_key, base_filters=base_filters, output_metrics=output_metrics)
    teams.info()
    logging.debug(teams)


def boro_analysis():
    #group_key = "Season"
    group_key = "Manager"
    base_filters = {
            "Team": ["Middlesbrough"]
            #, "Div": ["E1"]
            #, "Manager": ["Aitor Karanka", "Garry Monk"]
            }
    output_metrics = [
            "NumberOfMatches",
            "Points",
            "Goals", #"GoalsOpp",
            #'Shots', 'ShotsOpp',
            #'ShotsOnTarget', 'ShotsOnTargetOpp',
            # 'TSR', #'TSROpp',
            #'ShotPercent',
            #'SavePercent',
            # 'PDO', #'PDOOpp',
            # 'GraysonScore', 'GraysonScoreOpp',
            ]
    boro = get_summary(group_key, base_filters=base_filters, output_metrics=output_metrics)
    #boro.info()
    logging.debug(boro)
    pd.scatter_matrix(boro, diagonal='kde')


def best_rivalries():
    pass
#    Best rivalries (frequency, closeness, equality, action)


def main():

    build_fulldata()
    fulldata_analysis()

#    find_similar()
#    make_prediction()
#    do_classification()

#    test_soccernomics()
#    test_numbers_game()
    # test_footballintheclouds()
    # boro_analysis()
#    best_rivalries()


if __name__ == '__main__':
    main()
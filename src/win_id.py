#!/usr/bin/python

import sys
import pickle

import pandas as pd
from pandas.tools.plotting import scatter_matrix
import numpy as np
# import matplotlib.pyplot as plt
from time import time
import numpy as np

from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV
from sklearn.cross_validation import StratifiedShuffleSplit

# import logging
# import config
import utilities

pd.set_option('float_format', '{:f}'.format)
pd.set_option('display.max_columns', 30)

# sys.path.append("../tools/")

# from feature_format import featureFormat, targetFeatureSplit
# from tester import dump_classifier_and_data, test_classifier

SHOWVIZ = True
SEED = 42
MINIMP = 0.01


def featureFormat( dictionary, features, remove_NaN=True, remove_all_zeroes=True, remove_any_zeroes=False, sort_keys = False):
    """ convert dictionary to numpy array of features
        remove_NaN = True will convert "NaN" string to 0.0
        remove_all_zeroes = True will omit any data points for which
            all the features you seek are 0.0
        remove_any_zeroes = True will omit any data points for which
            any of the features you seek are 0.0
        sort_keys = True sorts keys by alphabetical order. Setting the value as
            a string opens the corresponding pickle file with a preset key
            order (this is used for Python 3 compatibility, and sort_keys
            should be left as False for the course mini-projects).
        NOTE: first feature is assumed to be 'poi' and is not checked for
            removal for zero or missing values.
    """


    return_list = []

    # Key order - first branch is for Python 3 compatibility on mini-projects,
    # second branch is for compatibility on final project.
    if isinstance(sort_keys, str):
        import pickle
        keys = pickle.load(open(sort_keys, "rb"))
    elif sort_keys:
        keys = sorted(dictionary.keys())
    else:
        keys = dictionary.keys()

    for key in keys:
        tmp_list = []
        for feature in features:
            try:
                dictionary[key][feature]
            except KeyError:
                print "error: key ", feature, " not present"
                return
            value = dictionary[key][feature]
            if value=="NaN" and remove_NaN:
                value = 0
            tmp_list.append( float(value) )

        # Logic for deciding whether or not to add the data point.
        append = True
        # exclude 'poi' class as criteria.
        if features[0] == 'poi':
            test_list = tmp_list[1:]
        else:
            test_list = tmp_list
        ### if all features are zero and you want to remove
        ### data points that are all zero, do that here
        if remove_all_zeroes:
            append = False
            for item in test_list:
                if item != 0 and item != "NaN":
                    append = True
                    break
        ### if any features for a given data point are zero
        ### and you want to remove data points with any zeroes,
        ### handle that here
        if remove_any_zeroes:
            if 0 in test_list or "NaN" in test_list:
                append = False
        ### Append the data point if flagged for addition.
        if append:
            return_list.append( np.array(tmp_list) )

    return np.array(return_list)


def targetFeatureSplit( data ):
    """ 
        given a numpy array like the one returned from
        featureFormat, separate out the first feature
        and put it into its own list (this should be the 
        quantity you want to predict)

        return targets and features as separate lists

        (sklearn can generally handle both lists and numpy arrays as 
        input formats when training/predicting)
    """

    target = []
    features = []
    for item in data:
        target.append( item[0] )
        features.append( item[1:] )

    return target, features


def explore_dataset(features_list, data_dict, name=None, feature=None, createviz=None):
	print("\n\n")		
	df = pd.DataFrame.from_dict(data_dict, orient='index')
	# df.replace({"NaN": np.nan}, inplace=True)
	df = df[features_list]

	if name:
		print("\n\n")
		print("Name: {0}...".format(name))
		print(df.loc[name].head(20))
		return

	if feature:
		print("\n\n")
		print("Feature: {0}...".format(feature))
		print(df[df[feature].notnull()][[feature, "Win"]])
		return

	print("\n\nSHAPE...")
	print("{0} rows and {1} columns".format(df.shape[0], df.shape[1]))
	feature_counter = len(df.columns) - 1 #exclude target variable
	print("{0} features".format(feature_counter))
	# print("{0} Wins".format(df[df.Win].shape[0]))
	print("\n\nINFO...")
	df.info()
	print("\n\nDESCRIBE...")
	print(df.describe(include="all"))

	if (not SHOWVIZ):
		return
	if (not createviz):
		return

	print("\n\n")
	num_fields = df.columns.values.tolist()
	try:
		num_fields.remove("email_address")
	except ValueError:
		pass
	try:
		num_fields.remove("Win")
	except ValueError:
		pass
	print("num_fields: {0}".format(num_fields))

	print("\n\n")
	print("Plot histograms for all numeric fields...")
	df.hist(column=num_fields) #, bins=146)
	plt.savefig('histograms_{0}.png'.format(createviz))

	print("\n\n")
	print("Plot scatter matrix for all numeric fields...")
	scatter_matrix(df[num_fields], diagonal="kde")
	plt.savefig('scatter_matrix_{0}.png'.format(createviz))

	print("\n\n")
	print("Plot box plots for all numeric fields by Win...")
	df.boxplot(by="Win")
	plt.savefig('boxplot_{0}.png'.format(createviz))

	plt.show()
	return


def remove_outliers(data_dict, to_remove):
	print("\n\n")
	for outlier in to_remove:
		print("Removing {0} as not an actual individual".format(outlier))
		data_dict.pop(outlier, 0 )
	return #data_dict


def add_features(features_list, data_dict):
	print("\n\n")
	def computeFraction( Win_messages, all_messages ):
	    """ given a number messages to/from Win (numerator) 
	        and number of all messages to/from a person (denominator),
	        return the fraction of messages to/from that person
	        that are from/to a Win
	    """
	    fraction = 0.
	    
	    def isNaN(num):
	        return num != num
	        
	    if (not isNaN(float(Win_messages))) and (not isNaN(float(all_messages))):
	        fraction = float(Win_messages) / float(all_messages)

	    return fraction

	for name in data_dict:

	    data_Winnt = data_dict[name]

	    from_Win_to_this_person = data_Winnt["from_Win_to_this_person"]
	    to_messages = data_Winnt["to_messages"]
	    fraction_from_Win = computeFraction( from_Win_to_this_person, to_messages )
	    data_Winnt["fraction_from_Win"] = fraction_from_Win

	    from_this_person_to_Win = data_Winnt["from_this_person_to_Win"]
	    from_messages = data_Winnt["from_messages"]
	    fraction_to_Win = computeFraction( from_this_person_to_Win, from_messages )

	    data_dict[name].update( {"fraction_from_Win":fraction_from_Win} )
	    data_dict[name].update( {"fraction_to_Win":fraction_to_Win} )
	    data_Winnt["fraction_to_Win"] = fraction_to_Win

	    if data_dict[name]["email_address"] == "NaN":
	    	data_dict[name].update( {"has_email_address":0} )
	    else:
	    	data_dict[name].update( {"has_email_address":1} )

	new_features_list = features_list+["fraction_from_Win", "fraction_to_Win", "has_email_address"]
	print("Added new features: fraction_from_Win, fraction_to_Win, has_email_address")
	    
	# print(data_dict)
	return new_features_list


def select_features(features_list, my_dataset):
	print("\n\n")
	# print("Removing email_address as not numeric or really a useful feature anymore")
	# features_list.remove("email_address")

	### Extract features and labels from dataset for local testing
	data = featureFormat(my_dataset, features_list, sort_keys = True)
	labels, features = targetFeatureSplit(data)

	clf = DecisionTreeClassifier(random_state=1)
	clf.fit(features, labels)

	kbest = 0
	selected_features_list = ["Win"] ## always included
	print("\n\n")
	print("Finding most important features...")
	for n, imp in enumerate(clf.feature_importances_):
		print "{0}, {1}, {2}".format(n, features_list[n+1], imp)
		if imp > MINIMP:
			kbest+=1
			selected_features_list.append(features_list[n+1])

	print("Selecting {0} best features...".format(kbest))
	selector = SelectKBest(f_classif, k=kbest)
	selector.fit(features, labels)

	selected_features = selector.transform(features)

	print("\n\n")
	print("Selected {0} features (including target variable)".format(len(selected_features_list)))
	print("Selected features are: {0}".format(selected_features_list))

	return selected_features_list, labels, selected_features


def scale_features(original_features):
	print("\n\n")
	print("Rescaling features using MinMaxScaler")
	scaler = MinMaxScaler()
	# StandardScaler()
	rescaled_features = scaler.fit_transform(original_features)
	return rescaled_features


def tune_and_test_classifier(clf, params, dataset, feature_list, folds = 1000):
	## Copied from tester.py>test_classifier but with modified output

	PERF_FORMAT_STRING = "\nAccuracy: {:>0.{display_precision}f}\nPrecision: {:>0.{display_precision}f}\nRecall: {:>0.{display_precision}f}\nF1: {:>0.{display_precision}f}\nF2: {:>0.{display_precision}f}"
	# RESULTS_FORMAT_STRING = "\tTotal predictions: {:4d}\tTrue positives: {:4d}\tFalse positives: {:4d}\
		# \tFalse negatives: {:4d}\tTrue negatives: {:4d}"

	data = featureFormat(dataset, feature_list, sort_keys = True)
	labels, features = targetFeatureSplit(data)
	cv = StratifiedShuffleSplit(labels, folds, random_state = SEED)

	gcv = GridSearchCV(clf, params,cv=cv)
	gcv.fit(features,labels)
	gcv_best = gcv.best_estimator_

	true_negatives = 0
	false_negatives = 0
	true_positives = 0
	false_positives = 0
	for train_idx, test_idx in cv: 
		features_train = []
		features_test  = []
		labels_train   = []
		labels_test    = []
		for ii in train_idx:
			features_train.append( features[ii] )
			labels_train.append( labels[ii] )
		for jj in test_idx:
			features_test.append( features[jj] )
			labels_test.append( labels[jj] )
        
		### fit the classifier using training set, and test on test set
		gcv_best.fit(features_train, labels_train)
		predictions = gcv_best.predict(features_test)
		for prediction, truth in zip(predictions, labels_test):
			if prediction == 0 and truth == 0:
				true_negatives += 1
			elif prediction == 0 and truth == 1:
				false_negatives += 1
			elif prediction == 1 and truth == 0:
				false_positives += 1
			elif prediction == 1 and truth == 1:
				true_positives += 1
			else:
				print "Warning: Found a predicted label not == 0 or 1."
				print "All predictions should take value 0 or 1."
				print "Evaluating performance for processed predictions:"
				break
	try:
		total_predictions = true_negatives + false_negatives + false_positives + true_positives
		accuracy = 1.0*(true_positives + true_negatives)/total_predictions
		precision = 1.0*true_positives/(true_positives+false_positives)
		recall = 1.0*true_positives/(true_positives+false_negatives)
		f1 = 2.0 * true_positives/(2*true_positives + false_positives+false_negatives)
		f2 = (1+2.0*2.0) * precision*recall/(4*precision + recall)
		print gcv_best
		print PERF_FORMAT_STRING.format(accuracy, precision, recall, f1, f2, display_precision = 3)
		# print RESULTS_FORMAT_STRING.format(total_predictions, true_positives, false_positives, false_negatives, true_negatives)
		print ""
	except:
		print "Got a divide by zero when trying out:", gcv_best
		print "Precision or recall may be undefined due to a lack of true positive predicitons."
		f1 = 0

	if f1 <> 0 and (precision < 0.3 or recall < 0.3):
		f1 = 0

	return f1, gcv_best


def select_algorithm(X_all, y_all):
	print("\n\n")

	algos = [
			{"Name": "NB",
			"Classifier": GaussianNB(),
			"ParamGrid": {
			    },
			},
			# {"Name": "SVM",
			# "Classifier": SVC(),
			# "ParamGrid": {
			# 	# 'kernel': ['linear', 'rbf'],
			# 	# 'C': [1, 1e3, 5e3, 1e4, 5e4, 1e5],
			#  #    'gamma': ['auto', 0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1],
			#  #    'max_iter': [-1, 1, 2, 3, 4, 5],
			# 	},
			# },
			# {"Name": "KNN",
			# "Classifier": KNeighborsClassifier(),
			# "ParamGrid": {
			# 	"n_neighbors": [3, 4, 5, 6, 7, 8, 9],
			# 	"p": [1, 2, 3],
			# 	'algorithm': ['auto', 'ball_tree', 'kd_tree', 'brute'],
			#     },
			# },
			# {"Name": "ADA",
			# "Classifier": AdaBoostClassifier(),
			# "ParamGrid": {
			# 	"n_estimators": [10, 20, 30, 40, 50, 60, 70, 80],
			# 	"learning_rate": [0.5, 1.0, 1.5, 2.0],
			# 	'algorithm': ['SAMME', 'SAMME.R'],
			#     },
			# },
			# {"Name": "CART",
			# "Classifier": DecisionTreeClassifier(),
			# "ParamGrid": {
			# 	"min_samples_split": [2, 3, 4, 5],
			# 	"max_depth": [None, 4, 5, 6, 7, 8],
			# 	'criterion': ['gini', 'entropy'],
			#     },
			# },
		]

	results = []
	names = [d['Name'] for d in algos]

	best_clf = None
	best_score = 0

	print("Selecting algorithm using cross validation")
	print("With GridSearchCV for parameter tuning")
	print("Candidates are: {0}".format(names))
	for algo in algos:
		# name = algo["Classifier"].__doc__[:24].strip()
		name = algo["Name"]
		print("\n\n")
		print("{0}".format(name))

		t0 = time()
		cv_score, cv_clf = tune_and_test_classifier(algo["Classifier"], algo["ParamGrid"], my_dataset, features_list)
		print("Algorithm tuned and tested in %0.3fs" % (time() - t0))
		print("Score: {0}".format(cv_score))

		if cv_score > best_score:
			best_score = cv_score
			best_clf = cv_clf

	print("\n\n")				
	print("Best classifier:")
	print(best_clf)
	print("Best score: {0}".format(best_score))

	assert best_score > 0, "THRESHOLD NOT MET"

	print("\n\n")
	return best_clf


### Task 1: Select what features you'll use.
### features_list is a list of strings, each of which is a feature name.
### The first feature must be "Win".
# features_list = ['Win','salary'] # You will need to use more features
features_list = ['Win', 'Goals', 'GoalsOpp', 'Shots', 'ShotsOpp', 'ShotsOnTarget', 'ShotsOnTargetOpp', 'ShotsHitWoodwork', 'ShotsHitWoodworkOpp', 'Corners', 'CornersOpp', 'Fouls', 'FoulsOpp', 'Offsides', 'OffsidesOpp', 'YellowCards', 'YellowCardsOpp', 'RedCards', 'RedCardsOpp', 'BookingPoints', 'BookingPointsOpp', 'Saves', 'SavesOpp', 'CleanSheet', 'CleanSheetOpp']
# features_list = ['Win', 'Shots', 'ShotsOpp', 'ShotsOnTarget', 'ShotsOnTargetOpp', 'ShotsHitWoodwork', 'ShotsHitWoodworkOpp', 'Corners', 'CornersOpp', 'Fouls', 'FoulsOpp', 'Offsides', 'OffsidesOpp', 'YellowCards', 'YellowCardsOpp', 'RedCards', 'RedCardsOpp', 'BookingPoints', 'BookingPointsOpp', 'Saves', 'SavesOpp', 'CleanSheet', 'CleanSheetOpp']

### Load the dictionary containing the dataset
# with open("final_project_dataset.pkl", "r") as data_file:
	# data_dict = pickle.load(data_file)
data_frame = utilities.get_master("fulldata")

data_frame["col_to_index"] = data_frame["Team"] + " vs " + data_frame["TeamOpp"] + " (" + data_frame["Date"] + ")"
# data_frame = data_frame[data_frame.Country == "England"]
# data_frame = data_frame[data_frame.Season >= "2000-2001"]
data_frame.set_index('col_to_index', inplace=True) #, verify_integrity=True)
data_frame = data_frame[features_list]
# data_frame = data_frame.head(2000)
data_frame.dropna(inplace=True)
data_frame = data_frame[data_frame.index.notnull()]
data_frame = data_frame.sample(n=2000, random_state=1)

data_dict = data_frame.to_dict('index')
# print("\n\DATADICT...")
# print(data_dict)
explore_dataset(features_list, data_dict)
# sys.exit()

### Task 2: Remove outliers
# explore_dataset(features_list, data_dict, name="TOTAL")
# explore_dataset(features_list, data_dict, name="THE TRAVEL AGENCY IN THE PARK")
# remove_outliers(data_dict, ["TOTAL", "THE TRAVEL AGENCY IN THE PARK"])

### Task 3: Create new feature(s)
# features_list = add_features(features_list, data_dict)
### Store to my_dataset for easy export below.
my_dataset = data_dict

features_list, labels, features = select_features(features_list, my_dataset)
explore_dataset(features_list, data_dict)
# explore_dataset(features_list, data_dict, createviz="final")

features = scale_features(features)
# sys.exit()

### Task 4: Try a varity of classifiers
### Please name your classifier clf for easy export below.
### Note that if you want to do PCA or other multi-stage operations,
### you'll need to use Pipelines. For more info:
### http://scikit-learn.org/stable/modules/pipeline.html

# Provided to give you a starting Winnt. Try a variety of classifiers.
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
clf = select_algorithm(features, labels) #, my_dataset, features_list)
sys.exit()

### Task 5: Tune your classifier to achieve better than .3 precision and recall 
### using our testing script. Check the tester.py script in the final project
### folder for details on the evaluation method, especially the test_classifier
### function. Because of the small size of the dataset, the script uses
### stratified shuffle split cross validation. For more info: 
### http://scikit-learn.org/stable/modules/generated/sklearn.cross_validation.StratifiedShuffleSplit.html

# Example starting Winnt. Try investigating other evaluation techniques!
# from sklearn.cross_validation import train_test_split
# features_train, features_test, labels_train, labels_test = \
#     train_test_split(features, labels, test_size=0.3, random_state=42)
test_classifier(clf, my_dataset, features_list)

### Task 6: Dump your classifier, dataset, and features_list so anyone can
### check your results. You do not need to change anything below, but make sure
### that the version of Win_id.py that you submit can be run on its own and
### generates the necessary .pkl files for validating your results.

dump_classifier_and_data(clf, my_dataset, features_list)
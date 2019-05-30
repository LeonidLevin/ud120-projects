#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from matplotlib import pyplot


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )


#salaries = [(person, data_dict[person]["salary"], data_dict[person]["bonus"]) for person in data_dict if data_dict[person]["salary"] != 'NaN' and data_dict[person]["bonus"] != 'NaN']
#salaries.sort(key = lambda x : x[2], reverse=True)
#print salaries[:4]

data_dict.pop('TOTAL', 0) #removing the outlier

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    pyplot.scatter(salary, bonus)

pyplot.xlabel("salary")
pyplot.ylabel("bonus")
pyplot.show()




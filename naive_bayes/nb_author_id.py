#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

t0 = time()
classifier.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1 = time()
pred = classifier.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"

accuracy = classifier.score(features_test, labels_test)

def NBAccuracy2(pred, labels_test):
    accurate = [ii for ii in range(0, len(pred)) if pred[ii]==labels_test[ii]]
    return len(accurate) * 1.0 / len(pred)

def NBAccuracy3(pred, labels_test):
    from sklearn.metrics import accuracy_score
    return accuracy_score(pred, labels_test)

accuracy2 = NBAccuracy2(pred, labels_test)
accuracy3 = NBAccuracy3(pred, labels_test)

print "accuracy:", accuracy, accuracy2, accuracy3

#########################################################

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:00:25 2021

@author: link4

Based on https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
"""

#%% Imports
from os import path
from setup import getTSVDataFrame
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import dbHelper as dbHelper

#%% Grid search cv
# need to beat 0.9741379310344828% accurancy
'''
from sklearn.model_selection import GridSearchCV
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer(use_idf=False)),
    ('svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None))
    ])

parameters = {
    'vect__ngram_range': [(1, 1), (1, 2)],
    'tfidf__use_idf': (True, False),
    'svm__alpha': [1e-1, 1e-2, 1e-3],
    'svm__max_iter': [5, 6, 7]
    }

gridSearchSVM = GridSearchCV(pipeline, parameters, cv=5, n_jobs=-1)
gridSearchSVM.fit(X_train, y_train)

print('best score', gridSearchSVM.best_score_)
print('best params', gridSearchSVM.best_params_)
'''
#%% Function to create model

def splitXAndY(df):
    ''''
    Split dataframe to X and y
    '''
    return df['msg'], df['type']

def createNewModel(filename="model.obj"):
    
    X_train, y_train = splitXAndY(dbHelper.getMessageTableDataFrame())
    X_test, y_test = splitXAndY(getTSVDataFrame(path.join('data', 'valid-data.tsv')))
    
    pipeline = Pipeline([
        ('vect', CountVectorizer(ngram_range=(1,2))),
        ('tfidf', TfidfTransformer(use_idf=False)),
        ('svm', SGDClassifier(loss='hinge', penalty='l2', alpha=0.001, random_state=42, max_iter=5, tol=None))
    ])
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    print('accuracy', acc)
    print('Classification report', classification_report(y_test, y_pred))
    print('confusion matrix', confusion_matrix(y_test, y_pred))
    
    filehandler = open(filename, "wb")
    pickle.dump(pipeline, filehandler)
    filehandler.close()
    return acc

#%% Run
if __name__ == '__main__':
    createNewModel()
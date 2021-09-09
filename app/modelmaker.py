# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:00:25 2021

@author: link4
"""
from os import path
from setup import getTSVDataFrame
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
# Split to X and y
def splitXAndY(filePath):
    ''''
    Get the data from the TSV files and split into X and y
    '''
    df = getTSVDataFrame(path.join('data', filePath))
    return df['msg'], df['type']

X_train, y_train = splitXAndY('train-data.tsv')
X_test, y_test = splitXAndY('valid-data.tsv')

print(X_train.head())
print(y_train.head())

# Tokenize the text
#count_vect = CountVectorizer()

#X_train_counts = count_vect.fit_transform(X_train)
#print(X_train_counts.shape)

# Frequency analysis
#tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
#X_train_tf = tf_transformer.transform(X_train_counts)
#print(X_train_tf.shape)

# Classify
#svm = SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None)
'''
pipeline = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer(use_idf=False)),
    ('svm', SGDClassifier(loss='hinge', penalty='l2', alpha=1e-3, random_state=42, max_iter=5, tol=None))
    ])


pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print('accuracy', accuracy_score(y_test, y_pred))
print('Classification report', classification_report(y_test, y_pred))
print('confusion matrix', confusion_matrix(y_test, y_pred))
'''

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

#%% Final pipeline
pipeline = Pipeline([
    ('vect', CountVectorizer(ngram_range=(1,2))),
    ('tfidf', TfidfTransformer(use_idf=False)),
    ('svm', SGDClassifier(loss='hinge', penalty='l2', alpha=0.001, random_state=42, max_iter=5, tol=None))
    ])
pipeline.fit(X_train, y_train)

y_pred = pipeline.predict(X_test)

print('accuracy', accuracy_score(y_test, y_pred))
print('Classification report', classification_report(y_test, y_pred))
print('confusion matrix', confusion_matrix(y_test, y_pred))

#%% Save model
filehandler = open("model.obj", "wb")
pickle.dump(pipeline, filehandler)
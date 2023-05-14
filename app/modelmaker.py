"""The code to make the model
Created on Thu Sep  9 15:00:25 2021

@author: link4

Based on https://scikit-learn.org/stable/tutorial/text_analytics/
working_with_text_data.html"""
from os import path
from typing import Tuple
from .setup import getTSVDataFrame
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import (classification_report,
                             confusion_matrix,
                             accuracy_score)
import pickle
from . import dbHelper as dbHelper
import pandas as pd
# Functions to create model


def splitXAndY(df) -> Tuple[pd.Series, pd.Series]:
    """Split data-frame to X and y

    Returns
    -------
    pd.Series
        msg column

    pd.Series
        type column"""
    return df['msg'], df['type']


def createNewModel(filename: str = "model.obj") -> float:
    """Create a new model and save to the filename

    Parameters
    ----------
    filename: str default model.obj
        The name to save the model as

    Returns
    -------
    float
        The accuracy score"""
    X_train, y_train = splitXAndY(dbHelper.getMessageTableDataFrame())
    X_test, y_test = splitXAndY(getTSVDataFrame(path.join('data',
                                                          'valid-data.tsv')))

    pipeline = Pipeline([
        ('vect', CountVectorizer(ngram_range=(1, 2))),
        ('tfidf', TfidfTransformer(use_idf=False)),
        ('svm', SGDClassifier(loss='hinge',
                              penalty='l2',
                              alpha=0.001,
                              random_state=42,
                              max_iter=5,
                              tol=None))
    ])
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    print('accuracy', acc)
    print('Classification report', classification_report(y_test, y_pred))
    print('confusion matrix', confusion_matrix(y_test, y_pred))

    with open(filename, "wb") as filehandler:
        pickle.dump(pipeline, filehandler)
        filehandler.close()
    return acc


if __name__ == '__main__':
    createNewModel()

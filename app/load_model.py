# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:52:16 2021

@author: link4
"""
import pickle
def loadmodel(filename='model.obj'):
    '''
    Parameters
    ----------
    filename : TYPE, optional
        The filename where the model can be found. The default is 'model.obj'.

    Returns
    -------
    The model as a python object

    '''
    file = open(filename, "rb")
    model = pickle.load(file)
    file.close()
    return model
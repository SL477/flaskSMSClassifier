# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 15:56:58 2021

@author: link4
"""

def predict(model, msg):
    '''
    

    Parameters
    ----------
    model : pass in the model.
    msg : The message array.

    Returns
    -------
    Array, False is spam, true is not spam

    '''
    return model.predict(msg)

if __name__ == '__main__':
    from load_model import loadmodel
    mdl = loadmodel()
    test_messages1 = ["how are you doing today",
                   "sale today! to stop texts call 98912460324",
                   "i dont want to go. can we try it a different day? available sat",
                   "our new mobile video service is live. just install on your phone to start watching.",
                   "you have won £1000 cash! call to claim your prize.",
                   "i'll bring it tomorrow. don't forget the milk.",
                   "wow, is your arm alright. that happened to me one time too"
                  ]
    preds = predict(mdl, test_messages1)
    for i in range(len(test_messages1)):
        print(test_messages1[i], preds[i])
        
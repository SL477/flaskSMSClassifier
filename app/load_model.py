"""Get the model"""
import pickle
from .modelmaker import createNewModel


def load_model(filename: str = 'model.obj'):
    """Get the trained model

    Parameters
    ----------
    filename : TYPE, optional
        The filename where the model can be found. The default is 'model.obj'.

    Returns
    -------
    The model as a python object"""
    try:
        with open(filename, "rb") as file:
            model = pickle.load(file)
    except:
        createNewModel(filename)
        with open(filename, "rb") as file:
            model = pickle.load(file)
    return model

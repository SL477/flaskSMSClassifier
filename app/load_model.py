"""Get the model"""
import pickle


def load_model(filename: str = 'model.obj'):
    """Get the trained model

    Parameters
    ----------
    filename : TYPE, optional
        The filename where the model can be found. The default is 'model.obj'.

    Returns
    -------
    The model as a python object"""
    file = open(filename, "rb")
    model = pickle.load(file)
    file.close()
    return model

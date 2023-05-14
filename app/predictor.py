"""Predict from the model whether it is spam or ham"""


def predict(model, msg: str) -> dict:
    """Predict from the model whether it is spam or ham

    Parameters
    ----------
    model:
        pass in the model

    msg: str
        The message string

    Returns
    -------
    dict
        output (ham/spam) and the original message (message_text)"""
    res = model.predict([msg])
    output = 'ham'
    if not res:
        output = 'spam'
    return {"output": output, "message_text": msg}


if __name__ == '__main__':
    from .load_model import load_model
    mdl = load_model()
    test_messages1 = [
        "how are you doing today",
        "sale today! to stop texts call 98912460324",
        "i dont want to go. can we try it a different day? available sat",
        "our new mobile video service is live. just install on your phone to start watching.",
        "you have won £1000 cash! call to claim your prize.",
        "i'll bring it tomorrow. don't forget the milk.",
        "wow, is your arm alright. that happened to me one time too"
        ]
    # predictions = predict(mdl, test_messages1)
    # for i in range(len(test_messages1)):
    #   print(test_messages1[i], predictions[i])

    for m in test_messages1:
        print(predict(mdl, m))

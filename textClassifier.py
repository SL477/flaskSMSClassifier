import tensorflow as tf
tf.get_logger().setLevel('ERROR')
def predict_message(message_text):
    """
    This is to workout whether or not a message is spam
    """
    tf.get_logger().setLevel('ERROR')
    # Load the model
    model = tf.saved_model.load("./smsClassifierModel")
    #print(list(model.signatures.keys()))
    predTensor = tf.convert_to_tensor(message_text)
    #print("predTensor",predTensor)
    f = model.signatures['serving_default']
    prediction = f(input_1=tf.constant([[message_text]]))
    #print("prediction",prediction)
    #print("prediction type",type(prediction))
    #print("pred", prediction['dense_1'].numpy()[0][0])
    pred = prediction['dense_1'].numpy()[0][0]
    output = 'spam'
    #if prediction[0][0] > 0.5:
    if pred > 0.5:
        output = 'ham'
    #return [prediction[0][0], output, message_text]
    return {"pred": "{:.2f}".format(pred), "output":output, "message_text": message_text}

if __name__ == "__main__":
    test_messages1 = ["how are you doing today",
                   "sale today! to stop texts call 98912460324",
                   "i dont want to go. can we try it a different day? available sat",
                   "our new mobile video service is live. just install on your phone to start watching.",
                   "you have won £1000 cash! call to claim your prize.",
                   "i'll bring it tomorrow. don't forget the milk.",
                   "wow, is your arm alright. that happened to me one time too"
                  ]
    for m in test_messages1:
        print(predict_message(m))

import tensorflow as tf
import pandas as pd
import setup
import dbHelper
from os import path

def createNewModel():
    """
    This is to retrain the model off of the data in the database
    """
    df_train = dbHelper.getMessageTableDataFrame()
    df_test = getTestData()

    # Text Vectorisation
    max_Length = 250
    max_tokens_num = 5000 # Max vocab size

    vectorise_layer = tf.keras.layers.experimental.preprocessing.TextVectorization(
        output_mode='int',
        output_sequence_length=max_Length,
        max_tokens=max_tokens_num,
        standardize='lower_and_strip_punctuation',
        split='whitespace'
    )

    # Get the full dataframe to adapt the text vectorization
    # df_full = pd.concat([df_test, df_train])
    # df_full.pop('type')
    # vectorise_layer.adapt(tf.constant((df_full)))
    vectorise_layer.adapt(tf.constant(df_train['msg']))

    # Model
    text_input = tf.keras.Input(shape=(1,), dtype=tf.string)
    model = vectorise_layer(text_input)
    model = tf.keras.layers.Embedding(max_tokens_num + 1, 128)(model)
    model = tf.keras.layers.Dropout(0.5)(model)

    model = tf.keras.layers.Conv1D(128, 7, padding='valid', activation='relu', strides=3)(model)
    model = tf.keras.layers.Conv1D(128, 7, padding='valid', activation='relu', strides=3)(model)
    model = tf.keras.layers.GlobalMaxPooling1D()(model)

    model = tf.keras.layers.Dense(128, activation='relu')(model)
    model = tf.keras.layers.Dropout(0.5)(model)
    
    model = tf.keras.layers.Dense(1, activation='sigmoid')(model)

    model = tf.keras.Model(text_input, model)
    print('summary\n',model.summary())

    # Compile
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['acc'])

    # Train
    history = model.fit(df_train['msg'], df_train['type'], epochs=10)

    return model

def getTestData():
    """
    This is to get the test data
    """
    return setup.getTSVDataFrame(path.join('data','valid-data.tsv'))

def evaluateModel(model):
    """
    This is to evaluate the model and return the loss and accuracy metrics
    """
    df_test = getTestData()
    return model.evaluate(df_test['msg'], df_test['type'])

def saveModel(model, folder):
    """
    This is to save the model
    """
    folder = './' + folder
    tf.saved_model.save(model, export_dir=folder)

if __name__ == "__main__":
    # Create the model
    model = createNewModel()
    stats = evaluateModel(model)
    print('Loss:', stats[0])
    print('Accuracy:', stats[1])
    saveModel(model, 'smsClassifierModel')
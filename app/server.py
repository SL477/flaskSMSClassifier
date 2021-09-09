# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 16:10:11 2021

@author: link4
This is the Flask server
"""
#%% Imports
from flask import Flask, request, send_from_directory, url_for, redirect, jsonify
import dbHelper
from load_model import loadmodel
from predictor import predict
from modelmaker import createNewModel

#%% Routes
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))

@app.route('/link477.png')
def icon():
    return redirect(url_for('static', filename='link477.png'))

@app.route('/myStyle.css')
def style():
    return redirect(url_for('static', filename='myStyle.css'))

@app.route('/data', methods=["POST", "GET"])
def getData():
    return dbHelper.getAllData()

@app.route('/classifier.js')
def getJS():
    return redirect(url_for('static', filename='classifier.js'))

@app.route('/classifymessage', methods=['POST'])
def classify_text_message():
    msg = request.form.get('msg')
    mdl = loadmodel()
    preds = predict(mdl, msg)
    return jsonify(preds)

@app.route('/addtodb', methods=["POST"])
def addToDB():
    """
    This is to insert into the database
    """
    msg = request.form.get('msg')
    typeStr = request.form.get('typestr')
    con = dbHelper.sql_connection()
    dbHelper.insertDataIntoMessages(con,msg, typeStr)
    con.close()
    return jsonify(True)

@app.route('/updatemsg', methods=['POST'])
def updatemsg():
    """
    This is to update a message's classification in the database
    """
    msgid = int(request.form.get('msgid'))
    typeStr = int(request.form.get('typestr'))
    dbHelper.updateClassification(msgid, typeStr)
    return jsonify(True)

@app.route('/deletemsg', methods=['POST'])
def deletemsg():
    """
    Delete message
    """
    msgid = int(request.form.get('msgid'))
    dbHelper.deleteMessage(msgid)
    return jsonify(True)

# TODO 
@app.route('/retrainmodel', methods=["POST"])
def retrainModel():
    '''
    This is to retrain the model based on what is in the database

    '''
    return jsonify({'accuracy': createNewModel()})

#%% Run
if __name__ == "__main__":
    app.run()
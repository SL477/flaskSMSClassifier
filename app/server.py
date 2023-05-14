"""This is the Flask server to host the app
Created on Thu Sep  9 16:10:11 2021

@author: link4"""
from flask import Flask, request, url_for, redirect, jsonify
from . import dbHelper as dbHelper
from .load_model import load_model
from .predictor import predict
from .modelmaker import createNewModel

app = Flask(__name__, static_url_path='')


@app.route('/')
def index():
    return redirect(url_for('static', filename='index.html'))


@app.route('/data', methods=["POST", "GET"])
def getData():
    return dbHelper.getAllData()


@app.route('/classifymessage', methods=['POST'])
def classify_text_message():
    msg = request.form.get('msg')
    mdl = load_model()
    preds = predict(mdl, msg)
    return jsonify(preds)


@app.route('/addtodb', methods=["POST"])
def addToDB():
    """This is to insert into the database"""
    msg = request.form.get('msg')
    typeStr = request.form.get('typestr')
    con = dbHelper.sql_connection()
    dbHelper.insertDataIntoMessages(con, msg, typeStr)
    con.close()
    return jsonify(True)


@app.route('/updatemsg', methods=['POST'])
def update_msg():
    """This is to update a message's classification in the database"""
    msgid = int(request.form.get('msgid'))
    typeStr = int(request.form.get('typestr'))
    dbHelper.updateClassification(msgid, typeStr)
    return jsonify(True)


@app.route('/deletemsg', methods=['POST'])
def delete_msg():
    """Delete message"""
    msgid = int(request.form.get('msgid'))
    dbHelper.deleteMessage(msgid)
    return jsonify(True)


@app.route('/retrainmodel', methods=["POST"])
def retrainModel():
    """This is to retrain the model based on what is in the database"""
    return jsonify({'accuracy': createNewModel()})


if __name__ == "__main__":
    app.run()

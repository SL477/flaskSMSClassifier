from flask import Flask, request, send_from_directory, url_for, redirect, jsonify

import dbHelper
from textClassifier import predict_message

#app = Flask(__name__, static_url_path='')
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

@app.route('/classifymessage', methods=["POST"])
def classify_text_message():
    msg = request.form.get('msg')
    return jsonify(predict_message(msg))

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
    return "true"

if __name__ == "__main__":
    app.run()
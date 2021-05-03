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
    #request_data = request.get_json(force = True)
    #print("request_data",request_data)
    #msg = request_data['msg']
    #msg = request.json.get('msg')
    #print("msg", msg)
    msg = request.form.get('msg')
    print("msg", msg)
    #return json.dumps(str(predict_message(msg)))
    #return json.dumps(predict_message(msg))
    return jsonify(predict_message(msg))

if __name__ == "__main__":
    app.run()
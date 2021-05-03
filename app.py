from flask import Flask, request, send_from_directory, url_for, redirect

import dbHelper

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

if __name__ == "__main__":
    app.run()
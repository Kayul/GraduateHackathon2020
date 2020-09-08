# import sqlite3
import json
import pathlib
import os
import flask
from flask import Flask, request, render_template, send_from_directory
from flask import jsonify
data = {
    "uploadTime": "18:36",
    "id": "3",
    "GPS": 3,
    "pollution": 4
}
p = os.path.dirname(os.path.realpath(__file__))
p = os.path.join(p, "index.html")

app = flask.Flask(__name__,
                  static_url_path='',
                  static_folder='static',
                  template_folder='templates')
app.config["DEBUG"] = True


# set the project root directory as the static folder, you can set others.
#app = Flask(__name__, static_url_path='/')


# @app.route('/js/<path:path>')
# def send_js(path):
#     return send_from_directory('js', path)


# @app.route('/dataControl.js')
# def root():
#     return app.send_static_file('index.html')


@app.route("/")
@app.route("/index", methods=['GET', 'POST', 'PUT'])
def home():
    return render_template("/index.html", data=data)


@app.route('/api')
def getAllData():
    return jsonify(data)


app.run()


db = ""


def create_con():
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def getData():
    print("t")

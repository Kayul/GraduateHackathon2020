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

@app.route("/")
@app.route("/index", methods=['GET'])
def home():
    return render_template("/index.html", data=data)

@app.route('/api')
def getAllData():

    # DATABASE CODE HERE!!

    return jsonify(data)

app.run()

db = ""

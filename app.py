from datetime import time

from flask import Flask, request, jsonify, render_template
import os
from firebase_admin import credentials, firestore, initialize_app

app = Flask(__name__)

cred = credentials.Certificate('key.json')
default_app = initialize_app(cred)
db = firestore.client()
ref = db.collection('test')

if __name__ == '__main__':
    app.run()

@app.route('/RichiArschloch')
def RichiArschloch():
    return render_template('RichiArschloch.html')

@app.route('/')
def index():
    return render_template('index.html')

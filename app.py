

from flask import Flask, request, jsonify, render_template
import os


app = Flask(__name__)


if __name__ == '__main__':
    app.run()





@app.route('/')
def index():
    return render_template('index.html')

from flask import Flask
from application import app
from application import db

app = Flask(__name__)

@app.route('/')
def hello_internet():
    return "Hello Internet!"
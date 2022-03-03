from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://data.db"
app.config['SQLALCHEMY_TRACL_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from flask-app import routes
#is git working
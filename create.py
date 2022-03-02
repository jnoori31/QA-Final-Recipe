from flask-app import db
from flask-app.models import Recipes

db.drop_all()
db.create_all()

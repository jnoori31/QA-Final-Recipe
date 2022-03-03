from application import db
from application.models import Recipes

db.drop_all()
db.create_all()

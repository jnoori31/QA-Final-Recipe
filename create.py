from application import db
from application.models import Recipe, User

db.drop_all()
db.create_all()

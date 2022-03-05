from application import db
from application import bcrypt
from flask_login import UserMixin

class User(db.Model, UserMixin):
    # Define columns for user data
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) # Primary key
    username = db.Column(db.String(length=30), nullable=False, unique=True) #Username for login/register
    email = db.Column(db.String(75), nullable = False, unique = True) # Email
    password_hash = db.Column(db.String(100), nullable = False) # Password
    first_name = db.Column(db.String(50), nullable = False) # User Forename
    last_name = db.Column(db.String(50), nullable = False) # User Surname
    recipes = db.relationship('Recipe', backref='owned_user', lazy=True)

@property
def password(self):
    return self.password

@password.setter
def password(self, plain_text_password):
    self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    instructions = db.Column(db.String(400), nullable=False)
    cooked = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
from application import db

class User(db.Model):
    # Define columns for user data
    id = db.Column(db.Integer, primary_key = True, autoincrement = True) # Primary key
    email = db.Column(db.String(75), nullable = False, unique = True) # Email
    password = db.Column(db.String(100), nullable = False) # Password
    first_name = db.Column(db.String(50), nullable = False) # User Forename
    last_name = db.Column(db.String(50), nullable = False) # User Surname
    recipes = db.relationship('Item', backref='owned_user', lazy=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(300), nullable=False)
    instructions = db.Column(db.String(400), nullable=False)
    cooked = db.Column(db.Boolean, default=False)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
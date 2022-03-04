from flask import Flask
from application import app, db
from application.models import User, Recipe
from flask import render_template, request

#<.....................HOME PAGE.................>
@app.route('/', methods=['GET'])
def home_page():
    return "Hello welcome to your recipe book!"

#<.......................Logic for User Login............................>

#<>>>>>>>>>>>>>>>>>>>>>C-R-U-D for Recipe...............>
@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    recipes = Recipe.query.all()
    return render_template('read.html', recipe=recipes)
    
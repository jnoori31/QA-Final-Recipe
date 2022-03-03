from flask import Flask
from application import app, db
from application.models import Recipe, User
from flask import request

#<.....................HOME PAGE.................>
@app.route('/', methods=['GET'])
def home_page():
    return "Hello welcome to your recipe book!"

#<.......................Logic for User Login............................>

#<>>>>>>>>>>>>>>>>>>>>>C-R-U-D for Recipe...............>
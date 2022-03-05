from flask import Flask
from application import app, db
from application.models import User, Recipe
from flask import render_template, request, redirect, url_for
from application.forms import CreateForm, UpdateForm

#<.....................HOME PAGE.................>
@app.route('/', methods=['GET'])
def home_page():
    #return "Hello welcome to your recipe book!"
    return render_template('home.html')

#<.......................Logic for User Login............................>

#<>>>>>>>>>>>>>>>>>>>>>C-R-U-D for Recipe...............>
#CREATE
@app.route('/create', methods=['GET', 'POST'])
def create():
    createform = CreateForm()

    if createform.validate_on_submit():
        recipe = Recipe(name=createform.name.data, 
        description=createform.description.data,
        ingredients=createform.ingredients.data,
        instructions=createform.instructions.data,
        cooked=createform.cooked.data)
        db.session.add(recipe)
        db.session.commit()
        # Instead of rendering a template, the next line redirects the user to the endpoint for the function called 'read'.
        return redirect(url_for('home_page'))
    return render_template('create.html', form=createform)

#READ
@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    recipes = Recipe.query.all()
    return render_template('read.html', recipe=recipes)

#UPDATE
@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    recipe = Recipe.query.filter_by(name=name).first()
    
    # Prepopulate the form boxes with current values when they open the page.
    if request.method == 'GET':
        updateform.name.data = recipe.name
        updateform.description.data = recipe.description
        updateform.ingredients.data = recipe.ingredients
        updateform.instructions.data = recipe.instructions
        updateform.cooked.data = recipe.cooked
        return render_template('update.html', form=updateform)
    
    # Update the recipe in the databse when they submit
    else:
        if updateform.validate_on_submit():
            recipe.name = updateform.name.data
            recipe.description = updateform.description.data
            recipe.ingredients = updateform.ingredients.data
            recipe.instructions = updateform.instructions.data
            recipe.cooked = updateform.cooked.data
            db.session.commit()
            return redirect(url_for('read'))
    
#DELETE
@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
        recipe = Recipe.query.filter_by(name=name).first()
        db.session.delete(recipe)
        db.session.commit()
        return redirect(url_for('read'))

#BOOLEAN UPDATE
@app.route('/has_been_cooked/<name>', methods=['GET'])
def has_been_cooked(name):
    recipe = Recipe.query.filter_by(name=name).first()
    recipe.cooked = True
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/to_cook/<name>', methods=['GET'])
def to_cook(name):
    recipe = Recipe.query.filter_by(name=name).first()
    recipe.cooked = False
    db.session.commit()
    return redirect(url_for('read'))
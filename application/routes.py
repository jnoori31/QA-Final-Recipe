from application import app, db
from application.models import User, Recipe
from flask import render_template, request, redirect, url_for, flash
from application.forms import CreateForm, UpdateForm, LoginForm, RegisterForm
from flask_login import login_user, login_required, logout_user

#<.....................HOME PAGE.................>
@app.route('/', methods=['GET'])
@login_required
def home_page():
    #return "Hello welcome to your recipe book!"
    return render_template('home.html')

#<.......................Login for User Logic............................>
@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('market_page'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)



#<.......................Register for User logic............................>    
@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        create_user = User(username=form.username.data, 
                email=form.email_address.data, 
                password=form.password1.data)
        db.session.add(create_user)
        db.session.commit()
        login_user(create_user)
        flash(f"Account created successfully! You are now logged in as {create_user.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)


#<..........................LOGOUT............................>
@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))

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
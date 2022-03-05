from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Email
from application.models import User

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    ingredients = StringField('Ingredients', validators=[DataRequired(),Length(min=2,max=300)])
    instructions = StringField('Instructions', validators=[DataRequired(),Length(min=2,max=300)])
    cooked = BooleanField('Cooked?')
    submit = SubmitField('Save Recipe')

class UpdateForm(FlaskForm):
    name = StringField('Title', validators=[DataRequired(), Length(min=2,max=30)])
    description = StringField('Description', validators=[DataRequired(), Length(min=2,max=300)])
    ingredients = StringField('Ingredients', validators=[DataRequired(),Length(min=2,max=300)])
    instructions = StringField('Instructions', validators=[DataRequired(),Length(min=2,max=300)])
    cooked = BooleanField('Cooked?')
    submit = SubmitField('Update Recipe')

class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError('Email Address already exists! Please try a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')
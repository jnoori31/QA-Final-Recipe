from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

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
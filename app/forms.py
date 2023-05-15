from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register')

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class PostForm(FlaskForm):
    body = StringField('Format: YEAR | MAKE | MODEL | EXTRA', validators=[DataRequired()])
    submit = SubmitField('Add Vehicle')

class UserSearchForm(FlaskForm):
    user = StringField('user', validators=[DataRequired()])
    submit = SubmitField('Search')

class AddDealerForm(FlaskForm):
    dealer_name = StringField('Dealer Name', validators=[DataRequired()])
    dealer_location = StringField('Dealer Location', validators=[DataRequired()])
    dealer_brand = StringField('Dealer Brand', validators=[DataRequired()])
    submit = SubmitField('Add Dealership')
from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegForm(FlaskForm):
    email = StringField('Your Email Address', validators=[InputRequired(),Email()])
    username = StringField('Enter Your Username', validators=[InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')
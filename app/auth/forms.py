from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import InputRequired,Email,EqualTo
from ..models import User

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[InputRequired(),Email()])
    username = StringField('Username',validators=[InputRequired()])
    password = PasswordField('Password',validators=[InputRequired()])
    remember = BooleanField('Remember Me!')
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address', validators=[InputRequired(),Email()])
    firstname= StringField('Your First Name', validators=[InputRequired()])
    lastname= StringField('Your Last Name', validators=[InputRequired()])
    username = StringField('Enter Your Username', validators=[InputRequired()])
    password = PasswordField('Password',validators = [InputRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [InputRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("The Email is already in use!")
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError("The username is already in use!")
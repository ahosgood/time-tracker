from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField
from wtforms.validators import (Email, EqualTo, InputRequired, Length,
                                ValidationError)

from app.models import User


class SignupForm(FlaskForm):
    email_address = StringField('Email address', validators=[InputRequired(message="Email address is required"), Email()],
                                description="We'll never share your email with anyone else.")
    password = PasswordField('Password', validators=[InputRequired(message="Password is required"), Length(min=8, max=72, message="Password must be between 8 and 72 characters")],
                             description="Must be between 8 and 72 characters.")
    confirm_password = PasswordField('Confirm password', validators=[InputRequired(
        message="Confirm your password"), EqualTo('password', message="Passwords must match.")])

    def validate_email_address(self, email_address):
        user = User.query.filter_by(email_address=email_address.data).first()
        if user is not None:
            raise ValidationError('Email address is already in use, please log in')


class LoginForm(FlaskForm):
    email_address = StringField('Email address', validators=[
                                InputRequired(message="Email address is required"), Email()])
    password = PasswordField('Password', validators=[InputRequired(message="Password is required"), Length(min=8, max=72, message="Password must be between 8 and 72 characters")],
                             description="Must be between 8 and 72 characters")
    remember_me = BooleanField('Remember me')

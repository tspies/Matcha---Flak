from flask_wtf                      import FlaskForm
from wtforms                        import StringField, PasswordField, SubmitField, BooleanField
from wtforms.fields.html5           import EmailField
from wtforms.validators             import DataRequired, Length, Email, EqualTo, ValidationError

from matcha.models                  import User


class LoginForm(FlaskForm):

    email           = EmailField('Email:', validators=[DataRequired(), Email()])
    submit          = SubmitField('Log In')
    password        = PasswordField('Password', validators=[DataRequired()])
    remember        = BooleanField("Remember Me")


class SignupForm(FlaskForm):

    email           = EmailField('Email:', validators=[DataRequired(), Email()])
    username        = StringField('Username:', validators=[DataRequired(), Length(min=3, max=20)])
    password        = PasswordField('Password', validators=[DataRequired()])
    pswd_confirm    = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit          = SubmitField('Signup')

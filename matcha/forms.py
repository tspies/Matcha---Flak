from flask_wtf                              import FlaskForm
from wtforms                                import SubmitField, PasswordField, BooleanField, StringField
from wtforms.fields.html5                   import EmailField


class LoginForm(FlaskForm):

    email           = EmailField('Email:')
    submit          = SubmitField('Log In')
    password        = PasswordField('Password')
    remember        = BooleanField("Remember Me")


class SignupForm(FlaskForm):

    email           = EmailField('Email:')
    username        = StringField('Username:')
    password        = PasswordField('Password')
    pswd_confirm    = PasswordField('Confirm Password')
    submit          = SubmitField('Signup')


class ForgotPasswordForm(FlaskForm):

    email           = StringField('Email:')
    submit          = SubmitField('Send Reset Link')


class ResetPasswordForm(FlaskForm):

    email           = StringField('Email:')
    password        = PasswordField('New Pssword:')
    pswd_confirm    = PasswordField('Confirm Password')
    submit          = SubmitField('Send Reset Link')
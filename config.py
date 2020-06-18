DEBUG = True # Turns on debugging features in Flask
BCRYPT_LEVEL = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com" # For use in application emails
# import os
# from
# basedir = os.path.abspath(os.path.dirname(__file__))
#
#
# class Config(object):
#
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'sqlite:///' + os.path.join(basedir, 'matcha.db')
#
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
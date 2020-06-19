from flask                                  import Flask
from flask_sqlalchemy                       import SQLAlchemy
from flask_bcrypt                           import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = "orangepotato"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matchadb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from matcha import models, routes, forms
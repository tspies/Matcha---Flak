from flask                                  import Flask
from flask_sqlalchemy                       import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "orangepotato"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matchadb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from matcha import models, routes
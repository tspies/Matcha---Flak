import sqlite3

from flask import Flask, g
from contextlib                             import closing
from flask_bcrypt                           import Bcrypt


SECRET_KEY = "orangepotato"
DATABASE = 'database.db'
TEST_DATABASE = ':memory:'

app = Flask(__name__)
app.config.from_object(__name__)
# app.config['SECRET_KEY'] = "orangepotato"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matchadb.sqlite3'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from matcha1 import routes
bcrypt = Bcrypt(app)


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read().decode('utf-8'))
        if db.commit():
            print("DATABASE Created")


@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(exception):
    g.db.close()



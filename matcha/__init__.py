import sqlite3
from contextlib             import closing

from flask                  import Flask, g
from flask_bcrypt           import Bcrypt
from flask_mail             import Mail

MAIL_SERVER = 'smtp.gmail.com'
MAIL_DEFAULT_SENDER = 'noreply@matcha.com'
MAIL_USERNAME = 'matchadatingxxx@gmail.com'
MAIL_PASSWORD = 'q1w2e3r4t5!'
MAIL_PORT = 465
MAIL_USE_TSL  = False
MAIL_USE_SSL = True

SECRET_KEY = "orangepotato"
DATABASE = 'database.db'
TEST_DATABASE = ':memory:'

app = Flask(__name__)
app.config.from_object(__name__)
bcrypt = Bcrypt(app)
mail = Mail(app)

from matcha import views


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


def query_db(query, args=(), one=False, commit=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.desciption[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv
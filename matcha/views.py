import sqlite3

from flask import render_template, g, request, flash

from matcha import app
from matcha.forms import LoginForm, SignupForm
from matcha.user_lib.create_user import user_lib_create_user
from matcha.validate_lib.signup import validate_lib_signup_form


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect("database.db")
    return db


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


@app.route("/")
def splash():
    return render_template("splash.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    form = LoginForm()
    user = query_db("SELECT * FROM users")
    print(user)
    # if form.validate_on_submit():
    #     user = check_exits_user_lib(form)
    #     if user:
    #         login_user(user, remember=form.remember.data)
    #         flash(f'You are logged in, welcome {user.username}', 'success')
    #         return redirect(url_for('home'))
    return render_template("login.html", form=form)


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    users = query_db("SELECT * FROM users")
    for user in users:
        print(user)
    form = SignupForm()
    if request.method == "POST":
        if validate_lib_signup_form(form):
            user_lib_create_user(form)
            flash("Signed In!", 'success')
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     if create_user_lib(form, hashed_password):
    #         flash(f'Account created for {form.email.data}', 'success')
    #         return redirect(url_for('login'))

    return render_template('signup.html', form=form)
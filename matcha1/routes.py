from flask import render_template, request, url_for, redirect, session, flash, Blueprint
# from match
# a.forms import LoginForm, SignupForm
from matcha1 import app, bcrypt
from flask_login import login_user, current_user, logout_user
# from matcha.user_lib.create_user import create_user as create_user_lib
# from matcha.user_lib.check_exists_user import check_exists_user as check_exits_user_lib
#

# @app.route("/test")
# def testdb():
#     print("TEST TEST TEST")
#     for user in query_db("SELECT * FROM users"):
#         print(f"'{user['username']}', '{user['email']}'")


@app.route("/")
def splash():
    return render_template("splash.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = LoginForm()
    # if form.validate_on_submit():
    #     user = check_exits_user_lib(form)
    #     if user:
    #         login_user(user, remember=form.remember.data)
    #         flash(f'You are logged in, welcome {user.username}', 'success')
    #         return redirect(url_for('home'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('splash'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    # if current_user.is_authenticated:
    #     return redirect(url_for('home'))
    # form = SignupForm()
    # if form.validate_on_submit():
    #     hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    #     if create_user_lib(form, hashed_password):
    #         flash(f'Account created for {form.email.data}', 'success')
    #         return redirect(url_for('login'))

    return render_template('signup.html', form=form)


@app.route('/home')
def home():
    return render_template("home.html", username="test")


@app.route('/profile_update')
def profile_update():
    return render_template("profile_update.html")


@app.route('/browse')
def browse():
    return "<h1>BROWSE</h1>"
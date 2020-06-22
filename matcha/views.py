import sqlite3

from flask                                      import render_template, g, request, flash, session, redirect, url_for

from matcha                                     import app
from matcha.forms                               import LoginForm, SignupForm
from matcha.validate_lib.email import validate_lib_email_verification
from matcha.validate_lib.login                  import validate_lib_login_form
from matcha.validate_lib.logout import validate_lib_logout_user
from matcha.validate_lib.signup                 import validate_lib_signup_form, validate_lib_send_verification_email
from matcha.user_lib.create_user                import user_lib_create_user


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
    if 'logged_in ' in session:
        if session['logged_in']:
            return redirect(url_for('home'))
    session['logged_in'] = False
    return render_template("splash.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    print(session['logged_in'])
    if not session['logged_in']:
        form = LoginForm()
        if request.method == "POST":
            return validate_lib_login_form(form)
        else:
            return render_template("login.html", form=form)
    return redirect(url_for('home'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if 'logged_in' in session:
        if not session['logged_in']:
            if request.method == "POST":
                if validate_lib_signup_form(form):
                    validate_lib_send_verification_email(form)
                    user_lib_create_user(form)
                    flash("You have Signed up!", 'success')
                    print(form.email.data)
                    return redirect(url_for('unverified'))
            return render_template('signup.html', form=form)
        else:
            return redirect(url_for('home'))
    return render_template('signup.html', form=form)


@app.route("/logout")
def logout():
    return validate_lib_logout_user()


@app.route('/home')
def home():
    if session.get('logged_in'):
        return render_template("home.html")
    return redirect(url_for('splash'))


@app.route('/not_verified/')
def unverified():
    return render_template("unverified.html")


@app.route('/verification/<token>')
def verification( token):
    print(token)
    return validate_lib_email_verification(token)


@app.route('/profile_update')
def profile_update():
    return render_template("profile_update.html")
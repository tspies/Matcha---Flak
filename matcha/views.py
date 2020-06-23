import sqlite3

from flask                                      import render_template, g, request, flash, session, redirect, url_for

from matcha                                     import app
from matcha.forms                               import LoginForm, SignupForm, ForgotPasswordForm, ResetPasswordForm, ProfileUpdateForm
from matcha.user_lib.profile                    import user_lib_validate_profile_update_form, user_lib_populate_profle_update_form
from matcha.user_lib.get_user                   import user_lib_get_user
from matcha.validate_lib.email                  import validate_lib_email_verification, validate_lib_forgot_password, validate_lib_reset_password
from matcha.validate_lib.login                  import validate_lib_login_form
from matcha.validate_lib.logout                 import validate_lib_logout_user
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
    if 'logged_in' in session:
        if not session['logged_in']:
            form = LoginForm()
            if request.method == "POST":
                return validate_lib_login_form(form)
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
                    return redirect(url_for('login'))
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
        users = query_db("SELECT * FROM users WHERE NOT username=?", (session['username'],))
        return render_template("home.html", users=users)
    return redirect(url_for('splash'))


@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if request.method == "POST":
        return validate_lib_forgot_password(form)
    return render_template('forgot_password.html', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    form = ResetPasswordForm()
    if request.method == "POST":
        return validate_lib_reset_password(form, token)
    return render_template("reset_password.html", form=form, token=token)


@app.route('/not_verified')
def unverified():
    return render_template("unverified.html")


@app.route('/verification/<token>')
def verification( token):
    print(token)
    return validate_lib_email_verification(token)


@app.route('/profile_update', methods=['GET', 'POST'])
def profile_update():
    if 'logged_in' in session:
        if session['logged_in']:
            if request.method == "POST":
                form = ProfileUpdateForm()
                user = user_lib_get_user(session['username'])
                return user_lib_validate_profile_update_form(form, user)
            else:
                form = ProfileUpdateForm()
                user = user_lib_get_user(session['username'])
                form = user_lib_populate_profle_update_form(form, user)

            return render_template("profile_update.html", form=form, user=user)
    return redirect(url_for('splash'))


@app.route('/profile_view/<username>')
def profile_view(username):
    user = query_db("SELECT * FROM users WHERE username=?", (username,), True)
    if user:
        return render_template("profile_view.html", user=user)
    else:
        flash('That user does not exist', 'danger')
        return redirect(url_for('home'))
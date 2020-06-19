from flask                                  import render_template, request, url_for, redirect, session, flash
from matcha.forms                           import LoginForm, SignupForm
from matcha                                 import app, bcrypt
from matcha.user_lib.create_user            import create_user as create_user_lib

@app.route("/")
def splash():
    return render_template("splash.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if request.method == 'POST':
    #     if request.form:
    #         username = request.form['username']
    #         password = request.form['password']
    #         email    = request.form['email']
    #         if email and password and username:
    #             usercheck = User.query.filter_by(username=username)
    #         else:
    #             return render_template("login.html")
    #         if usercheck:
    #             flash("A user with that usernmae or email already exists.")
    #             return render_template("login.html")
    #         else:
    #             user = User(username=username, password=password, email=email)
    #             db.session.add(user)
    #             db.session.commit()
    #             session['username'] = username
    #             return redirect(url_for("home"))
    #     else:
    #         return redirect(url_for('login'))
    # else:
    if form.validate_on_submit():
        flash(f'You are logged, welcome', 'success')
        session['email'] = form.email.data
        return redirect(url_for('home'))
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    session.pop('email', None)
    return redirect(url_for('splash'))


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user_check = create_user_lib(form, hashed_password)
        if user_check:
            flash(f'Account created for {form.email.data}', 'success')
            return redirect(url_for('login'))
        else:
            flash(f'A user with that email or username already exists', 'danger')

    return render_template('signup.html', form=form)


@app.route('/home')
def home():
    if "email" in session:
        email = session['email']
        return render_template("home.html", username=email )
    else:
        return redirect(url_for("login"))


# @app.route('/login')
# def login():
#     # return render_template("")

@app.route('/profile/<username>')
def profile(username):
    return f"<h1>PROFILE PAGE:</h1> {username}"


@app.route('/browse')
def browse():
    return "<h1>BROWSE</h1>"
from flask                                  import render_template, request, url_for, redirect, session, flash
from sqlalchemy                             import or_
from matcha.models                          import User
from matcha                                 import app, db


@app.route("/")
def splash():
    return render_template("splash.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form:
            username = request.form['username']
            password = request.form['password']
            email    = request.form['email']
            if email and password and username:
                usercheck = User.query.filter_by(username=username)
            else:
                return render_template("login.html")
            if usercheck:
                flash("A user with that usernmae or email already exists.")
                return render_template("login.html")
            else:
                user = User(username=username, password=password, email=email)
                db.session.add(user)
                db.session.commit()
                session['username'] = username
                return redirect(url_for("home"))
        else:
            return redirect(url_for('login'))
    else:
        return render_template("login.html")


@app.route('/home')
def home():
    if "username" in session:
        username = session['username']
        return render_template("home.html", username=username)
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
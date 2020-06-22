from flask import g, flash, redirect, url_for, render_template, current_app
from itsdangerous       import URLSafeTimedSerializer


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


def validate_lib_email_verification(token):

    username = decode_token(token)
    check = query_db("SELECT * FROM users WHERE username=?", (username,), True)
    print(check)
    if check:
        update_verified(username)
        flash("Email verified! Please login to continue.", 'success')
        return redirect(url_for('login'))
    else:
        flash("There seems to be an error with your token, would you like s to resend the token?", 'danger')
    return render_template("verification.html")


def update_verified(username):
    query_db("UPDATE users SET verified=True WHERE username=?", (username,))
    g.db.commit()


def decode_token(token):
    serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])

    try:
        username = serializer.loads(
            token,
            salt='email-confirm-salt',
            max_age=3600
        )
        return username
    except ValueError as e:
        return False
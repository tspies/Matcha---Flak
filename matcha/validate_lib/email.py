from matcha             import bcrypt
from flask              import g, flash, redirect, url_for, render_template


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


def validate_lib_email_verification(email, token):

    if bcrypt.check_password_hash(token, email):
        flash("Email verified!", 'success')
        return redirect(url_for('login'))
    else:
        flash("There seems to be an error with your token, would you like s to resend the token?", 'danger')
    return render_template("verification.html")
import re
from flask import flash, g


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


def validate_lib_signup_form(form):
    valid = True

    username = query_db("SELECT * FROM users WHERE username = ?", (form.username.data,))
    email = query_db("SELECT * FROM users WHERE email = ?", (form.email.data,))
    print(username)
    print(email)
    print(form.password.data)
    if username:
        flash("That username is already in use, please choose another one.", 'danger')
        return False
    if email:
        flash("That email is already in in use, plese choose another one.", 'danger')
        return False
    if not re.search("@", form.email.data):
        flash("Please us a valid email address, with a '@' symbol.", 'danger')
        return False
    if not valid_password(form.password.data):
        flash("Password is Invlaid please use a password between 6 and 15 character with at least one number, special character, one uppler case letter and on lower case letter with no spaces", 'danger')
        return False
    if not form.password.data == form.pswd_confirm.data:
        flash("Password and Confirm password do not match", 'danger')
        return False

    return valid


def valid_password(password):

    valid = False

    while 1:
        if len(password) < 6 or len(password) > 15:
            print("Broke on len")
            break
        elif not re.search("[a-z]", password):
            print("Broke on az")
            break
        elif not re.search("[0-9]", password):
            print("Broke on 09")
            break
        elif not re.search("[A-Z]", password):
            print("Broke on AZ")
            break
        elif not re.search("[!@#$%^&*()]", password):
            print("Broke on !@#")
            break
        elif re.search("\s", password):
            print("Broke on space")
            break
        else:
            valid = True
            break
    print(valid)
    return valid


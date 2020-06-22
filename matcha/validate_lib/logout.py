from flask import session, redirect, url_for


def validate_lib_logout_user():
    session.pop('username', None)
    session.pop('logged_in', None)
    return redirect(url_for('splash'))
from flask          import flash

from matcha.models  import User


def create_user(form, hashed_password):

    new_user = False

    username_check  = User.query.filter_by(username=form.username.data).first()
    email_check     = User.query.filter_by(email=form.email.data).first()

    if username_check or email_check:
        if username_check:
            flash(f'A user with that username already exists, please choose another', 'danger')
        if email_check:
            flash(f'A user with that email already exists, please choose another', 'danger')
    else:
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        new_user = True
    return new_user




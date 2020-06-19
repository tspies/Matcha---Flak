from matcha.models import User
from sqlalchemy     import or_
from matcha         import db


def create_user(form, hashed_password):

    new_user = False

    user_check = False

    if not user_check:
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        new_user = True
    return new_user
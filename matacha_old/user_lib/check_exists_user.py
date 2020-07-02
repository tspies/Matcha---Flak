from matcha.models import User
from matcha         import bcrypt


def check_exists_user(form):
    user = User.query.filter_by(email=form.email.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
        return user
    return None

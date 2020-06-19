from matcha             import db
from datetime           import datetime
from sqlalchemy_utils   import ChoiceType


class User(db.Model):

    GENDER_TYPES = [
        ('man', 'Man'),
        ('woman', 'Woman'),
        ('other', 'Other'),
    ]

    SEX_TYPES = [
        ('man', 'Man'),
        ('woman', 'Woman'),
        ('other', 'Other'),
    ]

    FAME_RATES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]

    __tablename__   = 'users'
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(50))
    email           = db.Column(db.String(50))
    password        = db.Column(db.String(60))
    likes           = db.Column(db.Integer, default=0)
    matches         = db.Column(db.Integer, default=0)
    bio             = db.Column(db.String(150), default="This is my Bio!")
    gender          = db.Column(ChoiceType(GENDER_TYPES))
    sex_orintation  = db.Column(ChoiceType(SEX_TYPES))
    fame_rate       = db.Column(ChoiceType(FAME_RATES))
    geo_location    = db.Column(db.String(150))
    date_joined     = db.Column(db.DateTime(), default=datetime.now)
    last_online     = db.Column(db.DateTime())

    # def __init__(self, username):
    #     self.username   = username
    def __repr__(self):
        return f'<User {self.username}> <{self.email}>'
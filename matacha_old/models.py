

class User:

    def __int__(self, username, email, password):
        self.username   = username
        self.email      = email
        self.password   = password

    def __repr__(self):
        return f"Matcha User('{self.username}', '{self.email}', '{self.password}')"
    # GENDER_TYPES = [
    #     ('man', 'Man'),
    #     ('woman', 'Woman'),
    #     ('other', 'Other'),
    # ]
    #
    # SEX_TYPES = [
    #     ('man', 'Man'),
    #     ('woman', 'Woman'),
    #     ('other', 'Other'),
    # ]
    #
    # FAME_RATES = [
    #     ('1', '1'),
    #     ('2', '2'),
    #     ('3', '3'),
    #     ('4', '4'),
    #     ('5', '5'),
    # ]
    #
    # __tablename__   = 'users'
    # id              = db.Column(db.Integer, primary_key=True)
    # username        = db.Column(db.String(50))
    # email           = db.Column(db.String(50))
    # password        = db.Column(db.String(60))
    # likes           = db.Column(db.Integer, default=0)
    # matches         = db.Column(db.Integer, default=0)
    # bio             = db.Column(db.String(150), default="This is my Bio!")
    # gender          = db.Column(ChoiceType(GENDER_TYPES))
    # sex_orintation  = db.Column(ChoiceType(SEX_TYPES))
    # fame_rate       = db.Column(ChoiceType(FAME_RATES))
    # geo_location    = db.Column(db.String(150))
    # date_joined     = db.Column(db.DateTime(), default=datetime.now)
    # last_online     = db.Column(db.DateTime())
from db import db

class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(55))
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def json(self):
        return { 'username': self.username }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).filter()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
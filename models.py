from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

db = SQLAlchemy()

class Dictionary(db.Model):
    __tablename__ = 'dictionary'

    id = db.Column(db.Integer, primary_key=True)
    amharic = db.Column(db.String(200))
    english = db.Column(db.TEXT)
    wordtype = db.Column(db.String(10))
    reference = db.Column(db.String(20))

    def __init__(self, amharic, english, wordtype=None, reference=None):
        self.amharic = amharic
        self.english = english
        self.wordtype = wordtype
        self.reference = reference

    def serialize(self):
        return {
        'id': self.id,
        'amharic': self.amharic,
        'english': self.english,
        'wordtype': self.wordtype,
        'reference': self.reference
        }


    def __repr__(self):
        return f"<Dictionary {self.amharic}>"

'''
class Bookmark(db.Model):
    __tablename__ = 'bookmark1'

    id = db.Column(db.Integer, primary_key=True)
    # dictionary = db.relationship('Dictionary', backref='bookmark', lazy=True)
    dict_id = db.Column(db.Integer, db.ForeignKey('dictionary1.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, dict_id):
        self.dict_id = dict_id

    def serialize(self):
        return {
        'id': self.id,
        'dict_id': self.dict_id,
        'date': self.date
        }

    def __repr__(self):
        return f"<Bookmark {self.dict_id}>"

class History(db.Model):
    __tablename__ = 'history1'

    id = db.Column(db.Integer, primary_key=True)
    # dictionary = db.relationship('Dictionary', backref='history', lazy=True)
    dict_id = db.Column(db.Integer, db.ForeignKey('dictionary1.id'))
    date = db.Column(db.DateTime, default=datetime.utcnow)


    def __init__(self, dict_id):
        self.dict_id = dict_id
    

    def serialize(self):
        return {
            'id': self.id,
            'dict_id': self.dict_id,
            'date': self.date
        }


    def __repr__(self):
        return f"<History {self.dict_id}>"

'''
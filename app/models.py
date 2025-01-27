from app import db


class Dictionary(db.Model):
    __tablename__ = 'dictionary'

    id = db.Column(db.Integer, primary_key=True)
    amharic = db.Column(db.String(200), index=True)
    english = db.Column(db.TEXT)
    wordtype = db.Column(db.String(20))
    reference = db.Column(db.String(200))

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

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dictionary(db.Model):
  __tablename__ = 'dictionary'

  id = db.Column(db.Integer)
  amharic = db.Column(db.String())
  english = db.Column(db.String())
  wordtype = db.Column()
  reference = db.Column()

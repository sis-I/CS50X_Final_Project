from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dictionary(db.Model):
  __tablename__ = 'dictionary1'

  id = db.Column(db.Integer, primery_key=True)
  amharic = db.Column(db.String(200))
  english = db.Column(db.TEXT)
  wordtype = db.Column(db.String(10))
  reference = db.Column(db.String(20))

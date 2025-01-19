from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database
    db.init_app(app)
    migrate = Migrate(app, db)
    sess = Session(app)

    with app.app_context():
        from app import routes, models

    return app

# 
app = create_app()
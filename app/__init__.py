from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Enable CORS
    cors = CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialize the database
    db.init_app(app)
    migrate = Migrate(app, db)
    sess = Session(app)

    with app.app_context():
        from app import routes, models

    return app

# 
app = create_app()
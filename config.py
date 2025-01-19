import os
import uuid

class Config:
    SECRET_KEY = os.getenv('SECRET_KY') or str(uuid.uuid4())

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://neondb_owner:joaK7L8ybSNE@ep-curly-sky-a26pjcpp.eu-central-1.aws.neon.tech/neondb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session configuration
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
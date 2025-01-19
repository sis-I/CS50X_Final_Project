import os
import uuid
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KY') or str(uuid.uuid4())

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_UNPOOLED') or 'postgresql://neondb_owner:joaK7L8ybSNE@ep-curly-sky-a26pjcpp.eu-central-1.aws.neon.tech/neondb?sslmode=require'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session configuration
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
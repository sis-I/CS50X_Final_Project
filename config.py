import os
import uuid
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KY') or str(uuid.uuid4())

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_UNPOOLED') or os.getenv('DATABASE_URL') # last for local development
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Session configuration
    SESSION_TYPE = 'filesystem' # Later user redis for session management
    SESSION_PERMANENT = False

    # Configuration for session to deploy on Vercel
    SESSION_FILE_DIR = os.path.join(os.getcwd(), 'flask_session')
    SESSION_FILE_THRESHOLD = 100

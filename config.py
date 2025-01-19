import os
import uuid

class Config:
    SECRET_KEY = os.getenv('SECRET_KY') or str(uuid.uuid4())
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://posgres:password@localhost:port/db_name'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
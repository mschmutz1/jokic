import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://localhost/BettingLines"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

    

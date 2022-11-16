from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base configuration"""

    # Flask specific
    SECRET_KEY = environ.get('SECRET_KEY')
    TEMPLATES_FOLDER = 'templates'
    STATIC_FOLDER = 'static'
    LESS_BIN = '/Users/dmd/.nvm/versions/node/v18.12.1/bin/lessc'
    ASSETS_AUTO_BUILD = True

class DevelopmentConfiguration(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    ASSETS_DEBUG = True

class ProductionConfiguration(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABASE_URI = environ.get('DEV_DATABASE_URI')
    ASSETS_DEBUG = False
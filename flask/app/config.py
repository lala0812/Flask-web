import os

# basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):         #dialect://username:password@host:port/database
    #SQLALCHEMY
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@localhost:5432/flask"
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
    #SECERT_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'LALA-SO-GREAT'
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY') or 'LALA-SO-GOOD'
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY') or 'LALA-SO-GOOD'
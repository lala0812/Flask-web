from flask import Flask
from flask_bootstrap import Bootstrap4
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from app.config import Config

app = Flask(__name__)#__name__ 代表目前執行的模組 
app.config.from_object(Config)
bootstrap = Bootstrap4(app)
db = SQLAlchemy(app) 
bcrypt = Bcrypt(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'
from app.routes import *



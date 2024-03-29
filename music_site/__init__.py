import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '3dff720eba7a4a3885fef9935674faeb'
app.config['SQLALCHEMY_DATABASE_URI'] = p.replace("postgres://", "postgresql://", 1) if (p := os.environ.get('DATABASE_URL')) else 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from . import routes

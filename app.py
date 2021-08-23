from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from playhouse.flask_utils import FlaskDB
import os


# setup FLASK env
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = os.urandom(16).hex()
app.config["DATABASE"] = os.environ.get("DATABASE_URL", "sqlite:///betsy.db")


# flask-mail env
mail = Mail(app)
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USERNAME"] = os.environ.get("BETSY_EMAIL")
app.config["MAIL_PASSWORD"] = os.environ.get("BETSY_PASSWORD")
app.config["MAIL_USE_TLS"] = True
# wrapper for peewee database
db_wrapper = FlaskDB(app)
db = db_wrapper.database

# flask-login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "You need to be logged in to view this page."
login_manager.login_message_category = "warning"


import routes
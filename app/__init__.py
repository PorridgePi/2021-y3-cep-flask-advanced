from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    return app

app = create_app()

app.secret_key = "thisisasecret"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = "login"
login.login_message = "You will need to login to access this totally top secret material!"
login.login_message_category = "danger"

from app import views, models

@app.cli.command("initdb")
def reset_db():
    # Reset database with dummy data
    db.drop_all()
    db.create_all()
    models.insert_dummy_data(db)

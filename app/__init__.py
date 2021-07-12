from flask_bootstrap import Bootstrap
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

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

from app import views, models

@app.cli.command("initdb")
def reset_db():
    # Reset database with dummy data
    db.drop_all()
    db.create_all()
    models.insert_dummy_data(db)

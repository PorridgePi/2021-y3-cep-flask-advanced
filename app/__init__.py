from flask_bootstrap import Bootstrap
from flask import Flask

def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    return app

app = create_app()

app.secret_key = "thisisasecret"

from app import views

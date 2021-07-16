from enum import unique
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login

from flask_login import UserMixin

class User(db.Model, UserMixin):
    # To use a different name in the table, provide an optional first argument which is a string.
    id = db.Column(db.Integer, primary_key=True) # Primary key (multiple primary keys for compound primary key)
    username = db.Column(db.String(50), unique=True) # Type of column is the first argument
    password = db.Column(db.String(256))
    email = db.Column(db.String(120), index=True, unique=True)
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return "<User {}>".formate(self.username)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

@login.user_loader # required to provide a callback function that will load the user object
def load_user(user_id):
    return User.query.get(int(user_id))

def insert_dummy_data(db):
    admin = User(username="admin", email="admin@example.com")
    guest = User(username="guest", email="guest@example.com")
    admin.set_password("secretpassword")
    guest.set_password("secretpassword")
    db.session.add(admin)
    db.session.add(guest)
    db.session.commit()

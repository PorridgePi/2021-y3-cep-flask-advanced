from enum import unique
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
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

def insert_dummy_data(db):
  admin = User(username="admin", email="admin@example.com", password="secretpassword")
  guest = User(username="guest", email="guest@example.com", password="secretpassword")
  db.session.add(admin)
  db.session.add(guest)
  db.session.commit()

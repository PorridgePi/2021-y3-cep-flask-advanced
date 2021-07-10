from app import app
from flask import render_template

# routes are defined here

@app.route('/')
def root():
    return "Hello, World!"

@app.route('/potato')
def potato():
    return render_template("potato.html")

@app.route('/bootstrap')
def bootstrap():
    return render_template("bootstrap.html")

@app.route('/form')
def form():
    return render_template("form.html")
from app import app
from flask import render_template

from app.form import TaskForm

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

@app.route("/wtform")
def wtform():
    form = TaskForm()
    return render_template("wtform.html", form=form)

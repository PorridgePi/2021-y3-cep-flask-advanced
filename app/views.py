from flask_login import login_user
from app import app

from flask.helpers import url_for
from flask import render_template, request, flash, redirect

from app.models import User
from app.form import TaskForm, LoginForm 

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

@app.route("/wtform", methods=["GET", "POST"])
def wtform():
    form = TaskForm()

    if request.method == "POST":
        if form.validate_on_submit():
            return "<h1>Form</h1> <br> {} <br> {} <br> {} <br> {}".format(form.name.data, form.description.data, form.completed.data, form.tdate.data)
        else:
            flash("Failure to subit form {}".format(form.errors))
    return render_template("wtform.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
    form = LoginForm()

    if request.method == "POST":
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()

            if user is None:
                flash("No such user", category="danger")
                return redirect(url_for("login"))
            elif not user.check_password(form.password.data):
                flash("Wrong password", category="danger")
                return redirect(url_for("login"))
            else:
                login_user(user)
                return redirect(url_for("root"))

    return render_template("login.html", form=form)

@app.route("/logout", methods=["POST", "GET"])
def logout():
    return None

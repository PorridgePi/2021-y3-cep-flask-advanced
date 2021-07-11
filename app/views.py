from app import app
from flask import render_template, request

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

@app.route("/wtform", methods=["GET", "POST"])
def wtform():
    form = TaskForm()

    if request.method == "POST":
        if form.validate_on_submit():
            return "<h1>Form</h1> <br> {} <br> {} <br> {} <br> {}".format(form.name.data, form.description.data, form.completed.data, form.tdate.data)
        else:
            return("Failure to subit form {}".format(form.errors))
    return render_template("wtform.html", form=form)

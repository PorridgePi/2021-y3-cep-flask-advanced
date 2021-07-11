from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField

class TaskForm(FlaskForm):
    name = StringField("Task Name")
    description = TextAreaField("Task Description")
    tdate = DateField("Date")
    completed = BooleanField("completed?")

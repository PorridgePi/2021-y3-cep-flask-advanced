from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.fields.html5 import DateField

from wtforms.validators import InputRequired, ValidationError

from datetime import datetime

class TaskForm(FlaskForm):
    name = StringField("Task Name", validators=[InputRequired()])
    description = TextAreaField("Task Description")
    tdate = DateField("Date")
    completed = BooleanField("completed?")

    def validate_tdate(form, field):
        today = datetime.today().date()

        if (field.data == None):
            raise ValidationError("Please enter a date.")

        if (today > field.data): # if the date is in the past
            raise ValidationError("Please do not enter a date in the past.")

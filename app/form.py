from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, PasswordField, SubmitField
from wtforms.fields.html5 import DateField

from wtforms.validators import InputRequired, ValidationError, DataRequired

from datetime import datetime
import string

class TaskForm(FlaskForm):
    name = StringField("Task Name", validators=[InputRequired()])
    description = TextAreaField("Task Description")
    tdate = DateField("Date")
    completed = BooleanField("completed?")

    def validate_name(form, field):
        # Returning more than one error when doing multiple validations on a single field
        # It is illegal to:
        # 1. Input a task name less than 3 characters
        # 2. Input a task name containing punctuations

        validated = True # default state of validation 

        if len(field.data) < 3:
            form.name.errors.append("Length of Task Name should be more than 3 characters.")
            validated = False

        if len([char for char in field.data if char in string.punctuation]) > 0: 
            form.name.errors.append("Task name should not contain punctuations.")
            validated = False

        return validated

    def validate_tdate(form, field):
        today = datetime.today().date()

        if (field.data == None):
            raise ValidationError("Please enter a date.")

        if (today > field.data): # if the date is in the past
            raise ValidationError("Please do not enter a date in the past.")

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Remember Me')
  submit = SubmitField('Sign In')
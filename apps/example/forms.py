from flask import current_app
from flask.ext.wtf import Form
from flask_wtf import RecaptchaField
from wtforms.fields import (
    TextAreaField,
    StringField,
    RadioField,
    HiddenField,
    SubmitField,
    )
from wtforms.validators import Required
import re

# Example form

# class ExampleForm(Form):
#     address = StringField(u"Address Entry",
#     [validators.DataRequired(message=u"You have to enter an address."),])
#     submit = SubmitField()

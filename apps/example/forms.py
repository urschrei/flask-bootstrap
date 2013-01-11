from flask import current_app
from flask.ext.wtf import (
    Form,
    Required,
    TextAreaField,
    StringField,
    RadioField,
    HiddenField,
    SubmitField,
    Recaptcha,
    RecaptchaField,
    validators
    )
import re

# Example form

# class ExampleForm(Form):
#     address = StringField(u"Address Entry",
#         [
#             validators.DataRequired(
#                 message=u"You have to enter an address."),])
#     submit = SubmitField()


from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField,ValidationError
from wtforms.validators import DataRequired, Email,ValidationError
import email_validator
  


class contactForm(FlaskForm):
    name = StringField("Name",  [validators.DataRequired("Please enter your name")])
    email = StringField("Email",  [validators.DataRequired(), validators.Email("Please enter your email")])
    subject = StringField("Subject",  [validators.DataRequired("Please enter the subject")])
    message = StringField("Message",  [validators.DataRequired("Please enter your message")])
    submit = SubmitField("Send")

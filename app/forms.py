from flask_wtf import FlaskForm
from wtforms.fields import TextField,TextAreaField
from wtforms.validators import Email,DataRequired

class ContactForm(FlaskForm):
    name = TextField("Full Name", validators = [DataRequired()])
    email = TextField("Email Address", validators = [DataRequired(), Email()])
    subject = TextField("Subject", validators = [DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    
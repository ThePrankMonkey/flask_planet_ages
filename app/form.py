from flask_wtf import FlaskForm
from wtforms import SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class BirthdayForm(FlaskForm):
    birthday = DateField('Birthday', format='%Y-%m-%d')
    submit = SubmitField('Get Birthdays')

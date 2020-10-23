from flask_wtf import FlaskForm
from wtforms import DateTimeField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired


class BirthdayForm(FlaskForm):
    birthday = DateTimeField('Birthday', format='%m/%d/%Y')
    # birthday = DateField('Birthday', format='%m/%d/%Y')
    # birthday = DateTimeField('Birthday', validators=[DataRequired()])
    submit = SubmitField('Get Birthdays')

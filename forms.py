from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

class chose_language:
	language = RadioField('Chose a language:', choices=[('Python','A dynamic language that can do both simple and very complex things.'),('HTML, CSS, JS','The language that makes up the web.')], validators=[DataRequired()])
	submit = SubmitField('Code!')

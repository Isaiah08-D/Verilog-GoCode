from flask import Flask, render_template, session, redirect, flash, url_for
from replit import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.config['SECRET_KEY'] = 'VLXG5dASre6k91gvFGAh'
bootstrap = Bootstrap(app)

class chose_language(FlaskForm):
	language = RadioField('Chose a language:', choices=[('A dynamic language that can do both simple and very complex things.','Python'),('The language that makes up the web.','HTML, CSS, JS')], validators=[DataRequired()])
	submit = SubmitField('Code!')
@app.route('/')
def index():
  return render_template("index.html", db=db)

@app.route('/code')
def code():
	session['logged_in'] = False
	form = chose_language()
	if session.get('logged_in') == False:
		flash('You must be logged in to view this page!')
		return render_template('index.html')
	if form.validate_on_submit():
		language = form.language.data
		name = form.name.data
		db[session.get('logged_in')][0] += (name, language)
		return redirect('/code/' + name)
	return render_template('code.html', form=form)

@app.route('/login')
def login():
	form = login()
	
app.run('0.0.0.0')

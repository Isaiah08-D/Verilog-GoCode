from flask import Flask, render_template, session, redirect, flash, url_for
from replit import db
import forms.py as forms

app = Flask(__name__)

app.config['SECRET_KEY'] = 'VLXG5dASre6k91gvFGAh'

@app.route('/')
def index():
  return render_template("index.html", db=db)

@app.route('/code')
def code():
	form = forms.chose_language()
	if session.get('logged_in') == False:
		flash('You must be logged in to view this page!')
		return render_template('index.html')
	if form.validate_on_submit():
		language = form.language.data
		name = form.name.data
		db[session.get('logged_in')][0] += (name, language)
		return redirect('/code/' + name)
	return render_template('login.html', form=form)

@app.route('/login')
def login():
	form = forms.login()
	
app.run('0.0.0.0')

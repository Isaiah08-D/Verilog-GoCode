from flask import Flask, render_template, session, redirect, flash, url_for
from replit import db
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
import forms.py

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", db=db)

@app.route('/code')
def code():
  

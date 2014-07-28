from flask import render_template
from blogapp import app
from blogapp.forms import RegistForm


@app.route('/')
def index():
	return "<h1>hello blog ! </h1>"

@app.route('/regist')
def regist():
	form = RegistForm()
	return render_template('regist.html', form = form)

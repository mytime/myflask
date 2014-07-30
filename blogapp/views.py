#coding:utf8
from flask import render_template, request
from blogapp import app
from blogapp.forms import RegistForm


@app.route('/')
def index():
	return "<h1>hello blog ! </h1>"

@app.route('/regist', methods=['GET','POST'])
def regist():
	form = RegistForm()
	if request.method == "POST":
		if form.validate():
			print form.data			
			return "regist ok"
	return render_template('regist.html', form = form)

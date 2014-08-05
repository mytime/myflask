#coding:utf8
from flask import render_template, request, flash, redirect, url_for, session
from blogapp import app
from blogapp.forms import RegistForm, LoginForm

from blogapp import db	#倒入__init__.py下的db
from blogapp.models import User	#倒入models

import hashlib
import string
import random


#加盐
def get_salt(n=10):
	return ''.join(random.sample(string.letters,n))

@app.route('/')
def index():
	if 'uid' in session:
		user = User.query.filter_by(id=session['uid']).first()
	else:
		user = None	
	return render_template('index.html', user=user)

#注册方法
@app.route('/regist', methods=['GET','POST'])
def regist():
	form = RegistForm()
	if request.method == "POST":
		if form.validate():
			username = form.data['username']
			email = form.data['email']
			password = form.data['password']			
			salt = get_salt()
			password = hashlib.sha1(salt+password).hexdigest()			
			user = User(username=username,email=email,password=password,salt=salt)
			db.session.add(user)	
			db.session.commit()
			return redirect(url_for('login'))
	return render_template('regist.html', form = form)
	
#登录方法	
@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	if request.method == "POST":
		if form.validate():
			username = form.data['username']
			password = form.data['password']
			user = User.query.filter_by(username=username).first()
			if user:
				password_salt = hashlib.sha1(user.salt+password).hexdigest()
				if password_salt == user.password:
					session['uid'] = user.id
					return redirect(url_for('index'))				
				else:				
					flash("username password not mathch !")	
			else:
				flask('username is not exist')		
	return render_template('login.html',form=form)
	


	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

#coding:utf8
from flask import render_template, request, flash, redirect, url_for, session
from blogapp import app
from blogapp.forms import RegistForm, LoginForm, PostForm

from blogapp import db	#倒入__init__.py下的db
from blogapp.models import User, Post	#倒入models

import hashlib
import string
import random


#加盐
def get_salt(n=10):
	return ''.join(random.sample(string.letters,n))

@app.route('/')
def index():
	#获取session
	if 'uid' in session:
		user = User.query.filter_by(id=session['uid']).first()
	else:
		user = None	
	#展现发帖列表
	posts = Post.query.all()
	return render_template('index.html', user=user, posts=posts)

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

	
@app.route('/post/add/', methods=['GET','POST'])
def post_add():
	#获取session
	if 'uid' in session:
		user = User.query.filter_by(id=session['uid']).first()
		
	form = PostForm()
	if request.method == "POST":
		if form.validate():
			print form.data
			#添加数据
			user = Post(author=user,title=form.data['title'], 
				content=form.data['content'])
			db.session.add(user)
			db.session.commit()
			return redirect(url_for('index'))
	return render_template('post_add.html', form=form)
		
@app.route('/post/<postid>/')
def post_disp(postid):
	post = Post.query.get(postid)
	return render_template('post_disp.html', post=post)
	
@app.route('/logout/')
def logout():
	if 'uid' in session:
		del session['uid']
	
	return redirect(url_for('index'))
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

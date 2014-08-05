#coding:utf8
from blogapp import db

#用户表
class User(db.Model):
	id = db.Column(db.Integer,primary_key =True)
	username = db.Column(db.String(20),index=True,unique=True)
	email = db.Column(db.String(30),index=True,unique=True)
	password = db.Column(db.String(120))
	salt = db.Column(db.String(50))
	posts = db.relationship('Post', backref='author', lazy='dynamic')  #对应post对象
	
	def __repr__(self):
		return '<User %r>'% self.username
		
#发帖表
class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(50))
	content = db.Column(db.Text())
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #外键
	
	def __repr__(self):
		return '<Post %r>' % self.title

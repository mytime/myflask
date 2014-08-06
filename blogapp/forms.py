#coding:utf8
from flask_wtf import Form
from wtforms import TextField, PasswordField, TextAreaField
from wtforms.validators import Required,Email,Length, EqualTo

#注册框
class RegistForm(Form):
	username = TextField(u"姓名", validators=[Required(u'用户名不能为空')])
	email = TextField(u"邮箱", validators=[Required(u'邮件不能为空'),Email(u'无效邮址')])
	password = PasswordField(u"密码", validators=[Length(message=u'长度不能少于6位', min=6 )])
	repassword = PasswordField(u"密码确认", validators=[EqualTo('password',message=u'口令不匹配')])
	
#登录框	
class LoginForm(Form):
	username = TextField(u"姓名", validators=[Required(u'用户名不能为空')])
	password = PasswordField(u"密码", validators=[Length(message=u'长度不能少于6位', min=6 )])

#发帖
class PostForm(Form):
	title = TextField(u'标题')
	content = TextAreaField(u'内容')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

#coding:utf8
from wtforms import Form,TextField, PasswordField

class RegistForm(Form):
	username = TextField(u"用户名")
	email = TextField(u"邮箱")
	password = PasswordField(u"密码")
	repassword = PasswordField(u"密码确认")

# -*- coding: utf-8 -*-
from datetime import datetime, date
from app import db


class User(db.Model):
	__tablename__ = 'users'
		
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), doc='username', nullable=False, unique=True)
	password = db.Column(db.String(20), doc='password', nullable=False)

#	def hash_password(self, pwd):
#		self.password_hash = pwd_context.encrypt(pwd)
#
#	def verify_password(self, pwd):
#		return pwd_context.verify(pwd, self.pwd)
#
#	def generate_auth_token(self, expiration=600):
#		s = Serializer(app.config['SECRET_KEY'], expires_in=expiration)
#		return s.dumps({'id': self.id})
#
#	@staticmethod
#	def verify_auth_token(token):
#		s = Serializer(app.config['SECRET_KEY'])
#		try:
#			data = s.loads(token)
#		except SignatureExpired:
#			return None  # valid token, but expired
#		except BadSignature:
#			return None  # invalid token
#		user = User.query.get(data['id'])
#		return user
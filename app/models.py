# -*- coding: utf-8 -*-
from datetime import datetime, date
import app
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

#from passlib.apps import custom_app_context as pwd_context
#from itsdangerous import (TimedJSONWebSignatureSerializer
#													as Serializer, BadSignature, SignatureExpired)

Base = declarative_base()

class User(Base):
	__tablename__ = 'users'
		
	id = Column(Integer, primary_key=True)
	username = Column(String(20), doc='username', nullable=False, unique=True)
	password = Column(String(20), doc='password', nullable=False, unique=True)

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
# -*- coding: utf-8 -*-
from datetime import datetime, date
from app import db


class User(db.Model):
	__tablename__ = 'users'
		
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), doc='Username', nullable=False, unique=True)
	password = db.Column(db.String(20), doc='Password', nullable=False)

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
		
class City(db.Model):
	__tablename__ = 'cities'
	
	id = db.Column(db.Integer, primary_key=True)
	cityname = db.Column(db.String(30), doc='City Name', nullable=False)
	state = db.Column(db.String(30), doc='State Name', nullable=False)
	stateCode = db.Column(db.String(2), doc='State Code', nullable=False)

class Demand(db.Model):
	__tablename__ = 'demands'
	
	id = db.Column(db.Integer, primary_key=True)
	#	Note that both role and goal can only be 0, 1, 2, representing photographer, model, other, respectively
	userId = db.Column(db.Integer, doc='Id of the User Who Posted the Demand', nullable=False)
	role = db.Column(db.Integer, doc='Role of the Host', nullable=False)
	goal = db.Column(db.Integer, doc='Role of the Goal', nullable=False)
	# price can be (null) representing it's free
	price = db.Column(db.Float, doc='Price of the Demand')
	cityId = db.Column(db.Integer, doc='Id of the City Where the Demand is Posted', nullable=False)


# database table initialization
#db.drop_all()
db.create_all()
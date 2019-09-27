from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort

import json

from app.models import User
from app import db

mod = Blueprint('action', __name__)


@mod.route('/loginForm', methods=['GET','POST'])
def loginForm():
	if request.method == 'POST':
		usr = request.form['usr']
		pwd = request.form['pwd']
		rmb = request.form['rmb']

		# `code` = the matched user information or None if there is no query matched from database
		is_usr = db.session.query(User).filter_by(username=usr).first()
		code = db.session.query(User).filter_by(username=usr, password=pwd).first()
		if code == None:
			return json.dumps({'re': False, 'action': 'The password is incorrect.' if is_usr else 'The username doesn\'t exist.'})
		else:
			return json.dumps({'re': True, 'action': url_for('general.home', usr=usr)})
			
	return code

@mod.route('/signupForm', methods=['GET','POST'])
def signupForm():
	if request.method == 'POST':
		usr = request.form['usr']
		pwd = request.form['pwd']
		
	code = db.session.query(db.exists().where(User.username == usr)).scalar()
	
	if not code:
		user = User(username=usr, password=pwd)
		db.session.add(user)
		db.session.commit()
		session['usr'] = usr
		return json.dumps({'re': not code, 'action': url_for('general.home', usr=session['usr'])})
	else:
		return json.dumps({'re': not code, 'action': "The username has existed."})
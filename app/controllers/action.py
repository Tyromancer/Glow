from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort

from app.models import User

mod = Blueprint('action', __name__)


@mod.route('/loginForm', methods=['GET','POST'])
def loginForm():
	code = 'fail'
	if request.method == 'POST':
		usr = request.form['usr']
		pwd = request.form['pwd']
		rmb = request.form['rmb']
		
#TODO: 从数据库验证登陆数据，如正确则跳转到home，如不对返回fail
		
		code = 'success'
		if code == 'success':
			return redirect(url_for('general.home', usr=session['usr']))
	return code
	
@mod.route('/signupForm', methods=['GET','POST'])
def signupForm():
	code = 'fail'
	if request.method == 'POST':
		usr = request.form['usr']
		pwd = request.form['pwd']

	user = User(username=usr, password=pwd)
	session.add(user)
	session.commit()
	
	
#TODO: 从数据库验证注册数据适合valid(如usr已被注册)，如valid则更新数据库并跳转到home，如不对返回fail及原因

	code = 'success'
	if code == 'success':
		return redirect(url_for('general.home', usr=session['usr']))
	return code
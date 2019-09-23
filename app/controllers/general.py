from flask import Blueprint, render_template, session, redirect, url_for, \
	request, flash, g, jsonify, abort
	
mod = Blueprint('general', __name__)


@mod.route('/')
def index():
	
	#	必须要登陆后才能浏览网站信息
	if 'user' in session:
		return redirect(url_for('general.home', usr=session['usr']))
	else:
		return redirect(url_for('general.login'), 302)

@mod.route('/login')
def login():
	return render_template('login.html')

@mod.route('/signup')
def signup():
	return render_template('signup.html')

@mod.route('/home')
def home(usr=None):
		
		#	必须要登陆后才能浏览网站信息
		if usr == None:
			redirect(url_for('general.login'), 302)
		
		return render_template('home.html', usr=session['usr'])
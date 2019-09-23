from flask import Blueprint, render_template, session, redirect, url_for, \
	request, flash, g, jsonify, abort
	
mod = Blueprint('action', __name__)


@mod.route('/loginForm', methods=['GET','POST'])
def loginForm():
#	form = MockCreate()
	if request.method == 'GET':
		render_template(url_for('general.login'))
	else:
		data.code = 'success'
#		data.usr = request.form['usr']
#		data.pwd = request.form['pwd']
#		data.rmb = request.form['rmb']
		return data
from flask import Blueprint, render_template, session, redirect, url_for, request, flash, g, jsonify, abort

import json

from app.controllers import utils

from app import db
from app.models import City


mod = Blueprint('general', __name__)


@mod.route('/')
def index():

	#	login is required to browse the site
	if 'usr' in session:
		return redirect(url_for('general.home', usr=session['usr']))
	else:
		return redirect(url_for('general.login'))

@mod.route('/login')
def login():
	return render_template('login.html')

@mod.route('/signup')
def signup():
	return render_template('signup.html')

@mod.route('/home/<usr>')
def home(usr=None):

	#	login is required to browse the site
	if usr == None:
		return redirect(url_for('general.login'))
	else:
		return render_template('home.html', usr=session['usr'])

@mod.route('/post/<state>/<city>')
def post(state=None, city=None):

	#	render all city names onto the page
	all_query_from_city =  db.session.query(City.cityname, City.state).all()
	formattd_city_dict = utils.format_cities(all_query_from_city)

	return render_template('post.html', cities=formattd_city_dict)
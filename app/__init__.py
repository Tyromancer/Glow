from datetime import datetime
from flask import Flask, session, g, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'cd48e1c22de0961d5d1bfb14f8a66e006cfb1cfbf3f0c0f3'

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from app.controllers import general
from app.controllers import action

app.register_blueprint(general.mod)
app.register_blueprint(action.mod)
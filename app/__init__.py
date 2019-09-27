from datetime import datetime
from flask import Flask, session, g, render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config)

db = SQLAlchemy(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

from app.controllers import general
from app.controllers import action

app.register_blueprint(general.mod)
app.register_blueprint(action.mod)
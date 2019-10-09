from flask import Flask
import flask_sqlalchemy

from web_travel.models import db
from web_travel import config


def create_app():
    travel_app = Flask(__name__)
    # travel_app.config.from_pyfile('config.py')
    travel_app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    travel_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    travel_app.app_context().push()
    db.init_app(travel_app)
    db.create_all()
    return travel_app

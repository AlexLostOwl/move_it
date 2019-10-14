from flask import Flask, render_template
from web_travel.models import db, User, Country, City, Place
from web_travel.crud import *
from . import config


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_CONNECTION_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.app_context().push()
    db.init_app(app)
    db.create_all()

    @app.route('/')
    def index():
        # Just an Example feel fre to delete
        save_user('Sasha', 'Umnnii_parol', 'Moi_Password')
        save_country('Greece')
        save_city('Smolensk', 'Germany')
        save_place('Nice Place', 'A place description', 'Bulgaria', 'Ramensk')
        return render_template('index.html', users=get_users(), country=get_countries(), city=get_cities(),
                               place=get_places())

    return app

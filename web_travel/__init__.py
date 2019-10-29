from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from web_travel.admin.views import blueprint as admin_blueprint
from web_travel.country.views import blueprint as country_blueprint
from web_travel.crud import *
from web_travel.city.views import blueprint as city_blueprint
from web_travel.db import db
from web_travel.place.views import blueprint as place_blueprint
from web_travel.user.models import User
from web_travel.user.views import blueprint as user_blueprint


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    # app.app_context().push()
    db.init_app(app)
    migrate = Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(country_blueprint)
    app.register_blueprint(city_blueprint)
    app.register_blueprint(place_blueprint)
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(userd_id):
        return User.query.get(userd_id)

    return app

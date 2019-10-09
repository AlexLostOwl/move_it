from web_travel.models import db, User, Country, City, Position
from web_travel import create_app


def save_users(username, password, email):
    user_exists = User.query.filter(User.email == email).count()
    if not user_exists:
        new_user = User(username=username, password=password, email=email)
        db.session.add(new_user)
        db.session.commit()


def save_country(country_name):
    if not Country.query.filter(Country.country_name == country_name).count():
        new_country = Country(country_name=country_name)
        db.session.add(new_country)
        db.session.commit()


def save_city(city_name):
    new_city = City(city_name=city_name)
    db.session.add(new_city)
    db.session.commit()


def save_position(description):
    new_description = Position(description=description)
    db.session.add(new_description)
    db.session.commit()


def test():
    save_city('Smolensk')
    save_users('Sasha', 'Ololo', 'o_email@email.com')
    save_country('Russia')
    save_position('Superposition')


app = create_app()
with app.app_context():
    test()

import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<User {self.username} id={self.id}>'


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, unique=True, nullable=False)

    cities = db.relationship('City', backref='city_in_country', lazy='dynamic')
    places = db.relationship('Place', backref='place_in_country', lazy='dynamic')

    def __repr__(self):
        return f'<Country {self.country_name} id={self.id}>'


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    places = db.relationship('Place', backref='place_in_city', lazy='dynamic')

    def __repr__(self):
        return f'<City {self.city_name} id={self.id}>'


class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    def __repr__(self):
        return f'<Place {self.place_name} id={self.id}>'

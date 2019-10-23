from web_travel.models import db


class Country(db.Model):
    __tablename__ = 'countries'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, unique=True, nullable=False)

    cities = db.relationship('City', backref='city_in_country', lazy='dynamic')
    places = db.relationship('Place', backref='place_in_country', lazy='dynamic')

    def __repr__(self):
        return f'<Country {self.country_name} id={self.id}>'

    def __str__(self):
        return self.country_name

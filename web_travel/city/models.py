from web_travel.db import db


class City(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String, nullable=False)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    places = db.relationship('Place', backref='place_in_city', lazy='dynamic')

    def __repr__(self):
        return f'<City {self.city_name} id={self.id}>'

from web_travel.db import db


class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    photos = db.relationship('Photo', backref='photo_in_place', lazy='dynamic')

    def __repr__(self):
        return f'<Place {self.place_name} id={self.id}>'


class Photo(db.Model):
    __tablename__ = 'photos'
    id = db.Column(db.Integer, primary_key=True)
    photo_link = db.Column(db.String)
    place_id = db.Column(db.Integer, db.ForeignKey('places.id'))

    def __repr__(self):
        return f'<Photo {self.photo_link} id={self.id}>'

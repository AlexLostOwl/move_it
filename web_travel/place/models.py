from web_travel.db import db


class Place(db.Model):
    __tablename__ = 'places'
    id = db.Column(db.Integer, primary_key=True)
    place_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))

    def __repr__(self):
        return f'<Place {self.place_name} id={self.id}>'

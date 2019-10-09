import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'User is {self.username} with email: {self.email}'


class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    country_name = db.Column(db.String, unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'Country is {self.country_name}'


class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String, nullable=False)

    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship('Country', backref='country', lazy='dynamic')

    def __repr__(self):
        return f'City is {self.city_name}'


class Position(db.Model):
    __tablename__ = 'position'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)

    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))

    city = db.relationship('City', backref='city', lazy='dynamic')
    country = db.relationship('Country', backref='country', lazy='dynamic')

    def __repr__(self):
        return f'Position is City: {self.city_id} County: {self.country_id}'

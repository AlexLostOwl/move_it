from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from web_travel.country.models import Country
from web_travel.city.models import City


class CityAddForm(FlaskForm):
    city = StringField(
        'City name',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    country = QuerySelectField(
        'Country name',
        query_factory=lambda: Country.query.order_by(Country.country_name)
        )
    submit = SubmitField('Add country', render_kw={'class': 'btn btn-primary'})

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        city_objects = City.query.filter_by(city_name=self.city.data).all()
        for city_object in city_objects:
            if city_object.country_id == self.country.data.id:
                flash(f'City {self.city.data} in {self.country.data} exists')
                return False
        return True

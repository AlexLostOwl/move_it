from flask import flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from web_travel.country.models import Country
from web_travel.crud import place_exists


class PlaceAddForm(FlaskForm):
    country = QuerySelectField(
        'Country name',
        query_factory=lambda: Country.query.order_by(Country.country_name),
        validators=[DataRequired()],
        id='countriesSelect',
        render_kw={'class': 'form-control', 'placeholder': 'test'}
        )
    place = StringField(
        'Place name',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    description = TextAreaField(
        'Place description',
        render_kw={'class': 'form-control'}
        )
    submit = SubmitField(
        'Add country',
        render_kw={'class': 'btn btn-primary'}
        )

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if place_exists(self.place.data, self.country.data.country_name):
            flash(f'Место {self.place.data} в {self.country.data.country_name} уже существует')
            return False
        return True

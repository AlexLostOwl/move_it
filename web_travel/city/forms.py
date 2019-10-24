from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, ValidationError

from web_travel.country.models import Country
from web_travel.city.models import City


class CityForm(FlaskForm):
    city = StringField('City name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    country = QuerySelectField('Country name', query_factory=lambda: Country.query.order_by(Country.country_name))
    submit = SubmitField('Add country', render_kw={'class': 'btn btn-primary'})

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

from web_travel.country.models import Country


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

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

from web_travel.country.models import Country


class CountryForm(FlaskForm):
    country_name = StringField('Country name ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Add country', render_kw={'class': 'btn btn-primary'})

    def validate_country_name(self, name):
        country_count = Country.query.filter_by(country_name=name.data).count()
        if country_count > 0:
            raise ValidationError('Country exists')

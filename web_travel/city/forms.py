from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from web_travel.country.models import Country
from web_travel.city.models import City


class CityForm(FlaskForm):
    city_name = StringField('City name', validators=[DataRequired()], render_kw={'class': 'form-control'})
    country_name = SelectField('Country', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit = SubmitField('Add country', render_kw={'class': 'btn btn-primary'})

    def validate_city_name(self, name):
        country_count = City.query.filter_by(city_name=name.data).count()
        if country_count > 0:
            raise ValidationError('City exists')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class CountryForm(FlaskForm):
    country_name = StringField('Country name ', validators=[DataRequired()], render_kw={'class': 'form-control'})
    submit = SubmitField('Add country', render_kw={'class': 'btn btn-primary'})

from flask import flash
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, StringField, RadioField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, Optional

from web_travel.country.models import Country
from web_travel.crud import place_exists, country_exists


class NonValidatingSelectMultipleField(SelectField):
    """
    Attempt to make an open ended select field that can accept dynamic
    choices added by the browser.
    """
    def pre_validate(self, form):
        pass


class PlaceAddForm(FlaskForm):
    country = QuerySelectField(
        'Выберите страну',
        query_factory=lambda: Country.query.order_by(Country.country_name),
        validators=[Optional()],
        id='countriesSelect',
        render_kw={'class': 'form-control'}
        )
    city = NonValidatingSelectMultipleField(
        'Выберите город',
        validators=[Optional()],
        choices=[],
        id='citiesSelect',
        render_kw={'class': 'form-control'}
    )
    place = StringField(
        'Введите название места',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    description = TextAreaField(
        'Введите описание',
        render_kw={'class': 'form-control'}
        )
    country_input_method = RadioField(
        'Можно добавить страну, если она отсутствует в списке',
        validators=[DataRequired()],
        choices=[('choose', 'Выбрать страну из списка'), ('create', 'Добавить страну')],
        default='choose',
        render_kw={'onclick': 'javascript:createOrChoose();', 'class': 'nobull'}
        )
    new_country = StringField(
        'Введите название страны',
        render_kw={'class': 'form-control'}
        )
    new_city = StringField(
        'Введите название города',
        render_kw={'class': 'form-control'}
        )
    submit = SubmitField(
        'Добавить',
        render_kw={'class': 'btn btn-primary'}
        )

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.country_input_method.data == 'choose':
            if place_exists(self.place.data, self.country.data.country_name):
                flash(f'Место {self.place.data} в {self.country.data.country_name} уже существует')
                return False
        if self.country_input_method.data == 'create':
            if country_exists(self.new_country.data):
                flash(f'Страна {self.new_country.data} уже существует')
                return False
        return True


class PlaceEditForm(FlaskForm):
    country = QuerySelectField(
        'Выберите страну',
        query_factory=lambda: Country.query.order_by(Country.country_name),
        validators=[Optional()],
        id='countriesSelect',
        render_kw={'class': 'form-control'}
        )
    city = NonValidatingSelectMultipleField(
        'Выберите город',
        validators=[Optional()],
        choices=[],
        id='citiesSelect',
        render_kw={'class': 'form-control'}
    )
    place = StringField(
        'Введите название места',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    description = TextAreaField(
        'Введите описание',
        render_kw={'class': 'form-control'}
        )
    country_input_method = RadioField(
        'Можно добавить страну, если она отсутствует в списке',
        validators=[DataRequired()],
        choices=[('choose', 'Выбрать страну из списка'), ('create', 'Добавить страну')],
        default='choose',
        render_kw={'onclick': 'javascript:createOrChoose();', 'class': 'nobull'}
        )
    new_country = StringField(
        'Введите название страны',
        render_kw={'class': 'form-control'}
        )
    new_city = StringField(
        'Введите название города',
        render_kw={'class': 'form-control'}
        )
    submit = SubmitField(
        'Изменить',
        render_kw={'class': 'btn btn-primary'}
        )

    def validate(self):
        if not FlaskForm.validate(self):
            return False
        if self.country_input_method.data == 'choose':
            if place_exists(self.place.data, self.country.data.country_name):
                flash(f'Место {self.place.data} в {self.country.data.country_name} уже существует')
                return False
        if self.country_input_method.data == 'create':
            if country_exists(self.new_country.data):
                flash(f'Страна {self.new_country.data} уже существует')
                return False
        return True

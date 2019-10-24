from flask import Blueprint, render_template, url_for, redirect, flash

from web_travel.city.forms import CityForm
from web_travel.city.models import City
from web_travel.country.models import Country
from web_travel import db
from web_travel.crud import city_exists, save_city


blueprint = Blueprint('city', __name__, url_prefix='/city')


@blueprint.route('/add-city')
def add_city():
    title = 'Add new city'
    city_form = CityForm()
    return render_template('city/add-city.html', page_title=title, form=city_form)


@blueprint.route('/adding-city', methods=['POST'])
def adding_city():
    form = CityForm()
    if form.validate_on_submit():
        if city_exists(form.city.data, form.country.data):
            flash("City exists :(")
            return redirect(url_for('city.add_city'))
        print(form.country.data)
        print(form.city.data)
        save_city(form.city.data, form.country.data)
        return redirect(url_for('city.add_city'))

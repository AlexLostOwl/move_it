from flask import Blueprint, render_template, url_for, redirect, flash

from web_travel.city.forms import CityAddForm
from web_travel.city.models import City
from web_travel import db


blueprint = Blueprint('city', __name__, url_prefix='/city')


@blueprint.route('/add-city')
def add_city():
    title = 'Add new city'
    city_form = CityAddForm()
    return render_template('city/add-city.html', page_title=title, form=city_form)


@blueprint.route('/adding-city', methods=['POST'])
def adding_city():
    form = CityAddForm()
    if form.validate_on_submit():
        city_objects = City.query.filter_by(city_name=form.city.data).all()
        for city_object in city_objects:
            if city_object.country_id == form.country.data.id:
                flash(f'City {form.city.data} in {form.country.data} exists')
                return redirect(url_for('city.add_city'))
        new_city = City(city_name=form.city.data, country_id=form.country.data.id)
        db.session.add(new_city)
        db.session.commit()
        flash(f'City {form.city.data} successful added')
        return redirect(url_for('city.add_city'))

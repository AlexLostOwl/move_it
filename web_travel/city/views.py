from flask import Blueprint, render_template, url_for, redirect, flash

from web_travel.city.forms import CityAddForm
from web_travel.city.models import City
from web_travel import db


blueprint = Blueprint('city', __name__, url_prefix='/city')


@blueprint.route('/add-city')
def add_city():
    title = 'Add new city'
    city_form = CityAddForm()
    return render_template('city/add-city.html',
                           page_title=title,
                           form=city_form)


@blueprint.route('/adding-city', methods=['POST'])
def adding_city():
    form = CityAddForm()
    if form.validate_on_submit():
        new_city = City(city_name=form.city.data, country_id=form.country.data.id)
        db.session.add(new_city)
        db.session.commit()
        flash(f'City {form.city.data} successful added')
        return redirect(url_for('city.add_city'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('city.add_city'))

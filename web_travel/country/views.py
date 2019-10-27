from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask.json import jsonify

from web_travel.country.forms import CountryAddForm
from web_travel.country.models import Country
from web_travel.crud import country_exists
from web_travel import db


blueprint = Blueprint('country', __name__, url_prefix='/country')


@blueprint.route('/add-country')
def add_country():
    title = 'Add new country'
    country_form = CountryAddForm()
    return render_template('country/add-country.html',
                           page_title=title,
                           form=country_form)


@blueprint.route('/adding-country', methods=['POST'])
def adding_country():
    form = CountryAddForm()
    if form.validate_on_submit():
        new_country = Country(country_name=form.country_name.data)
        db.session.add(new_country)
        db.session.commit()
        flash('Country successful add')
        return redirect(url_for('country.add_country'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(url_for('country.add_country'))


@blueprint.route('/getCities')
def get_cities():
    country = request.args.get('country')
    try:
        cities_objects = Country.query.filter_by(country_name=country).first().cities.all()
    except AttributeError:
        response = jsonify({'AttributeError': 'Wrong country or missing attibute'})
        return response, 400
    return jsonify(cities=[city_object.city_name for city_object in cities_objects])

from flask import Blueprint, request
from flask.json import jsonify

from web_travel.country.models import Country


blueprint = Blueprint('country', __name__, url_prefix='/countries')


@blueprint.route('/getCities')
def get_cities():
    country = request.args.get('country')
    try:
        cities_objects = Country.query.filter_by(country_name=country).first().cities.all()
    except AttributeError:
        response = jsonify({'AttributeError': 'Wrong country or missing attibute'})
        return response, 400
    return jsonify(cities=[city_object.city_name for city_object in cities_objects])


@blueprint.route('/getCountries')
def get_countries():
    data = {}
    data['data'] = []
    countries = Country.query.all()
    for country in countries:
        data['data'].append({
            'id': country.id,
            'country': country.country_name,
        })
    return jsonify(data)

from flask import Blueprint, jsonify

from web_travel.city.models import City
from web_travel.country.models import Country


blueprint = Blueprint('city', __name__, url_prefix='/cities')


@blueprint.route('/getCities')
def get_cities():
    data = {}
    data['data'] = []
    cities = City.query.all()
    for city in cities:
        country = Country.query.filter(Country.id == city.country_id).first().country_name
        data['data'].append({
            'id': city.id,
            'city': city.city_name,
            'country': country,
        })
    return jsonify(data)

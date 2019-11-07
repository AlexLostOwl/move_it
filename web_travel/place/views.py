from flask import Blueprint, render_template, url_for, request, redirect, flash
from flask.json import jsonify

from web_travel.place.models import Place
from web_travel.country.models import Country
from web_travel.city.models import City
from web_travel.crud import country_exists
from web_travel import db


blueprint = Blueprint('place', __name__, url_prefix='/places')


@blueprint.route('/getPlaces')
def get_places():
    data = {}
    data['data'] = []
    places = Place.query.all()
    for place in places:
        country = Country.query.filter(Country.id == place.country_id).first().country_name
        city = City.query.filter(City.id == place.city_id).first()
        city_name = city.city_name if city else ''
        data['data'].append({
            'id': place.id,
            'name': place.place_name,
            'country': country,
            'city': city_name,
        })
    return jsonify(data)

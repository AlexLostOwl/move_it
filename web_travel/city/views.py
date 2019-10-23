from flask import Blueprint, render_template, url_for, redirect, flash

from web_travel.city.forms import CityForm
from web_travel.city.models import City
from web_travel import db


blueprint = Blueprint('city', __name__, url_prefix='/city')


@blueprint.route('/add-city')
def add_city():
    title = 'Add new city'
    city_form = CityForm()
    return render_template('city/add-city.html', page_title=title, form=city_form)


# @blueprint.route('/adding-process', methods=['POST'])
# def adding_process():
#     form = CityForm()
#     if form.validate_on_submit():
#         new_city = City(city_name=form.city_name.data)
#         db.session.add(new_city)
#         db.session.commit()
#         flash('City successful add')
#         return redirect(url_for('index'))
#     else:
#         for field, errors in form.errors.items():
#             for error in errors:
#                 flash('Error in field "{}" - {}'.format(
#                     getattr(form, field).label.text,
#                     error
#                 ))
#     return redirect(url_for('city.add-city'))

from flask import abort, Blueprint, render_template, redirect, url_for, flash

from web_travel.admin.forms import PlaceAddForm, PlaceEditForm
from web_travel.crud import save_place, save_country, save_city
from web_travel.user.decorators import admin_required
from web_travel.place.models import Place
from web_travel.country.models import Country
from web_travel.city.models import City
from web_travel.db import db

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def index():
    title = 'Admin panel'
    return render_template('admin/index.html', page_title=title)


@blueprint.route('/add_place')
@admin_required
def add_place():
    title = 'Добавить новое место'
    place_form = PlaceAddForm()
    return render_template('admin/add_place.html',
                           page_title=title,
                           form=place_form)


@blueprint.route('/adding_place', methods=['POST'])
@admin_required
def adding_place():
    form = PlaceAddForm()
    if form.validate_on_submit():
        if form.country_input_method.data == 'choose':
            save_place(
                form.place.data, form.description.data,
                form.country.data.country_name, form.city.data
                )
            flash(f'Место {form.place.data} успешно добавлено')
            return redirect(url_for('admin.add_place'))
        if form.country_input_method.data == 'create':
            save_country(form.new_country.data)
            if form.new_city.data != '':
                save_city(form.new_city.data, form.new_country.data)
                save_place(
                    form.place.data, form.description.data,
                    form.new_country.data, form.new_city.data
                    )
            else:
                save_place(
                    form.place.data, form.description.data,
                    form.new_country.data
                    )
        return redirect(url_for('admin.add_place'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('admin.add_place'))


@blueprint.route('/places_list')
@admin_required
def places_list():
    return render_template('admin/places_list.html')


@blueprint.route('/edit_place/<int:place_id>')
@admin_required
def edit_place(place_id):
    place = Place.query.filter(Place.id == place_id).first_or_404()
    form = PlaceEditForm(obj=place)
    title = 'Изменение данных о месте'
    return render_template('admin/edit_place.html', page_title=title,
                           form=form, current_place_id=place_id)


@blueprint.route('/editing_place/<int:place_id>', methods=['POST'])
@admin_required
def editing_place(place_id):
    # TODO проверка страны на наличие такого же места
    # TODO форма страна и город заполняются старыми данными
    place = Place.query.filter(Place.id == place_id).first_or_404()
    form = PlaceEditForm()
    if form.validate_on_submit():
        if form.country_input_method.data == 'choose':
            country = Country.query.filter_by(id=form.country.data.id).first()
            if not country:
                abort(500)
            place.country_id = country.id
            if form.city.data == '':
                place.city_id = None
            else:
                city_object = City.query.filter(City.city_name == form.city.data,
                                                City.country_id == country.id).first()
                place.city_id = city_object.id
        form.populate_obj(place)
        db.session.commit()
        flash('Данные изменены успешно')
        return redirect(url_for('admin.places_list', place_id=place_id))
    return redirect(url_for('admin.edit_place', place_id=place_id))

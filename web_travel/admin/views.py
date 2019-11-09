from flask import abort, Blueprint, render_template, redirect, url_for, flash

from web_travel.admin.forms import PlaceAddForm, PlaceEditForm, CityAddForm, CountryAddForm
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
            return redirect(url_for('admin.places_list'))
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
        return redirect(url_for('admin.places_list'))
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
    title = "Редактирование мест"
    return render_template('admin/places_list.html', page_title=title)


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
        if form.country_input_method.data == 'create':
            place.country_id = create_country(form.new_country.data)
            if form.new_city.data != '':
                place.city_id = create_city(form.new_city.data, place.country_id)
            else:
                place.city_id = None
        form.populate_obj(place)
        db.session.commit()
        flash('Данные изменены успешно')
        return redirect(url_for('admin.places_list', place_id=place_id))
    return redirect(url_for('admin.edit_place', place_id=place_id))


def create_country(country):
    new_country = Country(country_name=country)
    db.session.add(new_country)
    db.session.flush()
    return new_country.id


def create_city(city, new_country_id):
    new_city = City(city_name=city, country_id=new_country_id)
    db.session.add(new_city)
    db.session.flush()
    return new_city.id


@admin_required
@blueprint.route('/delete_place/<int:place_id>')
def delete_place(place_id):
    place_for_delete = Place.query.filter_by(id=place_id)
    if not place_for_delete:
        abort(500)
    place_for_delete.delete()
    db.session.commit()
    flash('Место успешно удалено')
    return redirect(url_for("admin.places_list"))


@admin_required
@blueprint.route('/add_city')
def add_city():
    title = 'Add new city'
    city_form = CityAddForm()
    return render_template('admin/add_city.html',
                           page_title=title,
                           form=city_form)


@admin_required
@blueprint.route('/adding_city', methods=['POST'])
def adding_city():
    form = CityAddForm()
    if form.validate_on_submit():
        new_city = City(city_name=form.city.data, country_id=form.country.data.id)
        db.session.add(new_city)
        db.session.commit()
        flash(f'City {form.city.data} successful added')
        return redirect(url_for('admin.cities_list'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('admin.add_city'))


@blueprint.route('/cities_list')
@admin_required
def cities_list():
    title = "Редактирование городов"
    return render_template('admin/cities_list.html', page_title=title)


@admin_required
@blueprint.route('/add_country')
def add_country():
    title = 'Add new country'
    country_form = CountryAddForm()
    return render_template('admin/add_country.html',
                           page_title=title,
                           form=country_form)


@admin_required
@blueprint.route('/adding_country', methods=['POST'])
def adding_country():
    form = CountryAddForm()
    if form.validate_on_submit():
        new_country = Country(country_name=form.country_name.data)
        db.session.add(new_country)
        db.session.commit()
        flash('Country successful add')
        return redirect(url_for('admin.countries_list'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(url_for('admin.add_country'))


@blueprint.route('/countries_list')
@admin_required
def countries_list():
    title = "Редактирование стран"
    return render_template('admin/countries_list.html', page_title=title)

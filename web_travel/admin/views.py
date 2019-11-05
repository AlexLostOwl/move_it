from flask import Blueprint, render_template, redirect, url_for, flash

from web_travel.admin.forms import PlaceAddForm, PlaceEditForm
from web_travel.crud import save_place, save_country, save_city
from web_travel.user.decorators import admin_required
from web_travel.place.models import Place

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
    # TODO city заполняется при загрузке страницы
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
    title = 'Изменение данных о месте'
    form = PlaceEditForm()
    return render_template('admin/edit_place.html', page_title=title, form=form)
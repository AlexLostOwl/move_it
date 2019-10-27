from flask import Blueprint, render_template, redirect, url_for, flash, request

from web_travel.place.forms import PlaceAddForm
from web_travel.crud import save_place


blueprint = Blueprint('place', __name__, url_prefix='/place')


@blueprint.route('/add-place')
def add_place():
    title = 'Add new place'
    place_form = PlaceAddForm()
    return render_template('place/add-place.html',
                           page_title=title,
                           form=place_form)


@blueprint.route('/adding-place', methods=['POST'])
def adding_place():
    # TODO city заполняется при загрузке страницы
    form = PlaceAddForm()
    if form.validate_on_submit():
        save_place(form.place.data, form.description.data,
                   form.country.data.country_name, request.form.get('city'))
        flash(f'Место {form.place.data} успешно добавлено')
        return redirect(url_for('place.add_place'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
        return redirect(url_for('place.add_place'))

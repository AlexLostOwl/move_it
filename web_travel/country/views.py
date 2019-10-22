from flask import Blueprint, render_template, url_for, redirect, flash

from web_travel.country.forms import CountryForm
from web_travel.country.models import Country
from web_travel import db


blueprint = Blueprint('country', __name__, url_prefix='/country')


@blueprint.route('/add')
def add():
    title = 'Add new country'
    country_form = CountryForm()
    return render_template('country/add.html', page_title=title, form=country_form)


@blueprint.route('/adding-process', methods=['POST'])
def adding_process():
    form = CountryForm()
    if form.validate_on_submit():
        new_country = Country(country_name=form.country_name.data)
        db.session.add(new_country)
        db.session.commit()
        flash('Country successful add')
        return redirect(url_for('index'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Error in field "{}" - {}'.format(
                    getattr(form, field).label.text,
                    error
                ))
    return redirect(url_for('country.add'))

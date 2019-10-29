from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user

from web_travel.db import db
from web_travel.user.forms import LoginForm, RegistrationForm
from web_travel.user.models import User

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    title = 'Authorization'
    form = LoginForm()
    return render_template('uses/login.html', page_title=title, form=form)


@blueprint.route('process-login', methods=['POST'])
def process_login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            login_user(user)
            flash('You successfully logged in')
            return redirect(url_for('main.index'))
    flash('Wrond name or password')
    return redirect(url_for('user.login'))


@blueprint.route('/logout')
def logout():
    logout_user()
    flash('You have been successfully logged out')
    return redirect(url_for('main.index'))


@blueprint.route('/register')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    title = 'Registration'
    registration_form = RegistrationForm()
    return render_template('user/registration.html', page_title=title, form=registration_form)


@blueprint.route('/process-register', methods=['POST'])
def process_register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have been successfully registered')
        return redirect(url_for('user.login'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(f'Looks like mistakes in field {getattr(form, field).label.text}: {error}')
    flash('Please fix mistakes in forms')
    return redirect(url_for('user.register'))

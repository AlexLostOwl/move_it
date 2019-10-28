from flask import Blueprint, render_template, url_for, redirect, flash


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
def index():
    title = 'Administration'
    return render_template('admin/index.html', page_title=title)

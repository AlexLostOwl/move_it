from flask import Blueprint, render_template

from web_travel.user.decorators import admin_required

blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('/')
@admin_required
def index():
    title = 'Admin panel'
    return render_template('admin/index.html', page_title=title)

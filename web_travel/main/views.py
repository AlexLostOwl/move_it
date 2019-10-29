from flask import Blueprint, current_app, render_template

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    title = "Travel Project"
    test_text = "Hello this is the test page"
    return render_template('main/index.html', page_title=title, text=test_text)
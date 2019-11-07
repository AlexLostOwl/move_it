from flask import Blueprint, render_template

from web_travel.crud import get_random_place, get_description_by_place, get_photo_by_place

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
def index():
    welcome_string = "Travel Project"
    carousel_items = []
    for i in range(3):
        items = {'place': get_random_place()}
        description = get_description_by_place(items['place'])
        description = description[:100] + '..' if len(description) > 100 else description
        items['description'] = description
        items['photo_link'] = get_photo_by_place(items['place'])
        carousel_items.append(items)
    return render_template('main/index.html', jumbo_head=welcome_string, carousel_items=carousel_items)

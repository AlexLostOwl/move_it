from web_travel import create_app
from web_travel.rutraveller_parser import get_places

app = create_app()
with app.app_context():
    get_places()

from getpass import getpass
import sys

from web_travel import create_app
from web_travel.db import db
from web_travel.user.models import User


app = create_app()


with app.app_context():
    username = input('Please print admin usernname: ')

    if User.query.filter(User.username == username).count():
        print('User already exist')
        sys.exit(0)

    password1 = getpass('Please enter admin password: ')
    password2 = getpass('Please repeat admin password: ')
    if not password1 == password2:
        print('Passwords are not equal!')
        sys.exit(0)

    new_user = User(username=username, role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f'Admin user with id={new_user.id} has been created')

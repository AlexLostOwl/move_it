import os

# user = os.environ['POSTGRES_USER']
# password = os.environ['POSTGRES_PASSWORD']
# host = os.environ['POSTGRES_HOST']
# database = os.environ['POSTGRES_DB']
# port = os.environ['POSTGRES_PORT']

POSTGRES_USER = 'test'
POSTGRES_PASSWORD = 'password1'
POSTGRES_HOST = 'localhost'
POSTGRES_PORT = '5432'
POSTGRES_DB = 'travel_it'

DATABASE_CONNECTION_URI = f'postgres+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/' \
                          f'{POSTGRES_DB}'

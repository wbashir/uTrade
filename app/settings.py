import os

# configure our database
DATABASE = {
    'name': os.getenv('APP_DB_NAME'),
    'engine': os.getenv('APP_DB_ENGINE'),
    'user': os.getenv('APP_DB_USER'),
    'password': os.getenv('APP_DB_PASSWORD'),
    'host': os.getenv('APP_DB_HOST'),
    'port': os.getenv('APP_DB_PORT')
}

DEBUG = True

HOST = '0.0.0.0'
PORT = 3000

SERVER_NAME = '{0}:{1}'.format(HOST, PORT)

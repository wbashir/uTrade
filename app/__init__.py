from flask import Flask
from flask_peewee.db import Database

app = Flask(__name__)
app.config.from_object('app.settings')
app.config.from_object('app.local_settings')

# instantiate the db wrapper
db = Database(app)

from app.encoders import JSONEncoder

app.json_encoder = JSONEncoder

from app import views

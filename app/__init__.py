from flask import Flask
from flask_migrate import Migrate

from app.config import Config
from app.models import db

app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)

db.init_app(app)

from app.views import *

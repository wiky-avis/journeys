from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_migrate import Migrate

from app.config import Config
from app.models import Tour, db

app = Flask(__name__)
admin = Admin(app)
app.config.from_object(Config)
migrate = Migrate(app, db)

db.init_app(app)

from app.views import *

admin.add_view(ModelView(Tour, db.session))

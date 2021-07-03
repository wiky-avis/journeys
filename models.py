from flask_sqlalchemy import SQLAlchemy
from flask import Flask


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Tour(db.Model):
    __tablename__ = 'tours'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    departure = db.Column(db.String)
    picture = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2))
    stars = db.Column(db.Integer)
    country = db.Column(db.String)
    nights = db.Column(db.Integer)
    date = db.Column(db.Date)


db.create_all()

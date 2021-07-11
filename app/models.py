from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Tour(db.Model):
    __tablename__ = 'tour'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.Text)
    departure = db.Column(db.String)
    abbr = db.relationship(
        'Departure',
        primaryjoin='and_(Tour.id==Departure.tour_id, '
        'Departure.abbr==Tour.departure)')
    picture = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2))
    stars = db.Column(db.Integer)
    country = db.Column(db.String)
    nights = db.Column(db.Integer)
    date = db.Column(db.Date)


class Departure(db.Model):
    __tablename__ = 'departure'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    abbr = db.Column(db.String)
    tour_id = db.Column(db.Integer, db.ForeignKey('tour.id'))

    def __repr__(self) -> str:
        return self._repr(abbr=self.title)

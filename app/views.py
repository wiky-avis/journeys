from flask import render_template

from app import app, db
from app.models import Tour


@app.route('/')
def render_main():
    tours = db.session.query(Tour).all()
    #tours = db.session.query(Tour).order_by(Tour.title.desc()).limit(10)
    #tour = db.session.query(Tour).get(1) # получение одной записи
    return render_template('index.html', tours=tours)


@app.route('/departures/<departure>/')
def render_products():
    return render_template('departure.html')


@app.route('/tours/<int:tour_id>/')
def render_book(tour_id):
    tour = Tour.query.filter_by(id=tour_id).first()
    return render_template('tour.html', tour=tour)


@app.errorhandler(404)
def render_not_found(error):
    return 'Что-то не так, но мы все починим:\n{}'.format(error), 404


@app.errorhandler(500)
def render_server_error(error):
    return 'Что-то не так, но мы все починим', 500

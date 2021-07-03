from flask import Flask, render_template
from models import Tour, db


app = Flask(__name__)


@app.route('/')
def render_main():
    tours = db.session.query(Tour).all()
    #tours = db.session.query(Tour).order_by(Tour.title.desc()).limit(10)
    #tour = db.session.query(Tour).get(1) # получение одной записи
    return render_template('index.html', tours=tours)


@app.route('/departures/<departure>/')
def render_products():
    return render_template('departure.html')


@app.route('/tours/<int:id>/')
def render_book(book_id):
    print(type(book_id))
    return render_template('tour.html')


@app.errorhandler(404)
def render_not_found(error):
    return "Что-то не так, но мы все починим:\n{}".format(error), 404


@app.errorhandler(500)
def render_server_error(error):
    return "Что-то не так, но мы все починим", 500


app.run()

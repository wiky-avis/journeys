from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_main():
	return render_template('index.html')


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

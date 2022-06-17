from turtle import title
from flask import Flask, render_template
import data

app = Flask(__name__)


@app.errorhandler(404)
def render_not_found(_):
  return "Ничего не нашлось. Скоро мы это исправим :)", 404
    

@app.route('/')
def render_main():
    return render_template('index.html', tours=data.tours, title=data.title, departures=data.departures, subtitle=data.subtitle, description=data.description)

@app.route('/depatures/<departure>/')
def render_departures(departure):
    tours = dict(filter(lambda tour: tour[1]['departure'] == departure, data.tours.items()))
    return render_template('departure.html', title=data.title, departure=departure, departures=data.departures, tours=tours)

@app.route('/tours/<int:id>/')
def render_tours(id):
    return render_template('tour.html', tour=data.tours[id], title=data.title, departures=data.departures)



if __name__ == '__main__':
  app.run(debug=True)
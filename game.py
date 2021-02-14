import os

from flask import Flask, render_template, redirect, url_for, request
from src import streetview, mapinfo

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


# Home Page
@app.route('/')
def index():
    return render_template('welcomePage.html')


# Map Page
@app.route('/mapPage')
def show_map():
    place = mapinfo.FindPlace()
    location = place.get_location()
    return render_template('mapPage.html', location=location)


@app.route('/scorePage',  methods=['GET'])
def show_score():
    score = request.args.get('score')
    return render_template('scorePage.html', score=score)


@app.route('/refresh')
def refresh():
    """
    refreshes the question
    """
    streetview.StreetView()
    return redirect(url_for('show_map'))

# @app.route('/getscore')
# def get_score():
#     """
#     refreshes the question
#     """
#     streetview.StreetView()
#     return redirect(url_for('show_map'))


if __name__ == '__main__':
    app.run()

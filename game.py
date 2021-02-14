import os

from flask import Flask, render_template, redirect, url_for
import streetview

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')


# Home Page
@app.route('/')
def index():
    return render_template('welcomePage.html')


# Map Page
@app.route('/mapPage')
def show_map():
    return render_template('mapPage.html')


@app.route('/result')
def show_score():
    return render_template('calcScore.html')


@app.route('/refresh')
def refresh():
    """
    refreshes the question
    """
    streetview.StreetView()
    return redirect(url_for('show_map'))


if __name__ == '__main__':
    app.run()

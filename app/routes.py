from flask import render_template

from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/countries')
def countries():
    return render_template('countries.html')
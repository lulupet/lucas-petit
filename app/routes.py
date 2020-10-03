from flask import render_template

from app import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/countries')
def countries():
    return render_template('countries.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<id>')
def article(id):
    return render_template('articles/article_{}.html'.format(id))
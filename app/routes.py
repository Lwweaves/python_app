from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Luke'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Harrisburg!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Spiderman is the ultimate super hero'
        }

    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

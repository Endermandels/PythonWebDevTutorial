"""
Tutorial from Codemy.com on YouTube
    https://youtu.be/0Qxtt4veJIc?si=62kyEF-3QPqfB3yn

$env:FLASK_ENV="development" (enables development env)
$env:FLASK_DEBUG="True" (enables live feedback from source code changes)
$env:FLASK_APP="hello.py" (tells flask which file is the main app)

Jinja keywords:
    safe        (Don't strip HTML tags)
    capitalize
    lower
    upper
    title
    trim        (Trim trailing whitespace)
    striptags   (Strip HTML tags)
"""

from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    stuff = 'This is <strong>Bold</strong> text'
    pizza_toppings = ['cheese', 'pepperoni', 'pineapple']
    return render_template('index.html'
                           , stuff=stuff
                           , pizza_toppings=pizza_toppings)

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', username=name)
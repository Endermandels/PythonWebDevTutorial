"""
Tutorial from Codemy.com on YouTube
    https://youtu.be/0Qxtt4veJIc?si=62kyEF-3QPqfB3yn

$env:FLASK_ENV="development" (enables development env)
$env:FLASK_DEBUG="True" (enables live feedback from source code changes)
$env:FLASK_APP="hello.py" (tells flask which file is the main app)
"""

from flask import Flask, render_template

# Create Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

def index():
    return "<h1>Hello World!</h1>"



@app.route('/user/<name>')

def user(name):
    return f"<h1>Bye, {name}</h1>"
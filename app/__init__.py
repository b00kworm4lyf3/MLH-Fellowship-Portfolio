import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from .data import hobbies

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/hobbies')
def hobbyPage():
    return render_template('hobbies.html', title = "My Hobbies", url = os.getenv("URL"), hobbies = hobbies)

@app.route('/about')
def about():
    return render_template('about.html')

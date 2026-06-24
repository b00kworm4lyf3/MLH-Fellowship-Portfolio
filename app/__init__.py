import os
from flask import Flask, render_template
from dotenv import load_dotenv

from .data import user, hobbies, exp, edu

load_dotenv()
app = Flask(__name__)

LINKS = [{"name": "About",   "endpoint": "about", "tagline": "About Me"},
         {"name": "Work",    "endpoint": "work", "tagline": "Work Experience"},
         {"name": "Hobbies", "endpoint": "hobby", "tagline": "My Hobbies"}]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", user = user)

@app.route('/hobbies')
def hobby():
    return render_template('hobbies.html', title = "My Hobbies", hobbies = hobbies)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me", user = user, edu = edu)

@app.route('/work')
def work():
    return render_template('work.html', title="Work Experience", exp = exp)

@app.context_processor
def nav():
    return{"links": LINKS, "url": os.getenv("URL")}
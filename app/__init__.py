import os
from flask import Flask, render_template
from dotenv import load_dotenv
import folium


from .data import user, hobbies, exp, edu, travel

load_dotenv()
app = Flask(__name__)

LINKS = [
    {"name": "About",   "endpoint": "about", "tagline": "About Me"},
    {"name": "Work",    "endpoint": "work", "tagline": "Work Experience"},
    {"name": "Hobbies", "endpoint": "hobby", "tagline": "My Hobbies"},
    {"name": "Travel", "endpoint": "travel_page", "tagline": "My Travels"}
]

CONTACT = [
    {"label": "Contact Me", "href": "mailto:you@example.com"},
    {"label": "GitHub", "href": "https://github.com/"},
    {"label": "LinkedIn", "href": "https://linkedin.com/"},
]

@app.route('/')
def index():
    return render_template('index.html', title="Home", user = user)

@app.route('/hobbies')
def hobby():
    return render_template('hobbies.html', title = "My Hobbies", hobbies = hobbies)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me", user = user, edu = edu)

@app.route('/work')
def work():
    return render_template('work.html', title="Work Experience", exp = exp)

@app.route('/travel')
def travel_page():
    # Create a world map
    travel_map = folium.Map(location=[20, 0], zoom_start=2)

    # Loop through visited places
    for place in travel["visited"]:
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=f"{place['name']} (Visited - {place['year']})",
            icon=folium.Icon(color='green', icon='ok-sign')
        ).add_to(travel_map)

    # Loop through wishlist places
    for place in travel["wishlist"]:
        folium.Marker(
            location=[place["lat"], place["lon"]],
            popup=f"{place['name']} (Wishlist)",
            icon=folium.Icon(color='lightgreen', icon='star')
        ).add_to(travel_map)

    # Convert map to HTML
    map_html = travel_map._repr_html_()

    return render_template('travel.html', title="Travel", map_html=map_html)

@app.context_processor
def nav():
    return{"links": LINKS, "contact": CONTACT, "url": os.getenv("URL")}
import os
from flask import Flask, render_template
from dotenv import load_dotenv
import folium


from .data import user, hobbies, exp, travel

load_dotenv()
app = Flask(__name__)

LINKS = [
    {"name": "About",   "endpoint": "about", "tagline": "About Me"},
    {"name": "Work",    "endpoint": "work", "tagline": "Work Experience"},
    {"name": "Hobbies", "endpoint": "hobby", "tagline": "My Hobbies"},
    {"name": "Travel", "endpoint": "travel_page", "tagline": "My Travels"}
]

@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", user = user)

@app.route('/hobbies')
def hobby():
    return render_template('hobbies.html', title = "My Hobbies", hobbies = hobbies)

@app.route('/about')
def about():
    return render_template('about.html', title="About Me", user = user)

@app.route('/work')
def work():
    return render_template('work.html', title="Work Experience", exp = exp)

@app.route('/travel')
def travel_page():
    # Create a world map
    travel_map = folium.Map(location=[20, 0], zoom_start=2)

    # Visited: Paris
    folium.Marker(
        location=[48.8566, 2.3522],
        popup="Paris (Visited - 2023)",
        icon=folium.Icon(color='green', icon='ok-sign')
    ).add_to(travel_map)

    # Visited: Tokyo
    folium.Marker(
        location=[35.6762, 139.6503],
        popup="Tokyo (Visited - 2024)",
        icon=folium.Icon(color='green', icon='ok-sign')
    ).add_to(travel_map)

    # Wishlist: Bhutan
    folium.Marker(
        location=[27.5142, 90.4336],
        popup="Bhutan (Wishlist)",
        icon=folium.Icon(color='lightgreen', icon='star')
    ).add_to(travel_map)

    # Convert map to HTML
    map_html = travel_map._repr_html_()

    return render_template('travel.html', title="Travel", map_html=map_html)

@app.context_processor
def nav():
    return{"links": LINKS, "url": os.getenv("URL")}
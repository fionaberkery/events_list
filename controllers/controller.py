from flask import render_template, request 
from app import app
from models.event import Event
from models.eventslist import *


@app.route('/events')
def index():
    return render_template('index.html',title='Home', events=events)

@app.route('/addevents', methods=['POST'])
def events_page():
    event_date = request.form["date"]
    event_name = request.form["title"]
    event_no_of_guests = request.form["guests"]
    event_room_location = request.form["room"]
    event_description = request.form["description"]
    new_event = Event(event_date, event_name, event_no_of_guests, event_room_location, event_description) 
    add_new_event(new_event) 
    return render_template('index.html', title='Home, tasks=tasks')
    
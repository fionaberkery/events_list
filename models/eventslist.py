from models.event import *

event1 = Event("14/04/22", "Alumni Event", 50, 1, "Codeclan Alumni meeting with current students & alumni")
event2 = Event("30/05/22", "Sophie's Birthday", 200, 5, "Sophie's 30th birthday party with lots of friends" )
event3 = Event("14/07/22", "Summer Drinks Party", 150, 10, "Summer themed work drinks party")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)
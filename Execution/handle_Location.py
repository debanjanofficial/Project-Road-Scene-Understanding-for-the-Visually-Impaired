import geocoder
from handle_Print_and_Speak import print_and_speak

def get_current_position(self):
    g = geocoder.ip('me')
    if g.ok:
        city = g.city if g.city else ""
        state = g.state if g.state else ""
        country = g.country if g.country else ""
        street = g.street if g.street else ""
        position = f"{street}, {city}, {state}"
    else:
        position = "Unable to retrieve current position"
    print_and_speak("Your current position is " + position)
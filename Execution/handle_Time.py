import datetime
from handle_Print_and_Speak import print_and_speak

def get_current_time(self):
    current_time = datetime.datetime.now().strftime("%H:%M")
    print_and_speak("The current time is " + current_time)
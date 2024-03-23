import os
import handle_Stop
from handle_Print_and_Speak import print_and_speak

def shutdown(self):
    handle_Stop.stop_sensation(self)
    print_and_speak("Shutting down Sensation...")
    # Additional cleanup or shutdown operations can be added here.
    os._exit(0)
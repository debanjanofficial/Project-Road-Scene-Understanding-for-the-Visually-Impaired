import os
from handle_Print_and_Speak import print_and_speak

def start_camera(self):
    # Implementation for taking a picture can be added here
    self.camera_already_processed = True
    print_and_speak("Camera Started")

def stop_camera(self):
    # Implementation for taking a picture can be added here
    self.camera_already_processed = False
    print_and_speak("Camera Stopped")
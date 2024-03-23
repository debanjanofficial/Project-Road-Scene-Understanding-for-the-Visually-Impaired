import handle_Location
import handle_Picture
import handle_Time
import handle_Shutdown
import handle_Stop
import handle_Sensation_Start
from handle_Print_and_Speak import print_and_speak
import handle_Inactive_Sensation
import handle_Navigation
import handle_Navigation
import handle_Camera

def process_command(self, command):
    if "what" in command.lower() and "time" in command.lower():
        handle_Time.get_current_time(self)


    elif "position" in command.lower() or "location" in command.lower():
        handle_Location.get_current_position(self)
        
    elif command.lower() == "start navigation":
        if self.navigation_already_processed is False:
            handle_Navigation.start_navigation(self)
        else:
            print_and_speak("Navigation application is already running in background")

    elif command.lower() == "stop navigation" or command.lower() == "close navigation":
        handle_Navigation.stop_navigation(self)


    elif "picture" in command.lower() or "photo" in command.lower():
        if self.take_picture_already_processed is False:
            self.take_picture_already_processed = True
            handle_Picture.take_picture(self)
        else:
            print_and_speak("Picture is already captured. Camera running in background")

    elif command.lower() == "start camera":
        if self.camera_already_processed is False:
            handle_Camera.start_camera(self)
        else:
            print_and_speak("Camera is already running in background")

    elif command.lower() == "stop camera" or command.lower() == "close camera":
        handle_Camera.stop_camera(self)


    elif command.lower() == "stop sensation" or command.lower() == "close sensation":
        handle_Stop.stop_sensation(self)

    elif "shut down sensation" in command.lower() or "down sensation" in command.lower():
        handle_Shutdown.shutdown(self)

    else:
        print_and_speak("Invalid command.")


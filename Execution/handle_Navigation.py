from handle_Print_and_Speak import print_and_speak

def start_navigation(self):
    self.navigation_already_processed = True
    print_and_speak("Navigation started")

def stop_navigation(self):
    self.navigation_already_processed = False
    print_and_speak("Navigation stopped")
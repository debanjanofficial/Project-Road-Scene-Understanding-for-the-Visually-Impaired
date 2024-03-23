from handle_Print_and_Speak import print_and_speak

def stop_sensation(self):
    if self.sensation_active:
        self.sensation_active = False
        print_and_speak("Sensation stopped.")
    else:
        print_and_speak("Sensation is not active.")
from handle_Print_and_Speak import print_and_speak
import handle_Shutdown
import handle_Sensation_Start

def handle_inactive_sensation(self, command):
    if "start" in command.lower() or "hello" in command.lower() or ("sensation" in command.lower() and "down" not in command.lower() and command.lower()!= "stop sensation"):
        if not self.sensation_active:
            handle_Sensation_Start.start_sensation(self)
            self.take_picture_already_processed = False
            self.current_position_already_processed = False
            self.camera_already_processed = False
        else:
            print_and_speak("Sensation is already active.")
    elif command.lower() == "shut down sensation":
        handle_Shutdown.shutdown(self)
    else:
        print_and_speak("Sensation is not active. Start Sensation to proceed.")
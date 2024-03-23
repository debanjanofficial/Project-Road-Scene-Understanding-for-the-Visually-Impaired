from handle_Print_and_Speak import print_and_speak
import handle_input_commands
import handle_Inactive_Sensation
import speech_recognition as sr
import threading

def start_loop(self):
    while True:
        try:
            with sr.Microphone() as source:
                self.r.adjust_for_ambient_noise(source)
                audio = self.r.listen(source, timeout=5)
                #result = self.r.recognize_whisper(audio, model="medium.en")
                result = self.r.recognize_google(audio)
                print_and_speak("You said: " + result)

                if self.sensation_active:
                    handle_input_commands.process_command(self,result)
                else:
                    handle_Inactive_Sensation.handle_inactive_sensation(self, result)

        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print("Error:", e)

def start_sensation(self):
    self.sensation_active = True
    self.take_picture_already_processed = False
    self.navigation_already_processed = False
    self.camera_already_processed = False
    print_and_speak("Sensation started.")

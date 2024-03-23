import pyttsx3

def print_and_speak(message):
    print(message)
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(message)
    engine.runAndWait()

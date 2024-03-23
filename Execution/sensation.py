#!/usr/bin/env python3

import os
import speech_recognition as sr
import pyttsx3
import threading
from handle_Print_and_Speak import print_and_speak
import handle_Inactive_Sensation
import handle_input_commands
import handle_Sensation_Start

class Sensation:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 150)
        self.sensation_active = False

    # to start asr file but doesnt start sensation
    def start(self):
        print_and_speak("Welcome. Please start sensation to experience it.")
        handle_Sensation_Start.start_loop(self)


sensation = Sensation()
sensation.start()

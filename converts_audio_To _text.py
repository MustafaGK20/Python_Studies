#Program that converts audio to text

import speech_recognition as sr
from tkinter import *
import os

window = Tk()

def voice_To_text():

    rec = sr.Recognizer()

    with sr.Microphone() as mic:

        rec.adjust_for_ambient_noise(mic)
        print("Let's talk about something...")

        audio = rec.listen(mic)
        try:

            if "voice_message.txt" not in os.listdir():
                text = open("voice_message.txt", "x", encoding="utf-8")
                text.write(rec.recognize_google(audio, language="tr-TR"))
                print("Output in notebook")

            elif "voice_message.txt" in os.listdir():
                text = open(file="voice_message.txt", mode="w", encoding="utf-8")
                text.write(rec.recognize_google(audio, language="tr-TR"))
                print("Output in notebook")

        except Exception as e:
            print("Error occıred -> " + str(e))

Label(window, text="Voice Reconder: ", height=1, width=15).grid(column=0, row=0)
Button(window, text="Start", command=voice_To_text).grid(column=1, row=0)
Label(window, text="Output in notebook: ", height=1, width=15).grid(column=0, row=1)
Button(window, text="Quit", command=window.quit).grid(column=1, row=1)

window.mainloop()
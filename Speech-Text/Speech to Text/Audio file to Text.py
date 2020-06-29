"""
Created on Mon Jun 29 23:24:43 2020

@author: aurouS_EeRiE
"""


import speech_recognition as sr
filename = ("male.wav")
r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = r.record(source)
    text = r.recognize_google(audio_data)
    print(text)
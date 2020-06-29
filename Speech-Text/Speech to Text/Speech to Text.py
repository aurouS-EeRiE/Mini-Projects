"""
Created on Mon Jun 29 23:24:37 2020

@author: aurouS_EeRiE
"""


import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    print("Speak anything : ")
    audio = r.listen(source)
    
    try:
        text = r.recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print("Sorry, could not recognize your voice")
    
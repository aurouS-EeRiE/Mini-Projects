"""
Created on Mon Jun 29 23:18:57 2020

@author: aurouS_EeRiE
"""


import speech_recognition as sr
from translate import Translator
import pyttsx3 as p


language = input("Enter the language you want to translate to: ")
translator = Translator(to_lang = language)
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything you want to translate to {}: ".format(language))
    text = r.listen(source)
    try:
        recognised_text = r.recognize_google(text)
        print('You said : {}'.format(recognised_text))
    except sr.UnknownValueError:
        print("Sorry, could not recognize your voice")
    except sr.RequestError as e:
        print("Sorry, could not recognize your voice")
    
translation = translator.translate(recognised_text)
print(translation)


engine = p.init()
volume = engine.getProperty("volume")
engine.say(translation)
engine.runAndWait()
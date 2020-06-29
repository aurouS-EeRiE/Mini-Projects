"""
Created on Mon Jun 29 23:18:34 2020

@author: aurouS_EeRiE
"""


import speech_recognition as sr
from translate import Translator

r = sr.Recognizer()
translator = Translator(to_lang = "Spanish")


with sr.Microphone() as source:
    print("Speak anything you want to translate to Spanish: ")
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
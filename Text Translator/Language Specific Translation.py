"""
Created on Mon Jun 29 23:18:34 2020

@author: aurouS_EeRiE
"""


import pyttsx3 as p
from translate import Translator

language = input("Enter the language you want to translate to: ")
translator = Translator(to_lang = language)
translation = translator.translate("I love programming")
print(translation)

engine = p.init()
volume = engine.getProperty("volume")
engine.say(translation)
engine.runAndWait()
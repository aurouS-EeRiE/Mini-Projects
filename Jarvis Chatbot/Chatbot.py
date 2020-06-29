"""
Created on Mon Jun 29 23:26:25 2020

@author: aurouS_EeRiE
"""


import speech_recognition as sr
import pyttsx3 as p

from Information import info
from Movie_recomendation import recom
from Movie_Review import Movie
from Play_Music import music


r_1 = sr.Recognizer()
engine = p.init()
engine.say("Hello, how are you doing?")
engine.runAndWait()
print("Hello, how are you doing?")

with sr.Microphone() as source:
    r_1.adjust_for_ambient_noise(source)
    text_1 = r_1.listen(source)
    try:
        recognised_text_1 = r_1.recognize_google(text_1)
        print(recognised_text_1)
    except sr.UnknownValueError:
        print("Sorry, could not recognize your voice")
    except sr.RequestError as e:
        print("Sorry, could not recognize your voice")
    
    
r_2 = sr.Recognizer()
with sr.Microphone() as source:
    r_2.adjust_for_ambient_noise(source)
    engine.say("What would you like me to do?")
    engine.runAndWait()
    print("What would you like me to do?")
    print("What do you want ?")
    text_2 = r_2.listen(source)
    try:
        recognised_text_2 = r_2.recognize_google(text_2)
        print(recognised_text_2)
    except sr.UnknownValueError:
        print("Sorry, could not recognize your voice")
    except sr.RequestError as e:
        print("Sorry, could not recognize your voice")
        

r_3 = sr.Recognizer()
if "information" in r_3.recognize_google(text_2):
    engine.say("Information about what?")
    print("Information about what?")
    engine.runAndWait()
    with sr.Microphone() as source_1:
        text_3 = r_3.listen(source_1)
        try:
            information = r_3.recognize_google(text_3)
            bot = info()
            bot.get_info(information)
        except sr.UnknownValueError:
            print("Sorry, could not recognize your voice")
        except sr.RequestError as e:
            print("Sorry, could not recognize your voice")

            
r_4 = sr.Recognizer()
if "review" in r_4.recognize_google(text_2):
    engine.say("What is the name of the movie?")
    print("What is the name of the movie?")
    engine.runAndWait()
    with sr.Microphone() as source_2:
        text_4 = r_4.listen(source_2)
        try:
            rating = r_4.recognize_google(text_4)
            bot = Movie()
            bot.movie_review(rating)
        except sr.UnknownValueError:
            print("Sorry, could not recognize your voice")
        except sr.RequestError as e:
            print("Sorry, could not recognize your voice")
            
            
r_5 = sr.Recognizer()
if "music" in r_5.recognize_google(text_2):
    engine.say("Which artist or albumm do you prefer?")
    print("Which artist or albumm do you prefer?")
    engine.runAndWait()
    with sr.Microphone() as source_3:
        text_5 = r_5.listen(source_3)
        try:
            song = r_5.recognize_google(text_5)
            bot = music()
            bot.play(song)
        except sr.UnknownValueError:
            print("Sorry, could not recognize your voice")
        except sr.RequestError as e:
            print("Sorry, could not recognize your voice")


r_6 = sr.Recognizer()
if "recomendation" in r_6.recognize_google(text_2):
    bot = recom()
    bot.recom_info()
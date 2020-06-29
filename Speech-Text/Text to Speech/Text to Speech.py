"""
Created on Mon Jun 29 23:24:29 2020

@author: aurouS_EeRiE
"""


from gtts import gTTS 
import os 
mytext = 'This is a Text to Speech program'
language = 'en'
output = gTTS(text = mytext, lang = language, slow = False) 
output.save("output.mp3") 
os.system("start output.mp3") 
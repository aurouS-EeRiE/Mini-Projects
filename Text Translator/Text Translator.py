"""
Created on Mon Jun 29 23:18:19 2020

@author: aurouS_EeRiE
"""


from translate import Translator

translator = Translator(to_lang = "Spanish")
translation = translator.translate("I love programming")
print(translation)
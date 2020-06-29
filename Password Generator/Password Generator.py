"""
Created on Mon Jun 29 22:18:23 2020

@author: aurouS_EeRiE
"""


from tkinter import * 
import string
import random

def generate_pass():
    password = []
    for i in range(3):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        digit = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(digit)
    y = "".join(str(x) for x in password)
    final.config(text = y)
        
    
master = Tk()
master.title("Password Generator by aurouS_EeRiE")
master.geometry("300x100")


btn = Button(master, text = "generate password", command = generate_pass)
btn.grid(row = 2, column = 2)
final = Label(master, font = ("times", 15, "bold"))
final.grid(row = 4, column = 2)

master.mainloop()
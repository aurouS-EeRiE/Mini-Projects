"""
Created on Mon Jun 29 22:17:48 2020

@author: aurouS_EeRiE
"""


import tkinter as tk
import random

windows = tk.Tk()
windows.geometry("400x300")
windows.title("Rock Paper Scissor")

user_score = 0
comp_score = 0
user_Choice = ""
comp_choice = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissor':2}
    return rps[choice]
def number_to_choice(number):
    rps = {0:'rock',1:'paper',2:'scissor'}
    return rps[number]
def random_computer_choice():
    return random.choice(['rock','paper','scissor'])

def result(human_choice,comp_choice):
    global user_score
    global comp_score
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)
    if (user==comp):
        print("Tie")
    elif ((user-comp)%3==1):
        print("You win")
        user_score+=1
    else:
        print("Computer wins")
        comp_score+=1
    text_area = tk.Text(master=windows,height=12,width=30,bg = "#b3b3ff")
    text_area.grid(column=0,row=4)
    answer = "Your choice:{uc} \nComputer's choice:{cc} \n Your score:{u} \n Computer score:{c} ".format(uc = user_Choice, cc=comp_choice, u=user_score, c=comp_score)
    text_area.insert(tk.END,answer)

def rock():
    global user_Choice
    global comp_choice
    user_Choice='rock'
    comp_choice= random_computer_choice()
    result(user_Choice,comp_choice)
def paper():
    global user_Choice
    global comp_choice
    user_Choice='paper'
    comp_choice= random_computer_choice()
    result(user_Choice,comp_choice)
def scissor():
    global user_Choice
    global comp_choice
    user_Choice = 'scissor'
    comp_choice= random_computer_choice()
    result(user_Choice,comp_choice)

button1 = tk.Button(text='              ROCK                ',bg = '#ff9999',command=rock)
button1.grid(column=0,row=1)
button2 = tk.Button(text='              PAPER               ',bg ='#66ffcc',command=paper)
button2.grid(column=0,row=2)
button3 = tk.Button(text='              SCISSOR             ',bg ='#79d279',command=scissor)
button3.grid(column=0,row=3)
windows.mainloop()
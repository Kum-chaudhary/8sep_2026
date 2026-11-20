from tkinter import *
from tkinter import Label
from tkinter import Button
import random

screen = Tk()
screen.title("ROCK PAPER SCISSORS GAME")
screen.geometry("500x500")
screen.config(bg="teal")

user_choice = ""
computer_choice = ""

user_choice_var = StringVar()
computer_choice_var = StringVar()

user_choice_var.set("PENDING")
computer_choice_var.set("PENDING")

def UserChoiceGame(userchoice):
    user_choice_var.set(userchoice)
    game_choice_list = ['ROCK','PAPER','SCISSORS']
    computer_choice = random.choice(game_choice_list)
    computer_choice_var.set(computer_choice)


label = Label(screen,text ="ROCK PAPER SCISSORS", font=("arial",24,'bold'),bg="teal")
label.pack()

rock_btn = Button(screen,text = "ROCK", font=("arial",18,'bold'),bg="white",command=lambda: UserChoiceGame("ROCK"))
rock_btn.place(x=10,y=60)

paper_btn = Button(screen,text = "PAPER", font=("arial",18,'bold'),bg="white",command=lambda: UserChoiceGame("PAPER"))
paper_btn.place(x=110,y=60)

scissors_btn = Button(screen,text = "SCISSORS", font=("arial",18,'bold'),bg="white",command=lambda: UserChoiceGame("SCISSORS"))
scissors_btn.place(x=220,y=60)

user_choice_btn = Button(screen,text = "USER", font=("arial",18,'bold'),bg="white",command=lambda: UserChoiceGame(user_choice_var.get()))
user_choice_btn.place(x=10,y=150)

computer_choice_btn = Button(screen,text = "COMPUTER", font=("arial",18,'bold'),bg="white",command=lambda: UserChoiceGame(computer_choice_var.get()))
computer_choice_btn.place(x=10,y=210)

user_choice_btn = Button(screen,textvariable = user_choice_var, font=("arial",12,'bold'),bg="white",command=lambda: UserChoiceGame(user_choice_var.get()))
user_choice_btn.place(x=200,y=160)

computer_choice_btn = Button(screen,textvariable = computer_choice_var, font=("arial",12,'bold'),bg="white",command=lambda: UserChoiceGame(computer_choice_var.get()))
computer_choice_btn.place(x=200,y=220)

screen.mainloop()
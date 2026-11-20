
from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x400")
root.config(bg="lightblue")

# Heading
Label(
    root,
    text="Rock Paper Scissors",
    font=("Arial", 22, "bold"),
    bg="lightblue"
).pack(pady=20)


# User Label
user_label = Label(
    root,
    text="User: ",
    font=("Arial", 15),
    bg="lightblue"
)
user_label.pack(pady=10)


# Computer Label
computer_label = Label(
    root,
    text="Computer: ",
    font=("Arial", 15),
    bg="lightblue"
)
computer_label.pack(pady=10)


# Result Label
result_label = Label(
    root,
    text="Select Your Choice",
    font=("Arial", 16, "bold"),
    bg="lightblue"
)
result_label.pack(pady=20)


# Game Function
def play(user):

    computer = random.choice(["Rock", "Paper", "Scissors"])

    user_label.config(text="User: " + user)

    computer_label.config(text="Computer: " + computer)

    if user == computer:
        result = "Match Draw!"

    elif (user == "Rock" and computer == "Scissors") or \
         (user == "Paper" and computer == "Rock") or \
         (user == "Scissors" and computer == "Paper"):

        result = "You Win!"

    else:
        result = "Computer Wins!"

    result_label.config(text=result)


# Buttons
Button(
    root,
    text="Rock",
    font=("Arial", 12),
    command=lambda: play("Rock")
).pack(side=LEFT, padx=35, pady=20)

Button(
    root,
    text="Paper",
    font=("Arial", 12),
    command=lambda: play("Paper")
).pack(side=LEFT, padx=10, pady=20)

Button(
    root,
    text="Scissors",
    font=("Arial", 12),
    command=lambda: play("Scissors")
).pack(side=LEFT, padx=10, pady=20)


root.mainloop()

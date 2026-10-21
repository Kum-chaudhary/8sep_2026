import random

print("NUMBER GUESSING GAME !!!")

print("enter the number 1 - 100 ")

computer = random.randint(1,100)

status = True

while status:
    user_number = int(input("Enter your guess number:"))
    if user_number > computer:
        print("HINT : guess below number")
    elif user_number < computer:
        print("HINT : guess the upper number")
    else:
        print("You won !!")
        status = False
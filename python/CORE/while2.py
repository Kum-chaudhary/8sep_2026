status = True

while status:
    name = input("Enter your name:")
    choice = input("Do you want to continue or no press y for yes and press n for no :")
    if choice == 'y' or choice == 'yes':
        status = True
    else:
        status = False
        
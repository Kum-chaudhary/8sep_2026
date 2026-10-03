db = {
    "username" : "",
    "email" : "",
    "password" : ""
}

def signup(username,email,password):
    if username in db.keys():
        return "User already exist !"
    else:
        db["username"] = username
        db["email"] = email
        db["password"] = password
        return "successfully register !!"

def signin(email,password):
    if db["email"] == email:
        if db["password"] == password:
            return f"Hello {db["username"]} welcome to python application"
        else:
            return f"Invalid password"
    else: 
        return f"user does not exist !"
menu = """
        Menu 
        Press 1 for registration
        press 2 for login
        press 3 for logout
"""
status = True
while status:
    print(menu)
    choice = int(input("Enter your choice :"))
    if choice == 1:
            print("Registration form :")
            name  = input("Enter your name:")
            email = input("Enter your email:")
            password = input("Enter password :")

            print(signup(name,email,password))

    elif choice == 2:
            print("login screen :")
            email = input("enter email:")
            password = input("enter password:")

            print(signin(email,password))

    else:
            print("Invalid input !!")

exist_choice = input("If you want to login press 'y' for yes and 'n' for no")
if exist_choice == 'y' or exist_choice == 'yes':
     status = True
else:
     status = False
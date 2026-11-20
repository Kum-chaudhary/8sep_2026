from tkinter import *
from tkinter import messagebox

screen = Tk()
screen.title("Login Form")
screen.geometry("400x450")  
screen.config(bg="lightblue")

#temporary user data stored
user = {}

# signup function
def signup():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error",'please fill all the fileds')
    elif username in user:
        messagebox.showerror("Error",'Username already exists')
    else:
        user[username] = password
        messagebox.showinfo("Success",'Signup successful')

# login function
def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username in user and user[username] == password:
        messagebox.showinfo('welcome, login successful')
    else:
        messagebox.showerror("Error",'Invalid username or password')

# Heading

label = Label(screen, text="Login & Signup", font=("Arial", 20, "bold"), bg="lightblue")     
label.pack(pady=25)

label = Label(screen, text="Username", font=("Arial", 12), bg="lightblue")
label.pack()

user_entry = Entry(screen, font=("Arial", 12))
user_entry.pack(pady=10)

label = Label(screen, text="Password", font=("Arial", 12), bg="lightblue")
label.pack()

pass_entry = Entry(screen, font=("Arial", 12), show="*")
pass_entry.pack(pady=10)

# Login Button 
button = Button(screen, text="Login", font=("Arial", 12), command=login)
button.pack(pady=10)

# Signup Button
button = Button(screen, text="Signup", font=("Arial", 12), command=signup)
button.pack(pady=10)



screen.mainloop()
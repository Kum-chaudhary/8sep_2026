from tkinter import *
from tkinter import Label
from tkinter import Button

screen = Tk()

screen.geometry("500x500")

screen.config(background="blue")

counter_var = IntVar()
counter_var.set(0)

counter = 0

def increment():
    global counter , counter_var
    counter += 1
    counter_var.set(counter)

def decrement():
    global counter , counter_var
    counter -= 1
    counter_var.set(counter)
    
btn1 = Button(screen,text="+ Increment",font=('arial',25,'bold'),command=increment)
#btn1.pack()
btn1.place(x = 50,y = 50)

lbl1 = Label(screen,textvariable=counter_var,font=('arial',25,'bold'))
lbl1.place(x=50,y=165)

btn2 = Button(screen,text="- Increment",font=('arial',25,'bold'),command=decrement)
btn2.place(x=50,y=250)

screen.mainloop()
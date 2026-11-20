from tkinter import *
from tkinter import Label
from tkinter import Button

screen = Tk()

screen.geometry("500x500")

screen.config(background="blue")

btn1 = Button(screen,text="+ Increment",font=('arial',25,'bold'))
#btn1.pack()
btn1.place(x = 50,y = 50)

lbl1 = Label(screen,text='1',font=('arial',25,'bold'))
lbl1.place(x=50,y=180)

btn2 = Button(screen,text="- Increment",font=('arial',25,'bold'))
btn2.place(x=50,y=250)

screen.mainloop()
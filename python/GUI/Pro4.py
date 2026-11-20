from tkinter import *

screen = Tk()

screen.geometry("500x300")

btn1 = Button(screen,text="Btn1",font=('arial',25,'bold'))
btn1.pack()

btn2 = Button(screen,text="Btn2",font=('arial',25,'bold'))
btn2.pack(side='top')

btn3 = Button(screen,text="Btn3",font=('arial',25,'bold'))
btn3.pack(side='right')

btn4 = Button(screen,text="Btn4",font=('arial',25,'bold'))
btn4.pack(side='left')

btn5 = Button(screen,text="Btn5",font=('arial',25,'bold'))
btn5.pack(side='bottom')


screen.mainloop()
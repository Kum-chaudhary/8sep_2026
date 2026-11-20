from tkinter import *

screen = Tk()
screen.title("Rock Paper Sessior")

screen.geometry("700x700")
screen.config(background='blue')

btn1 = Button(screen,text="Rock",font=('Arial',24,'bold'))
btn1.pack(side=LEFT, padx=10,pady=10)

btn2 = Button(screen,text="Paper",font=('Arial',24,'bold'))
btn2.pack(side=LEFT, padx=10,pady=20)

btn3 = Button(screen,text="Scissors",font=('Arial',24,'bold'))
btn3.pack(side=LEFT, padx=10,pady=20)

lbl1 = Label(screen,text="Computer",font=('Arial',24,'bold'))
lbl1.place(x = 50,y = 50)

lbl2 = Label(screen,text="User",font=('Arial',24,'bold'))
lbl2.place(x = 50,y = 130)

screen.mainloop()
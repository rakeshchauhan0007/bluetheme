from tkinter import *
from turtle import width

root = Tk()

e=Entry(root,width=50)
e.pack()

def click(n):
    r = Label(root, text="you pressed red button")
    r.grid(row=0,column=0)

    b = Label(root, text="you pressed red button")
    b.grid(row=0,column=0)

    bl = Label(root, text="you pressed red button")
    bl.grid(row=1,column=0)
    g = Label(root, text="you pressed red button")
    g.grid(row=1,column=1)

red_button = Button(root, text="Red button",  command=lambda:click() )
#red_button.pack()
red_button.grid(row=0,column=0)
blue_button = Button(root, text="blue button",  command=lambda :click() )
#blue_button.pack()
blue_button.grid(row=0, column=1)
black_button = Button(root, text="black button", command=lambda :click( ))
#black_button.pack()
black_button.grid(row=1, column=0)
green_button = Button(root, text='greenbutton',command=lambda :click())
green_button.grid(row=1,column=1)
root.mainloop()
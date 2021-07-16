from tkinter import *
import tkinter.font as font

calculator = Tk()
calculator.geometry('435x400')
calculator.title('Simple calculator')
calculator.iconbitmap(r'C:\Users\yaziv\Downloads\hnet.com-image (1).ico')

myfonT=font.Font(family="jersey",size=15,slant='roman')
e = Entry(calculator, width=20, bg="black", font=myfonT, fg="cyan",
borderwidth=15, relief="sunken")
e.grid(row=0, column=0, columnspan=6)


def add(number):
    entry = e.get()
    e.delete(0, END)  # The information that are typed in e.get will be deleted
    e.insert(0, str(entry) + str(number))


def clear():
    e.delete(0, END)


def button_plus():
    plus = e.get()
    global addition
    global math
    math = "addition"  # global varible is the variable that can be use by any function
    addition = int(plus)
    e.delete(0, END)


def multiply():
    mul = e.get()
    global x
    x = int(mul)
    global math
    math = "multiplication"
    e.delete(0, END)


def subtract():
    mul = e.get()
    global s
    s = int(mul)
    global math
    math = "subtraction"
    e.delete(0, END)


def divide():
    mul = e.get()
    global d
    d = int(mul)
    global math
    math = "division"
    e.delete(0, END)

def module():
    mod= e.get()
    global m
    m=int(mod)
    global math
    math="module"
    e.delete(0,END)

def power():
    pow= e.get()
    global p
    p= int(pow)
    global math
    math= "power"
    e.delete(0,END)

def total():
    second_num = e.get()
    e.delete(0, END)

    if math == "addition":
        e.insert(0, addition + int(second_num))

    if math == "multiplication":
        e.insert(0, x * int(second_num))

    if math == "division":
        e.insert(0, d / int(second_num))

    if math == "subtraction":
        e.insert(0, s - int(second_num))

    if math=="module":
         f=m//int(second_num)
         r=m-f*int(second_num)
         e.insert(0,r)

    if math=="power":
        po=p**int(second_num)
        e.insert(0,po)



calculator.configure(background="black")

myfont =font.Font(family="jersey",size=15,slant='roman')

button_1 = Button(calculator, text="1", padx=25, pady=19, bg="black",
                  activebackground="thistle2",font=myfont,
                  fg="white",   relief="flat",
                  activeforeground="red", command=lambda: add(1))
button_2 = Button(calculator, text="2", padx=25, pady=19,
                  activebackground="MediumOrchid4",
                  fg="white",        font=myfont,
                  bg="black",     relief="flat",
                  activeforeground="red",
                  command=lambda: add(2))
button_3 = Button(calculator, text="3", padx=21, pady=19, bg="black", activebackground="magenta2",
                  font=myfont,
                  fg="white",      relief="flat",
                  activeforeground="red",
                  command=lambda: add(3))
button_4 = Button(calculator, text="4", padx=24, pady=19, bg="black", activebackground="OliveDrab4",
                  fg="white",       font=myfont,
                  relief="flat",
                  activeforeground="red",
                  command=lambda: add(4))
button_5 = Button(calculator, text="5", padx=25, pady=19, bg="black", activebackground="DarkSlategray2",
                  font=myfont,
                  fg="white",      relief="flat",
                  activeforeground="red",
                  command=lambda: add(5))
button_6 = Button(calculator, text="6", padx=25, pady=19, bg="black", activebackground="LightSteelBlue1",
                  font=myfont,
                  relief="flat",
                  fg="white",     activeforeground="red",
                  command=lambda: add(6))
button_7 = Button(calculator, text="7", padx=25, pady=20,bg="black", activebackground="coral",
                  font=myfont,
                  fg="white",      relief="flat",
                  activeforeground="red",
                  command=lambda: add(7))
button_8 = Button(calculator, text="8", padx=25, pady=20, bg="black", activebackground="RoyalBlue4",
                  font=myfont,
                  fg="white",       relief="flat",
                  activeforeground="red",
                  command=lambda: add(8))

button_9 = Button(calculator, text="9", padx=25, pady=20,bg="black", activebackground="dark goldenrod",
                  font=myfont,
                  fg="white",    relief="flat",
                  activeforeground="red",
                  command=lambda: add(9))
button_0 = Button(calculator, text="0", padx=29, pady=24, bg="black",
             fg="white",    activebackground="sea green",
                  font=myfont,
                 relief="flat",
                  activeforeground="red",
                  command=lambda: add(0))

myFont = font.Font(family='Jersey M54 Font',size=15,weight="bold")


button_add = Button(calculator, text="➕", padx=20, pady=20, bg="grey5",
                    fg="blue",
                    relief="flat", font=myFont, activeforeground="red",
                    activebackground="red", command=button_plus)
button_equal = Button(calculator, text="『=』",padx=9, pady=95, bg="light blue", fg="red",
                    borderwidth=7, relief="raised", font=myFont, activeforeground="red",
                      activebackground="red", command=total)
button_clear = Button(calculator, text="ⓒ", padx=24, pady=21, bg="grey5", fg="blue",
                      relief="flat", font=myFont,activeforeground="red",
                      activebackground="red", command=clear)
button_multiply = Button(calculator, text="❌", padx=20, pady=22, bg="grey5", fg="blue",
                         relief="flat", font=myFont, activeforeground="red",
                         activebackground="red", command=multiply)
button_divide = Button(calculator, text="➗", padx=20, pady=24, bg="grey5", fg="blue",
                       relief="flat", font=myFont, activeforeground="red",
                       activebackground="red", command=divide)
button_subtract = Button(calculator, text="➖", padx=20, pady=16,
                         bg="grey5", fg="blue", borderwidth=7,
                      relief="flat",font=myFont , activeforeground="red",
                         activebackground="red", command=subtract)
button_module=  Button(calculator, text="%", padx=18, pady=16,
                         bg="grey5", fg="blue", borderwidth=7,
                      relief="flat",font=myFont , activeforeground="red",
                         activebackground="red", command=module)
button_power = Button(calculator, text="^", padx=30, pady=16,
                         bg="grey5", fg="blue", borderwidth=7,
                      relief="flat",font=myFont , activeforeground="red",
                         activebackground="red", command=power)
#create Font object



button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=1, column=4)
button_equal.grid(row=1,column=5,rowspan=3, )
button_clear.grid(row=4, column=1)
button_multiply.grid(row=2, column=4)
button_divide.grid(row=3, column=4)
button_subtract.grid(row=4, column=4)
button_module.grid(row=4,column=2)
button_power.grid(row=4,column=5)
calculator.mainloop()

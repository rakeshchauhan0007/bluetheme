from tkinter import *

calculator = Tk()

calculator.title('ADD+')

e = Entry(calculator, width=20, borderwidth=10)
e.grid(row=0, column=0, columnspan=4)


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
    math="addition"# global varible is the variable that can be use by any function
    addition = int(plus)
    e.delete(0, END)


def multiply():
    mul = e.get()
    global x
    x=int(mul)
    global math
    math = "multiplication"
    e.delete(0, END)

def subtract():
    mul = e.get()
    global s
    s=int(mul)
    global math
    math = "subtraction"
    e.delete(0, END)

def divide():
    mul = e.get()
    global d
    d=int(mul)
    global math
    math = "division"
    e.delete(0, END)

def total():
     second_num = e.get()
     e.delete(0, END)

     if math=="addition":
       e.insert(0, addition + int(second_num))

     if math == "multiplication":
         e.insert(0, x* int(second_num))

     if math == "division":
         e.insert(0, d / int(second_num))

     if math == "subtraction":
         e.insert(0, s - int(second_num))

button_1 = Button(calculator, text="1", padx=15, pady=10, fg="blue", bg="grey", command=lambda: add(1))
button_2 = Button(calculator, text="2", padx=15, pady=10, bg="grey", command=lambda: add(2))
button_3 = Button(calculator, text="3", padx=15, pady=10, bg="grey", command=lambda: add(3))
button_4 = Button(calculator, text="4", padx=15, pady=10, bg="grey", command=lambda: add(4))
button_5 = Button(calculator, text="5", padx=15, pady=10, bg="grey", command=lambda: add(5))
button_6 = Button(calculator, text="6", padx=15, pady=10, bg="grey", command=lambda: add(6))
button_7 = Button(calculator, text="7", padx=15, pady=10, bg="grey", command=lambda: add(7))
button_8 = Button(calculator, text="8", padx=15, pady=10, bg="grey", command=lambda: add(8))
button_9 = Button(calculator, text="9", padx=15, pady=10, bg="grey", command=lambda: add(9))
button_0 = Button(calculator, text="0", padx=15, pady=10, bg="grey", command=lambda: add(0))
button_add = Button(calculator, text="+", padx=15, pady=10, bg="grey", command=button_plus)
button_equal = Button(calculator, text="=", padx=15, pady=10, bg="grey", command=total)
button_clear = Button(calculator, text="C", padx=15, pady=10, bg="grey", command=clear)
button_multiply = Button(calculator, text="X", padx=15, pady=10, bg="grey", command=multiply)
button_divide = Button(calculator, text="/", padx=15, pady=10, bg="grey", command= divide)
button_subtract = Button(calculator, text="-", padx=15, pady=10, bg="grey", command=subtract)

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=1, column=3)
button_5.grid(row=2, column=0)
button_6.grid(row=2, column=1)
button_7.grid(row=2, column=2)
button_8.grid(row=2, column=3)
button_9.grid(row=3, column=0)
button_0.grid(row=3, column=1)
button_add.grid(row=3, column=2)
button_equal.grid(row=3, column=3)
button_clear.grid(row=4, column=0)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)
calculator.mainloop()

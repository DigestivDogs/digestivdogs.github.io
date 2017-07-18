from Tkinter import *
import parser

def aboutwindow():
    aboutwindow = Tk()
    aboutwindow.title('Calculator - About')

    Label(aboutwindow, text="Name: DogeyDogs' Python Calculator\nWebsite: https://digestivdogs.github.io/\nCopyriright: DigestivDogs 2017\n\n\nAbout:\nHello, welcome to my Python Calculator...\nThis was a project that took me around 3 weeks to complete as I didn't\nknow Tkinter back then.\nKeep on the lookout for updates on the DigestivDogs website!\nIf the updates don't work you can always download an older version!\nEnjoy testing,\nDogeyDogs").pack()

    aboutwindow.mainloop()

mainwindow = Tk()
mainwindow.title('Calculator')

menubar = Menu(mainwindow)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=aboutwindow)
menubar.add_cascade(label='Help', menu=helpmenu)
 
mainwindow.config(menu=menubar)

i = 0

def factorial():
    whole_string = display.get()
    number = int(whole_string)
    fact = 1
    counter = number 
    try:
        while counter > 0:
            fact = fact*counter
            counter -= 1
        clear_all()
        display.insert(0, fact)
    except Exception:
        clear_all()
        display.insert(0, "Error")


def clear_all():
    display.delete(0, END)

def get_variables(num):
    global i
    display.insert(i, num)
    i += 1

def get_operation(operator):
    global i
    length = len(operator)
    display.insert(i, operator)
    i += length

def undo():
    whole_string = display.get()
    if len(whole_string):
        new_string = whole_string[:-1]
        print(new_string)
        clear_all()
        display.insert(0, new_string)
    else:
        clear_all() 
        display.insert(0, "Error, press AC")

def calculate():
    whole_string = display.get()
    try:
        formulae = parser.expr(whole_string).compile()
        result = eval(formulae)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error!")

mainwindow.columnconfigure(0,pad=3)
mainwindow.columnconfigure(1,pad=3)
mainwindow.columnconfigure(2,pad=3)
mainwindow.columnconfigure(3,pad=3)
mainwindow.columnconfigure(4,pad=3)

mainwindow.rowconfigure(0,pad=3)
mainwindow.rowconfigure(1,pad=3)
mainwindow.rowconfigure(2,pad=3)
mainwindow.rowconfigure(3,pad=3)

display = Entry(mainwindow, font = ("Calibri", 13))
display.grid(row = 1, columnspan = 6    , sticky = W+E)

one = Button(mainwindow, text = "1", command = lambda : get_variables(1), font=("Calibri", 12))
one.grid(row = 2, column = 0)
two = Button(mainwindow, text = "2", command = lambda : get_variables(2), font=("Calibri", 12))
two.grid(row = 2, column = 1)
three = Button(mainwindow, text = "3", command = lambda : get_variables(3), font=("Calibri", 12))
three.grid(row = 2, column = 2)

four = Button(mainwindow, text = "4", command = lambda : get_variables(4), font=("Calibri", 12))
four.grid(row = 3 , column = 0)
five = Button(mainwindow, text = "5", command = lambda : get_variables(5), font=("Calibri", 12))
five.grid(row = 3, column = 1)
six = Button(mainwindow, text = "6", command = lambda : get_variables(6), font=("Calibri", 12))
six.grid(row = 3, column = 2)

seven = Button(mainwindow, text = "7", command = lambda : get_variables(7), font=("Calibri", 12))
seven.grid(row = 4, column = 0)
eight = Button(mainwindow, text = "8", command = lambda : get_variables(8), font=("Calibri", 12))
eight.grid(row = 4, column = 1)
nine = Button(mainwindow , text = "9", command = lambda : get_variables(9), font=("Calibri", 12))
nine.grid(row = 4, column = 2)

cls = Button(mainwindow, text = "AC", command = clear_all, font=("Calibri", 12), foreground = "red")
cls.grid(row = 5, column = 0)
zero = Button(mainwindow, text = "0", command = lambda : get_variables(0), font=("Calibri", 12))
zero.grid(row = 5, column = 1)
result = Button(mainwindow, text = "=", command = calculate, font=("Calibri", 12), foreground = "red")
result.grid(row = 5, column = 2)

plus = Button(mainwindow, text = "+", command =  lambda : get_operation("+"), font=("Calibri", 12))
plus.grid(row = 2, column = 3)
minus = Button(mainwindow, text = "-", command =  lambda : get_operation("-"), font=("Calibri", 12))
minus.grid(row = 3, column = 3)
multiply = Button(mainwindow,text = "*", command =  lambda : get_operation("*"), font=("Calibri", 12))
multiply.grid(row = 4, column = 3)
divide = Button(mainwindow, text = "/", command = lambda :  get_operation("/"), font=("Calibri", 12))
divide.grid(row = 5, column = 3)

pi = Button(mainwindow, text = "pi", command = lambda: get_operation("3.141592"), font =("Calibri", 12))
pi.grid(row = 2, column = 4)
modulo = Button(mainwindow, text = "%", command = lambda :  get_operation("%"), font=("Calibri", 12))
modulo.grid(row = 3, column = 4)
left_bracket = Button(mainwindow, text = "(", command = lambda: get_operation("("), font =("Calibri", 12))
left_bracket.grid(row = 4, column = 4)
exp = Button(mainwindow, text = "exp", command = lambda: get_operation("**"), font = ("Calibri", 10))
exp.grid(row = 5, column = 4)

undo_button = Button(mainwindow, text = "<-", command = undo, font =("Calibri", 12), foreground = "red")
undo_button.grid(row = 2, column = 5)
fact = Button(mainwindow, text = "x!", command = factorial, font=("Calibri", 12))
fact.grid(row = 3, column = 5)
right_bracket = Button(mainwindow, text = ")", command = lambda: get_operation(")"), font =("Calibri", 12))
right_bracket.grid(row = 4, column = 5)
square = Button(mainwindow, text = "^2", command = lambda: get_operation("**2"), font = ("Calibri", 10))
square.grid(row = 5, column = 5)

mainwindow.mainloop()

from tkinter import *

import tkinter
import tkinter.messagebox

#This is the variable that stores answers and calculations and is displayed
#on the calculator 'screen'. User input is saved as a string.
a = ""

#This is used to tell if '=' has just been pressed, if you press an
#operator immediately after pressing '=' then you want to operate on the
#answer  that's just been calculated. If a number is pressed immediately after
#then a new calculation is going to be started. When '=' is pressed
#this becomes True. When anything else is pressed it becomes False.
count = False 

#Adds the user input to a. If '=' has just been pressed followed by  a number
#or '.' then a is cleared and a new calculation is started.
def add_to_variable(val, _event = None):
    global a
    global count

    if count == True and (val.isdigit() == True or val == "."):
        a = ""
        
    a += val
    E1.delete(0, END)
    Entry.insert(E1, 0 , a)
    count = False
    
#if user presses the delete button then the calculator is cleared
def delete(_event = None):
    global a
    a = ""
    E1.delete(0, END)

#when the user presses '=' the atring contained in a is evaluated, python
#automatically solves the calculation, the answer is then converted back into
#a string. If it can'tdo this then an error message is displayed.
def equals(_event = None):
    try:
      global a
      global count
      a = str(eval(a))
      E1.delete(0, END)
      Entry.insert(E1, 0, a)
      count = True
    except:
        tkinter.messagebox.showwarning("Warning", "Enter a valid calculation")
                                       
master = Tk()

#making the calculator's 'screen'
E1 = Entry(master, bd = 1)
E1.grid(row = 0, columnspan = 4, padx = 5, pady = 5)

#setting out all the buttons and binding the functions to them
B1 = Button(master, text = "C", command = delete).grid(row = 1, column = 0, sticky = NSEW, padx = 2, pady = 2)
B2 = Button(master, text = "^", command = lambda: add_to_variable("**")).grid(row = 1, column = 1, sticky = NSEW, padx = 2, pady = 2)
B3 = Button(master, text = "(", command = lambda: add_to_variable("(")).grid(row = 1, column = 2, sticky = NSEW, padx = 2, pady = 2)
B4 = Button(master, text = ")", command = lambda: add_to_variable(")")).grid(row = 1, column = 3, sticky = NSEW, padx = 2, pady = 2)
B5 = Button(master, text = "/", command = lambda: add_to_variable("/")).grid(row = 2, column = 0, sticky = NSEW, padx = 2, pady = 2)
B6 = Button(master, text = "7", command = lambda: add_to_variable("7")).grid(row = 2, column = 1, sticky = NSEW, padx = 2, pady = 2)
B7 = Button(master, text = "8", command = lambda: add_to_variable("8")).grid(row = 2, column = 2, sticky = NSEW, padx = 2, pady = 2)
B8 = Button(master, text = "9", command = lambda: add_to_variable("9")).grid(row = 2, column = 3, sticky = NSEW, padx = 2, pady = 2)
B9 = Button(master, text = "*", command = lambda: add_to_variable("*")).grid(row = 3, column = 0, sticky = NSEW, padx = 2, pady = 2)
B10 = Button(master, text = "4", command = lambda: add_to_variable("4")).grid(row = 3, column = 1, sticky = NSEW, padx = 2, pady = 2)
B11 = Button(master, text = "5", command = lambda: add_to_variable("5")).grid(row = 3, column = 2, sticky = NSEW, padx = 2, pady = 2)
B12 = Button(master, text = "6", command = lambda: add_to_variable("6")).grid(row = 3, column = 3, sticky = NSEW, padx = 2, pady = 2)
B13 = Button(master, text = "-", command = lambda: add_to_variable("-")).grid(row = 4, column = 0, sticky = NSEW, padx = 2, pady = 2)
B14 = Button(master, text = "1", command = lambda: add_to_variable("1")).grid(row = 4, column = 1, sticky = NSEW, padx = 2, pady = 2)
B15 = Button(master, text = "2", command = lambda: add_to_variable("2")).grid(row = 4, column = 2, sticky = NSEW, padx = 2, pady = 2)
B16 = Button(master, text = "3", command = lambda: add_to_variable("3")).grid(row = 4, column = 3, sticky = NSEW, padx = 2, pady = 2)
B17 = Button(master, text = "+", command = lambda: add_to_variable("+")).grid(row = 5, column = 0, sticky = NSEW, padx = 2, pady = 2)
B18 = Button(master, text = ".", command = lambda: add_to_variable(".")).grid(row = 5, column = 1, sticky = NSEW, padx = 2, pady = 2)
B19 = Button(master, text = "0", command = lambda: add_to_variable("0")).grid(row = 5, column = 2, sticky = NSEW, padx = 2, pady = 2)
B20 = Button(master, text = "=", command = equals ).grid(row = 5, column = 3, sticky = NSEW, padx = 2, pady = 2)

#binding keys on the keyboards to  the functions, you have to bind the keys
#directly to the functions themselves rather than binding the keys to the
#buttons
master.bind("<Delete>", delete)
master.bind("<^>", lambda x: add_to_variable("**"))
master.bind("(", lambda x: add_to_variable("("))
master.bind(")", lambda x: add_to_variable(")"))
master.bind("/", lambda x: add_to_variable("/"))
master.bind("7", lambda x: add_to_variable("7"))
master.bind("8", lambda x: add_to_variable("8"))
master.bind("9", lambda x: add_to_variable("9"))
master.bind("*", lambda x: add_to_variable("*"))
master.bind("4", lambda x: add_to_variable("4"))
master.bind("5", lambda x: add_to_variable("5"))
master.bind("6", lambda x: add_to_variable("6"))
master.bind("-", lambda x: add_to_variable("-"))
master.bind("1", lambda x: add_to_variable("1"))
master.bind("2", lambda x: add_to_variable("2"))
master.bind("3", lambda x: add_to_variable("3"))
master.bind("+", lambda x: add_to_variable("+"))
master.bind(".", lambda x: add_to_variable("."))
master.bind("0", lambda x: add_to_variable("0"))
master.bind("=", equals)
master.bind("<Return>", equals)

master.mainloop()

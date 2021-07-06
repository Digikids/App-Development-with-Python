import tkinter.messagebox
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Simple Calculator")
window.configure(bg="Orange")
window.geometry("300x300")

lbl1 = Label(window, text="First Number", bg="Orange")
lbl1.grid(column=0, row=0)
txt1 = Entry(window, width=10,borderwidth=5, bg ="white", fg = "black")
txt1.grid(column=1, row=0)

lbl2 = Label(window, text="Second Number", bg="Orange")
lbl2.grid(column=0, row=1)
txt2 = Entry(window, width=10,borderwidth=5, bg ="white", fg = "black")
txt2.grid(column=1, row=1)

lbl3 = Label(window, text="Answer", bg="Orange")
lbl3.grid(column=0, row=2)
txt3 = Entry(window, width=10,borderwidth=5, bg ="white", fg = "black")
txt3.grid(column=1, row=2)

def add(): 
    try:
        txt3.delete(0, END)
        num1 = txt1.get()
        num2 = txt2.get()
        if num1 or num2 != "":
            ans = int(num1) + int(num2)
            txt3.insert(0, ans)
        else:
            messagebox.showerror("Invalid Input", "Please type in a number")
    except ValueError:
        messagebox.showerror("Invalid Input", "Input can only be a number")

def subtract():
    txt3.delete(0, END)
    num1 = txt1.get()
    num2 = txt2.get()
    ans = int(num1) - int(num2)
    txt3.insert(0, ans)

def divide():
    txt3.delete(0, END)
    num1 = txt1.get()
    num2 = txt2.get()
    ans = int(num1) / int(num2)
    txt3.insert(0, ans)

def multiply():
    txt3.delete(0, END)
    num1 = txt1.get()
    num2 = txt2.get()
    ans = int(num1) * int(num2)
    txt3.insert(0, ans)

btnadd = Button(window, text="Addation", bg="Turquoise", command=add, padx=30, pady=20)
btnadd.grid(column=0,row=3)

btnsb = Button(window, text="Subtraction", bg="Turquoise", command=subtract, padx=30, pady=20)
btnsb.grid(column=0,row=4)

btnmt = Button(window, text="Multiplication", bg="Turquoise", command=multiply, padx=30, pady=20)
btnmt.grid(column=1,row=3)

btnds = Button(window, text="Division", bg="Turquoise", command=divide, padx=30, pady=20)
btnds.grid(column=1,row=4)

window.mainloop()
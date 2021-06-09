from tkinter import *

root =Tk()
root.title("My Calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3)

def button_click(number):
    entry.delete(0, END)
    current = entry.get()
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_num = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_num)
    entry.delete(0, END)

def button_subract():
    first_number = entry.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)

def button_divide():
    first_number = entry.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)

def button_multiply():
    first_number = entry.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num + int(second_number))
    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))
    if math == "division":
        entry.insert(0, f_num / int(second_number))
    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, bg="Cyan", command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = Button(root, text="2", padx=40, pady=20, bg="Cyan", command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = Button(root, text="3", padx=40, pady=20, bg="Cyan", command=lambda: button_click(3))
button_3.grid(row=3, column=2)

button_4 = Button(root, text="4", padx=40, pady=20, bg="Cyan", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = Button(root, text="5", padx=40, pady=20, bg="Cyan", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = Button(root, text="6", padx=40, pady=20, bg="Cyan", command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_7 = Button(root, text="7", padx=40, pady=20, bg="Cyan", command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = Button(root, text="8", padx=40, pady=20, bg="Cyan", command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = Button(root, text="9", padx=40, pady=20, bg="Cyan", command=lambda: button_click(9))
button_9.grid(row=1, column=2)

button_0 = Button(root, text="0", padx=40, pady=20, bg="Cyan", command=lambda: button_click(0))
button_0.grid(row=4, column=0)
button_clear = Button(root, text="Clear", padx=80, pady=20, bg="Cyan", command=button_clear)
button_clear.grid(row=4, column=1, columnspan=2)

button_add = Button(root, text="+", padx=40, pady=20, bg="Cyan", command = button_add)
button_add.grid(row=5, column=0)
button_equals = Button(root, text="=", padx=80, pady=20, bg="Cyan", command = button_equal)
button_equals.grid(row=5, column=1, columnspan=2)

button_multiply = Button(root, text="*", padx=40, pady=20, bg="Cyan", command = button_multiply)
button_multiply.grid(row=6, column=0)
button_Divide = Button(root, text="/", padx=40, pady=20, bg="Cyan", command = button_divide)
button_Divide.grid(row=6, column=1)
button_minus = Button(root, text="-", padx=40, pady=20, bg="Cyan", command= button_subract)
button_minus.grid(row=6, column=2)


root.mainloop()
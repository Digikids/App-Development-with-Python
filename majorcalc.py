from tkinter import *
import math

#SetUp
calc = Tk()
calc.title("Calculator")
calc.geometry("440x450")
calc.configure(bg="OliveDrab2")

# Entry Widget
en = Entry(calc, width=35, borderwidth=5, bg="white", fg="black")
en.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

b7 = Button(calc, text="7", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b7.grid(column=0, row=1)
b8 = Button(calc, text="8", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b8.grid(column=1, row=1)
b9 = Button(calc, text="9", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b9.grid(column=2, row=1)
b_plus = Button(calc, text="+", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_plus.grid(column=3, row=1)

b4 = Button(calc, text="4", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b4.grid(column=0, row=2)
b5 = Button(calc, text="5", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b5.grid(column=1, row=2)
b6 = Button(calc, text="6", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b6.grid(column=2, row=2)
b_minus = Button(calc, text="-", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_minus.grid(column=3, row=2)

b1 = Button(calc, text="1", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b1.grid(column=0, row=3)
b2 = Button(calc, text="2", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b2.grid(column=1, row=3)
b3 = Button(calc, text="3", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b3.grid(column=2, row=3)
b_multi = Button(calc, text="X", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_multi.grid(column=3, row=3)

b0 = Button(calc, text="0", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b0.grid(column=0, row=4)
bdeci = Button(calc, text=".", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
bdeci.grid(column=1, row=4)
b_equals = Button(calc, text="=", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_equals.grid(column=2, row=4)
b_div = Button(calc, text="/", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_div.grid(column=3, row=4)

b_square = Button(calc, text="x²", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_square.grid(column=0, row=5)
b_squareroot = Button(calc, text="√", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_squareroot.grid(column=1, row=5)
b_delete = Button(calc, text="DEL", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_delete.grid(column=2, row=5)
b_exit = Button(calc, text="EXIT", padx=40, pady=20, bg="Light blue", fg="black", width=2, height=2)
b_exit.grid(column=3, row=5)

calc.mainloop()
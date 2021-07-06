# Create your first GUI application (Graphical User Interphase)
from tkinter import *

window = Tk()

window.title("Welcome to my first application")
window.geometry("350x200")
window.configure(bg="Turquoise")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

txt = Entry(window, width=20)
txt.grid(column=2, row=0)
txt.focus()

def clicked():
    res = txt.get()
    lbl.configure(text=res)

btn = Button(window, text="Button 1", bg="red", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
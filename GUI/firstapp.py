# Create your first GUI application (Graphical User Interphase)
from tkinter import *

window = Tk()

window.title("Welcome to my first application")
window.geometry("350x200")

lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Click me")
btn.grid(column=1, row=0)

window.mainloop()
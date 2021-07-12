from tkinter import *

from tkinter import scrolledtext

window = Tk()

window.title("Message Box")

window.geometry('350x200')

messagebox.showwarning('Message title', 'Message content')  #shows warning message

messagebox.showerror('Message title', 'Message content')    #shows error message

res = messagebox.askquestion('Message title','Message content')

res = messagebox.askyesno('Message title','Message content')

res = messagebox.askyesnocancel('Message title','Message content')

res = messagebox.askokcancel('Message title','Message content')

res = messagebox.askretrycancel('Message title','Message content')

window.mainloop()
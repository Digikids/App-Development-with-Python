from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text = "Digikids")
w.grid(column=0, row=0)

messagebox.showinfo("showinfo", "Information")
  
messagebox.showwarning("showwarning", "Warning")
  
messagebox.showerror("showerror", "Error")
  
messagebox.askquestion("askquestion", "Are you sure?")
  
messagebox.askokcancel("askokcancel", "Want to continue?")
  
messagebox.askyesno("askyesno", "Find the value?")
  
  
messagebox.askretrycancel("askretrycancel", "Try again?")  
  
root.mainloop()



for i in list:
    occurrence = list.count(i)
    print(f"{i} has occurred {occurrence} times")

def fizz_buzz(num1):
    if num1 % 3 == 0:
        print("fizz")
    if num1 % 5 == 0:
        print("buzz")
    if num1 % 3 != 0 and num1 % 5 != 0:
        print(num1)
fizz_buzz(25)

list = [1,2,2,2,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8, 25, 50, 157, 90, 45]

for i in list:
    while i < 150:
        if i % 5 == 0:
            print(i)
    
        

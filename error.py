from tkinter import *
root = Tk()

frame1 = Frame(root, bg="grey")
frame1.pack(side=TOP)

frame2 = Frame(root, bg="Purple")
frame2.pack(side=BOTTOM)

btn1 = Button(frame1, text="Add question", bg="blue")
btn1.grid(row=0, column=0)
btn2 = Button(frame1, text="Question Bank", bg="blue")
btn2.grid(row=0, column=1)

lbl1 = Label(frame2,text="Name")
lbl1.grid(row=0, column=0)
ent1 = Entry(frame2)
ent1.grid(row=0, column=1)

lbl2 = Label(frame2,text="Age")
lbl2.grid(row=1, column=0)
ent2 = Entry(frame2)
ent2.grid(row=1, column=1)

root.mainloop()
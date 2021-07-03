import tkinter as tk

window = tk.Tk()



label = tk.Label(text="Happy Birthday Caroline",fg="Red",bg="Yellow", width=40,height=10)
label.pack()

button = tk.Button(text="Click me!", bg="Green", fg="Blue", width=40, height=10,)
button.pack()

entry = tk.Entry(fg="yellow", bg="Navy blue", width=50)
entry.pack()

frame = tk.Frame()
frame.pack()

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}
for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()

window.mainloop()
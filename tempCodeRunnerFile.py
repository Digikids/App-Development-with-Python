def show():
    a = int(spin1.get())
    b = int(spin2.get())
    cal = calendar.month(b, a)#pass here your year and then month values
    #in our case i use b for year and for month
    txt.delete(0.0, END)
    txt.insert(INSERT, cal)
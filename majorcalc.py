from tkinter import *
import math
import random
from tkinter import messagebox

def Calculator():

    COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
        'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
        'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
        'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
        'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
        'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
        'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
        'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
        'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
        'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
        'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
        'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
        'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
        'indian red', 'saddle brown', 'sandy brown',
        'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
        'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
        'pale violet red', 'maroon', 'medium violet red', 'violet red',
        'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
        'thistle', 'snow2', 'snow3',
        'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
        'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
        'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
        'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
        'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
        'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
        'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
        'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
        'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
        'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
        'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
        'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
        'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
        'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
        'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
        'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
        'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
        'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
        'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
        'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
        'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
        'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
        'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
        'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
        'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
        'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
        'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
        'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
        'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
        'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
        'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
        'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
        'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
        'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
        'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
        'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
        'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
        'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
        'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
        'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
        'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
        'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
        'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
        'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
        'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
        'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
        'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray20', 'gray21', 'gray22', 'gray23',
        'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
        'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
        'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
        'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
        'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
        'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
        'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
        'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
        'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']


    # Functions
    def choose_color():
        color = random.choice(COLORS)
        return color


    #SetUp
    calc = Tk()
    calc.title("Calculator")
    calc.geometry("430x450")
    calc.configure(bg=choose_color())
    calc.resizable(0, 0)

    # Entry Widget
    en = Entry(calc, width=35, borderwidth=5, bg="white", fg="black")
    en.grid(column=0, row=0, columnspan=4, padx=10, pady=10)

    def b_exit():
        iExit = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if iExit > 0:
            calc.destroy()
            return

    def b_square():
        first_number = en.get()
        i = int(first_number)
        en.delete(0, END)
        en.insert(0, i*i)

    def b_squareroot():
        first_number = en.get()
        i = int(first_number)
        en.delete(0, END)
        en.insert(0, math.sqrt(i))

    def button_click(number):
        current = en.get()
        en.delete(0, END)
        en.insert(0, str(current) + str(number))

    def b_add():
        first_number = en.get()
        global f_num
        global math
        math = "Addition"
        f_num = int(first_number)
        en.delete(0, END)

    def b_minus():
        first_number = en.get()
        global f_num
        global math
        math = "Subtraction"
        f_num = int(first_number)
        en.delete(0, END)

    def b_multiply():
        first_number = en.get()
        global f_num
        global math
        math = "Multiplication"
        f_num = int(first_number)
        en.delete(0, END)

    def b_divide():
        first_number = en.get()
        global f_num
        global math
        math = "Division"
        f_num = int(first_number)
        en.delete(0, END)

    def b_equal():
        second_num = en.get()
        global s_num 
        s_num = second_num
        en.delete(0, END)
        if math == "Addition":
            en.insert(0, f_num + int(second_num))
        if math == "Multiplication":
            en.insert(0, f_num * int(second_num))
        if math == "Division":
            en.insert(0, f_num / int(second_num))
        if math == "Subtraction":
            en.insert(0, f_num - int(second_num))

    def b_delete():
        en.delete(0, END)

    b7 = Button(calc, text="7", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(7))
    b7.grid(column=0, row=1)
    b8 = Button(calc, text="8", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(8))
    b8.grid(column=1, row=1)
    b9 = Button(calc, text="9", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(9))
    b9.grid(column=2, row=1)
    b_plus = Button(calc, text="+", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_add)
    b_plus.grid(column=3, row=1)

    b4 = Button(calc, text="4", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(4))
    b4.grid(column=0, row=2)
    b5 = Button(calc, text="5", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(5))
    b5.grid(column=1, row=2)
    b6 = Button(calc, text="6", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=lambda: button_click(6))
    b6.grid(column=2, row=2)
    b_minus = Button(calc, text="-", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_minus)
    b_minus.grid(column=3, row=2)

    b1 = Button(calc, text="1", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2,command=lambda: button_click(1))
    b1.grid(column=0, row=3)
    b2 = Button(calc, text="2", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2,command=lambda: button_click(2))
    b2.grid(column=1, row=3)
    b3 = Button(calc, text="3", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2,command=lambda: button_click(3))
    b3.grid(column=2, row=3)
    b_multi = Button(calc, text="X", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_multiply)
    b_multi.grid(column=3, row=3)

    b0 = Button(calc, text="0", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2,command=lambda: button_click(0))
    b0.grid(column=0, row=4)
    bdeci = Button(calc, text=".", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2)
    bdeci.grid(column=1, row=4)
    b_equals = Button(calc, text="=", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2,command=b_equal)
    b_equals.grid(column=2, row=4)
    b_div = Button(calc, text="/", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_divide)
    b_div.grid(column=3, row=4)

    b_square = Button(calc, text="x²", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_square)
    b_square.grid(column=0, row=5)
    b_squareroot = Button(calc, text="√", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command = b_squareroot)
    b_squareroot.grid(column=1, row=5)
    b_delete = Button(calc, text="DEL", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_delete)
    b_delete.grid(column=2, row=5)
    b_exit = Button(calc, text="EXIT", padx=40, pady=20, bg=choose_color(), fg="Black", width=2, height=2, command=b_exit)
    b_exit.grid(column=3, row=5)

    calc.mainloop()

def Login_Page():
    window = Tk()
    window.title("Login_Page")
    window.geometry("440x450")
    window.configure(bg="red")


    b_username = Button(window, text="user", padx=40, pady=20, bg="violet", fg="Black", width=2, height=2)
    b_username.grid(column=1, row=1)
    en = Entry(window, width=30, borderwidth=5, bg="white", fg="black")
    en.grid(column=2, row=1, columnspan=4, padx=10, pady=10)

    b_password = Button(window, text="pass", padx=40, pady=20, bg="violet", fg="Black", width=2, height=2)
    b_password.grid(column=1, row=2)
    entry = Entry(window, width=30, borderwidth=5, bg="white", fg="black")
    entry.grid(column=2, row=2, columnspan=4, padx=10, pady=10)
    bl_password = Button(window, text="Click Here to open Calculator", padx=40, pady=20, bg="violet", fg="Black", width=2, height=2, command=Calculator)
    bl_password.grid(column=1, row=3)

    window.mainloop()

Login_Page()
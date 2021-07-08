from tkinter import *
from PIL import ImageTk, Image # Importing Pillow to work with images

root = Tk() # Defining the surface
root.title("Image Viewer")

my_img1 = ImageTk.PhotoImage(Image.open("images/img7.jpg"))


image_list = [my_img1]

status = Label(root, text="Image 1 of " + str(len(image_list)))

my_label = Label(image = my_img1)
my_label.grid(row=2, column=0, columnspan=3)

button_back = Button(root, text="<<", bg="navy blue")
button_back.grid(row=1, column=0)

button_forward = Button(root, text=">>", bg="navy blue")
button_forward.grid(row=1, column=2)

root.mainloop()
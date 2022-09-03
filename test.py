import glob
import os
import tkinter as tk
from tkinter import *
import numpy
import matplotlib.pyplot as plt
import natsort
from PIL import Image, ImageTk

win = tk.Tk()
win.title('Sign Language')
figure_x, figure_y = 64, 64
# Add image file
figure = tk.PhotoImage(file="deaf-people-talking.png")
label = tk.Label(
    win,
    image=figure
)
label.place(x=0, y=0)
target_image = tk.Label(win)

# FUNCTION
def showimage(name):

    dir1 = r"C:\Users\HafizUsama\Documents\drinks"
    path1 = os.path.join(dir1, '*g')
    files = glob.glob(path1)
    files1 = natsort.natsorted(files, reverse=False)
    for x in files1:
        print(x)
        img = plt.imread(x)
        image = Image.open(img)
        imag = ImageTk.PhotoImage(image)
    target_image.config(image=imag)
    target_image.image = imag



def Take_input():
    INPUT = input_user.get("1.0", "end-1c")
    print(INPUT)
    showimage(INPUT)
    target_image.place(x=400, y=160)


l = tk.Label(win, text="Enter drink name :", bg='#325C7F', width=28)
input_user = tk.Text(win, height=4, width=25)
l.place(x=80, y=300)
input_user.place(x=80, y=320)

# Add Image
# Create button and image
convert_btn = tk.PhotoImage(file="translate.png")
img = tk.Button(win, image=convert_btn , command=lambda: Take_input(), borderwidth=0)
img.place(x=130, y=400)

win.resizable(False, False)
win.geometry("800x550")
win.mainloop()

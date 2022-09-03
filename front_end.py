import glob
import os
import tkinter as tk
from tkinter import *

import matplotlib.pyplot as plt
import natsort
from PIL import Image, ImageTk

from fiverr import displayImg

window = tk.Tk()
window.geometry("600x1000")
window.title("BarMaster")
window.config(padx=10, pady=10)

title_label = tk.Label(window, text='BarMaster')
title_label.config(font=('Arial', 32))
title_label.pack(padx=10, pady=10)

target_image = tk.Label(window)
target_image.pack(padx=10, pady=10)

target_information = tk.Label(window)
target_information.config(font=("Arial", 20))
target_information.pack(padx=10, pady=10)


# FUNCTION
def showimage():

    dir1 = r"C:\Users\HafizUsama\Documents\drinks"
    path1 = os.path.join(dir1, '*.png')
    files = glob.glob(path1)
    files1 = natsort.natsorted(files, reverse=False)
    for x in files1:
        print(x)
        img = plt.imread(x)
        image = Image.open(img)
        imag = ImageTk.PhotoImage(image)

    target_image.config(image=imag)
    target_image.image = imag


label_id_name = tk.Label(window, text="Name of drink")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Search drink", command=showimage)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

window.mainloop()

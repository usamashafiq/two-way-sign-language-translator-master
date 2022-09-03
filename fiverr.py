import os
from tkinter import *

from PIL import Image, ImageTk

root = Tk()
root.geometry("800x600")
photos = []
root.title('BarMaster')


# Add image file
figure = PhotoImage(file="wine-glass-people.jpg")
label = Label(
    root,
    image=figure
)

def displayImg(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)  # keep references!
    newPhoto_label = Label(image=photo)
    newPhoto_label.place(x=500, y=160)


list_files = os.listdir(r"C:\Users\HafizUsama\Documents\drinks")
list_files_final = []
for x in list_files:
    if x.endswith(".png"):
        # Prints only text file present in My Folder
        list_files_final.append(x)


# for file in list_files_final:
#     displayImg(file)
#     print(file)


def Take_input():
    INPUT = input_user.get("1.0", "end-1c")

    alpha = str(INPUT).lower() + ".png"
    print(alpha)
    for file in list_files_final:

        if alpha == file:
            displayImg(file)


l = Label(root, text="Search a Drink :", bg='#325C7F', width=28)
input_user = Text(root, height=2, width=25)
l.place(x=80, y=300)
input_user.place(x=80, y=320)

# Add Image
# Create button and image
convert_btn = PhotoImage(file="translate.png")
img = Button(root, image=convert_btn, command=lambda: Take_input(), borderwidth=0)
img.place(x=130, y=400)

root.resizable(False, False)
root.geometry("800x550")

root.mainloop()

# Libraries Required 

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from stegano.lsb import lsb


#GUI plane 

root = Tk()
root.title("Steganography Tool")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#00FFFF")



def showimage():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetype=(
            ("PNG file", "*.png"),
            ("JPG file", "*.jpg"),
            ("JPEG file", "*.jpeg"),
            ("All files", "."),
        ),
    )
    img = Image.open(filename)

    # Convert the image to RGB mode
    if img.mode != "RGB":
        img = img.convert("RGB")

    img = ImageTk.PhotoImage(img)
    lb1.configure(image=img)
    lb1.image = img


def hide():
    global secret
    global text1
    message = text1.get(1.0, END)
    secret = lsb.hide(str(filename), message)


def show():
    try:
        clear_message = lsb.reveal(str(filename))
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    except IndexError:
        text1.delete(1.0, END)
        text1.insert(END, "No message detected in the image.")


def save_secret():
    try:
        secret
    except NameError:
        text1.delete(1.0, END)
        text1.insert(END, "No secret message to save.")
    else:
        secret.save("secretImage.png")



Label(
    root, text="Image Steganography", bg="#2d4155", fg="white", font="aial 25 bold"
).place(x=100, y=0)



# Tkinter interface .. 

# first frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lb1 = Label(f, bg="black")
lb1.place(x=40, y=10)

# Second frame
f2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
f2.place(x=350, y=80)

text1 = Text(f2, font="Robote 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)
scrollbar1 = Scrollbar(f2)
scrollbar1.place(x=320, y=0, height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# third frame
f3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f3.place(x=10, y=370)

Button(
    f3, text="Open Image", width=10, height=2, font="arial 14 bold", command=showimage
).place(x=20, y=30)
Button(
    f3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save_secret
).place(x=180, y=30)
Label(f3, text="Picture, Image, Photo FIle", bg="#2f4155", fg="yellow").place(x=20, y=5)

# frame4
f4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
f4.place(x=360, y=370)

Button(
    f4, text="Hide Text", width=10, height=2, font="arial 14 bold", command=hide
).place(x=20, y=30)
Button(
    f4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show
).place(x=180, y=30)
Label(f4, text="Picture, Image, Photo FIle", bg="#2f4155", fg="yellow").place(x=20, y=5)
root.mainloop()

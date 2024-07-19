# import tkinter as tk

from tkinter import *
from PIL import Image, ImageTk
import os


window = Tk()

window.geometry("540x540")
window.title("LaunchX")

icon = PhotoImage(file="icon.png")
window.iconphoto(True, icon)

window.config(background="#252626")

photo = Image.open("photo.png")
photoR = photo.resize((125, 125))
photo = ImageTk.PhotoImage(photoR)

label = Label(window,
              text="Mejra's Games",
              font=("Roboto", 20),
              fg="whitesmoke",
              bg="#252626",
              pady=5,
              padx=20,
              relief=RAISED,
              bd=5,
              )
photoo = Label(window, image=photo, bg="#252626")
label.pack()
photoo.pack()

def click():
    print("Added!")
    
    filePath = "C:/ProgramData/Microsoft/Windows/Start Menu/Programs/NEMESIS M700/NEMESIS M700"
    
    if os.name== "nt":
        os.startfile(filePath)

uploadImg = Image.open("upload.png")
uploadR = uploadImg.resize((40,40))
uploadImg = ImageTk.PhotoImage(uploadR)

button = Button(window,
                text="Add",
                command=click,
                font=("Roboto"),
                bg="#ebebeb",
                padx=25, pady=10,
                relief=GROOVE,
                activebackground="#6ccbeb",
                image=uploadImg,
                compound="right")
button.place(x=200, y=250)

window.mainloop()


# root = tk.Tk()

# root.geometry("800x500")
# root.title("GameLauncher")

# label = tk.Label(root, text="Game Launcher", font=("Verdana", 18))
# label.pack(padx=20, pady=40)

# # textbox = tk.Text(root, height=3, font=("Arial", 15))
# # textbox.pack()

# # button = tk.Button(root, padx=30, pady=5, text="Start")
# # button.pack()

# btnFrame = tk.Frame(root)
# btnFrame.columnconfigure(0, weight=1)
# btnFrame.columnconfigure(1, weight=1)
# btnFrame.columnconfigure(2, weight=1)

# btn1 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn1.grid(row=0, column=0,  padx=15, pady=15, sticky=tk.W+tk.E)

# btn2 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn2.grid(row=0, column=1, padx=15, pady=15, sticky=tk.W+tk.E)

# btn3 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn3.grid(row=0, column=2,  padx=15, pady=15, sticky=tk.W+tk.E)

# btn1 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn1.grid(row=1, column=0,  padx=15, pady=15, sticky=tk.W+tk.E)

# btn2 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn2.grid(row=1, column=1, padx=15, pady=15, sticky=tk.W+tk.E)

# btn3 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
# btn3.grid(row=1, column=2,  padx=15, pady=15, sticky=tk.W+tk.E)

# btnFrame.pack(fill='x')


# root.mainloop()

import tkinter as tk
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import os

window = customtkinter.CTk()
window.geometry("540x540")
window.title("LaunchX")
# window.config(background="whitesmoke")

# icon = PhotoImage(file="icon.png")
# window.iconphoto(True, icon)
# window.config(background="#252626")

photo = Image.open("photo.png")
photoR = photo.resize((125, 125))
photo = ImageTk.PhotoImage(photoR)

label = customtkinter.CTkLabel(window,
                               text="Game Launcher",
                               font=("Sans Serif", 35),
                               pady=25,
                              )
label.pack()

def click():
    print("Added!")
    filePath = "C:/ProgramData/Microsoft/Windows"
    if os.name == "nt":
        os.startfile(filePath)

uploadImg = Image.open("upload.png")
uploadR = uploadImg.resize((45, 45))
uploadImg = ImageTk.PhotoImage(uploadR)

button = customtkinter.CTkButton(window,
                                 text="Add",
                                 command=click,
                                  font=("Sans Serif", 20),
                                 image=uploadImg,
                                 compound="right",
                                 
                                )
button.place(x=200, y=100)

frame = tk.Frame(window, bg="#212121")
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

# Load and resize images for game buttons
def load_images():
    global game_images
    game_images = {
        'game1_small': ImageTk.PhotoImage(Image.open("ac.png").resize((80, 80))),
        'game1_large': ImageTk.PhotoImage(Image.open("ac.png").resize((100, 100))),
        'game2_small': ImageTk.PhotoImage(Image.open("spider.png").resize((82, 82))),
        'game2_large': ImageTk.PhotoImage(Image.open("spider.png").resize((100, 100))),
        'game3_small': ImageTk.PhotoImage(Image.open("cyb2.png").resize((82, 82))),
        'game3_large': ImageTk.PhotoImage(Image.open("cyb2.png").resize((100, 100))),
        'game4_small': ImageTk.PhotoImage(Image.open("mc.png").resize((82, 82))),
        'game4_large': ImageTk.PhotoImage(Image.open("mc.png").resize((100, 100)))
    }

load_images()

def on_enter(event, small_img, large_img):
    event.widget.config(image=large_img,  cursor="hand2")
    
def on_leave(event, small_img):
    event.widget.config(image=small_img)

def openG1():
    game1Path = "F:/Games/Assassin's Creed - Syndicate/ACS.exe"
    if os.name == "nt":
        os.startfile(game1Path)

def openG2():
    game2Path = "F:/Games/Marvel’s Spider-Man - Miles Morales/MilesMorales.exe"
    if os.name == "nt":
        os.startfile(game2Path)

def openG3():
    game3Path = "F:/Games\Cyberpunk 2077/bin/x64/Cyberpunk2077.exe"
    if os.name == "nt":
        os.startfile(game3Path)

def openG4():
    game4Path = "F:/Games\Minecraft Dungeons/Dungeons.exe"
    if os.name == "nt":
        os.startfile(game4Path)

# Create buttons and bind hover events
gameOpen = Button(frame,
                  padx=10, pady=5,
                  image=game_images['game1_small'],
                  command=openG1,
                  )
gameOpen.grid(row=0, column=0, padx=10, pady=5)
gameOpen.bind("<Enter>", lambda e: on_enter(e, game_images['game1_small'], game_images['game1_large']))
gameOpen.bind("<Leave>", lambda e: on_leave(e, game_images['game1_small']))

gameOpen2 = Button(frame,
                   padx=10, pady=5,
                   image=game_images['game2_small'],
                   command=openG2)
gameOpen2.grid(row=0, column=1, padx=10, pady=5)
gameOpen2.bind("<Enter>", lambda e: on_enter(e, game_images['game2_small'], game_images['game2_large']))
gameOpen2.bind("<Leave>", lambda e: on_leave(e, game_images['game2_small']))

gameOpen3 = Button(frame,
                   padx=10, pady=5,
                   image=game_images['game3_small'],
                   command=openG3)
gameOpen3.grid(row=0, column=2, padx=10, pady=5)
gameOpen3.bind("<Enter>", lambda e: on_enter(e, game_images['game3_small'], game_images['game3_large']))
gameOpen3.bind("<Leave>", lambda e: on_leave(e, game_images['game3_small']))

gameOpen4 = Button(frame,
                   padx=10, pady=5,
                   image=game_images['game4_small'],
                   command=openG4)
gameOpen4.grid(row=0, column=3, padx=10, pady=5)
gameOpen4.bind("<Enter>", lambda e: on_enter(e, game_images['game4_small'], game_images['game4_large']))
gameOpen4.bind("<Leave>", lambda e: on_leave(e, game_images['game4_small']))

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

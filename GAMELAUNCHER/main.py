import tkinter as tk

from tkinter import *

root = tk.Tk()

root.geometry("800x500")
root.title("GameLauncher")

label = tk.Label(root, text="Game Launcher", font=("Verdana", 18))
label.pack(padx=20, pady=40)

# textbox = tk.Text(root, height=3, font=("Arial", 15))
# textbox.pack()

# button = tk.Button(root, padx=30, pady=5, text="Start")
# button.pack()

btnFrame = tk.Frame(root)
btnFrame.columnconfigure(0, weight=1)
btnFrame.columnconfigure(1, weight=1)
btnFrame.columnconfigure(2, weight=1)

btn1 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn1.grid(row=0, column=0,  padx=15, pady=15, sticky=tk.W+tk.E)

btn2 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn2.grid(row=0, column=1, padx=15, pady=15, sticky=tk.W+tk.E)

btn3 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn3.grid(row=0, column=2,  padx=15, pady=15, sticky=tk.W+tk.E)

btn1 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn1.grid(row=1, column=0,  padx=15, pady=15, sticky=tk.W+tk.E)

btn2 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn2.grid(row=1, column=1, padx=15, pady=15, sticky=tk.W+tk.E)

btn3 = tk.Button(btnFrame,padx=30, pady=5, text="Start")
btn3.grid(row=1, column=2,  padx=15, pady=15, sticky=tk.W+tk.E)

btnFrame.pack(fill='x')


root.mainloop()

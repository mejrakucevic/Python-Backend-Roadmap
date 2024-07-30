import tkinter
import customtkinter
import yt_dlp

# Functions

def startDownload():
    try:
        ytLink = link.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytLink])
        status_label.config(text="Download Complete!", fg="green")
    except Exception as e:
        print("Error:", e)
        status_label.config(text="Youtube link is invalid", fg="red")

# System settings

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('blue')

# App frame

app = customtkinter.CTk()
app.geometry('720x480')
app.title("YouTube Downloader")

# UI Elements

title = customtkinter.CTkLabel(app, text="Insert a YouTube link", font=('Arial', 32))
title.pack(padx=10, pady=10)

# Link input

url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url)
link.pack(pady=10)

# Download button

download = customtkinter.CTkButton(app, text="Download", font=('Arial', 22), command=startDownload)
download.pack(padx=15, pady=15)

# Status label

status_label = customtkinter.CTkLabel(app, text="")
status_label.pack(pady=10)

# Run app

app.mainloop()

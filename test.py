import tkinter as tk
from tkinter import *
import os

fin = 0

def start():
    global hours, minutes, seconds

    if hours == 4:
        return

    seconds -= 1

    if seconds == 00:
        minutes -= 1
        seconds = 60
        if minutes == 00:
            minutes += 0


    if minutes == 00:
        fin + 1

    if minutes == -1:
        minutes += 1
        seconds -=60

    if seconds == -1:
        seconds == 0

    if minutes == 00 and seconds == 00:
        root.destroy()


    clock.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

    root.after(1000, start)

    if minutes == 00 and seconds == 00 and hours == 00:
        return


root = tk.Tk()
clock = tk.Label(root, height=1, background="#000000", foreground='white',
                 font=("Bold", 20), anchor=CENTER, text="00:00:00")
clock.place(relx=0.5, rely=0.5, anchor=CENTER)
hours, minutes, seconds = 0, 2, 1
start()
root.mainloop()
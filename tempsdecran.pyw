from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os
import pygame
from pygame import mixer

window = Tk()
window.title("Temps d'écran")
window.geometry("600x400")
window.maxsize(600, 400)
window.minsize(600, 400)

pygame.init()
pygame.mixer.init()

canv = Canvas(window, width=600, height=400, bg='white')
canv.grid(row=0, column=0)

depart = 0
fin = 0
fois = 1

hours, minutes, seconds = 0, 0, 0


def parametrer():
    global depart
    hours, minutes, seconds = 0, 0, 1
    depart = 1
    fleche_haut = Button(window, text="↑", font=("Noticia", 15), bg="grey", width=5, height=1, command=haut)
    fleche_haut.place(x=100, y=230)
    fleche_bas = Button(window, text="↓", bg='grey', fg='black', font=("Noticia", 15), width=5, height=1, command=bas)
    fleche_bas.place(x=100, y=270)
    bouton_fois = Button(window, text="1h", font=("Noticia", 15), bg="grey", width=5, height=1, command=boutonfois)
    bouton_fois.place(x=450, y=270)
    fleche_haut = Button(window, text="Mute", font=("Noticia", 15), bg="grey", width=5, height=1, command=mute)
    fleche_haut.place(x=500, y=270)
    canv.delete("coucou")
    canv.create_text(200, 265, text="0.0.0", font=("Arial", 25), fill="black", tag="lala")

    try:
        canv.delete("caca")

    except:
        ff = 10

def mute():
    mixer.music.set_volume(0)

def boutonfois():
    global seconds
    global minutes
    global hours
    canv.delete("lala")
    hours, minutes, seconds = 1, 0, 2
    canv.create_text(200, 265, text=str(hours) + "." + str(minutes) + "." + str(seconds), font=("Arial", 25), fill="black", tag="lala")

def debut():
    global hours, minutes, seconds
    canv.delete("lala")
    start()

def arreter():
    window.destroy()

def haut():
    global seconds
    global minutes
    global hours
    canv.delete("lala")
    canv.create_text(200, 265, text=str(hours) + "." + str(minutes) + "." + str(seconds), font=("Arial", 25), fill="black", tag="lala")
    seconds = seconds + 1
    if seconds >= 60:
        seconds = 0
        minutes = minutes + 1
    if minutes == 60:
        seconds = 0
        minutes = 0
        hours = hours + 1

def bas():
    global seconds
    global minuts
    global hours
    canv.delete("lala")
    canv.create_text(200, 265, text=str(hours) + "." + str(minutes) + "." + str(seconds), font=("Arial", 25), fill="black", tag="lala")
    seconds = seconds - 1
    if seconds <= 0:
        messagebox.showwarning("Temps d'écran", "Vous ne pouvez pas mettre en dessous de 0 !")
        seconds = 0


def start():
    global hours, minutes, seconds
    clock = tk.Label(window, height=1, background="white", foreground='black',
                     font=("Bold", 77), anchor=CENTER, text="00:00:00")
    clock.place(relx=0.5, rely=0.65, anchor=CENTER)

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

    if minutes == 00:
        hours -= 1
        minutes = 60

    if minutes == -1:
        minutes += 1
        seconds -=60

    if hours == -1:
        hours = 0
        minutes = 0

    if seconds == -1:
        seconds == 0

    if seconds <= -2:
        messagebox.showwarning("Erreur","Erreur")
        window.destroy()

    if fin == 1:
        os.system("shutdown /s /t 1")

    if minutes == 00 and seconds == 00 and hours == 00:
        os.system("shutdown /s /t 1")


    clock.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

    window.after(1000, start)

    if minutes == 00 and seconds == 00 and hours == 00:
        return

    depart = 0

canv.create_text(313, 50, text="Temps d'écran", font=("Impact", 30), fill="black")
bouton_arreter = Button(window, text="Arrêter", font=("Noticia", 15), bg="grey", width=13, height=2, command=arreter)
bouton_arreter.place(x=400, y=100)
temps_decran = Button(window, text="Lancer", bg='grey', fg='black', font=("Noticia", 15), width=13, height=2, command=debut)
temps_decran.place(x=100, y=100)
config = Button(window, text="Configurer", bg='grey', fg='black', font=("Noticia", 15), width=13, height=2, command=parametrer)
config.place(x=250, y=100)


window.mainloop()
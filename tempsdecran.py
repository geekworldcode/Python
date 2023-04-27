from tkinter import *
import tkinter as tk
import os


window = Tk()
window.title("Temps d'écran")
window.geometry("600x400")
window.maxsize(600, 400)
window.minsize(600, 400)

canv = Canvas(window, width=600, height=400, bg='white')
canv.grid(row=0, column=0)

minute = 00
heure = 00
seconde = 00

def parametrer():
    global depart
    fleche_haut = Button(window, text="↑", font=("Noticia", 15), bg="grey", width=5, height=1, command=haut)
    fleche_haut.place(x=100, y=230)
    fleche_bas = Button(window, text="↓", bg='grey', fg='black', font=("Noticia", 15), width=5, height=1, command=bas)
    fleche_bas.place(x=100, y=270)
    canv.delete("coucou")
    depart = 1

def start():
    if depart == 1:
        global hours, minutes, seconds
        canv.delete("lala")
        hours, minutes, seconds = 10, 10, 10

        clock = tk.Label(window, height=1, background="white", foreground='black',
                        font=("Bold", 20), anchor=CENTER, text="00:00:00")
        clock.place(relx=0.5, rely=0.5, anchor=CENTER)

        if hours == 4:
            return

        seconds -= 1

        if seconds == 00:
            minutes -= 1
            seconds = 60
        if minutes == 00:
            minutes += 0

        if minutes == -1:
            minutes += 1
            seconds -=60

        if seconds == -1:
            seconds == 0

        if minutes == 00 and seconds == 00:
            window.destroy()

            clock.config(text=f'{hours:02}:{minutes:02}:{seconds:02}')

        window.after(1000, start)

        if minutes == 00 and seconds == 00 and hours == 00:
            return

    if depart == 0:
        canv.create_text(450, 375, text="Vous devez d'abord configurer !", font=("Arial", 15), fill="black", tag="caca")

def arreter():
    window.destroy()

def haut():
    global seconde
    global minute
    canv.delete("lala")
    canv.create_text(200, 265, text=str(heure) + "." + str(minute) + "." + str(seconde), font=("Arial", 25), fill="black", tag="lala")
    seconde = seconde + 1
    if seconde == 60:
        seconde = 0
        minute = minute + 1

def bas():
    global seconde
    global minute
    canv.delete("lala")
    canv.create_text(200, 265, text=str(heure) + "." + str(minute) + "." + str(seconde), font=("Arial", 25), fill="black", tag="lala")
    seconde = seconde - 1
    if seconde == 00:
        seconde = 0


canv.create_text(313, 50, text="Temps d'écran", font=("Impact", 30), fill="black")
bouton_arreter = Button(window, text="Arrêter", font=("Noticia", 15), bg="grey", width=13, height=2, command=arreter)
bouton_arreter.place(x=400, y=100)
temps_decran = Button(window, text="Lancer", bg='grey', fg='black', font=("Noticia", 15), width=13, height=2, command=start)
temps_decran.place(x=100, y=100)
config = Button(window, text="Configurer", bg='grey', fg='black', font=("Noticia", 15), width=13, height=2, command=parametrer)
config.place(x=250, y=100)


window.mainloop()
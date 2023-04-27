from tkinter import *
import random

nom_joueurs = ""
action_liste = ["Chanter du ACDC", "Imiter son voisin de droite", "Faire 15 pompes", "Faire le tour de la maison", "Imiter l'accent Québécois", "Faire un canular téléphonique"]
verite_liste = ["Ton pire ennemi ?", "Ton plus grand rêve ?", "Ton pire cauchemar ?", "Ton amoureuse/eux ?", "Ton jeu préféré ?", "Messi ou Ronaldo ?", "Ta voiture préférée ?"]

def jouer():
    global window2
    window2 = Tk()
    window2.title("Action ou vérité")
    window2.geometry("400x300")
    window2.minsize(400, 300)
    window.destroy()

    text2 = Label(window2, text="Nom des joueurs:", font=("Arial", 30))
    text2.pack()

    def joueurs():
        global nom_joueurs
        nom_joueurs = entry1.get("1.0", "end-1c").split(",")
        window3 = Tk()
        window3.title("Action ou vérité")
        window3.geometry("800x600")
        window3.minsize(400, 300)
        window2.destroy()

        text3 = Label(window3, text=random.choice(nom_joueurs), font=("Arial", 30))
        text3.pack()

        def action_def():
            window4 = Tk()
            window4.title("Action ou vérité")
            window4.geometry("300x20")
            window4.minsize(100, 100)
            text4 = Label(window4, text=random.choice(action_liste), font=("Arial", 15))
            text4.pack()
            if text3.winfo_exists():
                text3.destroy()
            text7 = Label(window3, text=random.choice(nom_joueurs), font=("Arial", 30))
            text7.pack()
            window4.mainloop()

        def verite_def():
            window5 = Tk()
            window5.title("Action ou vérité")
            window5.geometry("300x20")
            window5.minsize(100, 100)
            text5 = Label(window5, font=("Arial", 15))
            text5.pack()
            text5.config(text=random.choice(verite_liste))
            if text3.winfo_exists():
                text3.destroy()
            text6 = Label(window3, font=("Arial", 30))
            text6.pack()
            text6.config(text=random.choice(nom_joueurs))
            window5.mainloop()

        action = Button(window3, text="Action", font=("Arial", 20), width=20, height=5, bg="blue", command=action_def)
        action.place(x=250, y=100)

        verite = Button(window3, text="Vérité", font=("Arial", 20), width=20, height=5, bg="red", command=verite_def)
        verite.place(x=250, y=310)

        window3.mainloop()

    entry1 = Text(window2, width=20, height=3, font=("Arial", 20))
    entry1.place(x=40, y=100)
    bouton = Button(window2, text="Suivant", font=("Arial", 20), command=joueurs)
    bouton.place(x=270, y=230)

    window2.mainloop()

def quitter():
    window.destroy()


window = Tk()
window.title("Action ou vérité")
window.geometry("800x600")
window.minsize(800, 600)

text = Label(text="Action ou vérité", font=("Arial", 30))
text.pack()

bouton_jouer = Button(text="Jouer", font=("Arial", 30), bg="blue", height=2, width=10, command=jouer)
bouton_jouer.place(x=285, y=100)

bouton_quitter = Button(text="Quitter", font=("Arial", 30), bg="blue", height=2, width=10, command=quitter)
bouton_quitter.place(x=285, y=300)

window.mainloop()

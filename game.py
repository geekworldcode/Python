import pygame
import sys
from pygame import mixer
from tkinter import *
import time

# Initialiser pygame
pygame.init()
pygame.mixer.init()

# Variables
deplacement = 0
musique = "ryutheme.mp3"
background = "ryustage.png"

#Définitions

def vega():
    global musique, background
    musique = "vegatheme.mp3"
    background = "vegastage.png"

def balrog():
    global musique, background
    musique = "balrogtheme.mp3"
    background = "balrogstage.png"

def guile():
    global musique, background
    musique = "fritefighter.mp3"
    background = "guilestage.png"

def chunli():
    global musique, background
    musique = "chunlitheme.mp3"
    background = "chunlistage.png"

def ken():
    global musique, background
    musique = "kentheme.mp3"
    background = "kenstage.png"

def ryu():
    global musique, background
    musique = "ryutheme.mp3"
    background = "ryustage.png"

def quitter():
    window.destroy()
    pygame.quit()

def jouer():
    window.destroy()

def regler():
    window2 = Tk()
    window2.title("Frite Fighter")
    window2.geometry("800x600")
    window2.minsize(800, 600)

    # Charger la musique de fond et la jouer en boucle
    pygame.mixer.music.load("menutheme.mp3")
    pygame.mixer.music.play(loops=10000)
    mixer.music.set_volume(100)

    bouton_guile = Button(window2, text="Guile Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=guile)
    bouton_guile.place(x=70, y=20)
    bouton_ken = Button(window2, text="Ken Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=ken)
    bouton_ken.place(x=70, y=73)
    bouton_chunli = Button(window2, text="Chun li Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=chunli)
    bouton_chunli.place(x=70, y=126)
    bouton_balrog = Button(window2, text="Balrog Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=balrog)
    bouton_balrog.place(x=70, y=179)
    bouton_vega = Button(window2, text="Vega Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=vega)
    bouton_vega.place(x=70, y=232)
    bouton_ryu = Button(window2, text="Ryu Stage", font=("SSF4 ABUKET", 10), width=10, bg="orange", command=ryu)
    bouton_ryu.place(x=70, y=285)

    window2.mainloop()


window = Tk()
window.title("Frite Fighter")
window.geometry("800x600")
window.minsize(1250, 800)

# Charger la musique de fond et la jouer en boucle
pygame.mixer.music.load("menutheme.mp3")
pygame.mixer.music.play(loops=10000)
mixer.music.set_volume(100)

canv = Canvas(window, width=1250, height=800, bg='white')
canv.grid(row=0, column=0)
img = PhotoImage(file="bg.png")
canv.create_image(-320, 0 , anchor=NW, image=img)
canv.create_text(640, 126, text="Frite Fighter", font=("SSF4 ABUKET", 70), fill="black")
canv.create_text(640, 120, text="Frite Fighter", font=("SSF4 ABUKET", 70), fill="red")

bouton_jouer = Button(text="Jouer", font=("SSF4 ABUKET", 20), width=7, bg="orange", command=jouer)
bouton_jouer.place(x=555, y=280)
bouton_regler = Button(text="Regler", font=("SSF4 ABUKET", 20), width=7, bg="orange", command=regler)
bouton_regler.place(x=555, y=420)
bouton_quitter = Button(text="Quitter", font=("SSF4 ABUKET", 20), width=7, bg="orange", command=quitter)
bouton_quitter.place(x=555, y=560)

window.mainloop()


# Créer une surface d'affichage de 1500 x 900 pixels
ecran = pygame.display.set_mode((1500, 900))
pygame.display.set_caption("Frite Fighter")

# Charger l'image de fond et la mettre à l'échelle pour s'adapter à la taille de la fenêtre
fond = pygame.image.load(background)
fond = pygame.transform.scale(fond, (1500, 900))
fond = fond.convert()

# Attaques
shoryuken = pygame.image.load("shoryuken.png")

# Charger la musique de fond et la jouer en boucle
pygame.mixer.music.load(musique)
pygame.mixer.music.play(loops=10000)
mixer.music.set_volume(100)

# Créer une classe pour le personnage du jeu
class PERSO(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Charger l'image du personnage et définir sa position de départ
        self.original_image = pygame.image.load('ryu-hdstance.gif')
        self.original_image = pygame.transform.rotate(self.original_image, 0) # Pivoter l'image
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect()
        self.rect.center = (deplacement, 700)

        # Initialiser la vitesse et la direction du personnage
        self.velocity = 0
        self.direction = 0  # 0 = immobile, 1 = vers la droite, -1 = vers la gauche

    def jump(self):
        # Ajuster la vitesse vers le haut lorsque le personnage saute
        self.velocity = -25

    def update(self):
        global deplacement
        # Ajuster la position du personnage en fonction de sa vitesse actuelle
        self.velocity += 1
        self.rect.y += self.velocity

        # Empêcher le personnage de sortir de l'écran
        if self.rect.bottom > 900:
            self.rect.bottom = 900

        # Gérer le mouvement horizontal du personnage
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction = -1
            self.rect.x -= 4
            deplacement -= 5
        elif keys[pygame.K_RIGHT]:
            self.direction = 1
            self.rect.x += 4
            deplacement += 5
        else:
            self.direction = 0

        # Empêcher le personnage de sortir de l'écran
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 1500:
            self.rect.right = 1500

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Créer une instance de la classe PERSO
perso = PERSO()

# Ajouter une variable booléenne pour savoir si l'attaque doit être affichée
afficher_attaque = False

# Créer un groupe de sprites pour le personnage
sprites = pygame.sprite.Group()
sprites.add(perso)

def create_perso():
    # Créer un nouveau sprite de personnage avec les mêmes paramètres que le premier
    new_perso = PERSO()
    return new_perso

def create_attack():
    # Créer un nouveau sprite pour l'attaque
    attack = pygame.sprite.Sprite()
    attack.image = pygame.Surface((70, 50))
    attack.image.fill((255, 255, 255))  # Couleur rouge
    attack.image.set_alpha(2)
    attack.rect = attack.image.get_rect()
    attack.rect.center = perso.rect.center  # Positionne l'attaque au centre du personnage
    return attack

# Boucle principale du jeu
suite = True
while suite:
    for event in pygame.event.get():
        # Quitter le jeu lorsque la croix de la fenêtre est cliquée
        if event.type == pygame.QUIT:
            suite = False

        # Appeler la méthode jump du personnage lorsque la touche 'a' est enfoncée
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                perso.jump()
            if event.key == pygame.K_r:
                perso.kill()  # supprime le sprite PERSO
                canal_audio = pygame.mixer.Channel(1)
                son = pygame.mixer.Sound('shoryuken.mp3')
                canal_audio.play(son)
                afficher_attaque = True
                pygame.time.set_timer(pygame.USEREVENT, 1500)  # Déclenche un événement toutes les 1000 ms (1 seconde)

        # Désactiver l'affichage de l'attaque lorsque la touche 'r' est relâchée
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                afficher_attaque = False

        # Traitement de l'événement USEREVENT
        elif event.type == pygame.USEREVENT:
            # Rétablir l'état normal du jeu après la fin de l'attaque
            afficher_attaque = False
            perso.visible = True  # Rend le sprite PERSO visible
            sprites = pygame.sprite.Group()
            sprites.add(perso)

    # Si l'attaque doit être affichée, afficher le sprite de l'attaque
    if afficher_attaque:
        perso.visible = False  # Rend le sprite PERSO invisible
        perso_attaque = create_attack()  # Crée un nouveau sprite pour l'attaque
        sprites = pygame.sprite.Group()
        sprites.add(perso_attaque)

    # Afficher les sprites
    ecran.fill((255, 255, 255))
    sprites.draw(ecran)

    # Afficher l'image de fond
    ecran.blit(fond, (0, 0))

    # Mettre à jour et dessiner le groupe de sprites du personnage
    sprites.update()
    sprites.draw(ecran)

    # Dessiner l'attaque si la variable afficher_attaque est vraie
    if afficher_attaque:
        shoryuken_scaled = pygame.transform.scale(shoryuken, (650, 900))
        ecran.blit(shoryuken_scaled, ((deplacement - 100), 0))

    # Dessiner les sprites
    sprites.draw(ecran)

    # Rafraîchir l'affichage de la fenêtre
    pygame.display.flip()

# Quitter pygame et fermer la fenêtre
pygame.quit()

import pygame, sys

pygame.init()

#couleurs
couleur_blanche = pygame.Color(255, 255, 255)
couleur_noire = pygame.Color(0, 0, 0)
couleur_rouge = pygame.Color(255, 0, 0)
couleur_verte = pygame.Color(0, 255, 0)
couleur_bleue = pygame.Color(0, 0, 255)

#fenetre
ecran = pygame.display.set_mode((1200,900))
ecran.fill(couleur_blanche)
pygame.display.set_caption("Paint de Vincent")

suite = True
debut_ligne = 0, 0
couleur = couleur_noire
epaisseur = 1

#boucle de jeu
while suite:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            suite = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                suite = False
            elif event.key == pygame.K_r:
                couleur = couleur_rouge
            elif event.key == pygame.K_v:
                couleur = couleur_verte
            elif event.key == pygame.K_b:
                couleur = couleur_bleue
            elif event.key == pygame.K_n:
                couleur = couleur_noire
            elif event.key == pygame.K_p:
                epaisseur = epaisseur + 20
            elif event.key == pygame.K_m:
                epaisseur = epaisseur - 19
                if epaisseur < 1:
                    epaisseur = 1
            elif event.key == pygame.K_s:
                pygame.image.save(ecran, "Dessin.png")
        elif event.type == pygame.MOUSEMOTION:
            fin_ligne = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pygame.draw.line(ecran, couleur, debut_ligne, fin_ligne, epaisseur)
            debut_ligne = fin_ligne
    pygame.display.flip()

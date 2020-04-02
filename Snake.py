from upemtk import *
from time import sleep
from random import randint

# dimensions du jeu
taille_case = 15
largeur_plateau = 40
hauteur_plateau = 40


def case_vers_pixel(case):
    """
	Fonction recevant les coordonnées d'une case du plateau sous la
	forme d'un couple d'entiers (ligne, colonne) et renvoyant les
	coordonnées du pixel se trouvant au centre de cette case. Ce calcul
	prend en compte la taille de chaque case, donnée par la variable
	globale taille_case.
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case

def affiche_murs(murs):
    for mur in murs:
        x, y = case_vers_pixel(mur)
        rectangle(x-7.5, y-7.5, x+7.5, y+7.5,
                  couleur='orange', remplissage='orange')

def affiche_pommes(pommes):
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')

def affiche_pommes_or(pommes):
    """
    Fonction permettant l'affichage des pommes en or.
    """
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='black', remplissage='yellow')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')

def affiche_pommes_poison(pommes):
    """
    Fonction permettant l'affichage des pommes empoisonnées du mode hardcore.
    """
    for pomme in pommes:
        x, y = case_vers_pixel(pomme)
        cercle(x, y, taille_case/2,
               couleur='darkred', remplissage='red')
        rectangle(x-2, y-taille_case*.4, x+2, y-taille_case*.7,
                  couleur='darkgreen', remplissage='darkgreen')

def coordonnees_objets(murs, murs_hardcore):
    """
    Fonction permettant les calculs des coordonnées des objets.
    Pommes ou murs ou pommes empoisonnées.
    """
    objet_x = randint(0, 39)   # position en x d'un objet
    objet_y = randint(3, 39)   # position en y d'un objet
    # change la position de l'objet si apparition sur serpent ou sur un mur
    for mur in murs:
        for mur_hardcore in murs_hardcore:
            while ((objet_x, objet_y) == serpent[0]) or ((objet_x, objet_y) == mur) or\
                    ((objet_x, objet_y) == mur_hardcore):
                objet_x = randint(0, 39)
                objet_y = randint(3, 39)
    return objet_x, objet_y

def affiche_serpent(serp):
    x, y = case_vers_pixel(serp)
    if serp == serpent[0]:   # tête du serpent
        cercle(x, y, taille_case/2 + 1,
               couleur='darkgreen', remplissage='#A1CC00')
    else:   # corps du serpent
        cercle(x, y, taille_case/2 + 1,
               couleur='darkgreen', remplissage='#6E8C00')

def change_direction(direction, touche):
    if touche == 'Up':
        if direction == (0, 1):
            return direction
        else:
            return (0, -1)
    elif touche == 'Down':
        if direction == (0, -1):
            return direction
        else:
            return (0, 1)
    elif touche == 'Right':
        if direction == (-1, 0):
            return direction
        else:
            return (1, 0)
    elif touche == 'Left':
        if direction == (1, 0):
            return direction
        else:
            return (-1, 0)
    else:
        return direction


# programme principal
if __name__ == "__main__":
    commencer = True
    jouer = False
    rejouer = False
    hardcore = False
    special = False
    chance_pomme = False

    while commencer:
        # initialisation du jeu
        framerate = 13    # taux de rafraîchissement du jeu en images/s
        score = 0   # score du jeu
        direction = (1, 0)  # direction initiale du serpent
        serpent = [(10, 20), (9, 20), (8, 20)]  # liste des coordonnées de cases adjacentes décrivant le serpent

        # création des murs (diffère si mode hardcore)
        nb_murs = randint(10, 20)
        nb_murs_hardcore = randint(20, 40)
        murs = []
        murs_hardcore = []
        for compte_mur in range(nb_murs):
            mur_x, mur_y = coordonnees_objets(murs, murs_hardcore)
            murs.append((mur_x, mur_y))
        for compte_mur in range(nb_murs_hardcore):
            mur_x, mur_y = coordonnees_objets(murs, murs_hardcore)
            murs_hardcore.append((mur_x, mur_y))

        # création des pommes
        pomme_x, pomme_y = coordonnees_objets(murs, murs_hardcore)
        pommes = [(pomme_x, pomme_y)]  # liste des coordonnées des cases contenant des pommes

        # création des pommes empoisonnées pour mode hardcore
        pomme_poison_x, pomme_poison_y = coordonnees_objets(murs, murs_hardcore)
        pommes_poison = [(pomme_poison_x, pomme_poison_y)]

        # création des pommes en or pour mode spécial
        # liste vide car apparaît selon certaines conditions
        pommes_or = []

        if not rejouer:
            cree_fenetre(taille_case * largeur_plateau, taille_case * hauteur_plateau)

        efface_tout()
        rectangle(0, 0, 600, 600, remplissage='#C2F592')
        rectangle(190, 200, 405, 235, couleur='green', remplissage='#E7FFCB', epaisseur=3)
        rectangle(195, 300, 400, 335, couleur='darkred', remplissage='#FFCBCB', epaisseur=3)
        rectangle(205, 400, 390, 435, couleur='orange', remplissage='#FFEECB', epaisseur=3)
        texte(130, 30, 'Sssnake: le jeu', couleur='green', police='Helvetica', taille=40)
        texte(200, 200, 'Mode Classique', couleur='green', police='Helvetica', taille=20)
        texte(205, 300, 'Mode Hardcore', couleur='darkred', police='Helvetica', taille=20)
        texte(215, 400, 'Mode Spécial', couleur='orange', police='Helvetica', taille=20)
        while not jouer:
            action = attend_clic_gauche()
            if 190 <= action[0] <= 405 and 200 <= action[1] <= 235:
                efface_tout()
                jouer = True
            elif 195 <= action[0] <= 400 and 300 <= action[1] <= 335:
                efface_tout()
                jouer = True
                hardcore = True
            elif 205 <= action[0] <= 390 and 400 <= action[1] <= 435:
                efface_tout()
                jouer = True
                special = True
            else:
                continue

        while jouer:
            commencer = False
            # affichage des objets
            efface_tout()
            rectangle(0, 0, 600, 600, remplissage='#A1EFF9')
            texte(50, 10, 'Mode Classique', couleur='green', police='Helvetica', taille=18)
            texte(350, 10, 'Score : '+str(score), couleur='green', police='Helvetica', taille=18)
            ligne(0, 45, 600, 45, couleur='green', epaisseur=2)
            affiche_pommes(pommes)
            affiche_murs(murs)
            if hardcore: #mode choisi
                efface_tout()
                rectangle(0, 0, 600, 600, remplissage='#FFC7C7')
                texte(50, 10, 'Mode Hardcore', couleur='darkred', police='Helvetica',taille=18)
                texte(350, 10, 'Score : '+str(score), couleur='darkred', police='Helvetica', taille=18)
                ligne(0, 45, 600, 45, couleur='darkred', epaisseur=2)
                affiche_pommes_poison(pommes_poison)
                affiche_pommes(pommes)
                affiche_murs(murs_hardcore)
            if special: #mode choisi
                efface_tout()
                rectangle(0, 0, 600, 600, remplissage='#FFEEC2')
                texte(50, 10, 'Mode Spécial', couleur='orange', police='Helvetica', taille=18)
                texte(350, 10, 'Score : '+str(score), couleur='orange', police='Helvetica', taille=18)
                ligne(0, 45, 600, 45, couleur='orange', epaisseur=2)
                affiche_pommes(pommes)
                affiche_murs(murs)
                if chance_pomme:
                    affiche_pommes_or(pommes_or)
            for longeur in serpent:
                affiche_serpent(longeur)
            mise_a_jour()

            # gestion des événements
            # déplacement de la tête
            avance = serpent[0]
            serpent[0] = (direction[0] + serpent[0][0], direction[1] + serpent[0][1])

            # déplacement du corps
            for corps in range(len(serpent)):
                if corps == 0:
                    continue
                elif corps == 1:
                    avance_encore = serpent[1]
                    serpent[1] = avance
                else:
                    avance_suite = avance_encore
                    avance_encore = serpent[corps]
                    serpent[corps] = avance_suite

            # pomme mangée
            if serpent[0][0] == pomme_x and serpent[0][1] == pomme_y:
                score += 1
                pomme_x, pomme_y = coordonnees_objets(murs, murs_hardcore)
                pommes[0] = (pomme_x, pomme_y)
                # apparition d'un nouveau corps
                nouveau_corps = (serpent[0][0] - direction[0], serpent[0][1] - direction[1])
                serpent.append(nouveau_corps)
                # changement de position des pommes empoisonnées si mode hardcore
                if hardcore:
                    pomme_poison_x, pomme_poison_y = coordonnees_objets(murs, murs_hardcore)
                    pommes_poison[0] = (pomme_poison_x, pomme_poison_y)
                    framerate += 2
                # apparition des pommes en or si mode spécial (une chance sur quatre)
                if special:
                    if not chance_pomme:
                        chance = randint(1, 100)
                        if chance <= 25:
                            pomme_or_x, pomme_or_y = coordonnees_objets(murs, murs_hardcore)
                            pommes_or.append((pomme_or_x, pomme_or_y))
                            chance_pomme = True

            # pomme empoisonnée mangée pour mode hardcore
            if hardcore:
                if serpent[0][0] == pomme_poison_x and serpent[0][1] == pomme_poison_y:
                    pomme_poison_x, pomme_poison_y = coordonnees_objets(murs, murs_hardcore)
                    pommes_poison[0] = (pomme_poison_x, pomme_poison_y)
                    # suppression d'un corps
                    if len(serpent) == 1:
                        jouer = False
                    else:
                        serpent.pop(0)
                    # changement de position des vraies pommes
                    pomme_x, pomme_y = coordonnees_objets(murs, murs_hardcore)
                    pommes[0] = (pomme_x, pomme_y)
                    framerate += 5

            # pomme en or mangée pour mode spécial
            if special:
                if chance_pomme:
                    pomme_or_x, pomme_or_y = pommes_or[0][0], pommes_or[0][1]
                    if serpent[0][0] == pomme_or_x and serpent[0][1] == pomme_or_y:
                        score += 3
                        # apparition de trois nouveaux corps
                        nouveau_corps_1 = (serpent[0][0] - direction[0], serpent[0][1] - direction[1])
                        nouveau_corps_2 = (nouveau_corps_1[0] - direction[0], nouveau_corps_1[1] - direction[1])
                        nouveau_corps_3 = (nouveau_corps_2[0] - direction[0], nouveau_corps_2[1] - direction[1])
                        serpent.append(nouveau_corps_1)
                        serpent.append(nouveau_corps_2)
                        serpent.append(nouveau_corps_3)
                        pommes_or.pop(0)
                        chance_pomme = False

            # le serpent entre en collision avec lui-même
            collision = serpent[:]
            collision.pop(0)
            for mort_par_collision in collision:
                if mort_par_collision == serpent[0]:
                    jouer = False

            # quitte le plateau
            if special: # a la Pac-Man
                special_serpent = serpent[0]
                if serpent[0][0] < 0:
                    serpent[0] = (39, special_serpent[1])
                elif serpent[0][0] > 39:
                    serpent[0] = (0, special_serpent[1])
                elif serpent[0][1] < 3:
                    serpent[0] = (special_serpent[0], 39)
                elif serpent[0][1] > 39:
                    serpent[0] = (special_serpent[0], 3)
            else:
                if serpent[0][0] < 0 or serpent[0][0] > 39 or serpent[0][1] < 3 or serpent[0][1] > 39:
                    jouer = False

            # cogne le mur
            if hardcore:
                for element in murs_hardcore:
                    if element == serpent[0]:
                        jouer = False
            else:
                for element in murs:
                    if element == serpent[0]:
                        jouer = False

            ev = donne_ev()
            ty = type_ev(ev)
            # quitte le jeu
            if ty == 'Quitte':
                jouer = False
            # change de direction
            elif ty == 'Touche':
                print(touche(ev))
                direction = change_direction(direction, touche(ev))

            # attente avant rafraîchissement
            sleep(1/framerate)

        hardcore = False
        special = False
        chance_pomme = False
        efface_tout()
        rectangle(0, 0, 600, 600, remplissage='#CDBCBC')
        rectangle(140, 400, 290, 435, couleur='green', remplissage='#D8C2FF', epaisseur=3)
        rectangle(340, 400, 440, 435, couleur='green', remplissage='#FFA5A5', epaisseur=3)
        texte(135, 60, 'Votre score est de:', couleur='green', police='Helvetica', taille=30)
        texte(taille_case*largeur_plateau/2,taille_case*largeur_plateau/3, str(score), couleur='green', police='Helvetica', taille=50)
        texte(150, 400, 'Réessayer', couleur='green', police='Helvetica', taille=20)
        texte(350, 400, 'Quitter', couleur='green', police='Helvetica', taille=20)
        while not commencer:
            action = attend_clic_gauche()
            if 140 <= action[0] <= 300 and 400 <= action[1] <= 435:
                commencer = True
                rejouer = True
                efface_tout()
            if 340 <= action[0] <= 445 and 400 <= action[1] <= 435:
                break


        efface_tout()

    # fermeture et sortie
    ferme_fenetre()
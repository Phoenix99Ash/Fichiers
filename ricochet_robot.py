from upemtk import *
from random import randint
from time import sleep

# déclaration des variables
taille_case = 45
largeur_plateau = 25
hauteur_plateau = 16
framerate = 8

murs_verticaux = [(181, 1), (181, 46), (451, 1), (451, 46),
                  (631, 46), (631, 91), (271, 91), (271, 136),
                  (406, 136), (406, 181), (136, 181), (136, 226),
                  (676, 181), (676, 226), (316, 226), (316, 271),
                  (46, 271), (46, 316), (541, 271), (541, 316),
                  (181, 406), (181, 451), (586, 406), (586, 451),
                  (271, 451), (271, 496), (451, 496), (451, 541),
                  (361, 541), (361, 586),(91, 586), (91, 631),
                  (676, 586), (676, 631), (181, 631), (181, 676),
                  (451, 631), (451, 676),(226, 676), (226, 721),
                  (541, 676), (541, 721)]

murs_horizontaux = [(586, 91), (631, 91), (676, 91), (721, 91),
                    (226, 136), (271, 136), (406, 136), (451, 136),
                    (91, 181), (136, 181), (631, 181), (676, 181),
                    (46, 271), (91, 271), (1, 226), (46, 226),
                    (316, 271), (361, 271), (541, 316), (586, 316),
                    (181, 451), (226, 451), (586, 451), (631, 451),
                    (271, 451), (316, 451), (1, 496), (46, 496),
                    (316, 541), (361, 541), (406, 541), (451, 541),
                    (676, 541), (721, 541), (46, 586), (91, 586),
                    (631, 586), (676, 586), (451, 631), (496, 631),
                    (136, 676), (181, 676)]

pions = [(14, 13), (1, 6), (3, 14), (9, 3),  # pions carre
         (14, 4), (9, 11), (2, 4), (6, 10),  # pions rond
         (1, 13), (12, 6), (10, 14), (5, 2),  # pions halter
         (7, 5), (4, 9), (13, 1), (13, 9),  # pions triangle
         (7, 12)]  # pion multicolore

couleur_objet = ['#A90000', '#A96900', '#118000', '#0A00A1']
couleur_emplacement = ['#FFA1A1', '#FFCD6A', '#ADFFAA', '#A5B8FF']


def case_vers_pixel(case):
    """
    reçoit une coordonnée puis renvoie une coordonnée calculée en pixel
    :param tuple case: coordonnée d'une case
    return tuple: coordonnée d'un pixel

    >>> case_vers_pixel((2,4))
    (112.5, 202.5)
    """
    i, j = case
    return (i + .5) * taille_case, (j + .5) * taille_case


def affiche_robot(rob, color):
    """
    reçoit la liste de coordonnées des robots ainsi que la couleur et dessine les pions sur le plateau

    :param lst rob: liste de coordonnées des robots
    :param lst color: liste de couleur
    """
    for player in range(len(rob)):
        x, y = case_vers_pixel(rob[player])
        image(x+1, y+1, 'robotek'+color[player]+'.gif')


def affiche_emplacement(rob, color):
    for player in range(len(rob)):
        x, y = case_vers_pixel(rob[player])
        rectangle(x - taille_case/2 + 1, y - taille_case/2 + 1, x + taille_case/2 + 1, y + taille_case/2 + 1,
                  remplissage=color[player])


def affiche_pion(position, coloration, but, couleur_but):
    """
    Reçoit en paramètre 'position' la liste des pions, 'coloration' la liste des couleurs, 'but'
    """
    rectangle(330, 330, 390, 390, remplissage='white')
    nb_pion = 0
    color_pion = 0
    for pion in position:
        x, y = case_vers_pixel(pion)
        if nb_pion < 4:  # pions carre
            rectangle(x-6, y-6, x+8, y+8, remplissage='white')
            rectangle(x-4, y-4, x+6, y+6, remplissage=coloration[color_pion])
            if 0 <= but <= 3:
                rectangle(361-6, 361-6, 361+8, 361+8, remplissage='white')
                rectangle(361-4, 361-4, 361+6, 361+6, remplissage=coloration[couleur_but])
        elif 4 <= nb_pion < 8:  # pions rond
            cercle(x+1, y+1, 8, epaisseur=2)
            cercle(x+1, y+1, 7, remplissage=coloration[color_pion])
            if 4 <= but <= 7:
                cercle(361+1, 361+1, 8, epaisseur=2)
                cercle(361+1, 361+1, 7, remplissage=coloration[couleur_but])
        elif 8 <= nb_pion < 12:  # pions halter
            rectangle(x-7, y-7, x-3, y+9, remplissage=coloration[color_pion])
            rectangle(x+5, y-7, x+9, y+9, remplissage=coloration[color_pion])
            ligne(x-2, y+1, x+5, y+1, epaisseur=8)
            if 8 <= but <= 11:
                rectangle(361-7, 361-7, 361-3, 361+9, remplissage=coloration[couleur_but])
                rectangle(361+5, 361-7, 361+9, 361+9, remplissage=coloration[couleur_but])
                ligne(361-2, 361+1, 361+5, 361+1, epaisseur=8)
        elif 12 <= nb_pion < 16:  # pions triangle
            polygone([(x+2, y-12), (x-7, y+5), (x+12, y+5)], remplissage=coloration[color_pion], epaisseur=2)
            if 12 <= but <= 15:
                polygone([(361+2, 361-12), (361-7, 361+5), (361+12, 361+5)],
                         remplissage=coloration[couleur_but], epaisseur=2)
        else:  # pion multicolore
            cercle(x+1, y+1, 9, remplissage=coloration[color_pion])
            cercle(x+1, y+1, 7, remplissage=coloration[color_pion+1])
            cercle(x+1, y+1, 5, remplissage=coloration[color_pion+2])
            cercle(x+1, y+1, 3, remplissage=coloration[color_pion+3])
            if but == 16:
                cercle(361+1, 361+1, 9, remplissage=coloration[color_pion])
                cercle(361+1, 361+1, 7, remplissage=coloration[color_pion+1])
                cercle(361+1, 361+1, 5, remplissage=coloration[color_pion+2])
                cercle(361+1, 361+1, 3, remplissage=coloration[color_pion+3])
        nb_pion += 1
        color_pion += 1
        if color_pion > 3:
            color_pion = 0


def nouveau_objectif(but, couleur_but, ancien_objectif, score):
    '''
    '''
    if commencer or (robot[actif] == pions[16] and couleur_but == 'multicolore') or \
            (robot[actif] == pions[but] and couleur_objet[actif] == couleur_objet[couleur_but]):
        if commencer or positif or solo:
            nouveau_but = randint(0, 16)
            score+=1
            while nouveau_but in ancien_objectif:
                nouveau_but = randint(0, 16)
            ancien_objectif.append(nouveau_but)
            if nouveau_but == 0 or nouveau_but == 4 or nouveau_but == 8 or nouveau_but == 12:
                nouvelle_couleur_but = 0
            elif nouveau_but == 1 or nouveau_but == 5 or nouveau_but == 9 or nouveau_but == 13:
                nouvelle_couleur_but = 1
            elif nouveau_but == 2 or nouveau_but == 6 or nouveau_but == 10 or nouveau_but == 14:
                nouvelle_couleur_but = 2
            elif nouveau_but == 3 or nouveau_but == 7 or nouveau_but == 11 or nouveau_but == 15:
                nouvelle_couleur_but = 3
            else:
                nouvelle_couleur_but = 'multicolore'
            return nouveau_but, nouvelle_couleur_but, ancien_objectif, score, False
        return but, couleur_but, ancien_objectif, score, True
    return but, couleur_but, ancien_objectif, score, False


def avance(touche):
    """
    reçoit en paramètre un évènement d'une touche et renvoie une coordonnée coorespondante
    à cette dernière sinon, il ne se passe rien.
    :param str touche: flèche directionnelle
    return tuple: coordonnée correspondant à la touche

    >>> avance('Up')
    (0, -1)
    >>> avance('Down')
    (0, 0)
    >>> avance('Right')
    (1, 0)
    >>> avance('Left')
    (-1, 0)
    >>> avance('CQFD')
    (0, 0)
    """
    if touche == 'Up':
        return 0, -1
    elif touche == 'Down':
        return 0, 1
    elif touche == 'Right':
        return 1, 0
    elif touche == 'Left':
        return -1, 0
    else:
        return 0, 0


def contact(rob, direction):
    """
    fonction recevant en paramètre les coordonnées du robot et la coordonnée de la direction de
    ce dernier et renvoie une coordonnée pour ne plus bouger

    :param lst rob: liste de coordonnées du robot
    :param tuple direction: coordonnée
    return tuple: coordonnée
    """
    # cogne les bords du plateau
    if rob[0] == 0 and direction == (-1, 0):
        return 0, 0
    elif rob[0] == 15 and direction == (1, 0):
        return 0, 0
    elif rob[1] == 0 and direction == (0, -1):
        return 0, 0
    elif rob[1] == 15 and direction == (0, 1):
        return 0, 0
    # cogne la case centrale
    elif rob[0] == 6 and 7 <= rob[1] <= 8 and direction == (1, 0):
        return 0, 0
    elif rob[0] == 9 and 7 <= rob[1] <= 8 and direction == (-1, 0):
        return 0, 0
    elif rob[1] == 6 and 7 <= rob[0] <= 8 and direction == (0, 1):
        return 0, 0
    elif rob[1] == 9 and 7 <= rob[0] <= 8 and direction == (0, -1):
        return 0, 0
    # cogne un autre robot
    else:
        for autre_robot in range(4):
            if autre_robot == actif:
                continue
            elif rob[0] == robot[autre_robot][0]-1 and rob[1] == robot[autre_robot][1] \
                    and direction == (1, 0):
                return 0, 0
            elif rob[0] == robot[autre_robot][0]+1 and rob[1] == robot[autre_robot][1] \
                    and direction == (-1, 0):
                return 0, 0
            elif rob[0] == robot[autre_robot][0] and rob[1] == robot[autre_robot][1]-1 \
                    and direction == (0, 1):
                return 0, 0
            elif rob[0] == robot[autre_robot][0] and rob[1] == robot[autre_robot][1]+1 \
                    and direction == (0, -1):
                return 0, 0
        for brique in range(0,len(murs_verticaux),2):
            if (rob[0] == ((murs_verticaux[brique][0]-1)/45)-1) and (rob[1] == (murs_verticaux[brique][1]-1)/45) \
                    and direction == (1, 0):
                return 0, 0
            elif (rob[0] == (murs_verticaux[brique][0]-1)/45) and (rob[1] == (murs_verticaux[brique][1]-1)/45) \
                    and direction == (-1, 0):
                return 0, 0
        for obstacle in range(0,len(murs_horizontaux),2):
            if (rob[0] == (murs_horizontaux[obstacle][0]-1)/45) and \
                    (rob[1] == ((murs_horizontaux[obstacle][1]-1)/45)-1) and direction == (0, 1):
                return 0, 0
            elif (rob[0] == (murs_horizontaux[obstacle][0]-1)/45 and rob[1] == (murs_horizontaux[obstacle][1]-1)/45) \
                    and direction == (0, -1):
                return 0, 0
        return direction


def affiche_menu(jeu):
    """
    Reçoit en paramètre le booléen 'jeu' pour lancer le jeu et renvoie deux variables booléens différentes
    'True, False' si le joueur choisi le premier mode,
    'True, True' si le joueur choisi, le deuxième mode,
    'False', False' sinon
    Attention, le test marche si le joueur clique parmi les deux modes

    :param bool jeu: un booléen
    return bool: activation d'un mode
    """
    rectangle(0, 0, 1125, 720, remplissage='#E1FFFD')
    rectangle(400, 300, 722, 380, couleur='#00B4A5', remplissage='#59F9EC', epaisseur=4)
    rectangle(400, 460, 722, 540, couleur='#9369FF', remplissage='#C8B3FF', epaisseur=4)
    ligne(0, 200, 1125, 200, couleur='#FF74EC', epaisseur=3)
    texte(250, 65, 'Ricochet Robot: le jeu', couleur='#FF74EC', taille=50)
    texte(455, 322.5, 'Partie classique', couleur='#256761')
    texte(490, 482.5, 'Mode solo', couleur='#3D06CA')
    while not jeu:
        action = attend_ev()
        tyaction = type_ev(action)
        if tyaction == 'ClicGauche':
            if 400 <= abscisse(action) <= 722 and 300 <= ordonnee(action) <= 380:
                return True, False
            elif 400 <= abscisse(action) <= 722 and 460 <= ordonnee(action) <= 540:
                return True, True
        elif tyaction == 'Quitte':
            return False, False
        else:
            continue


def affiche_plateau(mur_hor, mur_ver, score, score1, score2, score3, score4, time):
    """
    Reçoit en paramètre les listes des murs, les 4 différents scores ainsi que le temps et renvoie le temps
    Construit le déroulement du jeu selon les évènements que le joueur choisi.
    :param list mur_hor: liste des coodonnées
    :param list mur_ver: liste des coordonnées
    :param int score: score entier
    :param int score1: score entier
    :param int score2: score entier
    :param int score3: score entier
    :param int score4: score entier
    :param int time: durée limitée
    return time: durée limitée

    """
    rectangle(0, 0, 720, 720, remplissage='#F1EAC7', epaisseur=8) #couleur beige
    #construction d'un quadrillage
    for horizontal in range(1, 720, 45):
        ligne(0, horizontal, 720, horizontal, couleur='black', epaisseur=1)
    for vertical in range(1, 720, 45):
        ligne(vertical, 0, vertical, 720, couleur='black', epaisseur=1)
    #placement des murs
    rectangle(315, 315, 405, 405, couleur='black', remplissage='black', epaisseur=8)
    for elem in range(0, len(mur_hor), 2):
        ligne(mur_ver[elem][0], mur_ver[elem][1], mur_ver[elem+1][0], mur_ver[elem+1][1], epaisseur=8)
        ligne(mur_hor[elem][0], mur_hor[elem][1], mur_hor[elem+1][0], mur_hor[elem+1][1], epaisseur=8)
    #menu du plateau
    rectangle(724, 595, 1125, 640, remplissage='#EACCF9')
    texte(760, 600, 'Sélection du Robot actif', couleur='#8000C0')
    coordo_x = 0
    for cases in range(4):
        rectangle(724+coordo_x, 640, 824.25+coordo_x, 720, remplissage=couleur_objet[cases])
        coordo_x += 100.25
    if not solo:
        rectangle(724, 0, 1125, 100, remplissage='#EACCF9')
        coordo_x = 0
        for nb_joueur in range(4):
            rectangle(724+coordo_x, 390, 824.25+coordo_x, 430, remplissage='#D0DBD8')
            rectangle(724+coordo_x, 430, 824.25+coordo_x, 510, remplissage='#B7FFEA')
            rectangle(724+coordo_x, 510, 824.25+coordo_x, 550, remplissage='#D0DBD8')
            rectangle(724+coordo_x, 550, 824.25+coordo_x, 590, remplissage='#D0DBD8')
            texte(758+coordo_x, 390, 'J'+str(nb_joueur+1))
            texte(760+coordo_x, 440, str(score1), taille = 40)
            texte(765+coordo_x, 515, '+')
            texte(770+coordo_x, 550, '-')
            if not affiche_score:
                rectangle(724, 510, 1125, 590, remplissage='#D0DBD8')
            coordo_x += 100.25
            score1, score2, score3, score4 = score2, score3, score4, score1
        if not chemin:
            texte(770, 23, 'Chemin trouvé', taille=35, couleur='#8000C0')
            return time
        else:
            texte(770, 150, 'Temps restant: '+str(int(time)), taille=30, tag='timer')
            if time <= 0:
                efface('timer')
                texte(770,120,'Déplacez le pion',taille=25,tag='déplacement')
            if confirmation:
                efface('déplacement')
                texte(770, 120,'Avez-vous trouvé \nle bon nombre \nde déplacement ?',taille = 25, tag='question')
                texte(950,350, 'oui', taille=25, couleur="green", tag='yes')
                texte(850,350, 'non', taille=25, couleur="red", tag='no')
                rectangle(845, 350, 905, 390, couleur='red', epaisseur=4, tag='non')
                rectangle(945, 350, 995, 390, couleur='green', epaisseur=4, tag='oui')
            if positif or negatif:
                efface('yes')
                efface('no')
                efface('oui')
                efface('non')
                efface('question')
            return time - 0.15
    else:
        texte(770, 23, 'Score du joueur : '+str(score-1), taille = 25, couleur="purple")


if __name__ == "__main__":
    commencer = True
    jouer = False
    solo = False
    chemin = False
    confirmation = False
    positif = False
    negatif = False
    affiche_score = False

    while commencer:
        joueur = None
        robot = [None]
        for position_robot in range(4):  # définition de la position des robots
            while joueur in robot:
                joueur = (randint(0, 15), randint(0, 15))
                while 7 <= joueur[0] <= 8 and 7 <= joueur[1] <= 8:
                    joueur = (randint(0, 15), randint(0, 15))
            robot.append(joueur)
        robot.remove(None)
        emplacement = robot[:]

        score_solo, score_j1, score_j2, score_j3, score_j4 = 0, 0, 0, 0, 0
        actif = 0  #défini le robot actif acctuel
        deplacement = (0, 0)
        temps = 60
        deja_trouver = [] #liste des objectifs déjà trouvés
        objectif, couleur_objectif, deja_trouver, score_solo, confirmation = \
            nouveau_objectif('Début', 'Début', deja_trouver, score_solo)
        print(objectif,couleur_objectif, deja_trouver, score_solo, confirmation)
        cree_fenetre(taille_case * largeur_plateau, taille_case * hauteur_plateau)
        jouer, solo = affiche_menu(jouer)

        while jouer:
            commencer = False
            efface_tout()
            objectif, couleur_objectif, deja_trouver, score_solo, confirmation = \
                nouveau_objectif(objectif, couleur_objectif, deja_trouver, score_solo)
            temps = affiche_plateau(murs_horizontaux, murs_verticaux, score_solo,
                                    score_j1, score_j2, score_j3, score_j4, temps)
            if not solo:
                if positif:
                    emplacement = robot[:]
                    positif = False
                elif negatif:
                    robot = emplacement[:]
                    negatif = False
                affiche_emplacement(emplacement, couleur_emplacement)
            affiche_pion(pions, couleur_objet, objectif, couleur_objectif)
            affiche_robot(robot, couleur_objet)
            mise_a_jour()

            if solo or (temps <= 0 and not confirmation):
                robot[actif] = (robot[actif][0] + deplacement[0], robot[actif][1] + deplacement[1])
            deplacement = contact(robot[actif], deplacement)

            ev = donne_ev()
            ty = type_ev(ev)
            if ty == 'Quitte' or score_j1 + score_j2 + score_j3 + score_j4 == 17 or score_solo == 17:
                jouer = False
            elif ty == 'Touche' and deplacement == (0, 0) and (solo or (temps <= 0 and not confirmation)):
                deplacement = avance(touche(ev))
                deplacement = contact(robot[actif], deplacement)
            elif ty == 'ClicDroit' and affiche_score == True:
                affiche_score = False
            elif ty == 'ClicGauche' and deplacement == (0, 0):
                if 724 <= abscisse(ev) <= 1125 and 0 <= ordonnee(ev) <= 100 and not chemin and not solo:
                    chemin = True
                elif 845 <= abscisse(ev) <= 905 and 350 <= ordonnee(ev) <= 390 and confirmation:
                    negatif = True
                    confirmation = False
                elif 945 <= abscisse(ev) <= 995 and 350 <= ordonnee(ev) <= 390 and confirmation:
                    positif = True
                    affiche_score = True
                    temps = 60
                    chemin = False
                coox = 0
                for robot_actif in range(4):
                    if 724+coox <= abscisse(ev) <= 824.25+coox and 640 <= ordonnee(ev) <= 720 and (solo or (temps <= 0 and not confirmation)):
                        actif = robot_actif
                    if 724+coox <= abscisse(ev) <= 824.25+coox and 510 <= ordonnee(ev) <= 550 and affiche_score:
                        if robot_actif == 0:
                            score_j1 += 1
                        elif robot_actif == 1:
                            score_j2 += 1
                        elif robot_actif == 2:
                            score_j3 += 1
                        else:
                            score_j4 += 1
                    if 724+coox <= abscisse(ev) <= 824.25+coox and 550 <= ordonnee(ev) <= 590 and affiche_score:
                        if robot_actif == 0:
                            score_j1 -= 1
                        elif robot_actif == 1:
                            score_j2 -= 1
                        elif robot_actif == 2:
                            score_j3 -= 1
                        else:
                            score_j4 -= 1
                    coox += 100.25

            sleep(1/framerate)

        efface_tout()
        commencer = False

    ferme_fenetre()

















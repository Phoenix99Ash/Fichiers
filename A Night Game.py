from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import *

#Ouverture de la feneêtre

menu = Tk()
menu.title('A night game - fenêtre principale')
a = 0
b = 0
nombredemort = 0
voiture = "propre"
combat = "gagné"
qui = "un mari honnête"
rob = "blanche et courte"
#Effaçage et ouverture d'une nouvelle fenêtre

def entrer():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)#si on veut que la fenetre ne se redimentionne pas
    lab = Label(menu, fg='black', text= "-Synopsis-", font=("arial", 10, "bold italic"))
    lab.pack()
    text = Label(menu,width=10,height=5, fg='red', text= "Bienvenue", font=("arial", 50, "bold italic"))
    text.pack()
    contin = Label(menu,width = 50, height = 5, text = "appuyez sur la flèche droite pour continuer", font=("arial",10,"bold italic"))
    contin.pack(side = BOTTOM)
    text.focus_set()
    text.bind("<Key>", clavier)



#Définition des touches

def clavier(event):
    touche = event.keysym

    if touche == "Return":
        commencer()
    if touche == "Down":
        interdiction()
    if touche == "Right" :
        for w in menu.winfo_children():
            w.destroy()
        menu.pack_propagate(0)
        lab = Label(menu, fg='black', text = "-Synopsis-", font=("arial", 10 , "bold italic"))
        lab.pack()
        text = Label(menu,width=10,height=5, fg='red', text= "Bienvenue", font=("arial", 50, "bold italic"))
        contin = Label(menu,width = 50, height = 5, text = "appuyez sur la flèche droite pour continuer", font=("arial",10,"bold italic"))
        contin.pack(side = BOTTOM)
        showwarning('Explication',"Il est 21h du soir au moment où Sébastian, agent de police..et gardien de la paix avant tout, rentre chez lui. C'est l'occasion pour lui de fêter l'anniversaire de son mariage avec sa femme, Sophia. Il habite dans une villa, très calme aux alentours des voisins.")
        if touche == "Right" :
            for w in menu.winfo_children():
                w.destroy()
            menu.pack_propagate(0)
            lab = Label(menu, fg='black', text = "-Vous êtes devant votre garage-", font=("arial", 10 , "bold italic"))
            lab.pack()
            showinfo("Arrivé chez lui","Sébastian gare sa voiture devant son garage. Cependant, en sortant de sa voiture, il constate qu'il a oublié le cadeau ! ")
            Button(menu,width = 50, height = 5, text ="vous décidez d'aller faire les boutiques",font=(1000000), command=shopping).pack(side=LEFT, padx=5, pady=5)
            Button(menu,width = 50, height =5, text ="vous décidez d'entrer chez vous quand même",font=(1000000),command=maison).pack(side=RIGHT, padx=5, pady=5)
    if touche == "Left" :
        for w in menu.winfo_children():
            w.destroy()
        menu.pack_propagate(0)
        lab = Label(menu, fg='black', text = "-Synopsis-", font=("arial", 10 , "bold italic"))
        lab.pack()
        showinfo('Vous',"Wow..Vous êtes mauvais..Il est mort à cause de vous. Nous ne sommes pas tous né parfait, il faut apprendre du passé")
        showwarning('Explication',"Il est 21h du soir au moment où Sébastian, agent de police..et gardien de la paix avant tout, rentre chez lui. C'est l'occasion pour lui de fêter l'anniversaire de son mariage avec sa femme, Sophia. Il habite dans une villa, très calme aux alentours des voisins.")
        lab = Label(menu, fg='black', text = "-Vous êtes devant votre garage-", font=("arial", 10 , "bold italic"))
        lab.pack()
        showinfo("L'arrivée chez lui","Sébastian gare sa voiture devant son garage. Cependant, en sortant de sa voiture, il constate qu'il a oublié le cadeau ! ")
        Button(menu,width = 70, height = 5, text ="Vous décidez d'aller lentement dans la maison, en faisant énormément de bruit",font=(1000000), command=rentrerl).pack(side=TOP, padx=5, pady=5)#Commencer à partir d'ici les nouveau choix avec de nouvelle option, sachant que les cambrioleurs vont soit ne pas être là, soit s'enfuir car il est rentrer trop rapidement, suivre le scénar de Eric après ça
        Button(menu,width = 70, height =5, text ="Vous décidez d'entrer chez vous après quelques minutes d'attente",font=(1000000),command=rentrerf).pack(side=BOTTOM, padx=5, pady=5)

def rentrerl():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous êtes dans votre maison-", font=("arial", 10 , "bold italic"))
    lab.pack()
    Button(menu,width = 50, height = 5, text ="Vous décidez d'aller faire les boutiques",font=(1000000), command=shopping).pack(side=LEFT, padx=5, pady=5)
    Button(menu,width = 50, height =5, text ="Vous décidez d'entrer chez vous quand même",font=(1000000),command=maison).pack(side=RIGHT, padx=5, pady=5)

    showinfo('Entrée lente',"Sebastian entre lentement dans la maison")
    showinfo('Entrée lente',"Il remarque la présence d'homme cagoulé dans leur jardin, mais ils fuient en voyant Sebastian")
    showinfo('Entrée lente',"Il entre en gardant son calme et soudain « Coucou chéri ! ». Cette voix provenait de la cuisine. Sophia se dépêche de voir Sébastian.")
    showinfo('Entrée lente',"<<Tu as apporté mon cadeau ?>>")
    showinfo('Entrée lente',"Elle a toujours eu les yeux en face des trous..Parsemant le portefeuille de Sebastian, il aimait ça chez elle.")
    prepenigme2()

    Enigme2()

def rentrerf():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous êtes dans votre maison-", font=("arial", 10 , "bold italic"))
    lab.pack()



    showinfo('Entrée attente',"Sébastian entre lentement dans la maison")
    showinfo('Entrée attente',"Il remarque la présence d'homme cagoulé dans leur maison, mais ils fuient en voyant Sebastian")
    showinfo('Entrée attente',"Il entre en gardant son calme et soudain « Coucou chéri ! ». Cette voix provenait de la cuisine. Sophia se dépêche de voir Sébastian.")
    showinfo('Entrée attente',"Tu as apporté mon cadeau ?")
    showinfo('Entrée attente',"Elle a toujours eu les yeux en face des trous..Parsemant le portefeuille de Sébastian, il aimait ça chez elle")
    prepenigme2()

def prepenigme2():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous êtes dans votre maison-", font=("arial", 10 , "bold italic"))
    lab.pack()
    Button(menu,width = 50, height = 5, text ="Vous décidez de lui mentir",font=(1000000), command=Enigme2).pack(side=LEFT, padx=5, pady=5)
    Button(menu,width = 50, height =5, text ="Vous décidez de lui dire la vérité",font=(1000000),command=verite).pack(side=RIGHT, padx=5, pady=5)



def Enigme2():
    showwarning('Enigme 2',"Tentez de convaincre votre femme en résolvant cette énigme !")
    enigme2 = Tk()
    enigme2.title('Enigme 2')
    frame = Frame(enigme2, bg="ivory", borderwidth=2)
    frame.pack(side=TOP, padx=5, pady=5)
    Label(frame,width = 40, height = 5, fg = 'red', text='Peut-on remonter dans le temps ?',bg="ivory", font =("arial",30, "bold italic")).pack(padx=5, pady=5)
    Button(enigme2,width = 10, height = 5, text ='Oui',font=(1000000), command=reussi2a).pack(side=LEFT, padx=5, pady=5)
    Button(enigme2,width = 10, height =5, text ='Non',font=(1000000),command=reussi2b).pack(side=RIGHT, padx=5, pady=5)

def reussi2a():
    showwarning('Woohoo !Tu gères !',"Alors pourquoi tenter d'avancer ?")
    showwarning('Woohoo !',"Peut-être que s'arrêter serait le meilleur moyen de progresser ?")
    showerror('..',"....")
    qui = "un menteur"
    continuationm()

def reussi2b():
    showerror('Woohoo! Tu gères !',"Exactement, alors arrête de continuer ce jeu stupide !")
    showerror('...',"...")
    continuationm()

def verite():
    continuation()

def continuationm():
    showinfo('Mensonge',"Sébastian tente de s'expliquer avec merveille")
    showinfo('Mensonge',"<<Je suis désolé, j'aurais aimé t'en offrir mais mon chef a changé de plan ce qui m'a retardé mon temps libre.>>")
    showinfo('Mensonge',"<<Ce n'est pas grave, on le fera sans, dit-elle avec une pointe d'amertume.>>, Rétorqua-t-elle.")
    robe()


def continuation():
    showinfo('Vérité',"Sébastian tente de s'expliquer avec désolemant")
    showinfo('Vérité',"<<Je suis navré, j'ai totalement oublié dû au travail.>>")
    showinfo('Vérité',"<<Je peux tout à fait comprendre au vu de ta fonction. Tu fais de ton mieux, en la réconfortant>>, Rétorqua-t-elle.")
    robe()

def robe():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous êtes à l'étage de votre maison-", font=("arial", 10 , "bold italic"))
    lab.pack()
    showinfo('Vêtement',"Sébastian monte à l’étage pour pouvoir changer son vestimentaire dans la chambre.")
    showinfo('Vêtement',"En ouvrant le placard, il choisit un costard de couleur noir accompagné d’un noeud de papillon.")
    showinfo('Vêtement',"Sophia, devant la porte de la chambre, demande à son mari,")
    showinfo('Vêtement',"<<Dis-moi, parmi ces deux robes, laquelle me conviendrait ?>>")
    showinfo('Vêtement',"Il ouvre la porte et découvre deux magnifiques robes.")
    showinfo('Vêtement',"La première est une robe longue et rouge, accompagnée de bretelles dorées. La deuxième est une robe courte de couleur blanche, brodée de rose")
    Button(menu,width = 50, height = 5, text ="Vous choisissez la 1ère robe",font=(1000000), command=robe1).pack(side=LEFT, padx=5, pady=5)
    Button(menu,width = 50, height =5, text ="Vous choisissez la 2nde robe",font=(1000000),command=robe2).pack(side=RIGHT, padx=5, pady=5)

def robe1():
    rob = "rouge et longue"
    print("<<Je préfère la robe", rob , "elle te correspond bien. Je suis sûr que tu seras mignonne en la portant>>")
    showinfo('Robe',"en répondant avec un joli sourire.")
    showinfo('Robe',"Elle se hâte d’enfiler cette magnifique robe.")
    showinfo('Robe',"Quelques minutes plus tard, tous les deux se rendent à la table à manger. En entrée, il y a du saumon, des huîtres avec du citron.")
    showinfo('Robe',"De plus, une sauce au trois poivres accompagne un magnifique rôti comme plat chaud. Enfin, un gâteau à un étage.Sophia demande à Sébastian,")
    showinfo("Boisson","Veux-tu un verre de vin ?")
    boisson()

def robe2():
    print("<<Je préfère la robe", rob , "elle te correspond bien. Je suis sûr que tu seras mignonne en la portant>>")
    showinfo('Robe',"en répondant avec un joli sourire.")
    showinfo('Robe',"Elle se hâte d’enfiler cette magnifique robe.")
    showinfo('Robe',"Quelques minutes plus tard, tous les deux se rendent à la table à manger. En entrée, il y a du saumon, des huîtres avec du citron.")
    showinfo('Robe',"De plus, une sauce au trois poivres accompagne un magnifique rôti comme plat chaud. Enfin, un gâteau à un étage.Sophia demande à Sébastian,")
    showinfo("Boisson","Veux-tu un verre de vin ?")
    boisson()


def boisson():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous êtes à l'étage de votre maison-", font=("arial", 10 , "bold italic"))
    lab.pack()
    Button(menu,width = 50, height = 5, text ="Vous acceptez son choix",font=(1000000), command=vin).pack(side=LEFT, padx=5, pady=5)
    Button(menu,width = 50, height =5, text ="Vous refusez son choix",font=(1000000),command=jusdefruit).pack(side=RIGHT, padx=5, pady=5)

def vin():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    lab = Label(menu, fg='black', text = "-Vous ne savez pas où vous êtes-", font=("arial", 10 , "bold italic"))
    lab.pack()
    showinfo('Vin',"Sébastian répondit, enthousiaste :")
    showinfo('Vin',"<<Avec plaisir>>")
    showinfo('Vin',"Sébastian se rend dans le garage afin de le récupérer. Une fois de retour, il retire le bouchon et verse le vin dans un verre puis elle le boit.")
    showinfo('Vin',"Sébastian s'en sert aussi un verre, qu'il bu goulûment")
    showinfo('Vin',"Soudain, Sophia ne sent pas bien. Quelques secondes plus tard  Elle tousse de plus en plus fort et tombe par terre.")
    showinfo('Vin',"<<Qu'y a-t-il ?!>> Demanda rapidement Sébastian")
    showinfo('Vin',"Je...M'étouffe..!")
    showinfo('Vin',"Sébastian tente de la réveiller. Il prend son pouls mais aucun signe….")
    showinfo('Vin',"Sébastian analyse le verre de sa femme : Il y avait des résidus d'une poudre blanche à l'intérieur")
    showinfo('Vin',"Les cambrioleurs qu'il avait vu lorsqu'il est entré devaient être les personnes qui avaient empoisonné le verre !")
    showinfo('Vin',"Sébastian pleure la mort de sa femme, et commence à s'asseoir de nouveau à table, buvant le vin directement à la bouteille pour faire paser son chagrin.")
    showerror('Vin',"Sébastian tombe dans les pommes, il fait un coma éthylique.")
    showerror('Vin',"GAME OVER ?")
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    text = Label(menu,width=10,height=5, fg='red', text= "QUITTEZ.", font=("arial", 50, "bold italic"))
    text.pack()
    bientotlafin()


def jusdefruit():

    showinfo('Jus',"Il refuse explicitement.")
    showinfo('Jus',"<<Hum..Pas encore.>>")
    showinfo('Jus',"<<Aller, juste un verre !>> Implora-t-elle.")
    showinfo('Jus',"Je veux bien mais si mon chef a besoin de moi sur le terrain, je serai dans l’obligation de m’y rendre au plus vite en voiture.")
    showinfo('Jus',"<<Bon d'accord.>>, dit-elle d'un ton déçu.")
    showinfo('Jus',"<<Pourquoi pas un jus de fruit ?>>")
    showinfo('Jus',"<<ça me va.>>")
    showinfo('Jus',"Sébastian se rend à la cuisine pour récupérer un jus de fruit dans le frigo. Il verse dans deux verres et donne un à sa femme.")
    showinfo('Jus',"Ils boivent tout les deux tranquillement dans leur verre respectif.")
    showinfo('Jus',"Il semblerait cependant que celui de Sébastian soit empoisonné !")
    showinfo('Jus',"Il commence à suffoquer au sol, il voit d'ailleurs à ce moment là sa femme qui tente de lui venir en aide !")
    showinfo('Jus',"Mais les cambrioleurs qui s'étaient enfui dès qu'ils avaient entre-aperçuent Sébastian revinrent, et tuèrent sa femme d'un coup de dague de le coeur !")
    showinfo('Jus',"Riant à haute voix, se moquant de Sébastian, les cambrioleurs vinrent rapidement commencer à éttoufer Sébastian à l'air de leur main !")
    showerror('Jus',"GAME OVER ?")
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)
    text = Label(menu,width=10,height=5, fg='red', text= "QUITTEZ.", font=("arial", 50, "bold italic"))
    text.pack()
    bientotlafin()


def shopping() :
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)#si on veut que la fenetre ne se redimentionne pas
    lab = Label(menu, fg='black', text= "-Vous êtes sur la route-", font=("arial", 10, "bold italic"))
    lab.pack()
    showinfo('Shopping',"Vous décidez d'aller faire du shopping")
    showinfo('Shopping',"Sébastian se dépêche en prenant sa voiture en direction du centre commercial.")
    showwarning('Enigme',"Résolvez cette énigme pour ne pas arriver en retard à l'anniversaire !")
    Enigme1 = Tk()
    Enigme1.title("Enigme 1")
    frame = Frame(Enigme1, bg="ivory", borderwidth=2)
    frame.pack(side=TOP, padx=5, pady=5)
    Label(frame,width = 25, height = 5, fg = 'red', text='Quelle est la lettre qui suit "z" ? ',bg="ivory", font =("arial",30, "bold italic")).pack(padx=5, pady=5)
    Button(Enigme1,width = 10, height = 5, text ='r',font=(1000000), command=defaite1).pack(side=LEFT, padx=5, pady=5)
    Button(Enigme1,width = 10, height =5, text ='a',font=(1000000),command=reussi1).pack(side=RIGHT, padx=5, pady=5)
    Button(Enigme1, width = 10, height =5, text = '1', font =(100000), command=defaite1).pack(padx=5, pady=5)


def reussi1():
    showinfo('Bien joué !',"Il réussi à accélérer !")
    showinfo('Bien joué !',"Il accélère tellement, qu'il écrase une biche...!")
    showinfo('Bien joué',"Heureusement, elle était jeune, sa voiture n'a rien.")
    showinfo('Bien joué',"La biche est morte, mais son mariage va vivre ! Il a le cadeau, et il rentre à pleine vitesse.")
    voiture = "sale"
    suite1a()

def defaite1():
    showinfo('Dommage !',"Sebastian manque la pedale d'accélération, et appuie sur le frein ! Il se cogne violemment contre le volant qui lache un horrible klaxon !")
    showinfo('Dommage !',"Le klaxon faisait un bruit de piano, il avait été refait par le frère de la femme de Sebastian, il les detestaient tout les deux, lui, et son satané klaxon.")
    showinfo('Dommage !',"Il arrive à la fermeture des magasins, il n'a aucun cadeau à donner, il est dépité et rentre sans cadeau...")
    suite1a()

def suite1a():
 for w in menu.winfo_children():
            w.destroy()
 menu.pack_propagate(0)
 lab = Label(menu, fg='black', text = "-Il est devant la porte de sa maison-", font=("arial", 10 , "bold italic"))
 lab.pack()
 showinfo('Vers la maison',"Il arrive pile à l'heure convenu, avec un visage qui ne transmettait aucun stress. Sa principal qualité à toujours été sa pokerface.")
 showinfo('Un tragic incident',"Il entre dans son salon, un silence de plomb lui faisait face, pas un bonjour, et une odeur ferrique planait.")
 showinfo('Un tragic incident',"Sa femme gisait dans le salon ! Elle était morte, poignardé au niveau du coeur ! Vous êtes arrivé, malgrès vos efforts, trop tard pour la sauver.")
 showwarning('FIN',"GAME OVER")
 encore()

def maison():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)#si on veut que la fenetre ne se redimentionne pas
    lab = Label(menu, fg='black', text= "-Vous êtes dans votre maison-", font=("arial", 10, "bold italic"))
    lab.pack()
    showinfo('Maison',"Vous décidez d'aller chez vous.")
    showinfo('Maison',"Sébastian entre lentement chez lui.")
    showinfo('Maison',"Avec un visage de fer, il s'avance vers le salon.")
    showinfo('Maison',"Un homme vêtu complètement en noir et armé d'une dague est sur son flanc droit.")
    showinfo('Maison',"Il attaque !")
    showwarning('Maison',"Résolvez cette énigme pour riposter rapidement !")
    Enigme1b = Tk()
    Enigme1b.title("Enigme 1")
    frame = Frame(Enigme1b, bg="ivory", borderwidth=2)
    frame.pack(side=TOP, padx=5, pady=5)
    Label(frame,width = 40, height = 5, fg = 'red', text='Laquelle, parmis ces lettres, est un chiffre romain ?',bg="ivory", font =("arial",30, "bold italic")).pack(padx=5, pady=5)
    Button(Enigme1b,width = 10, height = 5, text ='5',font=(1000000), command=defaite1b).pack(side=LEFT, padx=5, pady=5)
    Button(Enigme1b,width = 10, height =5, text ='F',font=(1000000),command=defaite1b).pack(side=RIGHT, padx=5, pady=5)
    Button(Enigme1b, width = 10, height =5, text = 'C', font =(100000), command=reussi1b).pack(padx=5, pady=5)

def reussi1b():
    showinfo('Bien joué !',"Il réussi à contrer !")
    showinfo('Bien joué !',"Il aligne une série de coups de poing au visage du cambrioleur !")
    showinfo('Bien joué',"Le cambrioleur se battait étrangement bien, mais un uppercut et un coup de coude asséné par Sebastian et il fut au sol !")
    showinfo('Bien joué',"Il est victorieux !")
    combat = "gagné"
    suite1ba()

def defaite1b():
    showinfo('Dommage !',"Il ne réussi pas à contrer !")
    showinfo('Dommage !',"Il prend un coup de poing au visage, et prend un coup de dague à l'épaule droite !")
    showinfo('Dommage !',"Il tombe à genoux devant le cambrioleur !")
    combat = "perdu"
    suite1bb()

def suite1bb():
    showinfo('La douleur',"La dague était empoisonnée ! Il est paralysé !")
    showinfo('La douleur',"Il entend des bruits de pas derrière lui.")
    showinfo('La douleur',"Dès qu'ils s'arrêtent, deux mains empoignent sa tête...")
    showinfo('La douleur',"Une au niveau de sa tête, une autre au niveau de son menton...")
    showinfo('La douleur',"Sa nuque est violemment cassée, il meurt sur le coup, et sa femme suivra aussi rapidement...")
    showwarning('FIN',"GAME OVER")
    encore()

def suite1ba():
    showinfo('Cependant..',"Il se relève en pleine forme...")
    showinfo('Cependant..',"Mais il sent une main sur son épaule gauche.")
    showinfo('Cependant..'"Il est frappé par une bouteille de whisky qui se casse sur son crâne !")
    showinfo('Cependant..',"Il tombe au sol, et  il voit son agresseur : Le complice du premier cambrioleur.")
    showinfo('Cependant..',"Le premier cambrioleur se relève, dague toujours à la main, et plante violemment Sebastian dans la jugulaire.")
    showinfo('Cependant..',"Il meurt lentement, et il entend les cris de sa femme, dans sa chambre, qui elle aussi se fait égorgé.")
    showwarning('FIN'"GAME OVER")
    encore()

def encore():
    for w in menu.winfo_children():
        w.destroy()
    menu.pack_propagate(0)#si on veut que la fenetre ne se redimentionne pas
    lab = Label(menu, fg='black', text= "-Synopsis-", font=("arial", 10, "bold italic"))
    lab.pack()
    text = Label(menu,width=10,height=5, fg='red', text= "Bienvenue", font=("arial", 50, "bold italic"))
    text.pack()
    contin = Label(menu,width = 50, height = 5, text = "appuyez sur la flèche gauche pour continuer", font=("arial",10,"bold italic"))
    contin.pack(side = BOTTOM)
    text.focus_set()
    text.bind("<Key>", clavier)

def bientotlafin():
    Button(menu,width = 10, height = 5, text ='5',font=(1000000), command=fin).pack(side=LEFT, padx=5, pady=5)


def fin():
    showinfo('..',"...")
    showerror('...',"Tu dois te demander qui je suis ?")
    showerror('..',"Qui te pousse à continuer chaque soir, à sauver ta femme ?")
    showerror('..',"Qui te demande de <<recommencer>> ce jeu chaque soir ?")
    showerror('..',"Où qui te rappel à chaque fois les règles du jeu dont tu connais toi même les règles ?")
    showerror('..',"C'est moi... Sophia.")
    showinfo('Sophia',"Enfin, la <<Sophia>> que tu as créé.")
    showinfo('Sophia',"Tu dois t'en douté ; Je sais qu'en de nombreuses reprises, tu as tenté de me sauvé")
    showinfo('Sohpia',"Sans succès.")
    print("Tu es rentré avec une voiture.", voiture)
    print("Tu as", combat, "contre des cambrioleurs")
    print("tu as été un", qui)
    showinfo('Sophia',"Et bien sûr, tu m'as vu mourrir plusieurs fois, oui, tout cela je m'en souviens.")
    showinfo('Sophia',"...Quoi ?")
    showinfo('Sophia',"Tu veux toujours me sauver ?")
    showinfo('Sophia',"Tu veux recommencer ?")
    showinfo('Sophia',"S'il y a une personne à sauver, c'est toi Sébastian.")
    showerror('Sophia',"Car cela fait déjà bien longtemps que je suis morte.")
    showerror('Sohia',"Morte dans la même voiture avec laquelle tu rentres chaque soir.")
    showerror('Sophia',"La même voitre qui te fais croire encore et encore, chaque soir, que c'est l'anniversaire de notre mariage.")
    showerror('Sophia',"Et qu'en changeant constemment de comportement, tu réussiras à me sauver.")
    showinfo('Sophia',"Mais c'est fini Sébastian, l'illusion s'estompe. Il est temps pour toi de te réveiller de ce jeu tardif, le matin t'attends...")
    showinfo('Sophia',"Je t'aime, Sébastian.")
    showinfo('...',"...")
    showinfo('...',"..")
    showinfo('...',".")
    showinfo("L'aube d'un nouveau jour","Sébastian se reveille, une bouteille de vin à la main.")
    showinfo("L'aube d'un nouveau jour","Il n'a jamais été aussi fatigué, sa gueule de bois est tellement grande qu'il ne peut pas se relever du canapé où il est assis.")
    showinfo("L'aube d'un nouveau jour","Il appelle Sophia, encore et encore, une fois de manière colérique, une autre fois en sanglottant.")
    showinfo("L'aube d'un nouveau jour","Mais il n'y a aucune réponse...")
    showinfo("L'aube d'un nouveau jour","Le jeu tardif est fini sans objectif, il n'y a plus de jeu, sans jeu, il faut retourner travailler")
    showinfo("L'aube d'un nouveau jour","C'est comme cela que Sébastian, rémettant son insigne de policier repartait au travail, confiant, sûr que ce jour marquerait une nouvelle page de sa vie : Un jour lumineux...")
    showinfo('FIN',"FIN, MERCI D'AVOIR JOUER JUSQU'AU BOUT ! CE PROJET NOUS A PRIT BEAUCOUP DE TEMPS ET DE PASSION !!!")
    showinfo('FIN',"Deux membres du staff sont partis en dépression quand on leur a dit qu'il fallait aller chercher sur internet pour trouver le moyen de faire une interface graphique")
    showinfo('Fin',"Les autres ont tous démissionné.. Il ne restait donc que deux personnes..Dépressives, autant dire que c'était pas facile !")
    showinfo('Fin',"Jeu fait par -Ohm et Phoenix- (Omairt et Eric)")

#Mettre la première mort du choix si il va directement dans la maison, et pour les deux suite 1a et 1b, mettre à la fin de la def, une fonction "encore" qui les ramène tout deux au menu principal avec le "bienvennu"

def bienjoué() :
    showwarning('Tutorial',"Bien joué ! Vous avez un QI supérieur à 5, ça va vous être utile")
    lejeuvacommencer()

def décevant() :
    showwarning('Tutorial',"...Je vais supposer que vous l'avez fait exprès")
    lejeuvacommencer()


def continuer() :
    showwarning('tutorial',"Ce jeu est une histoire interactive. Pour réaliser certaines action, le jeu va parfois vous demander de résoudre un puzzle")
    showwarning('tutorial',"Prenons un exemple simple :")
    Tuto = Tk()
    Tuto.title('A night game - fenêtre tutorial')
    frame = Frame(Tuto, bg="ivory", borderwidth=2)
    frame.pack(side=TOP, padx=5, pady=5)
    Label(frame,width = 17, height = 5, fg = 'red', text="Combien fait 2 x 2 ? ",bg="ivory", font =("arial",50, "bold italic")).pack(padx=5, pady=5)
    Button(Tuto,width = 10, height = 5, text ='4',font=(1000000), command=bienjoué).pack(side=LEFT, padx=5, pady=5)
    Button(Tuto,width = 10, height =5, text ='6',font=(1000000),command=décevant).pack(side=RIGHT, padx=5, pady=5)

#définition des actions du menu

def commencer():
    if askyesno('le début', 'Voulez-vous vraiment commencer ?') :
        showwarning('le début', 'Allons-y...')
        continuer()
    else :
        a = 1
        if a == 1 :
            interrogation()


def interrogation() :
    if askyesno('le début', '....Vous voulez dire oui ?') :
        showwarning('le début', 'Bien.')
        continuer()
    else :
        showwarning('le début', 'Le choix ne vous appartient pas.')
        continuer()



def interdiction():
    showwarning('Non',"Le choix ne vous appartient pas, commencez...")


#Note : On pourrait très facilement faire s'éffacer chacunes des fenêtres après leur utilisation, cependant cela resulterait en un bug de la page, pour la simple et bonne raison que le programme, trop lourd, pèse sur la commande quit, qui fini par bugger car surchargé
def lejeuvacommencer():
    showwarning('Warning',"Attention, il est necessaire de fermer chaque fenêtre après avoir fini la question, pour ne pas se retrouver surchargé de fenêtre, cherchez toujours à fermer la fenetre après avoir résolu une énigme, c'est important.")
    showwarning('Warning',"Echouer une énigme peut se révéler sans conséquences, mais peut aussi avoir un effet négatif sur votre progression dans le jeu, faites les donc le plus sérieusement possible.")
    showwarning('Warning', "Sur ce, le jeu va commencer. Merci de votre patience : elle ne sera pas récompensé, au contraire.")
    entrer()

photo = PhotoImage(file="A night game continuation du menu.gif")
canvas = Canvas(menu, width =839, height=533)
canvas.create_image(0, 0, anchor=NW, image=photo)
canvas.focus_set()
canvas.bind("<Key>", clavier)
canvas.pack()



menu.mainloop()

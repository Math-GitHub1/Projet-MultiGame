########## Importer les modules necessaires ##############
from tkinter import *
import random
from tkinter import messagebox
import tkinter as tk
##########################################################
##########    Fonctions ##################################
########################################################## 

def Morpion():
    global Mafenetre1
    Mafenetre1.destroy()#Detruire le menu pour utiliser le score
    Morpion = Tk()
    Morpion.title("[ Morpion ]")
    
    #fonction pour desactiver les boutons.
    def desactive_boutons():
        Bu1.config(state= DISABLED)
        Bu2.config(state= DISABLED)
        Bu3.config(state= DISABLED)
        Bu4.config(state= DISABLED)
        Bu5.config(state= DISABLED)
        Bu6.config(state= DISABLED)
        Bu7.config(state= DISABLED)
        Bu8.config(state= DISABLED)
        Bu9.config(state= DISABLED)
        
    #fonctions qui verifies le gagnant de la partie.
    def CheckGagnant():
        global gagnant
        gagnant = False
        check( Bu1, Bu2, Bu3)
        check( Bu4, Bu5, Bu6)
        check( Bu7, Bu8, Bu9)
        check( Bu1, Bu4, Bu7)
        check( Bu2, Bu5, Bu8)
        check( Bu3, Bu6, Bu9)
        check( Bu1, Bu5, Bu9)
        check( Bu3, Bu5, Bu7)
        
    def check(A,B,C):
        global Joueur, gagnant,count
        if click == False:
            Joueur = "O"
        else:
            Joueur = "X"

        if A["text"] + B["text"] + C["text"] == "XXX" or A["text"] + B["text"] + C["text"] == "OOO":
            A.config(bg="green")
            B.config(bg="green")
            C.config(bg="green")
            gagnant = True
            import tkinter
            tkinter.messagebox.showinfo(title="Winner", message="Félicitation ! Vous avez gagné la partie !")
            desactive_boutons
        if count == 9 and gagnant == False:
            import tkinter
            tkinter.messagebox.showinfo(title="Dommage", message="Egalité !")

    #fonction du clique des boutons.       
    def Button_click(b):
        global click,count,tableau
        if b["text"]== "" and click == True :
            b["text"] = "X"
            click = False
            count += 1
            CheckGagnant()
            
        elif b["text"]== "" and click== False :
            b["text"] = "O"
            click = True
            count += 1
            CheckGagnant()
        else :
            messagebox.showerror("Morpion","Ce carreaux est déjà utilisé, il faut que tu en choisisses un autre.")
            
    #Creation des boutons (9 boutons car 9 cases).       
    Bu1= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu1))
    Bu2= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu2))
    Bu3= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu3))
    
    Bu4= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu4))
    Bu5= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu5))
    Bu6= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu6))
    
    Bu7= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu7))
    Bu8= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu8))
    Bu9= Button(Morpion,text="",font=("Helvetica",20), height=3,width=8, bg="SystemButtonFace", command=lambda: Button_click(Bu9))
                 
    #Creation d'une grille pour les boutons.
    Bu1.grid(row=0, column=0)
    Bu2.grid(row=0, column=1)
    Bu3.grid(row=0, column=2)

    Bu4.grid(row=1, column=0)
    Bu5.grid(row=1, column=1)
    Bu6.grid(row=1, column=2)

    Bu7.grid(row=2, column=0)
    Bu8.grid(row=2, column=1)
    Bu9.grid(row=2, column=2)
    
    Morpion.mainloop()
                                       
def Pong():
    global Madenetre1
   
    def deplacement():
        global dx, dy, PosX2, PosY2, score
        if canvas.coords(balle)[1]<0:
            dy=-1*dy
        if canvas.coords(balle)[2]>500:
            dx=-1*dx
        if canvas.coords(balle)[0]<0:
            dx=-1*dx
        if canvas.coords(balle)[3]>=PosY2 and canvas.coords(balle)[2]>=canvas.coords(raquette)[0] and canvas.coords(balle)[0]<=canvas.coords(raquette)[2] and canvas.coords(balle)[3]<=490:
            dy=-1*dy
            score=score+1
            TextGame.set("Score : "+ str(score))
        if canvas.coords(balle)[3]<550:
            tk.after(10,deplacement)
        canvas.move(balle,dx,dy)
 
    def KeyBoard(event):
        global PosX2, Mafenetre1
        Key = event.keysym
 
        if Key == 'Right':
            canvas.move(raquette,40,0)
        if Key == 'Left':
            canvas.move(raquette,-40,0)
   
    Mafenetre1.destroy()#Detruire le menu pour utiliser le score
    tk = Tk()
    tk.title("[ Pong ]")
 
    canvas = Canvas(tk,width = 500, height = 500 , bd=0, bg="grey")
    canvas.pack(padx=10,pady=10)
 
    balle = canvas.create_oval(PosX,PosY,PosX+20,PosY+20,fill='green')
    raquette = canvas.create_rectangle(PosX2,PosY2,PosX2+100,PosY2+10,fill='black')
 
    TextGame = StringVar()
    LabelGame = Label(tk, textvariable = TextGame , bg ="grey")
    TextGame.set("Score : "+ str(score))
    LabelGame.pack(padx = 15, pady = 5)
 
    canvas.focus_set()
 
    canvas.bind('<Key>',KeyBoard)
 
    deplacement()
   
    tk.mainloop()

def Pendu():
    global Mafenetre1
    Mafenetre1.destroy()#Detruire le menu pour utiliser le score
    # Fonction pour initialiser une nouvelle partie
    def nouvelle_partie():
        global mot_a_trouver, mot_trouve, fautes
        # Réinitialiser les variables globales
        mot_a_trouver = random.choice(mots)
        mot_trouve = "_" * len(mot_a_trouver)
        fautes = 0
        # Mettre à jour l'affichage
        mot_trouve_label.config(text=mot_trouve)
        compteur_fautes.config(text="Fautes : 0")
        for bouton in boutons:
            bouton.config(state=tk.NORMAL)
            
    # Fonction appelée lorsque le joueur clique sur une lettre
    def lettre_cliquee(lettre):
        global mot_trouve, fautes
        if lettre in mot_a_trouver:
            # Remplacer les "_" par la lettre trouvée
            nouveau_mot = ""
        for i in range(len(mot_a_trouver)):
            if mot_a_trouver[i] == lettre:
                nouveau_mot += lettre
            else:
                nouveau_mot += mot_trouve[i]
        mot_trouve = nouveau_mot
        # Mettre à jour l'affichage du mot trouvé
        mot_trouve_label.config(text=mot_trouve)
        # Vérifier si le joueur a gagné
        if "_" not in mot_trouve:
            mot_trouve_label.config(text=f"Gagné ! Le mot était {mot_a_trouver}")
            for bouton in boutons:
                bouton.config(state=tk.DISABLED)
        else:
            # Incrémenter le compteur de fautes
            fautes += 1
            # Mettre à jour l'affichage du compteur de fautes
            compteur_fautes.config(text=f"Fautes : {fautes}")
            # Vérifier si le joueur a perdu
            if fautes == 6:
                mot_trouve_label.config(text=f"Perdu ! Le mot était {mot_a_trouver}")
                for bouton in boutons:
                    bouton.config(state=tk.DISABLED)

    # Créer la fenêtre Tkinter
    fenetre = tk.Tk()
    fenetre.title("[ Jeu du pendu ]")

    # Créer un label pour afficher le mot à trouver
    mot_trouve_label = tk.Label(fenetre, text=mot_trouve, font=("Arial", 24))
    mot_trouve_label.pack()

    # Créer des boutons pour chaque lettre de l'alphabet
    lettres = "abcdefghijklmnopqrstuvwxyz"
    boutons = []
    for lettre in lettres:
        bouton = tk.Button(fenetre, text=lettre, command=lambda lettre=lettre: lettre_cliquee(lettre))
        bouton.pack(side=tk.LEFT)
        boutons.append(bouton)

    # Créer un label pour afficher le compteur de fautes
    compteur_fautes =tk.Label(fenetre, text="Fautes : 0")
    compteur_fautes.pack()

     # Créer un bouton pour recommencer la partie
    bouton_rejouer = tk.Button(fenetre, text="Rejouer", command=nouvelle_partie)
    bouton_rejouer.pack()

    # Démarrer une nouvelle partie
    nouvelle_partie()

    # Boucler sur l'interface graphique
    fenetre.mainloop()
##########################################################
##########    Variables ##################################
##########################################################
PosX=60
PosY=10
PosX2=200
PosY2=480
dx=3
dy=3
score=0

click = True
count = 0

mots = ["python", "programmation", "ordinateur", "internet", "informatique"]
mot_a_trouver = ""
mot_trouve = ""
fautes = 0
#########################################################
########## Interface graphique ##########################
##########################################################
 
Mafenetre1 = Tk()
Mafenetre1.title('[ Multi Game ]')
Mafenetre1['bg']='white'
 
#Menu principal
Frame1 = Frame(Mafenetre1,bg="cyan4",borderwidth=4,relief=GROOVE)
Frame1.pack(side=LEFT,padx=50,pady=50)
Label(Frame1,text="Menu Principal",fg="white",bg="cyan4").pack(padx=80,pady=30)
Button(Frame1,text="Jeu du Morpion",fg='black',command= Morpion).pack(padx=40,pady=50)
Button(Frame1,text="Jeu du Pong",fg='black',command= Pong).pack(padx=50,pady=50)
Button(Frame1,text="Jeu du Pendu",fg='black',command=Pendu).pack(padx=50,pady=40)
Button(Frame1,text="Quitter",fg='black',command=Mafenetre1.destroy).pack(padx=50,pady=40)

 
Mafenetre1.mainloop ()


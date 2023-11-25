import tkinter as tk
from tkinter import messagebox
from main import*

Liste_fonctions=["Liste des noms des présidents","Liste des mots les moins importants","Mots ayant le score TF-IDF le plus élevé","Mots les plus répétés par le président Chirac","Présidents qui ont parlé de la Nation et celui qui en a le plus parlé","Quel est le premier président a avoir parlé d'écologie ?","Quels sont les mots que tous les présidents ont évoqués"]
n=len(Liste_fonctions)

class InterfaceGraphique:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.fenetre.title("Interface Graphique")
        self.fenetre.attributes("-fullscreen", True)  # Met la fenêtre en mode plein écran

        # Barre de menus
        self.barre_menu = tk.Menu(self.fenetre)
        self.fenetre.config(menu=self.barre_menu)
        
        #Bouton quitter
        self.barre_menu.add_command(label="Quitter", command=self.quitter)
        
        # Événement de fermeture de la fenêtre
        self.fenetre.protocol("WM_DELETE_WINDOW", self.quitter)

        # Cadre principal
        self.cadre_principal = tk.Frame(self.fenetre, bd=2, relief=tk.SOLID)  # Ajout de la bordure au cadre principal
        self.cadre_principal.pack(fill=tk.BOTH, expand=True)
        
        # Partie gauche avec les boutons
        largeur_ecran = self.fenetre.winfo_screenwidth()
        largeur_cadre_gauche = int(largeur_ecran / 2)  # Environ la moitié de la largeur de l'écran
        self.cadre_gauche = tk.Frame(self.cadre_principal, bd=2, relief=tk.SOLID, width=largeur_cadre_gauche,)  # Ajout de la bordure au cadre gauche
        self.cadre_gauche.pack(side=tk.LEFT, fill=tk.Y)
        self.label_gauche=tk.Label(self.cadre_gauche, text="Liste des fonctions disponibles", font=("Helvetica", 16))
        self.label_gauche.grid(row=0, sticky="nsew", pady=50, padx=20)

        self.boutons = []
        for i in range(1, n+1):
            bouton = tk.Button(self.cadre_gauche, text=Liste_fonctions[i-1], command=lambda i=i: self.action_bouton(i))
            bouton.grid(row=i, column=0, sticky="nsew", pady=7, padx=20)  # Ajuste l'espacement et la largeur des boutons
            self.boutons.append(bouton)

        # Ajout d'une colonne supplémentaire pour rendre le cadre gauche plus large
        self.cadre_gauche.grid_columnconfigure(1, weight=1)

        # Partie droite avec le rendu
        self.cadre_droite = tk.Frame(self.cadre_principal, bd=2, relief=tk.SOLID)  # Ajout de la bordure au cadre droit
        self.cadre_droite.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        self.label_droite2=tk.Label(self.cadre_droite, text="", font=("Helvetica",16))
        self.label_droite=tk.Label(self.cadre_droite, text="Sortie de l'algorithme", font=("Helvetica",16))
        self.label_droite2.pack(fill=tk.BOTH)
        self.label_droite.pack(fill=tk.BOTH)

        # Utilisation d'un widget de texte pour le rendu
        self.texte_rendu = tk.Text(self.cadre_droite, wrap=tk.WORD, font=("Helvetica", 16))
        self.texte_rendu.pack(pady=50, padx=50)

    def action_bouton(self, numero_bouton):
        """Fonction attribuant à chaque bouton une action associée à une fonctionnalité"""
        resultat = ""
        if numero_bouton==1: #Renvoie les noms des présidents
            resultat = "Les présidents sont : \n"
            for nom in Liste_nom_president:
                resultat+=nom+"\n"
        elif numero_bouton==2: #Renvoie les mots peu importants
            text=mots_peu_importants(Matrice_TF_IDF)
            indice=0
            for i in range(0,len(text),4):
                if len(text)-i>=4:
                    resultat+=text[i]+" "+text[i+1]+" "+text[i+2]+" "+text[i+3]+"\n"
                indice=i
            for j in range(len(text)-indice-4):
                resultat+=text[indice-4+j]+" " 
        elif numero_bouton==3: #Renvoie les mots importants
            text=mots_importants(Matrice_TF_IDF)
            indice=0
            for i in range(0,len(text),4):
                if len(text)-i>=4:
                    resultat+=text[i]+" "+text[i+1]+" "+text[i+2]+" "+text[i+3]+"\n"
                indice=i
            for j in range(len(text)-indice-4):
                resultat+=text[indice-4+j]+" " 
        elif numero_bouton==4: #Renvoie tous les mots prononcés par Chirac
            text=mot_repetes_par_Chirac(Matrice_TF_IDF)
            indice=0
            for i in range(0,len(text),4): # Parcours de la liste 'text' par pas de 4
                if len(text)-i>=4:# Ajout des 4 mots actuels à la chaîne résultat
                    resultat+=text[i]+" "+text[i+1]+" "+text[i+2]+" "+text[i+3]+"\n"
                indice=i# Mise à jour de l'indice pour connaître la position du dernier groupe de 4 mots
            for j in range(len(text)-indice-4): # Ajout des mots restants après le dernier groupe de 4 mots
                resultat+=text[indice-4+j]+" " 
        elif numero_bouton==5: # Renvoie les présidents ayant parlé de nation et celui qui en a le plus parlé
            text=list(president_parle_Nation(Matrice_TF_IDF))
            resultat=text[0][0]
            for i in range(1,len(text[0])-1):
                resultat=resultat+", "+ text[0][i]
            resultat=resultat+" et "+text[0][-1]+" en ont parlé. "
            resultat=resultat+"C'est "+str(text[1])+" qui en a le plus parlé."
        elif numero_bouton==6: #Renvoie le premier président ayant parlé d'écologie
            resultat=president_ecologie(Matrice_TF_IDF,Liste_années_textes,Liste_nom_fichier)
        elif numero_bouton==7: #Renvoie les mots que tous les présidents ont prononcé
            text=mots_evoques_par_tous(Matrice_TF_IDF)
            indice=0
            for i in range(0,len(text),4):
                if len(text)-i>=4:
                    resultat+=text[i]+" "+text[i+1]+" "+text[i+2]+" "+text[i+3]+"\n"
                indice=i
            for j in range(len(text)-indice-4):
                resultat+=text[indice-4+j]+" " 
        self.texte_rendu.delete("1.0", tk.END)  
        self.texte_rendu.insert(tk.END, resultat)

    def quitter(self):
        self.fenetre.destroy()

fenetre_principale = tk.Tk()
interface = InterfaceGraphique(fenetre_principale)
fenetre_principale.mainloop()
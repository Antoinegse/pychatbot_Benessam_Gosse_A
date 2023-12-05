import os
import math

("IMPORTANT : pour les mots 'peu importants', nous avons décidé de leur affecter un score tf-idf de None, et non 0. C'est pour cela que dans la définition de la fonction "
 "idf, on calcule le logarithme sans ajouter +1.)")
 
def cleaning_directory(dossier):
    """Fonction prenant en argument un dossier de fichiers et renvoyant ces fichiers dépourvus de ponctuation et de majuscules.
     -> list"""
    global directory
    directory=os.listdir(dossier)
    Liste_nom_president=[]
    for fichier in directory :
        name=fichier[11:-4] # Permet de prendre uniquement le nom du président dans le titre du fichier
        Liste_nom_president=affichage(name,Liste_nom_president)
        file=open('speeches-20231108/'+ fichier,"r",encoding="utf-8")
        file_clean=open('cleaned/'+fichier[:-4]+"_cleaned.txt","w",encoding='utf-8')
        lignes=file.readlines()
        for line in lignes: # "Nettoie" le fichier de la ponctuation et des majuscules
                for lettre in line:
                    if lettre in ["à","è","é","ô","ù"]:
                        file_clean.write(chr(ord(lettre)))
                    elif lettre in [".",",",";","?","!",":","-",'"',"`"]:
                        file_clean.write(" ")
                    elif lettre=="'":
                        file_clean.write("e ")
                    else:
                        file_clean.write(lower(lettre))
        file.close()
        file_clean.close()
    return Liste_nom_president

def lower(lettre:str):
    """Fonction prenant en argument une lettre et renvoyant cette même lettre si c'est une minuscule, ou son équivalent en minuscule si c'est une majuscule."""
    if 65<=ord(lettre)<=90 or 192<=ord(lettre)<=223:
        return chr(ord(lettre)+32)
    else:
        return lettre

def prenom(nom:str):
    """Fonction prenant en argument le nom d'un président et renvoyant ce dernier sans le chiffre qui le suit
        -> str"""
    if nom[-1] in ["0","1","2","3","4","5","6","7","8","9"]:
            nom = nom[:-1]
    return Prenom_president[nom],nom



def affichage(nom : str,liste : list):
    """Fonction prenant en argument le nom d'un président et une liste, puis ajoute dans cette liste le prénom et le nom du président
       -> list"""
    surname,nom=prenom(nom)
    denomination=surname+" "+nom
    if denomination not in liste:
        liste.append(denomination)
    return liste



def fréquence(phrase : str, dico : dict):
    """Fonction prenant en argument une phrase et un entier, et remplissant le nombre d'occurences des mots présents dans la phrase dans la liste globale liste_TF"""
    for mot in phrase.split() :
        if mot in dico.keys():
            dico[mot]+=1
        else :
            dico[mot]=1
    return dico



def idf(mot):
    """Fonction prenant en argument un mot et un entier, calcule son score idf et l'ajoute au dictionnaire global IDF"""
    somme=0
    for l in range(len(clean_directory)):
        if mot in liste_TF[l].keys():
            somme+=1
    IDF[mot] = round(math.log(len(directory)/somme),5)

def TF_IDF(dossier):
    """Fonction prenant en argument un dossier de fichiers et renvoyant une matrice dans laquelle est présent le mot et son score tf idf selon le document
       -> list"""
    M_TF_IDF=[]
    for i in range(len(dossier)): #Cette double boucle permet de calculer le nombre d'occurences de chaque mot dans chaque document
        with open('cleaned/'+dossier[i],"r",encoding='utf-8') as f:
            lignes = f.readlines()
            for e in lignes :
                liste_TF[i]=fréquence(e,liste_TF[i])
    for l in range(len(dossier)): #Cette double boucle permet de calculer le score idf de chaque mot
        for k in liste_TF[l].keys():
            idf(k)
    for mot in IDF.keys(): # Ces boucles imbriquées permettent de créer une matrice et de lui ajouter chaque mot, ainsi que son score tf-idf
        L=[]
        for i in range(len(directory)):
            if mot in liste_TF[i].keys():
                L.append(liste_TF[i][mot]*IDF[mot])
            else:
                L.append(None)
        M_TF_IDF.append(L)
    return M_TF_IDF

def mots_peu_importants(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots dont la moyenne des scores tf-idf est inférieure à 0,5
    -> list"""
    Liste_mot=[]
    for i in range(len(matrice)): #Parcourt les différents lignes(soit les mots) de la matrice en argument
        moy=0
        occ=0
        for j in range(len(clean_directory)): #Parcourt les différents score d'un mot et fait la moyenne de ces scores ne comptant pas les scores nuls ici None
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
                occ+=1
        moy/=occ
        if moy<=0.5: #Les mots non importants sont ici les mots dont la moyenne de leurs scores est inférieure à 0.5
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

def mots_importants(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots dont la moyenne des scores tf-idf est supérieure à 1
    -> list"""
    Liste_mot=[]
    for i in range(len(matrice)): #Parcourt les différents lignes(soit les mots) de la matrice en argument
        moy=0
        occ=0
        for j in range(len(clean_directory)): #Parcourt les différents score d'un mot et fait la moyenne de ces scores ne comptant pas les scores nuls ici None
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
                occ+=1
        moy/=occ
        if moy>=4.2: #Les mots importants sont ici les mots dont la moyenne de leurs scores est supérieure à 4.2
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

def mot_repetes_par_Chirac(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots répétés par Chirac ayant un score tf-idf inférieur à 0,2
    -> list"""
    Liste_mots=list(IDF.keys())
    Liste_mots_repetes=[]
    for i in range(len(matrice)): #On ajoute tous les mots peu importants prononcés par Chirac à une liste
        if matrice[i][0]!=None and matrice[i][0]<=0.5:
            Liste_mots_repetes.append(Liste_mots[i])
        elif matrice[i][1]!=None and matrice[i][1]<=0.5:
            if Liste_mots[i] not in Liste_mots_repetes:
                Liste_mots_repetes.append(Liste_mots[i])
    return Liste_mots_repetes

def president_parle_Nation(matrice):
    """Fonction prenant en argument une matrice, la parcourant et renvoyant le nom des présidents ayant prononcé
       le mot "nation" ainsi que le nom de celui qui l'a plus répété.
       -> """
    liste_mots=list(IDF.keys())
    liste_président=[]
    president_qui_a_plus_de_nation=""
    indice_nation=0
    for i in range(len(liste_mots)): #On trouve l'endroit où se trouve le mot 'nation' dans la liste des mots.
        if liste_mots[i]=="nation":
            indice_nation=i
            break
    max=matrice[indice_nation][0]
    for j in range(len(matrice[indice_nation])): #On parcourt la matrice à l'indice obtenu précédemment
        if matrice[indice_nation][j] != None: #On donne le nom du président qui a prononcé le mot
            name=directory[j][11:-4]
            name=prenom(name)
            name=name[0]+" "+name[1]
            if name not in liste_président :
                liste_président.append(name)
            if matrice[indice_nation][j]<max :
                max=matrice[indice_nation][j]
                president_qui_a_plus_de_nation=liste_président[-1]
    return liste_président,president_qui_a_plus_de_nation

def president_ecologie(matrice:list,liste_années:list,liste_nom:list):
    """Fonction renvoyant le nom du premier président qui a parlé d'écologie et/ou de climat, ainsi que l'année associée.
       -> str"""
    Liste_apparition_ecologie=[] #Liste pour stocker les indices des textes où le mot climat apparaît
    liste_clés=list(IDF.keys())
    indice_climat=None
    indice_ecologie=None
    if "climat" in liste_clés:
        indice_climat=liste_clés.index("climat")
    if "écologie" in liste_clés:
        indice_ecologie=liste_clés.index("écologie")
    for i in range(len(directory)): #Parcours des textes
        if indice_climat!=None and matrice[indice_climat][i]!=None:
            Liste_apparition_ecologie.append(i)
        if indice_ecologie!=None and matrice[indice_ecologie][i]!=None:
            Liste_apparition_ecologie.append(i)
    indice_min_annee=Liste_apparition_ecologie[0]
    for indice in Liste_apparition_ecologie: #Recherche de l'indice de l'année associée à la première mention du climat
        if liste_années[indice]<liste_années[indice_min_annee]:
            indice_min_annee=indice
    return "C'est " + liste_nom[indice_min_annee] + " en " + str(liste_années[indice_min_annee])

def mots_evoques_par_tous(matrice:list):
    """Fonction parcourant une matrice et renvoyant tous les mots ayant un score tf-idf différent de None, les mots présents dans tous les textes """
    Liste_cles=list(IDF.keys())
    Liste_mot_evoques=[]
    for i in range(len(matrice)):
        booleen=True
        for score in matrice[i]:
            if score==None:
                booleen=False
        if booleen: #Si le mot a un score non nul, on l'ajoute à la liste renvoyée
            Liste_mot_evoques.append(Liste_cles[i])
    return Liste_mot_evoques

def Tokenisation(question):
    mots_question = []
    for e in question :
        if e!=" ":
            mots_question.append(e)
    return mots_question

def recherche_corpus(question):
    mot_corpus=[]
    dossier = "cleaned"
    fichiers = os.listdir(dossier)
    for fichier in fichiers :
        with open(fichier, "r") as f:
            lignes = f.readlines()
            for ligne in lignes :
                for i in question :
                     if i in ligne:
                         mot_corpus.append(i)
    return mot_corpus

def vecteur_TF_IDF_question(question):
    matrice_question=[[]for i in range(len(clean_directory))]
    mots_questions=Tokenisation(question)
    intersection=recherche_corpus(mots_questions)
    TF_question={}
    TF_question=fréquence(question,TF_question)
    for mot in TF_question.keys():
        TF_question[mot]/=len(mots_questions)
    mot_hors_corpus=[]
    for mot in set(mots_questions):
        if mot not in intersection:
            mot_hors_corpus.append(mot)
    Liste_clés=list(IDF.keys())    
    for i in range(len(Liste_clés)+len(mot_hors_corpus)):
        for j in range(len(clean_directory)):
            if (i<=len(IDF.keys())-len(mot_hors_corpus)) and (Liste_clés[i] in intersection):
                matrice_question[j].append(TF_question[Liste_clés[i]]*IDF[Liste_clés[i]])
            else:
                matrice_question[j].append(0)
    return matrice_question   
    

global Prenom_president
Prenom_president = {"Chirac":"Jacques","Mitterrand":"François","Macron":"Emmanuel",
     "Giscard dEstaing":"Valéry","Hollande":"François","Sarkozy":"Nicolas"}
global clean_directory
clean_directory=os.listdir(r'cleaned')
global liste_TF
liste_TF=[{},{},{},{},{},{},{},{}]
global IDF
IDF={}
Liste_nom_fichier=['Jacques Chirac','Jacques Chirac', 'Valéry Giscard dEstaing', 'François Hollande', 'Emmanuel Macron', 'François Mitterrand', 'Nicolas Sarkozy']
Liste_années_textes=[1995,2002,1974,2012,2017,1981,1988,2007]
Liste_nom_president=cleaning_directory("speeches-20231108")
Matrice_TF_IDF=TF_IDF(clean_directory)

import os
import math
 
def cleaning_directory(dossier):
    global directory
    directory=os.listdir(dossier)
    Liste_nom_president=[]
    for fichier in directory :
        name=fichier[11:-4]
        Liste_nom_president=affichage(name,Liste_nom_president)
        file=open('speeches-20231108/'+ fichier,"r",encoding="utf-8")
        file_clean=open('cleaned/'+fichier[:-4]+"_cleaned.txt","w",encoding='utf-8')
        lignes=file.readlines()
        for line in lignes:
                for lettre in line:
                    if lettre in ["à","è","é","ô","ù"]:
                        file_clean.write(chr(ord(lettre)))
                    elif lettre in [".",",",";","?","!",":","'","-",'"']:
                        file_clean.write(" ")
                    else:
                        file_clean.write(lettre.lower())
        file.close()
        file_clean.close()
    return Liste_nom_president

        
def prenom(nom):
    if nom[-1] in ["0","1","2","3","4","5","6","7","8","9"]:
            nom = nom[:-1]
    return Prenom_president[nom],nom

def affichage(nom,liste):
    surname,nom=prenom(nom)
    denomination=surname+" "+nom
    if denomination not in liste:
        liste.append(denomination)
    return liste

def fréquence(phrase : str,i):
    K=liste_TF[i]
    for mot in phrase.split() :
        if mot in K.keys():
            K[mot]+=1
        else :
            K[mot]=1

def idf(m,i):
    K=liste_TF[i]
    for j in K.keys():
        somme=0
        for l in range(len(clean_directory)):
                if j in liste_TF[l].keys():
                    somme+=1
        IDF[j] = round(math.log(len(directory)/somme),5)

def TF_IDF(dossier):
    M_TF_IDF=[]
    for i in range(len(dossier)):
        with open('cleaned/'+dossier[i],"r",encoding='utf-8') as f:
            lignes = f.readlines()
            for e in lignes :
                fréquence(e,i)
    for l in range(len(dossier)):
        for k in liste_TF[i].keys():
            idf(k,l)
    for mot in IDF.keys():
        L=[]
        for i in range(len(directory)):
            if mot in liste_TF[i].keys():
                L.append(liste_TF[i][mot]*IDF[mot])
            else:
                L.append(None)
        M_TF_IDF.append(L)
    return M_TF_IDF

def mots_peu_importants(matrice):
    Liste_mot=[]
    for i in range(len(matrice)):
        moy=0
        for j in range(len(clean_directory)):
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
        moy/=len(clean_directory)
        if moy<=0.2:
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

def mots_importants(matrice):
    Liste_mot=[]
    for i in range(len(matrice)):
        moy=0
        for j in range(len(clean_directory)):
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
        moy/=len(clean_directory)
        if moy>=1:
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

def mot_repetes_par_Chirac(matrice):
    Liste_mots=list(IDF.keys())
    Liste_mots_repetes=[]
    for i in range(len(matrice)):
        if matrice[i][0]!=None and matrice[i][0]<=0.2 :
            Liste_mots_repetes.append(Liste_mots[i])
        elif matrice[i][1]!=None and matrice[i][1]<=0.2:
            if Liste_mots[i] not in Liste_mots_repetes:
                Liste_mots_repetes.append(Liste_mots[i])
    return Liste_mots_repetes

def president_parle_Nation(matrice):
    liste_mots=list(IDF.keys())
    liste_président=[]
    president_qui_a_plus_de_nation=""
    for i in range(len(liste_mots)):
        if liste_mots[i]=="nation":
            indice=i
            break
    max=matrice[i][0]
    for j in range(len(matrice[i])):
        if matrice[i][j] != None:
            name=directory[j][11:-4]
            name=prenom(name)
            name=name[0]+" "+name[1]
            if name not in liste_président :
                liste_président.append(name)
            if matrice[i][j]<max :
                max=matrice[i][j]
                president_qui_a_plus_de_nation=liste_président[-1]
    return liste_président,president_qui_a_plus_de_nation

def president_ecologie(matrice,liste_années,liste_nom):
    Liste_apparition_ecologie=[]
    liste_clés=list(IDF.keys())
    indice_climat=liste_clés.index("climat")
    for i in range(len(directory)):
        if matrice[indice_climat][i]!=None:
            Liste_apparition_ecologie.append(i)
    min_annee=Liste_apparition_ecologie[0]
    for indice in Liste_apparition_ecologie:
        if liste_années[indice]<min_annee:
            min_annee=indice
    return "C'est " + liste_nom[min_annee] + " en " + str(liste_années[indice])

def mots_evoques_par_tous(matrice):
    Liste_cles=list(IDF.keys())
    Liste_mot_evoques=[]
    for i in range(len(matrice)):
        booleen=True
        for score in matrice[i]:
            if score==None:
                booleen=False
        if booleen:
            Liste_mot_evoques.append(Liste_cles[i])
    return Liste_mot_evoques    
    

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
print(Matrice_TF_IDF)

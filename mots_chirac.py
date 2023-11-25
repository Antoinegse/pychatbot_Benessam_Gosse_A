from main import *

def mot_repetes_par_Chirac(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots répétés par Chirac ayant un score tf-idf inférieur à 0,2
    -> list"""
    Liste_mots=list(IDF.keys())
    Liste_mots_repetes=[]
    for i in range(len(matrice)): #On ajoute tous les mots peu importants prononcés par Chirac à une liste
        if matrice[i][0]!=None and matrice[i][0]<=0.2 :
            Liste_mots_repetes.append(Liste_mots[i])
        elif matrice[i][1]!=None and matrice[i][1]<=0.2:
            if Liste_mots[i] not in Liste_mots_repetes:
                Liste_mots_repetes.append(Liste_mots[i])
    return Liste_mots_repetes

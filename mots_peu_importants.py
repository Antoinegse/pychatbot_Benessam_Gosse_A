from main import *

def mots_peu_importants(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots dont la moyenne des scores tf-idf est inférieure à 0,5
    -> list"""
    Liste_mot=[]
    for i in range(len(matrice)):
        moy=0
        occ=0
        for j in range(len(clean_directory)):
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
                occ+=1
        moy/=occ
        if moy<=0.2:
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

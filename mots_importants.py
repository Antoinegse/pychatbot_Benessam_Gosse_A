def mots_importants(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots dont la moyenne des scores tf-idf est supérieure à 1
    -> list"""
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

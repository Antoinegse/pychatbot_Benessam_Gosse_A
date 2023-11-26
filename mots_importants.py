def mots_importants(matrice):
    """Fonction prenant en argument une matrice et renvoyant les mots dont la moyenne des scores tf-idf est supérieure à 1
    -> list"""
    Liste_mot=[]
    for i in range(len(matrice)): #Parcourt les différents lignes(soit les mots) de la matrice en argument
        moy=0
        for j in range(len(clean_directory)): #Parcourt les différents score d'un mot et fait la moyenne de ces scores ne comptant pas les scores nuls ici None
            if matrice[i][j]!=None:
                moy+=matrice[i][j]
        moy/=len(clean_directory)
        if moy>=4.2: #Les mots importants sont ici les mots dont la moyenne de leurs scores est supérieure à 4.2
            mots=list(IDF.keys())
            mot=mots[i]
            Liste_mot.append(mot)
    return Liste_mot

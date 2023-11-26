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

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

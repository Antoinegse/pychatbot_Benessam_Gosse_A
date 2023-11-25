from main import *
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

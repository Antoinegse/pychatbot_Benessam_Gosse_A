from main import *
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

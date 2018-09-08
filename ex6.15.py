# 6.15 
# Écrire une boucle de programme qui demande à l’utilisateur d’entrer des notes d’élèves. 
# La boucle se terminera seulement si l’utilisateur entre une valeur négative. 
# Avec les notes ainsi entrées, construire progressivement une liste. 
# Après chaque entrée d’une nouvelle note (et donc à chaque itération de la boucle), 
# afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes.

from math import *

minC= 20
maxC = 0
i = 0
longueur = 0
listCote = []
listNom = []


listNom.append(input("Veuillez entrer le prénom de l'eleve  ou entrée Fin pour cloturer le programme "))
if (listNom[longueur]!="Fin"):

        cote = input("Veuillez entrer la cote ")
        cote = int(cote)

        while cote > 0 and cote <= 20 and listNom[longueur]!="Fin":
                listCote.append(cote)
                longueur = longueur + 1 
                moyenne = sum (listCote) / (longueur)
                print ("La moyenne actuelle est de ", moyenne)
                listNom.append(input("Veuillez entrer le prénom de l'eleve  ou entrée Fin pour cloturer le programme "))
                cote = input("Veuillez entrer un cote ")
                cote = int(cote)

        minC    = min(listCote)
        maxC    = max(listCote)

        while (i<longueur) and (longueur!=0):
            if listCote[i] == minC :
                eMinC = listNom[i]
            elif listCote[i] == maxC :
                eMaxC = listNom[i]
            i = i + 1
                


        print("Cote maximale: ", maxC," pour l'eleve ", eMaxC, " Cote minimale de  ", minC, " Pour l'élève ", eMinC)
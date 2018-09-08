# 5.11 Soient les listes suivantes :


t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []

#  Écrivez un petit programme qui crée une nouvelle liste t3. 
# Celle-ci devra contenir tous les éléments des deux listes en les alternant, 
# de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :

l = len(t1)
i = 0


if (l == len(t2)):
    while (i < l):
        t3.append(t2[i])
        t3.append(t1[i])
        i = i + 1
    print (t3)
else:
    print ('Erreur les deux listes ne font pas la même longueur')
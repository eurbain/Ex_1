
# 6.12 
# Demander à l’utilisateur qu’il entre un nombre. 
# Afficher ensuite : soit la racine carrée de ce nombre, soit un message indiquant que la racine carrée de ce nombre ne peut être calculée.

from math import *

num  = input ("Veuillez entrez un nombre ")

num = int(num)
if (num%2):
    print("Il n'est pas possible de calculer la racine carré de ", num)
elif (num == 2):
    print ("2 n'a pas de racinne carrée")
else:
    result =  sqrt(num)
    result = int(result)
    print("La racine carrée de ", num, " est de ", result)
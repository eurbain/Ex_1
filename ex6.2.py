# 6.2
# Écrivez un programme qui calcule le périmètre et l’aire d’un triangle quelconque dont l’utilisa- teur fournit les 3 côtés.
# (Rappel : l’aire d’un triangle quelconque se calcule à l’aide de la formule :
# S= d⋅d−a⋅d−b⋅d−c

from math import *

c1=input("Entrer le 1er coté du triangle ")

c2=input("Entrer le 2ème coté du triangle ")

c3=input("Entrer le 3ème coté du triangle ")

c1 = int(c1)
c2 = int(c2)
c3 = int(c3)

p = c1 + c2 + c3
d = p / 2
s = d * ((d-c1) * (d-c2) * (d - c3))
s = sqrt(s)



print ("Perimètre du triangle entrée est de ", p," la surface est quand à elle de ", s)



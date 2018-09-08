# 6.3
# Écrivez un programme qui calcule la période d’un pendule simple de longueur donnée.
#  La formule qui permet de calculer la période d’un pendule simple est T = 2 Pi RacineCarre ( l / G )
# l représentant la longueur du pendule 
# g la valeur de l’accélération de la pesanteur au lieu
# d’expérience. Ici g = 9.80665


from math import *

g = 9.80665
l = input("Entree la longeur du pendule ")
l = float (l)

periode = 2 * pi * ( sqrt(l/g))

print ("La période du pendule est de ", periode)

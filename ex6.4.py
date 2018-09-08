#
# 6.4 
# Écrivez un programme qui permette d’encoder des valeurs dans une liste.
#  Ce programme devrait fonctionner en boucle, l’utilisateur étant invité à entrer sans cesse de nouvelles valeurs,
#  jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’entrée. 
# Le programme se terminerait alors par l’affichage de la liste. Exemple de fonctionnement :
# Veuillez entrer une valeur : 25 Veuillez entrer une valeur : 18 Veuillez entrer une valeur : 6284 Veuillez entrer une valeur : [25, 18, 6284]


i = 0
test ='1'
liste=[]

while test!=0:
    entree = input("Veuillez entrer votre chiffre ")
    if (entree != ""):
        entree = int(entree)
        liste.append(entree) 
    else:
        #condition de sortie
        # Si l'entrée est videe on sort de la condition
        test = 0 

print (liste)
    
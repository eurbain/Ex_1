# 5.12 Écrivez un programme qui affiche « proprement » tous les éléments d’une liste. 
# Si on l’appliquait par exemple à la liste t2 de l’exercice ci-dessus, on devrait obtenir :
# Janvier Février Mars Avril Mai Juin Juillet Août Septembre Octobre Novembre Décembre

t = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

l = len(t)
i = 0 
output = ""


while i < l :
    output = output + t[i] + ", "    
    i = i + 1


print (output)
# 5.13 
# Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait afficher :
# le plus grand élément de cette liste a la valeur 75.


l = [32, 5, 12, 8, 3, 75, 102, 15]
i = len(l)
m = 0

while i > 0 :
    i = i - 1
    if (l[i]> m) : 
        m = l[i]

print ("Le plus grand élément de la liste est ", m)
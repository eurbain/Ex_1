# 5.14 
# Écrivez un programme qui analyse un par un tous les éléments d’une liste de nombres 
# (par exemple celle de l’exercice précédent) pour générer deux nouvelles listes. 
# L’une contiendra seulement les nombres pairs de la liste initiale, et l’autre les nombres impairs. Par exemple, 
# si la liste initiale est celle de l’exercice précédent, 
# le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], 
# et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce : pensez à utiliser l’opérateur modulo (%) déjà cité précédemment.


entree  = [32, 5, 12, 8, 3, 75, 102, 15]
i       = len(entree)
lpair   = []
limpair = []

while i > 0 :
    i = i - 1
    if (entree[i] % 2) == 0: 
        lpair.append(entree[i])
    else:
        limpair.append(entree[i])
        


print ("Les éléments pair de la liste sont  ", lpair)
print ("Les éléments pair de la liste sont  ", limpair)
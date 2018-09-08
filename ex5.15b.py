# 5.15 
# Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots 
# (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) 
# pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères, 
# l’autre les mots comportant 6 caractères ou davantage.


entree  = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
lentree = len(entree)
sortieS = ""
sortieL = ""
pivot   = 6
i       = 0

while (i<lentree):
    if (len(entree[i])>6):
        sortieL = sortieL + " " + (entree[i])
    else:
        sortieS = sortieS + " " + (entree[i])
    i = i + 1


print ("Les prenoms de moins de ", pivot, " lettres sont ", sortieS)

print ("Les prenoms de plus de ", pivot, " lettres sont ", sortieL)
# En partant de l’exercice précédent, écrivez un script 
# qui détermine si une chaîne de caractères donnée est un palindrome 
# (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens),
# comme par exemple « radar » ou « s.o.s ».

entree  = 'radar'
l       =   len(entree) - 1
i       =   l
sortie  = ''

while (i> -1):
    sortie = sortie + entree[i]   
    i = i - 1 

if ( entree == sortie):
    print("Youpi, c'est un palindrome")
else:
    print ("Même Joueur joue encore")

# 6.14
# ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien',
# 'Alexandre-Benoît', 'Louise']
# Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant.

prenom = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
i = 0
longueurListe = len(prenom)


while i< longueurListe :
    longueur = len(prenom[i])
    print (prenom[i], "compte ", longueur, " lettre")
    i = i + 1

 
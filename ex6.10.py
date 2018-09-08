#6.10 Demander à l’utilisateur son nom et son sexe (M ou F). 
# En fonction de ces données, afficher « Cher Monsieur » ou « Chère Mademoiselle » suivi du nom de la personne.



nom     =   input ("Veuillez entrer votre nom ")
sexe    =   input ("Veuillez entrer votre sexe ")

if (sexe=="M" or sexe=="m"):
        print("Cher Monsieur ", nom)
elif (sexe=="F" or sexe =="f"):
        print("Cher Madame ", nom)
else:
        print("ERREUR - Sexe indéfini ")
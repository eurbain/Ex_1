# Écrivez un script qui recopie une chaîne (dans une nouvelle variable), en insérant des astérisques entre les caractères.
# Ainsi par exemple, « gaston » devra devenir « g*a*s*t*o*n »


entree = "TestEdwin"

l = len(entree)
i = 0
sortie = ""

while ( i < l):
    sortie= sortie  + entree[i] + "*"
    i=i + 1


print(sortie)



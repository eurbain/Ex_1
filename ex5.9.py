#5.9 Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant. 
# Ainsi par exemple, « zorglub » deviendra « bulgroz ».

entree  = 'Zorglub'
l       =   len(entree) - 1
i       =   l
sortie  = ''

while (i> -1):
    sortie = sortie + entree[i]   
    i = i - 1 

print (sortie)
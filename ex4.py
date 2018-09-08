# Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13
# mais n’affiche que ceux qui sont des multiples de 7.

i = 0
x = 13
y = 50
z = 7

while i < y:
    t = i * x
    if (t % z) == 0 :
        print (t)
    i = i + 1
    

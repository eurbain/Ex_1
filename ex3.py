## Table de multiplication de 'z' avec modulo 'y'

# Creation des variables de base
z = 7
x = 0
i = 0
y = 3 

# boucle

while i < 11:
    x = z * i
    if (x % y) == 0:  # Alors X est un multiple de Y
        print (x, "*")
    else:
        print (x)
    i = i + 1
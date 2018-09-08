# 6.13 
# Convertir une note scolaire N quelconque, 
# entrée par l’utilisateur sous forme de points (par exemple 27 sur 85), 
# en une note standardisée suivant le code ci-après :
# Note
# N>= 80% A
#   >= 60 % B >= 50 % C >= 40 % D
# E

note    =   input("Veuillez entrer la cote à analyser ")
som     =   input("Veuillez entrer la note maximum possible ")

note    =   float (note)
som     =   int(som)

pourcent  =   (note / som )  * 100

if ( pourcent >= 80):
    result = 'A'
elif (pourcent>= 60):
    result = 'B'
elif ( pourcent >= 50 ):
    result = 'C'
elif ( pourcent >= 40):
    result = 'D'
else:
    result = 'E'

print ("La note finale est de ", result)

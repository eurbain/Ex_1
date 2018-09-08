# Écrivez un programme qui convertisse en degrés Celsius une température exprimée au départ en degrés Fahrenheit, ou l’inverse.
# La formule de conversion est : T F =T C ×1,8 + 32


t = 10
tc = 0
tf = 0

tf = t * 1.8 + 32
tc = t / 1.8 - 32

print ("De Fahrenheit à Celsius = ", tc, " Degres Celsius")
print ("De Celsius à Fahrenheit= ", tf, " Degres Fahrenheit")
#6.1 
# Écrivez un programme qui convertisse en mètres par seconde 
# et en km/h une vitesse fournie
# par l’utilisateur en miles/heure. (Rappel : 1 mile = 1609 mètres)

entree = input("Veuillez entrer une vitesse en Miles / Par heure")
vmile = float(entree)

vkmh = vmile * 1.609
vms = vkmh / 3,6

print(entree, "Miles/heure nous donne ", vkmh,"Km/h et ", vms, "M/s")
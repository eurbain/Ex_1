entree = 103604


## Calcul des valeurs 

seconde = entree % 60 
minute = entree // 60
heure = minute // 60
minute = minute % 60
jour = heure // 24
heure = heure % 24


## Impression selective
## N'imprime que si la valeur est suppérrieur à 0
## Prend en  compte le pluriel


if jour > 1 :
    tjour = 'jours'
    print (jour, tjour)
elif jour == 1 :
    tjour = 'jour'
    print (jour, tjour)

if  heure > 1 : 
    theure = " heures "
    print (heure, theure)
else :
    theure == "heure"
    print (heure, theure)


if minute > 1 :
    tminute=" minutes"
    print (minute, tminute)
else :
    tminute="minute"
    print (minute, tminute)


if (seconde>0) : 
    tseconde="secondes"
    print (seconde, tseconde)
else : 
    tseconde == "seconde"
    print (seconde, tseconde)



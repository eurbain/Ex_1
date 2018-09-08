#6.9 Déterminer si une année (dont le millésime est introduit par l’utilisateur) est bissextile ou non. 
# Une année A est bissextile si A est divisible par 4. 
# Elle ne l’est cependant pas si A est un multiple de 100, 
# à moins que A ne soit multiple de 400.
#
# Output vaut 1 si l'année est bissextile
# Output vaut 0 si l'année n'est pas bissextile


a = input("Entrez votre année pour savoir si elle est bissextile ")
a = int(a)
output = 1  

if (a%4):
    output = 0
else:
    if (a%100)==0:
        if (a%400):
            output=0
        else: 
            output = 1

if output:
    print(a," est une année bissextile")
else:
    print(a," n'est pas une année bissextile")
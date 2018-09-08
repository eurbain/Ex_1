# 6.8 E
# Ecrire un programme qui, étant données deux bornes entières a et b,
# additionne les nombres multiples de 3 et de 5 compris entre ces bornes. 
# Prendre par exemple a = 0, b = 32 ; le résultat devraitêtrealors0+15+30=45.
#
# Modifier légèrement ce programme pour qu’il additionne les nombres multiples de 3 ou de 5 
# comprisentrelesbornesaetb.Aveclesbornes0et32,lerésultatdevraitdoncêtre:0+3+ 5 +6+9+10+12+15+18+20+21+24+25+27+30=225.

a = int(input('Entrez la première borne '))
b = int(input("Entrez la deuxième borne "))
v = int(input("Enrre 1 pour la version 1 du programme 2 pour la deuxieme "))

s = 0
a, b = min(a,b), max(a,b)
# pour être sur que les bornes sont de le bon ordre


if v==1:
        while a!=b:
            if a%3 == 0 and a%5 == 0   :
                    s = s + a
            a = a + 1

        print("boucle 1 ", s)
else:
        while a!=b:
            if a%3 == 0 or a%5 == 0   :
                    s = s + a
            a = a + 1

        print("Boule 2 ",s)
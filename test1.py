# Premier essai de script Python
# petit programme simple affichant une suite de Fibonacci, c.à.d. une suite # de nombres dont chaque terme est égal à la somme des deux précédents.
a, b, c = 1, 1, 1
print(b)
while c<50:
    a, b, c = b, a+b, c+1
    print(b)
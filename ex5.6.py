# Écrivez un script qui détermine si une chaîne contient ou non le caractère « e ».

text="EdwinDoRemIA"
i = 0
r = 0
l = len(text)
letterL = "a"
letterU = "A"

while i<l:
    if (text[i] == letterL):
        r = r + 1
    elif (text[i] == letterU):
        r = r + 1
    i = i + 1


if (r>0):
    print("La lettre ", letterU, " apparait ", r, " fois dans le mot")
else:
    print("La lettre ", letterU, " n'apparait pas dans la châine")
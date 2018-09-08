# Écrivez un programme qui calcule les intérêts accumulés chaque année pendant 20 ans, par capitalisation d’une somme de 100 euros placée en banque au taux fixe de 4,3 %

lenght = 20     # durée du placement
taux = 0.043    # Taux d'investissement
capital = 100   # Capital
capital2 = capital
temp = capital
i = 1           # Compteur

while i < lenght:
        capital = capital + capital * taux
        capital2 = capital2 + temp * taux
        if i == 1:
            print ("Au bout de ", i, "an Vous avez ", capital, "€ de capital avec capitalisation ")
            print ("Au bout de ", i, "an Vous avez ", capital2, "€ de capital sans capitalisation ")
        else:
            print ("Au bout de ", i, "ans Vous avez ", capital, "€ de capital avec capitalisation ")
            print ("Au bout de ", i, "ans Vous avez ", capital2, "€ de capital sans capitalisation ")
        i = i + 1


# Parcourir les nombres de 0 à 100 inclus
for i in range(101):
    # Vérifier si le nombre n'est pas 26, 37 ou 88
    if i not in (26, 37, 88):
        print(i, end=" ")

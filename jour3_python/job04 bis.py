# Initialiser une chaîne vide
resultat = ""

# Parcourir les nombres de 1 à 100 inclus
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        resultat += "FizzBuzz "
    elif i % 3 == 0:
        resultat += "Fizz "
    elif i % 5 == 0:
        resultat += "Buzz "
    else:
        resultat += str(i) + " "

# Afficher le résultat final
print(resultat)

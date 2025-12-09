def draw_tapis_inverse(n):
    for i in range(n + 1):          # Pour chaque ligne
        for j in range(n + 1):      # Pour chaque colonne
            if j == n - i:          # Si on est sur la diagonale inversée
                print('/', end='')  # On affiche une diagonale /
            else:
                print('#', end='')  # Sinon on affiche un #
        print()  # Retour à la ligne
        

# Exemple d'utilisation
draw_tapis_inverse(10)


    
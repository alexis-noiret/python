# Définition de la fonction
def pair_impair(nombre):
    # Vérifier que c'est un entier
    if not isinstance(nombre, int):
        print(f"{nombre} n'est pas un entier.")
        return
    # Vérifier que c'est positif
    if nombre < 0:
        print(f"{nombre} n'est pas positif.")
        return
    # Vérifier si pair ou impair
    if nombre % 2 == 0:
        print(f"{nombre} est pair")
    else:
        print(f"{nombre} est impair")

# Appels de la fonction avec différentes valeurs
pair_impair(4)       # ➜ 4 est pair
pair_impair(7)       # ➜ 7 est impair
pair_impair(-3)      # ➜ -3 n'est pas positif.
pair_impair(3.5)     # ➜ 3.5 n'est pas un entier.
pair_impair(0)       # ➜ 0 est pair



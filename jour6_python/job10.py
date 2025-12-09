L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

produit = 1

for nombre in L:
    if 25 <= nombre <= 90:
        produit*= nombre 

print(f"le produit des valeurs dans l'intervalle [25, 90] est : {produit}")
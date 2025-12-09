montant_investissement = 20000  
taux_rendement = 5             


gain_annuel = montant_investissement * taux_rendement / 100

print("Gain annuel initial :", gain_annuel, "€")

montant_investissement = montant_investissement + 5000
taux_rendement = taux_rendement + 2


gain_annuel = montant_investissement * taux_rendement / 100


print("\nAprès augmentation du capital et du taux :")
print("Montant investi :", montant_investissement, "€")
print("Taux de rendement :", taux_rendement, "%")
print("Nouveau gain annuel :", gain_annuel, "€")

montant_investissement = montant_investissement * 0.9

taux_rendement = taux_rendement - 1

gain_annuel = montant_investissement * taux_rendement / 100
print("\nAprès retrait de 10% et diminution du taux :")
print("Montant investi final :", montant_investissement, "€")
print("Taux de rendement final :", taux_rendement, "%")
print("Gain annuel final :", gain_annuel, "€")
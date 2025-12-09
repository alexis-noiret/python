nom= "stylo"
prix_unitaire= 2.00
quantité_en_stock= 100

print("information produit:" )
print("nom: ",nom)
print("prix unitaire: ",prix_unitaire)
print("quantité en stock :",quantité_en_stock)

quantite= int(input("combien de produits souhaitez vous acheter?"))

nouveau_prix=prix_unitaire * 1.10
nouveau_stock= quantité_en_stock - quantite

print("information produit:" )
print("nom: ",nom)
print("prix unitaire: ",nouveau_prix)
print("quantité en stock: ",nouveau_stock)
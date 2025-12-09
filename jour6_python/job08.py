#Écrire un programme qui calcule la somme de toutes les valeurs paires de la liste

liste : L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
L=[8,24,27,48,2,16,9,7,84,91]
somme_paire = sum(x for x in L if x % 2 ==0)

print("somme des valeurs paires de la liste: ", somme_paire)




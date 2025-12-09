liste = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
somme_paire=0
for nombre in liste:
    if nombre % 2 == 0: 
        somme_paire += nombre

print("somme des valeurs paires de la liste: ", somme_paire)
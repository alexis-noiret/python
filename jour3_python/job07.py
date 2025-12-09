chaine = "abcdefghijklmnopqrstuvwxyz" * 10
index = 0
taille_ligne = 1
while index + taille_ligne <= len(chaine):
    print(chaine[index:index+taille_ligne])
    index += taille_ligne
    taille_ligne += 1

    # Chaîne de base répétée 10 fois
chaine = "abcdefghijklmnopqrstuvwxyz" * 10

# Initialisation de l'indice et de la taille de la première ligne
index = 0
taille_ligne = 1

# Calcul de la largeur maximale pour centrer la pyramide
# On calcule le nombre de lignes possibles
total_caracteres = len(chaine)
ligne = 0
while (ligne * (ligne + 1)) // 2 <= total_caracteres:
    ligne += 1
largeur_max = ligne - 1  # nombre de lignes réalisables

# Affichage de la pyramide
index = 0
for i in range(1, largeur_max + 1):
    ligne_chaine = chaine[index:index+i]
    index += i
    print(ligne_chaine.center(largeur_max * 2))  # centrage


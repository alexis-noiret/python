def draw_rectangle(width, height):
    # Affiche la première ligne du rectangle (bord supérieur)
    print('|' + '-' * (width - 2) + '|')
    
    # Affiche les lignes intermédiaires (bords verticaux avec espace au milieu)
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    
    # Affiche la dernière ligne du rectangle (bord inférieur)
    if height > 1:  # Pour éviter d'afficher une ligne vide si height = 1
        print('|' + '-' * (width - 2) + '|')

# Exemple d'utilisation
draw_rectangle(10, 3)

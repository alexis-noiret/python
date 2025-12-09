def draw_triangle(width, height):
    # Affiche chaque ligne du triangle
    for i in range(height):
        print(' ' * (height - i - 1) + '/' + ' ' * (2 * i) + '\\')
    
    # Affiche la base du triangle
    print( '/ ' + '_' * (2 * (height - 1)) +' \\')

# Exemple d'utilisation
draw_triangle(11, 6)

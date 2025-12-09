#Écrire une fonction qui contient une liste nommée « fruits » qui contient les
#strings pomme, cerise, orange, melon. Cette fonction doit à son appel ajouter
#à la liste « fruits » un string « mangue » à l’index 2.

def get_fruit ():
    fruits=["pomme","cerise","orange","melon"]
    fruits.insert(2, "mangue")
    print(fruits)
get_fruit()
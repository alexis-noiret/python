#Écrire une fonction qui contient une liste nommée « fruits » qui contient les strings « pomme », « cerise », « orange ». Cette fonction doit à son appel ajouter à la liste « fruits » un String « Melon » à la fin de cette liste.

def get_fruit ():
    fruits=["pomme","cerise","orange"]
    fruits.append("melon")
    print(fruits)
get_fruit()
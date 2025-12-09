#Écrire un programme qui crée une liste nommée « L » d’au moins 5 entiers
#puis successivement :
#➔ Afficher la deuxième valeur de la liste
#➔ Écrire une fonction qui remplace L[3] par la somme des cases voisines
#L[2] & L[4], puis afficher à nouveau le tableau.
#➔ Puis afficher la dernière valeur de la liste.



L=[1,2,3,4,5]
print("deusieme valeur de la liste: ", L[1])

def modifier_liste(liste):
    liste[3]= liste[2] + liste[4]

modifier_liste(L)

print("Liste aprés modification: ", L)

print("derniere valeur de la liste: ",L[-1])
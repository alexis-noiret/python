#Écrire un programme qui échange les valeurs de la première et de la
#dernière case d’une liste quelconque non vide.


L=[1,2,3,4,5]
print("avant echange: ",L)
L[0],L[-1]= L[-1],L[0]
print("apres echange: ",L)
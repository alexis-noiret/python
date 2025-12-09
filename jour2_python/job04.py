#Créez un programme qui affiche dans le terminal 
#les tables de multiplications de 1 à N. N étant un 
#entier supérieur à zéro saisi par l’utilisateur.  

N = int(input("Entrez un entier superieur a 0 : "))

for i in range(1, N + 1):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)

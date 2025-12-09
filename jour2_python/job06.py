#Écrire un programme qui affiche à l’aide d’une boucle de type while les 
#premiers résultats de la multiplication de N par 7. N étant un entier renseigné 
#par l’utilisateur. 

N = int(input("Entrz un nombre"))
i = 1
while i <= 10:
    print(N * 7 * i)
    i += 1
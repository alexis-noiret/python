def supprimer_doublons(L):
    nouvelle_liste = [] 
    for element in L:
        deja_present = False

        for unique in nouvelle_liste:
            if element == unique:
                deja_present = True

        if deja_present == False:
            nouvelle_liste = nouvelle_liste + [element]

    return nouvelle_liste

L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
resultat = supprimer_doublons(L)
print("Liste sans doublons :", resultat)

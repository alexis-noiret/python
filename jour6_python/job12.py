def tri_croissant(L):
    n = 0
    for _ in L:
        n += 1

    i = 0
    while i < n:
        j = i + 1
        while j < n:
           
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j += 1
        i += 1

    return L

ma_liste = [42, 7, 11, 39, 2]
resultat = tri_croissant(ma_liste)
print("Liste triée :", resultat)


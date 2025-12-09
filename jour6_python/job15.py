def arrondir_et_trier(L):
    i = 0
    for x in L:  
        entier = int(L[i])
        decimal = L[i] - entier
        if decimal >= 0.5:
            L[i] = entier + 1
        else:
            L[i] = entier
        i = i + 1

    n = 0
    for _ in L:
        n = n + 1

    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
            j = j + 1
        i = i + 1

    return L

ma_liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
print(arrondir_et_trier(ma_liste))

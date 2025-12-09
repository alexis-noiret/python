def my_sort(lst):
    """
    Trie une liste dans l'ordre croissant en utilisant un tri à bulles.
    Retourne la liste triée et affiche le nombre total d'échanges nécessaires.
    """
    n = len(lst)               # Longueur de la liste
    total_coups = 0            # Compteur pour le nombre de coups (échanges)
    trie = False               # Indique si la liste est triée

    while not trie:
        trie = True            # On suppose que la liste est triée
        for i in range(n - 1):
            # Comparer l'élément courant avec l'élément adjacent
            if lst[i] > lst[i + 1]:
                # Échanger les éléments si nécessaire
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                total_coups += 1  # On compte cet échange comme un coup
                trie = False      # Comme on a échangé, la liste n'était pas encore triée
    print(f"Nombre total de coups nécessaires : {total_coups}")
    return lst


# --- Exemple d'utilisation ---
ma_liste = [5, 2, 9, 1, 5, 6]
liste_triee = my_sort(ma_liste)
print("Liste triée :", liste_triee)

def arrondir_notes_luke(liste_notes):
    notes_arrondies = []
    
    for note in liste_notes:
        if note < 40:
            # L'étudiant échoue, on ne change rien
            notes_arrondies.append(note)
        else:
            # Calcul du prochain multiple de 5
            prochain_multiple_5 = ((note // 5) + 1) * 5
            # Vérifier la règle d'arrondi
            if prochain_multiple_5 - note < 3:
                notes_arrondies.append(prochain_multiple_5)
            else:
                notes_arrondies.append(note)
    
    return notes_arrondies


# --- Exemple d'utilisation ---
notes = [33, 38, 39, 40, 42, 84, 87, 91]
print(arrondir_notes_luke(notes))

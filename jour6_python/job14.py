def my_long_word(n, texte):
    mot = ""        
    resultat = []   

    for c in texte:
        if c != " " and c != "," and c != ".":
            mot = mot + c         
        else:
            if mot != "":         
                taille = 0
                for lettre in mot:
                    taille += 1
                if taille > n:    
                    resultat = resultat + [mot]
                mot = ""         

    if mot != "":
        taille = 0
        for lettre in mot:
            taille += 1
        if taille > n:
            resultat = resultat + [mot]

    phrase = ""
    for i in resultat:
        if phrase != "":
            phrase = phrase + " "
        phrase = phrase + i

    return phrase

texte = "Le savoir est une arme puissante contre l'ignorance"
print(my_long_word(4, texte))

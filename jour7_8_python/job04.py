def cesar(message, decalage):
    resultat = ""  # on commence avec une chaîne vide
    
    for caractere in message:
        # On vérifie si le caractère est une lettre
        if caractere.isalpha():
            # On détermine si c'est une majuscule ou une minuscule
            base = ord('A') if caractere.isupper() else ord('a')
            
            # On décale la lettre dans l'alphabet
            nouvelle_lettre = chr((ord(caractere) - base + decalage) % 26 + base)
            
            resultat += nouvelle_lettre
        else:
            # On garde les caractères non alphabétiques tels quels
            resultat += caractere
    
    return resultat


# --- Partie interactive ---
message = input("📝 Entrez le message à chiffrer : ")
decalage = int(input("🔢 Entrez le décalage (ex: 3 pour +3 ou -3 pour -3) : "))

message_crypte = cesar(message, decalage)

print("\n🔒 Message chiffré :", message_crypte)


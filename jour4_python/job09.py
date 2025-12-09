def moyenne(note1,note2,note3):
    somme= note1 + note2 + note3
    return somme / 3

note1 = float(input("entrez la premiere note:"))
note2 = float(input("entrez la deusiéme note:"))
note3 = float(input("entrez la troisiéme note:"))

moyenne_etudiant = moyenne(note1, note2, note3)

if 15 <= moyenne_etudiant <= 20:
    print("trés bon éléve")
elif 11 <= moyenne_etudiant <= 14:
    print("bon éléve")
elif 8 <= moyenne_etudiant <= 10:
    print("éléve moyen")
elif 0 <= moyenne_etudiant <= 7:
    print("éléve devant faire des efforts")
else:
    print("moyenne invalide")
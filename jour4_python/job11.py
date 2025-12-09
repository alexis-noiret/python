# Définition de la fonction
def time_to_text(minutes):
    # Vérifier que l'entrée est un entier
    if not isinstance(minutes, int):
        print("Erreur : le nombre de minutes doit être un entier.")
        return
    if minutes < 0:
        print("Erreur : le nombre de minutes doit être positif.")
        return

    # Calcul des heures et minutes
    heures = minutes // 60      # division entière pour obtenir les heures
    minutes_restantes = minutes % 60  # reste de la division pour les minutes

    # Affichage du résultat
    print(f"{heures} heures et {minutes_restantes} minutes")

# Appels de la fonction
time_to_text(150)  # ➜ 2 heures et 15 minutes
time_to_text(50)   # ➜ 0 heures et 50 minutes
time_to_text(180)  # ➜ 3 heures et 0 minutes

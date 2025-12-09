def distance_par_semaine(nb_marches, hauteur_marche):
    # Calcul en centimètres
    distance_cm = 7 * 5 * 2 * nb_marches * hauteur_marche
    
    # Conversion en mètres
    distance_m = distance_cm / 100
    
    # Affichage formaté
    print(f"Pour {nb_marches} marches de {hauteur_marche} cm, le gardien parcourt {distance_m:.2f} m par semaine.")


# --- Partie interactive ---
nb_marches = int(input("🪜 Entrez le nombre de marches du phare : "))
hauteur_marche = float(input("📏 Entrez la hauteur d'une marche en cm : "))

distance_par_semaine(nb_marches, hauteur_marche)


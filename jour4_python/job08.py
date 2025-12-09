def fruits_par_saison(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine, navet")
    
fruits_par_saison("fruits", "hiver")
fruits_par_saison("légumes","été")
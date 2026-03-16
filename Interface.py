import random

from BDD import Heros as liste_heros_dbz, mechants as liste_monstres_dbz

from herosmonstres import Creature

def creer_equipe(liste_source, est_heros):
    """Gère la sélection visuelle des personnages dans le terminal."""
    equipe_finale = []
    
    print("") 
    if est_heros:
        print("--- SELECTION DES HEROS (DBZ) ---")
    else:
        print("--- SELECTION DES MECHANTS ---")

    nb = int(input("Combien de combattants voulez-vous ? "))

    for i in range(nb):
        print("") 
        print(f"Personnage n°{i+1} :")
        
        for index, perso in enumerate(liste_source):
            
            print(f"[{index}] {perso['nom']} - {perso['description']}")

        choix = int(input("Votre choix (numéro) : "))
        data = liste_source[choix]

        nouveau = Creature(
            data["nom"], 
            data["description"], 
            data["pv"], 
            data["pv"], 
            data["defense"], 
            data["initiative"], 
            30, 
            data["typeDegats"]
        )
        
        equipe_finale.append(nouveau)
        print(f"-> {data['nom']} est prêt au combat !")

    return equipe_finale

def lancer_jeu():
    """Fonction principale de ton interface de combat."""
    print("")
    print(" >>>  BIENVENUE DANS FATE OF THE ARENA  <<< ")
    print(" Note : PV = Points de Vie (la santé de vos guerriers) ")
    print("")

   
    camp_gentils = creer_equipe(liste_heros_dbz, True)
    camp_mechants = creer_equipe(liste_monstres_dbz, False)

    print("\n >>>  LE COMBAT COMMENCE !  <<< \n")

    combat_en_cours = True
    while combat_en_cours:
      
        tous_les_combattants = camp_gentils + camp_mechants
        tous_les_combattants.sort(key=lambda c: c.lancer_initiative(), reverse=True)

        for attaquant in tous_les_combattants:
            if attaquant.pv <= 0:
                continue

            print(f"\n--- Tour de {attaquant.nom} (PV : {attaquant.pv}) ---")

            if attaquant in camp_gentils:
                cibles_potentielles = camp_mechants
            else:
                cibles_potentielles = camp_gentils

            print("Cibles disponibles :")
            for idx, cible in enumerate(cibles_potentielles):
                statut = "VIVANT" if cible.pv > 0 else "KO"
                print(f"[{idx}] {cible.nom} | PV : {cible.pv} | {statut}")

            choix_cible = int(input(f"Qui {attaquant.nom} doit-il attaquer ? "))
            victime = cibles_potentielles[choix_cible]

            attaquant.attaque(victime)

       
        pv_heros = sum(h.pv for h in camp_gentils)
        pv_mechants = sum(m.pv for m in camp_mechants)

        if pv_heros <= 0 or pv_mechants <= 0:
            combat_en_cours = False
            print("\n >>>  TERMINE  <<<")
            print("L'équipe des Méchants a gagné !" if pv_heros <= 0 else "L'équipe des Héros a gagné !")


if __name__ == "__main__":
    lancer_jeu()
import random
from BDD import heros as liste_heros_dbz
from BDD import mechants as liste_monstres_dbz
from Creature import Creature,Heros,Monstre
from actions import Soin, Buff, Debuff, ramasser_carte, invoquer_shenron, verifier_mort, Fusions
def phase_preparation(heros):
    objets_dispo = ["Potion", "Anti-para", "Queue de phénix", "Haricot Magique"]

    for h in heros:
        print(f"\nPréparation de {h.nom}")
        inventaire = []

        for i in range(3):
            print("Choisis un objet :")
            for j, obj in enumerate(objets_dispo):
                print(f"{j} - {obj}")

            try:
                    choix = int(input("Choix : "))
            except ValueError:
                    print("Entrez un numéro valide.")
                    continue
            if 0 <= choix < len(objets_dispo):
                inventaire.append(objets_dispo[choix])
            else:
                print("Choix invalide")

        h.inventaire = inventaire
        print("Inventaire de", h.nom, ":", h.inventaire)
        input("Appuyer sur Entrée pour continuer...")

def creer_equipe(liste_source, est_heros):
    liste_source2 = liste_source.copy()
    equipe_finale = []

    if est_heros:
        print("--- SELECTION DES HEROS (DBZ) ---")
    else:
        print("--- SELECTION DES MECHANTS ---")

    
    try:
        nb = int(input("Combien de combattants voulez-vous ? "))
    except ValueError:
        print("Entrez un numéro valide.")
        

    for i in range(nb):
        print(f"\nPersonnage n°{i+1} :")

        for index, perso in enumerate(liste_source2):
            print(f"[{index+1}] {perso['nom']} - {perso['description']}")

        try:
            choix = int(input("Votre choix (numéro) : "))
        except ValueError:
            print("Entrez un numéro valide.")
            continue
        perso = liste_source2[choix-1]
        liste_source2.pop(choix-1)

        if est_heros:
            armes = [
                {"nom": "Épée de Trunks", "bonus": 15},
                {"nom": "Bâton Magique",  "bonus": 10},
                {"nom": "Poings d'Acier", "bonus": 5},
                {"nom": "Sans arme",      "bonus": 0}
            ]

            print(f"\nQuelle arme pour {perso['nom']} ?")
            for idx, a in enumerate(armes):
                print(f"[{idx+1}] {a['nom']} (+{a['bonus']} dégâts)")

            try:
                choix_arme = int(input("Votre choix d'arme (numéro) : "))

            except ValueError:
                print("Entrez un numéro valide.")
                continue
            arme_choisie = armes[choix_arme-1]
            perso["inventaire"].append(arme_choisie)

            degats_finaux = perso["degats"][0], perso["degats"][1] + arme_choisie["bonus"]

        else:
            degats_finaux = perso["degats"]

        if est_heros:
            nouveau = Heros(
                perso["nom"],
                perso["description"],
                perso["pv"],
                perso["pv_max"],
                perso["defense"],
                perso["initiative"],
                perso["degats"],
                perso["typeDegats"],
                perso["actions"],
                perso["etat"],
                perso["Carte"],
                perso["arme"],
                perso["inventaire"],
                perso["peut_fusionner"],
                perso["fusion_avec"]
            )
        else:
            nouveau = Monstre(
                perso["nom"],
                perso["description"],
                perso["pv"],
                perso["pv_max"],
                perso["defense"],
                perso["initiative"],
                degats_finaux,
                perso["typeDegats"],
                perso["actions"],
                perso["etat"],
                perso["Carte"],
                perso["resistances"]
            )

        equipe_finale.append(nouveau)
        phase_preparation([nouveau])

    

    return equipe_finale

def boucle_combat(heros, monstres):
    cartes = []  
    morts = []    

    creatures = heros + monstres
    print("\nLancement de l'initiative...")
    ordre = sorted(creatures, key=lambda c: c.lancer_initiative(), reverse=True)
    print("\nOrdre de jeu :")
    for c in ordre:
        print("-", c.nom)

    while True:
        for joueur in ordre:
            if joueur.pv <= 0:
                continue

            print("\nTour de", joueur.nom, "| PV :", joueur.pv, "/", joueur.pv_max)

            if joueur in heros:
                print("1 - Attaquer")
                print("2 - Magie")
                print("3 - Objets")
                print("4 - Ramasser une boule")
                print("5 - FUSION!")
                print("6 - Passer son tour")
                try:
                    choix = int(input("Choix : "))
                except ValueError:
                    print("Entrez un numéro valide.")
                    continue

                if choix == 1:
                    print("\nCibles :")
                    for i in range(len(monstres)):
                        print(i+1, "-", monstres[i].nom, "| PV :", monstres[i].pv)
                    
                    try:
                        cible = int(input("Cible : ")) - 1
                    except ValueError:
                        print("Entrez un numéro valide.")
                        continue
                    if 0 <= cible < len(monstres):
                        joueur.attaque(monstres[cible])
                        verifier_mort(monstres[cible], monstres, morts, cartes)  
                    else:
                        print("Cible invalide")

                elif choix == 2:
                    print("1 - Magie de soin")
                    print("2 - Magie de renforcement")
                    print("3 - Debuff sur ennemi")
                     
                    try:
                        choix_sort =int(input("Choix du sort : "))
                    except ValueError:
                        print("Entrez un numéro valide.")
                        continue

                    if choix_sort == 1:
                        action = Soin("Soin", joueur, joueur)
                        action.executer()
                    elif choix_sort == 2:
                        action = Buff("Buff", joueur, joueur)
                        action.executer()
                    elif choix_sort == 3:
                        print("\nCibles :")
                        for i in range(len(monstres)):
                            print(i+1, "-", monstres[i].nom, "| PV :", monstres[i].pv)
                         
                        try:
                            cible = int(input("Cible : ")) - 1
                        except ValueError:
                            print("Entrez un numéro valide.")
                            continue
                        if 0 <= cible < len(monstres):
                            action = Debuff("Debuff", joueur, monstres[cible])
                            action.executer()
                        else:
                            print("Cible invalide")

                elif choix == 3:
                    if len(joueur.inventaire) == 0:
                        print(joueur.nom, "n'a aucun objet !")
                    else:
                        print("\nInventaire de", joueur.nom)
                        for i in range(len(joueur.inventaire)):
                            print(i+1, "-", joueur.inventaire[i])
                        try:
                            choix_objet = int(input("Quel objet utiliser ? ")) - 1

                        except ValueError:
                            print("Entrez un numéro valide.")
                            continue
                        objet = joueur.inventaire[choix_objet]

                        if objet == "Haricot Magique":
                            joueur.pv = joueur.pv_max
                            joueur.inventaire.remove(objet)
                            print(joueur.nom, "mange un haricot magique et récupère tous ses PV !")
                        elif objet == "Potion":
                            joueur.pv = joueur.pv + 50
                            if joueur.pv > joueur.pv_max:
                                joueur.pv = joueur.pv_max
                            joueur.inventaire.remove(objet)
                            print(joueur.nom, "utilise une Potion et récupère 50 PV !")
                        elif objet == "Anti-para":
                            joueur.etat = "normal"
                            joueur.inventaire.remove(objet)
                            print(joueur.nom, "est soigné de son état !")

                elif choix == 4:
                    print("1 - Ramasser Les boules de cristalles laissé par un mort")
                    print("2 - Invoquer shenron ")
                    try:
                        choix = int(input("Choix : "))
                    except ValueError:
                        print("Entrez un numéro valide.")
                        continue
                    if choix == 1:
                        ramasser_carte(joueur, cartes)  
                        nb_boules = 0
                        for obj in joueur.inventaire:
                            if "Boule" in str(obj):
                                nb_boules = nb_boules + 7
                    elif choix == 2:
                        invoquer_shenron(heros, morts)

                elif choix == 5:
                    if joueur.peut_fusionner == False:
                        print(joueur.nom, "ne peut pas fusionner !")
                    else:
                        print("\nAvec qui voulez-vous fusionner ?")
                        for i in range(len(heros)):
                            print(i+1, "-", heros[i].nom)
                          
                        try:
                            choix_fusion = int(input("Choix : ")) - 1
                        except ValueError:
                            print("Entrez un numéro valide.")
                            continue
                        if 0 <= choix_fusion < len(heros):
                            partenaire = heros[choix_fusion]
                            if partenaire.nom == joueur.fusion_avec:
                                Fusions(joueur, partenaire, heros)
                                ordre = sorted(heros + monstres, key=lambda c: c.lancer_initiative(), reverse=True)
                                print("\nNouvel ordre de jeu :")
                                for c in ordre:
                                    print("-", c.nom)
                                break  
                            else:
                                print(joueur.nom, "ne peut pas fusionner avec", partenaire.nom)
                        else:
                            print("Choix invalide")

                elif choix == 6:
                    print(joueur.nom, "passe son tour.")

            else:
                print("\nTour de", joueur.nom, "(méchant)")
                print("1 - Attaquer")
                print("2 - Passer son tour")
                try:
                    choix = int(input("Choix : "))
                except ValueError:
                    print("Entrez un numéro valide.")
                    continue
                if choix == 1:
                    print("\nCibles :")
                    for i in range(len(heros)):
                        print(i+1, "-", heros[i].nom, "| PV :", heros[i].pv)
                    try:
                        cible = int(input("Cible : ")) - 1
                    except ValueError:
                        print("Entrez un numéro valide.")
                        continue
                     
                    if 0 <= cible < len(heros):
                        joueur.attaque(heros[cible])
                        verifier_mort(heros[cible], heros, morts, cartes) 
                    else:
                        print("Cible invalide")
                elif choix == 2:
                    print(joueur.nom, "passe son tour.")

            
            if len(monstres) == 0:
                print("\nVictoire ! Les héros ont gagné !")
                return
            if len(heros) == 0:
                print("\nDéfaite... Les monstres ont gagné.")
                return
    
def lancer_jeu():
        print(" >>>  BIENVENUE DANS FATE OF THE ARENA ! <<< ")

        camp_gentils  = creer_equipe(liste_heros_dbz, True)
        camp_mechants = creer_equipe(liste_monstres_dbz, False)

        print("\n >>>  LE COMBAT COMMENCE !  <<< \n")

        boucle_combat(camp_gentils, camp_mechants)

if __name__ == "__main__":
    lancer_jeu()
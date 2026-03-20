import random
from Creature import Action, Creature,Heros
from BDD import heros, mechants
from BDD import hero_fusion


class Soin(Action):  # Haricot magique
    def executer(self):
        super().executer()
        if self.cible.pv < self.cible.pv_max:
            self.cible.pv = self.cible.pv + 50
            print(f"{self.cible.nom} a mangé un haricot magique et récupère 50 pv({self.cible.pv_max} PV) !")
        else:
            print("Vous avez deja vos pv au max !")

class Buff(Action):
    def executer(self):
        super().executer()
        self.cible.defense += 2
        self.cible.etat = "Boosté"   # ← etat au lieu de etats
        print(f"Défense de {self.cible.nom} augmentée de 2.")

class Debuff(Action):
    def executer(self):
        super().executer()
        self.cible.defense -= 2
        self.cible.etat = "Affaibli"  # ← etat au lieu de etats
        print(f"Défense de {self.cible.nom} diminuée de 2.")



def Fusions(heros_1, heros_2, equipe):
    if heros_1.peut_fusionner and heros_2.peut_fusionner:
        if heros_1.fusion_avec == heros_2.nom and heros_2.fusion_avec == heros_1.nom:
            nom_fusion = None
            if heros_1.nom == "Goku" or heros_1.nom == "Vegeta":
                nom_fusion = "Gogeta"
            elif heros_1.nom == "Trunks" or heros_1.nom == "Goten":
                nom_fusion = "Gotenks"

            fusion_data = None
            for i in hero_fusion:
                if i["nom"] == nom_fusion:
                    fusion_data = i
                    break

            if fusion_data is None:
                print("Fusion introuvable dans la database !")
                return None

            fusion_objet = Heros(
                fusion_data["nom"],
                fusion_data["description"],
                fusion_data["pv"],
                fusion_data["pv_max"],
                fusion_data["defense"],
                fusion_data["initiative"],
                fusion_data["degats"],
                fusion_data["typeDegats"],
                fusion_data["actions"],
                fusion_data["etat"],
                fusion_data["Carte"],
                fusion_data["arme"],
                heros_1.inventaire + heros_2.inventaire,
                False,
                None
            )

            equipe.remove(heros_1)
            equipe.remove(heros_2)
            equipe.append(fusion_objet)
            fusion_objet.pv=heros_1.pv+heros_2.pv

            print("FUUUUUUUUUUSION YAA!!!!!")
            print(fusion_objet.nom, "a rejoint l'équipe !")
        else:
            print(heros_1.nom, "et", heros_2.nom, "ne peuvent pas fusionner ensemble!")
    else:
        print("Ces personnages ne peuvent pas fusionner ensemble!")
        return None

def verifier_mort(personnage, equipe, morts, cartes):
    if personnage.pv <= 0:
        personnage.pv = 0
        personnage.etat = "mort"
        equipe.remove(personnage)
        morts.append(personnage)
        print(personnage.nom, "est mort !")
        cartes.append(personnage.carte)
        print("La boule", personnage.carte, "est sur le terrain !")


def ramasser_carte(joueur, cartes):
    if len(cartes) == 0:
        print("Aucune boule sur le terrain !")
    else:
        print("Boules disponibles :")
        for i in range(len(cartes)):
            print(i+1, "- Boule", cartes[i])
        choix = int(input("Quelle boule ramasser ? ")) - 1
        carte = cartes.pop(choix)
        joueur.inventaire.append("Boule " + str(carte))
        print(joueur.nom, "a ramassé la boule", carte)


def invoquer_shenron(heros, morts):
    print("\nLes 7 boules sont réunies !")
    print("Shenron, apparais !")
    if len(morts) == 0:
        print("Shenron : Il n'y a personne à ressusciter !")
    else:
        print("\nQui voulez-vous ressusciter ?")
        for i in range(len(morts)):
            print(i+1, "-", morts[i].nom)
        choix = int(input("Choix : ")) - 1
        ressuscite = morts[choix]
        ressuscite.pv = ressuscite.pv_max
        ressuscite.etat = "normal"
        heros.append(ressuscite)
        morts.remove(ressuscite)
        print(ressuscite.nom, "revient à la vie avec", ressuscite.pv, "PV !")
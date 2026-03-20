import random

def lancer_des(nombre, faces):
    total = 0
    for _ in range(nombre):
        total += random.randint(1, faces)
    return total

class Creature():
    
    def __init__(self, nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, Carte):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.pv_max = pv_max        
        self.defense = defense
        self.initiative_base = initiative
        self.degats = degats
        self.type_degat = typeDegats
        self.actions = actions
        self.etat = etat
        self.carte = Carte

    def lancer_initiative(self):
        resultat = random.randint(1, 20) + self.initiative_base
        print(self.nom, "lance l'initiative :", resultat)
        return resultat

    def afficher_actions(self):
        if self.actions:
            print("Actions de", self.nom)
            for action in self.actions:
                print("  -->", action)
        else:
            print(self.nom, "n'a aucune action disponible.")

    def afficher_caracteristiques(self):
        print("---", self.nom, "(", self.type_degat, ") ---")
        print("PV:", self.pv, "/", self.pv_max, "| Défense:", self.defense)
        print("Initiative:", self.initiative_base)
        print("Dégâts:", self.degats)
        print("État:", self.etat)
        print("Description:", self.description)

    def attaque(self, cible):
        jet = random.randint(1, 20)
        print("\nJet d'attaque :", jet)

        if jet == 1:
            print("Échec critique !")
            degats = lancer_des(self.degats[0], self.degats[1])
            self.pv -= degats
            print(self.nom, "se blesse de", degats)
            print("PV de", self.nom, ":", self.pv)
            return

        if jet == 20:
            print("Coup critique !")
            degats = lancer_des(self.degats[0], self.degats[1]) * 2
            print(self.nom, "inflige", degats, "dégâts critiques à", cible.nom)
        elif jet >= cible.defense:
            print("L'attaque touche !")
            degats = lancer_des(self.degats[0], self.degats[1])
            print(self.nom, "inflige", degats, "dégâts à", cible.nom)
        else:
            print("L'attaque rate !")
            return

        if hasattr(cible, "resistances") and self.type_degat in cible.resistances:
            print(cible.nom, "résiste au type", self.type_degat)
            degats //= 2

        cible.pv -= degats
        print("Dégâts infligés :", degats)
        print("PV de", cible.nom, ":", cible.pv)

        if cible.pv <= 0:
            cible.pv = 0
            cible.etat = "mort"


class Heros(Creature):

    def __init__(self, nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, Carte, arme, inventaire, peut_fusionner, fusion_avec):
        super().__init__(nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, Carte)
        self.arme = arme
        self.inventaire = inventaire
        self.peut_fusionner = peut_fusionner
        self.fusion_avec = fusion_avec

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        print("Arme :", self.arme)
        print("Inventaire :", len(self.inventaire), "objet(s)")


class Monstre(Creature):

    def __init__(self, nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, Carte, resistances):
        super().__init__(nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, Carte)
        self.resistances = resistances

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        if self.resistances:
            print("Résistances :")
            for resistance in self.resistances:
                print("  -", resistance)
        else:
            print("Résistances : Aucune")


class Action:
    def __init__(self, nom, lanceur, cible):
        self.nom = nom
        self.lanceur = lanceur
        self.cible = cible

    def executer(self):
        print("L'action", self.nom, "est lancée par", self.lanceur.nom, "sur", self.cible.nom)
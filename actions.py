import random

# Classe de base pour toutes les actions possibles dans le jeu
class Action:
    def __init__(self, nom_action, personnage_qui_lance, personnage_cible):
        self.nom = nom_action
        self.lanceur = personnage_qui_lance
        self.cible = personnage_cible
    def executer(self):
        print("Action : " + self.nom)
        print(self.lanceur.nom + " agit sur " + self.cible.nom)

# Classe pour gérer le soin, qui hérite des caractéristiques de la classe Action
class Soin(Action):
    def executer(self):
        super().executer() 
        montant_du_soin = random.randint(5, 15)
        self.cible.pv = self.cible.pv + montant_du_soin
        if self.cible.pv > self.cible.pv_max:
            self.cible.pv = self.cible.pv_max
        print("Soin effectuée. " + self.cible.nom + " a maintenant " + str(self.cible.pv) + " PV.")

# Classe pour gérer les améliorations, qui hérite aussi de la classe Action
class Buff(Action):
    def executer(self):
        super().executer()
        self.cible.defense = self.cible.defense + 2
        if "Booste" not in self.cible.etats:
            self.cible.etats.append("Booste") 
        print("Defense de " + self.cible.nom + " augmentee de 2.")

# Classe pour gérer les malus, qui hérite de la classe Action
class Debuff(Action):
    def executer(self):
        super().executer() 
        self.cible.defense = self.cible.defense - 2
        if "Affaibli" not in self.cible.etats:
            self.cible.etats.append("Affaibli")
        print("Defense de " + self.cible.nom + " diminuee de 2.")
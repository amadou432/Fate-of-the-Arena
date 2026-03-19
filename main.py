import random

heros = [
    {
        "nom": "Goku",
        "description": "Guerrier Saiyan légendaire, défenseur de la Terre aux pouvoirs infinis.",
        "pv": 500,
        "pv_max": 500,
        "defense": 20,
        "initiative": 22,
        "actions": ["Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": True,
        "fusion_avec": "Vegeta",
        "Carte": None
    
    },
    {
        "nom": "Gohan",
        "description": "Fils de Goku, demi-Saiyan au potentiel caché qui surpasse son père.",
        "pv": 420,
        "pv_max": 420,
        "defense": 18,
        "initiative": 19,
        "actions": ["Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 10),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": False,
        "Carte": None

    },
    {
        "nom": "Vegeta",
        "description": "Prince des Saiyans, rival éternel de Goku, fier guerrier d'élite.",
        "pv": 480,
        "pv_max": 480,
        "defense": 19,
        "initiative": 20,
        "actions": ["Final Flash"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": True,
        "fusion_avec": "Goku",
        "Carte": None

    },
    
    {
        "nom": "Trunks",
        "description": "Guerrier du futur, fils de Vegeta, porteur de l'épée légendaire.",
        "pv": 350,
        "pv_max": 350,
        "defense": 17,
        "initiative": 18,
        "actions": ["Final Flash"],
        "typeDegats": "tranchant",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": True,
        "fusion_avec": "Goten",
        "Carte": None
  
    },
    {
        "nom": "Goten",
        "description": "Fils cadet de Goku, prodige Saiyan et meilleur ami de Trunks.",
        "pv": 320,
        "pv_max": 320,
        "defense": 15,
        "initiative": 17,
        "actions": ["Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 10),
        "peut_fusionner": True,
        "partenaire_fusion": "Trunks",
        "arme": None,
        "inventaire": [],
        "peut_fusionner": True,
        "fusion_avec": "Trunks",
        "Carte": None

    },
    
    {
        "nom": "Krilin",
        "description": "Meilleur ami humain de Goku, maître du Destructo Disk et du Kamehameha.",
        "pv": 180,
        "pv_max": 180,
        "defense": 13,
        "initiative": 16,
        "actions": ["Destructo Disk"],
        "typeDegats": "tranchant",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 6),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": False,
        "Carte": None
 
    },
    {
        "nom": "Gotenks",
        "description": "Fusion légendaire de Trunks et Goten, puissance démultipliée et caractère imprévisible.",
        "pv": 620,        
        "pv_max": 620,        
        "defense":22,   
        "initiative": 21, 
        "actions": ["Kamehameha Jr"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (4, 12),            
        "arme": None,
        "inventaire": [],
        "peut_fusionner": False,
        "duree_fusion": 5             
    },
    {
        "nom": "Gogeta",
        "description": "Fusion parfaite de Goku et Vegeta par la danse de fusion, la plus puissante jamais vue.",
        "pv": 1280,
        "pv_max": 1280,
        "defense": 28,
        "initiative":  27,
        "actions": ["Big Bang Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (5, 12),
        "arme": None,
        "inventaire": [],
        "peut_fusionner": False,
        "duree_fusion": 5
}
]

mechants = [
    {
        "nom": "Broly",
        "description": "Saiyan légendaire à la puissance incontrôlable, destructor de planètes.",
        "pv": 600,
        "pv_max": 600,
        "defense": 18,
        "initiative": 14,
        "actions": ["Eraser Cannon"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (4, 12),
        "resistances": ["contondant", "tranchant", "percant"] 
    },
    {
        "nom": "Freezer",
        "description": "Empereur galactique tyrannique, destructeur de la planète Vegeta.",
        "pv": 520,
        "pv_max": 520,
        "defense": 10,
        "initiative": 18,
        "actions": ["Death Beam"],
        "typeDegats": "glace",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 12),
        "resistances": ["tranchant", "percant", "glace"]  
    },
    {
        "nom": "Cell",
        "description": "Androïde parfait créé par le Dr Gero, absorbeur de puissance.",
        "pv": 450,
        "pv_max": 450,
        "defense": 19,
        "initiative": 17,
        "actions": ["Kamehameha Solaire"],
        "typeDegats": "poison",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["poison", "feu"]  
    },
    {
        "nom": "Buu Majin",
        "description": "Créature magique antique à la régénération infinie et à la puissance absurde.",
        "pv": 700,
        "pv_max": 700,
        "defense": 15,
        "initiative": 12,
        "actions": ["Candy Beam"],
        "typeDegats": "magie",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (4, 10),
        "resistances": ["contondant", "tranchant", "percant", "feu"] 
    },
    
    {
        "nom": "Raditz",
        "description": "Frère aîné de Goku, premier ennemi Saiyan à menacer la Terre.",
        "pv": 220,
        "pv_max": 220,
        "defense": 14,
        "initiative": 15,
        "actions": ["Saturday Crush"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 8),
        "resistances": ["contondant"]  
    },
    {
    "nom": "Janemba",
    "description": "Démon né de l'énergie maléfique des enfers, capable de déformer la réalité.",
    "pv": 620,
    "pv_max": 620,
    "defense": 19,
    "initiative": 16,
    "actions": ["Dimension Sword"],
    "typeDegats": "magique",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (4, 12),
    "resistances": ["contondant", "tranchant", "magique"]
},
{
    "nom": "Cooler",
    "description": "Frère aîné de Freezer, plus froid et plus impitoyable, doté d'une forme finale terrifiante.",
    "pv": 540,
    "pv_max": 540,
    "defense": 21,
    "initiative": 19,
    "actions": ["Supernova de Cooler"],
    "typeDegats": "feu",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (4, 12),
    "resistances": ["tranchant", "percant", "glace"]
},
{
    "nom": "Zamatsu",
    "description": "Dieu Kaïo devenu immortel, convaincu que les mortels doivent être anéantis.",
    "pv": 700,
    "pv_max": 700,
    "defense": 23,
    "initiative": 18,
    "actions": ["Tranche Sainte"],
    "typeDegats": "magique",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (4, 12),
    "resistances": ["contondant", "tranchant", "percant", "feu"]
},
]

etats = [
    "normal",
    "empoisonné",#Lorsqu'il subit des dégats de poison
    "saigne",#Lorsqu'il subit des dégats tranchant
    "étourdi",#Lorsqu'il subit des dégats contondant
    "brûlé",#Lorsqu'il subit des dégats de feu
    "paralysé",#Lorsqu'il subit des dégats perçant
    "Boosté"
    "Affaibli"
    "mort"
]

types_degats = [
    "contondant",
    "tranchant",
    "perçant",
    "feu",
    "poison",
    
]

armes = [
    "Épée de Trunks",        #Fais des attaques de type tranchant
    "Bâton Magique de Goku",  #Fais des attaques de type contontant
    "Destructo Disk",         #Fais des attaques de type perçant
    "Queue Saiyan",           #Fais des attaques de type contondant
    "Gants empoisonnés",      #Fais des attaques de type poison
    "Souffle de Freezer"      #Fais des attaques de type feu
]

class Creature():
    
    def __init__(self, nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, tours_etat, peut_fusionner, Carte):
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
        self.tours_etat = tours_etat
        self.peut_fusionner = peut_fusionner
        self.carte = Carte

    def lancer_initiative(self):

        resultat = random.randint(1, 20) + self.initiative_base
        print(f"{self.nom} lance l'initiative : {resultat}")
        return resultat

    def afficher_actions(self):
        if self.actions:
            print(f"Actions de {self.nom} :") 
            for action in self.actions:
                print(f"  --> {action}")
        else:
            print(f"{self.nom} n'a aucune action disponible.")

    def afficher_caracteristiques(self):#Demander au profs quels sont les caractéristiques qu'on doit afficher 
        print(f"--- {self.nom} ({self.type_degat}) ---")
        print(f"PV: {self.pv} | Défense: {self.defense}")
        print(f"Description: {self.description}")
    
    def attaque(self, cible):
        jet = random.randint(1,20)
        print("Jet d'attaque :", jet)
        print(f"{self.nom} attaque {cible.nom} et inflige {self.degats} dégâts ({self.type_degats}) !")

        if jet == 1:
             print("Echec critique !")
             degats_infli = lancer_des(self.nb_des, self.faces)
             self.pv -= degats_infli
             print(self.nom, "se blesse de", degats_infli)
             return
        if jet >= cible.defense:
             degats = lancer_des(self.nb_des, self.faces)
             if jet == 20:
                print("Coup critique !")
                degats = 2
                print("L'attaque touche")
        else: 
             print("L'attaque rate")
             return
        if hasattr(cible, "resistances") and self.type_degats in cible.resistances:
             print(cible.nom, "résiste au type", self.type_degats)
             degats //= 2
        if hasattr(cible, "faiblesses") and self.type_degats in cible.faiblesses:
             print(cible.nom, "est faible contre", self.type_degats)
             degats= 2
        cible.pv -= degats
        print("Degats infligés :", degats)
        print(cible.nom, "PV restant :", cible.pv)

class heros(Creature):#A modifier les classes s'ecrivent toujours en majuscules
            
            def __init__(self, nom, description, pv, defense, initiative_base, degat, type_degat, arme,inventaire):
                super().__init__(nom, description, pv, defense, initiative_base, degat, type_degat)
                self.arme = arme
                self.inventaire = inventaire

            def afficher_caracteristiques(self):
             super().afficher_caracteristiques()
             print(f"Arme : {self.arme} | Inventaire : {len(self.inventaire)} objets")

class mechants(Creature):#A modifier les classes s'ecrivent toujours en majuscules
    def __init__(self, nom, description, pv, defense, initiative_base, degat, type_degat):
        super().__init__(nom, description, pv, defense, initiative_base, degat, type_degat)
        self.resistances = []

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        if self.resistances:
            print("Résistances :")
            for resistance in self.resistances:
                print(f"  - {resistance}")
        else:
            print("Résistances : Aucune")

class Action:
            def __init__(self, nom, lanceur, cible):
                self.nom = nom
                self.lanceur = lanceur
                self.cible = cible

            def executer(self):
             print(f"L'action {self.nom} est lancée par {self.lanceur.nom} sur {self.cible.nom} !")

class Soin(Action):  # Haricot magique
    def executer(self):
        super().executer()
        self.cible.pv = self.cible.pv_max  
        print(f"{self.cible.nom} a mangé un haricot magique et récupère tous ses PV ({self.cible.pv_max} PV) !")# faire de tels sorte que lorsquon donne un haricot magique a son coequipier , que la phrase change .

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


def lancer_des(nombre, faces):
    total = 0
    for _ in range(nombre):
        total += random.randint(1, faces)
    return total

def Attaque_classique(attaquant, cible,jet):
    print(attaquant['nom']," attaque ",cible['nom'])
    print(f"Jet du dé : {jet}")

    if jet==20:
        print("Attaque critique!")
        nombre_des = attaquant["degats"][0]  
        faces_des  = attaquant["degats"][1]
        degats = lancer_des(nombre_des, faces_des) * 2
        cible["pv"] = cible["pv"] - degats
        
        print("Dégâts infligés :", degats)
        print("PV restants de ",cible['nom'] ," : ",cible['pv'])
    elif jet==1:
        print("Echec critique!")
        nombre_des = attaquant["degats"][0]  
        faces_des  = attaquant["degats"][1]
        degats = lancer_des(nombre_des, faces_des) 
        attaquant["pv"] = attaquant["pv"] - degats
        
        print("Dégâts infligés :", degats)
        print("PV restants de ",attaquant['nom'] ," : ",attaquant['pv'])
    elif jet > cible["defense"]:
        print("L'attaque touche !")
        nombre_des = attaquant["degats"][0]  
        faces_des  = attaquant["degats"][1]
        degats = lancer_des(nombre_des, faces_des)
        cible["pv"] = cible["pv"] - degats
        
        print("Dégâts infligés :", degats)
        print("PV restants de ",cible['nom'] ," : ",cible['pv'])

        if cible["pv"] <= 0:
            cible["pv"] = 0
            cible["etat"] = "mort"#pk pas l'enlever et appeler la fonction verifier_mort
            print(cible['nom'] ," est mort !")
    else:
        print("L'attaque échoue.")

def Attaque_tranchant(attaquant,cible,jet):
    if jet > cible["defense"]:
        print("Attaque Tranchant!")
        print(f"Jet du dé : {jet}")
        nombre_des = attaquant["degats"][0]  
        faces_des  = attaquant["degats"][1]
        degats = lancer_des(nombre_des, faces_des) 
        if "tranchant" in cible["resistances"]:
            cible["pv"] = cible["pv"] - degats
            
            print("Dégâts infligés :", degats)
            print("PV restants de ",cible['nom'] ," : ",cible['pv'])
        else:
            degats = lancer_des(nombre_des, faces_des) // 2
                
            cible["pv"] = cible["pv"] - degats
                
            print("Dégâts infligés :", degats)
            print("PV restants de ",cible['nom'] ," : ",cible['pv'])
            
            if cible["pv"]<=0:
                print(cible['nom']," est mort")
    else:
        print("L'attaque échoue.")

def Creer_equipe(liste_source, est_heros):
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

def Fusions(heros_1, heros_2,equipe):
    if heros_1["peut_fusionner"] and heros_2["peut_fusionner"]:
        if heros_1["fusion_avec"] == heros_2["nom"] and heros_2["fusion_avec"] == heros_1["nom"]:
            nom_fusion = None
            if heros_1["nom"] == "Goku" or heros_1["nom"] == "Vegeta":
                nom_fusion = "Gogeta"
            elif heros_1["nom"] == "Trunks" or heros_1["nom"] == "Goten":
                nom_fusion = "Gotenks"
            
            fusion=None
            for i in heros:
                if i["nom"] == nom_fusion:
                    fusion = i
                    break
            
            if fusion is None:
                print(f"Fusion introuvable dans la database. Vérifie les noms !")
                return None
 
            equipe.remove(heros_1)
            equipe.remove(heros_2)
            equipe.append(fusion)
            print("FUUUUUUUUUUSION YAA!!!!!")
            print(f"{fusion['nom']} a rejoint l'équipe !")
            fusion["inventaire"].append( heros_1["inventaire"])
            fusion["inventaire"].append( heros_2["inventaire"])
        else:
            print(f"{heros_1["nom"]} et {heros_2["nom"]} ne peuvent pas fusionner ensemble! ")
    else:
        print("Ses personnages ne peuvent pas fusionner ensemble!")
        return None    
 
def verifier_mort(hero,equipe):
    if  hero["pv"] >= 0:
        hero["pv"] = 0
        hero["etat"] = "mort"
        hero["carte"] = 7     
        equipe.remove(hero)
        print(f"{hero["nom"] }est mort et a laissé les boules de cristalles sur le terrain.")

def creer_equipe():
    print("hello world")

def lancer_jeu():
    """Fonction principale de ton interface de combat."""
    print("")
    print(" >>>  BIENVENUE DANS FATE OF THE ARENA 🐉 <<< ")
    print(" Note : PV = Points de Vie (la santé de vos guerriers) ")
    print("")

   
    camp_gentils = creer_equipe(heros, True)
    camp_mechants = creer_equipe(mechants, False)

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
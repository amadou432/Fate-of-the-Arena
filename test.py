import random
def lancer_des(nombre, faces):
    total = 0
    for _ in range(nombre):
        total += random.randint(1, faces)
    return total


class Creature():
    
    def __init__(self, nom, description, pv, pv_max, defense, initiative, degats, typeDegats, actions, etat, tours_etat, resistances, peut_fusionner, Carte):
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
        self.resistances = resistances
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
   

# heros = [
#     {
#         "nom": "Goku",
#         "description": "Guerrier Saiyan légendaire, défenseur de la Terre aux pouvoirs infinis.",
#         "pv": 500,
#         "defense": 20,
#         "initiative": 22,
#         "actions": ["Kamehameha"],
#         "typeDegats": "foudre",
#         "etat": "normal",
#         "tours_etat": 0,
#         "degats": (3, 10),
#         "resistances": ["contondant"],
#         "peut_fusionner": True,
#         "Carte": None

#     },
#     {
#        "nom": "Broly",
#         "description": "Saiyan légendaire à la puissance incontrôlable, destructor de planètes.",
#         "pv": 600,
#         "defense": 18,
#         "initiative": 14,
#         "actions": ["Eraser Cannon"],
#         "typeDegats": "foudre",
#         "etat": "normal",
#         "tours_etat": 0,
#         "degats": (4, 12),
#         "resistances": ["contondant", "tranchant", "percant"] 
    
#     }
# ]

# joueur_1 = Creature(**heros[0])
# joueur_2 = Creature(**heros[1])

 
# print(joueur_1.nom)
# joueur_1.lancer_initiative()
# joueur_1.afficher_actions()
# joueur_1.afficher_caracteristiques()
# joueur_1.attaque(joueur_2)

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
        "resistances": ["contondant"],#Demander au prof si les heros peuvent avoir une liste de résistances eux aussi 
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
        "resistances": ["contondant"],
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
        "resistances": ["contondant", "tranchant"],
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
        "resistances": ["contondant", "tranchant"],
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
        "resistances": ["contondant"],
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
        "resistances": [] ,
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
        "resistances": ["contondant", "tranchant"],
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
        "resistances": ["contondant", "tranchant", "magique"],
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
    }
    ]

joueur_1 = heros[0]
joueur_2 = heros[1]
joueur_3 = heros[2]
equipe = [
    joueur_1,
    joueur_2,
    joueur_3
    ]

for i in equipe:
    print(i["nom"])
    print(i["pv"])

Fusions(joueur_1 , joueur_3, equipe)

for i in equipe:
    print(i["nom"])
    print(i["pv"])

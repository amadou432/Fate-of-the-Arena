import random

heros = [
    {
        "nom": "Goku",
        "description": "Guerrier Saiyan légendaire, défenseur de la Terre aux pouvoirs infinis.",
        "pv": 500,
        "defense": 20,
        "initiative": 22,
        "actions": ["Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["contondant"],
        "peut_fusionner": True,
        "Carte": None

    },
    {
        "nom": "Gohan",
        "description": "Fils de Goku, demi-Saiyan au potentiel caché qui surpasse son père.",
        "pv": 420,
        "defense": 18,
        "initiative": 19,
        "actions": ["Kamehameha"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 10),
        "resistances": ["contondant"],
        "peut_fusionner": False,
        "Carte": None

    },
    {
        "nom": "Vegeta",
        "description": "Prince des Saiyans, rival éternel de Goku, fier guerrier d'élite.",
        "pv": 480,
        "defense": 19,
        "initiative": 20,
        "actions": ["Final Flash"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["contondant", "tranchant"]  ,
        "peut_fusionner": True,
        "Carte": None

    },
    
    {
        "nom": "Trunks",
        "description": "Guerrier du futur, fils de Vegeta, porteur de l'épée légendaire.",
        "pv": 350,
        "defense": 17,
        "initiative": 18,
        "actions": ["Final Flash"],
        "typeDegats": "tranchant",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["contondant", "tranchant"],
        "peut_fusionner": True,
        "Carte": None
  
    },
    {
        "nom": "Goten",
        "description": "Fils cadet de Goku, prodige Saiyan et meilleur ami de Trunks.",
        "pv": 320,
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
        "peut_fusionner": True,
        "Carte": None

    },
    
    {
        "nom": "Krilin",
        "description": "Meilleur ami humain de Goku, maître du Destructo Disk et du Kamehameha.",
        "pv": 180,
        "defense": 13,
        "initiative": 16,
        "actions": ["Destructo Disk"],
        "typeDegats": "tranchant",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 6),
        "resistances": [] ,
        "peut_fusionner": False,
        "Carte": None
 
    },
    {
    "nom": "Gotenks",
    "description": "Fusion légendaire de Trunks et Goten, puissance démultipliée et caractère imprévisible.",
    "pv": 620,        
    "defense":22,   
    "initiative": 21, 
    "actions": ["Kamehameha Jr"],
    "typeDegats": "foudre",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (4, 12),            
    "resistances": ["contondant", "tranchant"],
    "peut_fusionner": False,
    "duree_fusion": 5             
    },
    {
    "nom": "Gogeta",
    "description": "Fusion parfaite de Goku et Vegeta par la danse de fusion, la plus puissante jamais vue.",
    "pv": 500 + 480 + 300,
    "defense": max(20, 19) + 8,
    "initiative": max(22, 20) + 5,
    "actions": ["Big Bang Kamehameha"],
    "typeDegats": "foudre",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (5, 12),
    "resistances": ["contondant", "tranchant", "magique"],
    "peut_fusionner": False,
    "duree_fusion": 5
}
]

mechants = [
    {
        "nom": "Broly",
        "description": "Saiyan légendaire à la puissance incontrôlable, destructor de planètes.",
        "pv": 600,
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
    "empoisonné",
    "étourdi",
    "brûlé",
    "paralysé",
    "bouclier",
    "mort"
]

types_degats = [
    "contondant",
    "tranchant",
    "perçant",
    "feu",
    "poison",
    "magique"
]

armes = [
    "Épée de Trunks",        #Fais des attaques de type tranchant
    "Bâton Magique de Goku",  #Fais des attaques de type contontant
    "Destructo Disk",         #Fais des attaques de type perçant
    "Queue Saiyan",           #Fais des attaques de type contondant
    "Gants empoisonnés",      #Fais des attaques de type poison
    "Souffle de Freezer"      #Fais des attaques de type feu
]

class Creature:
    def __init__(self, nom, description, pv, pv_max , defense, initiative_base, degat, type_degat):
        self.nom = nom
        self.description = description
        self.pv = pv
        self.pv_max = pv_max
        self.defense = defense
        self.initiative_base = initiative_base
        self.degat = degat
        self.type_degat = type_degat
        self.actions = []
        self.etats = []

    def lancer_initiative(self):

        resultat = random.randint(1, 20) + self.initiative_base
        print(f"{self.nom} lance l'initiative : {resultat}")
        return resultat

    def afficher_actions(self):
        print(f"Actions de {self.nom} : {', '.join([a.nom for a in self.actions]) if self.actions else 'Aucune'}")

    def afficher_caracteristiques(self):
        print(f"--- {self.nom} ({self.type_degat}) ---")
        print(f"PV: {self.pv} | CA: {self.defense}")
        print(f"Description: {self.description}")

    def attaque(self, cible):
        print(f"{self.nom} attaque {cible.nom} et inflige {self.degat} dégâts ({self.type_degat}) !")
        cible.pv -= self.degat
        
class heros(Creature):
            
            def __init__(self, nom, description, pv, defense, initiative_base, degat, type_degat, arme):
                super().__init__(nom, description, pv, defense, initiative_base, degat, type_degat)
                self.arme = arme
                self.inventaire = []

            def afficher_caracteristiques(self):
             super().afficher_caracteristiques()
             print(f"Arme : {self.arme} | Inventaire : {len(self.inventaire)} objets")

class mechants(Creature):
    def __init__(self, nom, description, pv, defense, initiative_base, degat, type_degat):
        super().__init__(nom, description, pv, defense, initiative_base, degat, type_degat)
        self.resistances = []

    def afficher_caracteristiques(self):
        super().afficher_caracteristiques()
        print(f"Résistances : {', '.join(self.resistances) if self.resistances else 'Aucune'}")

class Action:
            def __init__(self, nom, lanceur, cible):
                self.nom = nom
                self.lanceur = lanceur
                self.cible = cible

            def executer(self):
             print(f"L'action {self.nom} est lancée par {self.lanceur.nom} sur {self.cible.nom} !")

# Classe pour gérer le soin, qui hérite des caractéristiques de la classe Action
class Soin(Action):#Aricot magique
    def executer(self):
        super().executer() 
        montant_du_soin = random.randint(5, 15)
        self.cible.pv = self.cible.pv + montant_du_soin
        if self.cible.pv > self.cible.pv_max:
            self.cible.pv = self.cible.pv_max
        print("Aricot magique mangé. " + self.cible.nom + " a maintenant " + str(self.cible.pv) + " PV.")

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


def lancer_des(nombre, faces):
    total = 0
    for _ in range(nombre):
        total += random.randint(1, faces)
    return total

def attaque_classique(attaquant, cible,jet):
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
            cible["etat"] = "mort"
            print(cible['nom'] ," est mort !")
    else:
        print("L'attaque échoue.")

def attaque_tranchant(attaquant,cible,jet):
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
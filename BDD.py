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
        "resistances": ["contondant"]
    },
    {
        "nom": "Gohan",
        "description": "Fils de Goku, demi-Saiyan au potentiel caché qui surpasse son père.",
        "pv": 420,
        "defense": 18,
        "initiative": 19,
        "actions": ["Masenko"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 10),
        "resistances": ["contondant"]
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
        "resistances": ["contondant", "tranchant"]  
    },
    {
        "nom": "Piccolo",
        "description": "Namekien stratège et mentor de Gohan, guerrier sage aux bras extensibles.",
        "pv": 300,
        "defense": 16,
        "initiative": 15,
        "actions": ["Canon Makankosappo"],
        "typeDegats": "magie",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 8),
        "resistances": ["poison", "magie"]  
    },
    {
        "nom": "Trunks",
        "description": "Guerrier du futur, fils de Vegeta, porteur de l'épée légendaire.",
        "pv": 350,
        "defense": 17,
        "initiative": 18,
        "actions": ["Burning Attack"],
        "typeDegats": "tranchant",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["contondant", "tranchant"]  
    },
    {
        "nom": "Goten",
        "description": "Fils cadet de Goku, prodige Saiyan et meilleur ami de Trunks.",
        "pv": 320,
        "defense": 15,
        "initiative": 17,
        "actions": ["Kamehameha Jr", "Frappe Ki"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (2, 10),
        "resistances": ["contondant"],
        "peut_fusionner": True,
        "partenaire_fusion": "Trunks"
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
        "resistances": []  
    },
    {
    "nom": "Gotenks",
    "description": "Fusion légendaire de Trunks et Goten, puissance démultipliée et caractère imprévisible.",
    "pv": 350 + 320 + 200,        
    "defense": max(17, 15) + 5,   
    "initiative": max(18, 17) + 3, 
    "actions": ["Kamehameha Jr"],
    "typeDegats": "foudre",
    "etat": "normal",
    "tours_etat": 0,
    "degats": (4, 12),            
    "resistances": ["contondant", "tranchant"],  
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
        "nom": "Vegeta (Saiyan Saga)",
        "description": "Prince des Saiyans dans sa forme la plus arrogante et impitoyable.",
        "pv": 400,
        "defense": 18,
        "initiative": 19,
        "actions": ["Galick Gun"],
        "typeDegats": "foudre",
        "etat": "normal",
        "tours_etat": 0,
        "degats": (3, 10),
        "resistances": ["contondant"]  
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
]
armes = [
    "Épée de Trunks",
    "Bâton Magique de Goku",
    "Destructo Disk",
    "Bâton de Piccolo",
    "Épée de Gohan",
    "Queue Saiyan",
    "Ceinture lestée de Goku"
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
    "Antennes de Piccolo",    #Fais des attaques de type magique
    "Queue Saiyan",           #Fais des attaques de type contondant
    "Gants empoisonnés",      #Fais des attaques de type poison
    "Souffle de Freezer"      #Fais des attaques de type feu
]

nbr_de=0

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

jet=lancer_des(1,20)
print(jet)
attaque_tranchant(heros[1],mechants[1],jet)
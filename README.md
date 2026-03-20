# ⚔️ Fate of the Arena — Système de combat RPG (DBZ)

Projet Python REPL de combat au tour par tour dans l'univers Dragon Ball Z, réalisé dans le cadre du cours POO Advanced 2.

---

## 📋 Prérequis

- Python 3.8 ou supérieur
- Aucune bibliothèque externe requise (uniquement `random`, inclus dans la librairie standard Python)

---

## 🚀 Lancer le jeu

```bash
python main.py
```

---

## 📂 Structure du projet

```
├── main.py        # Point d'entrée, boucle de jeu et gestion du combat
├── Creature.py    # Classes Creature, Heros, Monstre et Action
├── actions.py     # Sous-classes d'actions : Soin, Buff, Debuff, Fusions, utilitaires
├── BDD.py         # Base de données : héros, monstres, fusions, armes
└── README.md
```

---

## 🎮 Déroulement du jeu

1. Sélection des héros parmi une liste de personnages DBZ
2. Choix d'une arme pour chaque héros
3. Constitution de l'inventaire de départ (3 objets par héros)
4. Sélection des monstres adversaires
5. Lancer de l'initiative pour déterminer l'ordre de jeu
6. Combat au tour par tour jusqu'à la victoire ou la défaite

---

## 🧑‍💻 Concepts POO utilisés

- **Classes** : `Creature`, `Heros`, `Monstre`, `Action`
- **Héritage** : `Heros` et `Monstre` héritent de `Creature` ; `Soin`, `Buff`, `Debuff` héritent de `Action`
- **Polymorphisme** : `afficher_caracteristiques()` et `executer()` sont surchargées dans les sous-classes
- **Attributs et méthodes** : chaque classe possède ses propres attributs spécifiques et méthodes

---

## ✨ Fonctionnalités supplémentaires

### 🔀 Système de Fusion
Certains héros peuvent fusionner ensemble pendant le combat pour former un personnage encore plus puissant :
- **Goku + Vegeta → Gogeta** (1280 PV, dégâts 5d12)
- **Trunks + Goten → Gotenks** (620 PV, dégâts 4d12)

Pour fusionner, choisir l'option `5 - FUSION!` pendant le tour d'un héros compatible. Les PV actuels des deux personnages sont additionnés dans le fusionné, et leurs inventaires sont combinés.

### 🐉 Dragon Balls & Shenron
Chaque monstre porte une boule de cristal (`Carte`). À sa mort, la boule tombe sur le terrain. Les héros peuvent :
- **Ramasser une boule** (option 4) pendant leur tour
- **Invoquer Shenron** une fois les 7 boules réunies pour **ressusciter un héros mort**

### 🎒 Inventaire et objets
À la préparation du combat, chaque héros choisit 3 objets parmi :
- **Haricot Magique** — restaure tous les PV
- **Potion** — restaure 50 PV
- **Anti-para** — soigne un état négatif (empoisonné, paralysé...)
- **Queue de phénix** — (réservé pour extension future)

### 💪 Magie (Buff / Debuff / Soin)
Les héros ont accès à des actions magiques en combat :
- **Soin** : récupère 50 PV
- **Buff** : augmente la défense de +2 et passe en état "Boosté"
- **Debuff** : réduit la défense d'un ennemi de -2 et le passe en état "Affaibli"

---

## ⚙️ Règles de combat

- **Attaque** : jet 1d20. Si le résultat ≥ défense de la cible → l'attaque touche
- **Critique réussi (20)** : dégâts doublés
- **Échec critique (1)** : le lanceur s'inflige les dégâts à lui-même
- **Résistances** : si le type de dégâts correspond à une résistance de la cible, les dégâts sont divisés par 2
- **Initiative** : jet 1d20 + bonus d'initiative de la créature

---

## 👥 Personnages disponibles

| Héros | PV | Dégâts | Type |
|---|---|---|---|
| Goku | 500 | 3d10 | Foudre |
| Vegeta | 480 | 3d10 | Foudre |
| Trunks | 350 | 3d10 | Tranchant |
| Goten | 320 | 2d10 | Foudre |
| Gohan | 420 | 2d10 | Foudre |
| Krilin | 180 | 2d6 | Tranchant |

| Monstre | PV | Résistances |
|---|---|---|
| Broly | 600 | Contondant, Tranchant, Perçant |
| Freezer | 520 | Tranchant, Perçant, Glace |
| Cell | 450 | Poison, Feu |
| Buu Majin | 700 | Contondant, Tranchant, Perçant, Feu |
| Zamasu | 700 | Contondant, Tranchant, Perçant, Feu |
| Janemba | 620 | Contondant, Tranchant, Magique |
| Cooler | 540 | Tranchant, Perçant, Glace |
| Raditz | 220 | Contondant |

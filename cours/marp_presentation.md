---
# Les Fondamentaux de l'Algorithmique et de Python 🐍
## Introduction à la pensée algorithmique et au langage Python

Antoine Oberlaender

---
# Pourquoi l'Algorithmique et Python ?

* Planifier avant d'agir, comme construire une cabane ou organiser un voyage.
* L'algorithmique : Instructions claires et ordonnées pour résoudre un problème.
* Python : Le langage pour traduire ces instructions en actions pour l'ordinateur.

---
# Sommaire

* Introduction à l'Algorithmique
* Bases de Python
* Structures de Données Fondamentales en Python
* Fonctions
* Programmation Orientée Objet (POO) en Python (Introduction)

---
# Qu'est-ce qu'un Algorithme ?

* Suite finie et non ambiguë d'instructions.
* **Exemple : Traverser une route**
    1. S'approcher du bord du trottoir.
    2. Regarder à gauche.
    3. Si une voiture arrive, attendre. Sinon, continuer.
    4. Regarder à droite.
    5. Si une voiture arrive, attendre. Sinon, continuer.
    6. Si la voie est libre des deux côtés, traverser.
---
# Qu'est-ce qu'un Algorithme ?

* Suite finie et non ambiguë d'instructions.
* **Exemple : Traverser une route**
    1. S'approcher du bord du trottoir.
    2. Regarder à gauche.
    3. Si une voiture arrive, attendre. Sinon, continuer.
    4. Regarder à droite.
    5. Si une voiture arrive, attendre. Sinon, continuer.
    6. Si la voie est libre des deux côtés, traverser.

---
# La Pensée Algorithmique

* **Titre :** Décomposer pour résoudre
* Décomposer un problème complexe en sous-problèmes plus petits.
* **Exemple : Organiser un voyage Paris-Rome**
    1. Choisir les dates.
    2. Définir le budget.
    3. Réserver le transport.
    4. Réserver l'hébergement.
    5. Planifier les activités.
    6. Préparer les valises.

---
# La Pensée Algorithmique

* **Titre :** Décomposer pour résoudre
* Décomposer un problème complexe en sous-problèmes plus petits.
* **Exemple : Faire une tasse de thé**
    1. Prendre une bouilloire.
    2. Remplir la bouilloire d'eau.
    3. Mettre la bouilloire à chauffer.
    4. ... (Etc.)

---
# Pseudo-code et Organigrammes

* **Pseudo-code :** Description d'un algorithme en langage simple.
* **Organigramme :** Représentation graphique avec symboles standardisés.
* **Exemple : Jeu du "plus ou moins"**
    * **Pseudo-code :**
        ```
        NOMBRE_SECRET = Choisir un nombre aléatoire entre 1 et 100
        TANT QUE (pas trouvé)
            LIRE proposition_joueur
            SI proposition_joueur < NOMBRE_SECRET ALORS
                AFFICHER "C'est plus !"
            SINOSI proposition_joueur > NOMBRE_SECRET ALORS
                AFFICHER "C'est moins !"
            SINOS
                AFFICHER "Bravo, vous avez trouvé !"
        FIN TANT QUE
        ```

---
# Bases de Python

* Python : Langage pour traduire les algorithmes en instructions exécutables.
* **Variables et types de données :**
    * `age = 30` (entier)
    * `prix_baguette = 1.10` (flottant)
    * `nom_utilisateur = "Alice"` (chaîne)
    * `est_traitee = True` (booléen)
* **Opérateurs :** +, -, \*, /, ==, !=, >, <, and, or, not

---
# Exemple Python : Opérateurs

```python
a = 10
b = 5
somme = a + b  # somme vaut 15
est_plus_grand = a > b  # est_plus_grand vaut True
peut_sortir = (temperature > 15) and (not pleut) 
```

-----

# Exemple Python : Entrées et sorties

``` python
nom = input("Quel est votre nom ? ")
print("Bonjour, " + nom + " !") 
```

-----

# Structures de Données Fondamentales en Python

- **Listes :** Collection ordonnée et modifiable.
    - \`courses = \["pommes", "bananes", "lait"\]\`
- **Tuples :** Collection ordonnée et non modifiable.
    - \`point = (10, 20)\`
- **Dictionnaires :** Paires clé-valeur.
    - \`contact = {"nom": "Dupont", "prenom": "Jean"}\`
- **Ensembles :** Éléments uniques.
    - \`ingredients = {"farine", "sucre", "oeufs"}\`

-----

# Exemple Python : Listes

``` python
courses = ["pommes", "bananes", "lait"]
print(courses)  # Affiche "pommes"
courses.append("pain")  # Ajoute "pain" à la end 
```

-----

# Exemple Python : Dictionnaires

``` python
contact = {
    "nom": "Dupont",
    "prenom": "Jean",
    "telephone": "0123456789"
}
print(contact["prenom"])  # Affiche "Jean" 
```

-----

# Fonctions

- Blocs de code réutilisables.
- **Exemple Python :**
  ``` python
  def saluer(nom):
      print("Bonjour, " + nom + " !")
  
  saluer("Alice")  # Affiche "Bonjour, Alice !" 
  ```
- **Valeurs de retour :**
  ``` python
  def additionner(a, b):
      return a + b
  
  somme = additionner(5, 3)  # somme vaut 8 
  ```

-----

# Programmation Orientée Objet (POO)

- Organisation du code autour d'"objets".
- **Concepts clés :**
    - **Classe :** Un plan pour créer des objets.
    - **Objet :** Une instance spécifique d'une classe.
    - **Attributs :** Données associées à un objet.
    - **Méthodes :** Fonctions associées à un objet.
- **Exemple : Classe Chien** (voir le document pour le code complet)

-----

# Exemple Python : Classe Chien

``` python
class Chien:
    def __init__(self, nom, race):
        self.nom = nom
        self.race = race

    def aboyer(self):
        return f"{self.nom} dit: Woof!"

mon_chien = Chien("Médor", "Labrador")
print(mon_chien.aboyer())  # Affiche "Médor dit: Woof!" 
```

-----

# Suite

- Pratiquer avec les exercices du document.
- Explorer davantage Python et la POO.
- Construire des projets pour mettre en pratique.

-----
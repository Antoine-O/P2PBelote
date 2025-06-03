# Les Fondamentaux de l'Algorithmique et de Python 🐍

Imaginez que vous voulez construire quelque chose de complexe, comme une superbe cabane dans les arbres ou organiser un grand voyage. Avant de commencer à clouer des planches ou à réserver des billets, vous avez besoin d'un plan, d'instructions claires. C'est là qu'interviennent l'algorithmique et la programmation.
-----

# **Sommaire**

[**Sommaire **](#sommaire)

[**Introduction à l'Algorithmique **](#introduction-à-lalgorithmique)

[Qu'est-ce qu'un algorithme ?](#quest-ce-quun-algorithme-)

[La Pensée algorithmique](#la-pensée-algorithmique)

[Pseudo-code et organigrammes](#pseudo-code-et-organigrammes)

[Complexité algorithmique (introduction simple : O(n), O(n²))](#complexité-algorithmique-introduction-simple--on-on)

[**Bases de Python **](#bases-de-python)

[Installation de Python et d'un IDE (VS Code, PyCharm Community)](#installation-de-python-et-dun-ide-vs-code-pycharm-community)

[Variables, types de données (entiers, flottants, chaînes, booléens)](#variables-types-de-données-entiers-flottants-chaînes-booléens)

[Exemple en Python](#exemple-en-python)

[Opérateurs (arithmétiques, de comparaison, logiques)](#opérateurs-arithmétiques-de-comparaison-logiques)

[Exemple en Python](#exemple-en-python-1)

[Entrées et sorties (input(), print())](#entrées-et-sorties-input-print)

[Exemple en Python](#exemple-en-python-2)

[Exemple en Python](#exemple-en-python-3)

[Mini-projet 1 : Calculatrice simple, jeu du "plus ou moins".](#mini-projet-1--calculatrice-simple-jeu-du-plus-ou-moins)

[**Structures de Données Fondamentales en Python **](#structures-de-données-fondamentales-en-python)

[Listes (création, accès, modification, méthodes courantes)](#listes-création-accès-modification-méthodes-courantes)

[Exemple en Python](#exemple-en-python-4)

[Tuples (immutabilité, cas d'usage)](#tuples-immutabilité-cas-dusage)

[Exemple en Python](#exemple-en-python-5)

[Dictionnaires (clés-valeurs, accès, modification)](#dictionnaires-clés-valeurs-accès-modification)

[Exemple en Python](#exemple-en-python-6)

[Ensembles (sets) (unicité, opérations d'ensemble)](#ensembles-sets-unicité-opérations-densemble)

[Exemple en Python](#exemple-en-python-7)

[Exercices](#exercices)

[**Fonctions **](#fonctions)

[Exemple en Python](#exemple-en-python-8)

[Paramètres et arguments](#paramètres-et-arguments)

[Exemple en Python](#exemple-en-python-9)

[Valeurs de retour (return)](#valeurs-de-retour-return)

[Exemple en Python](#exemple-en-python-10)

[Portée des variables (locale, globale)](#portée-des-variables-locale-globale)

[Exemple en Python](#exemple-en-python-11)

[Fonctions anonymes (lambda)](#fonctions-anonymes-lambda)

[Exemple en Python](#exemple-en-python-12)

[Mini-projet 2 : Modularisation du mini-projet 1 avec des fonctions.](#mini-projet-2--modularisation-du-mini-projet-1-avec-des-fonctions)

[**Programmation Orientée Objet (POO) en Python (Introduction) **](#programmation-orientée-objet-poo-en-python-introduction)

[Concepts clés : classes, objets, attributs, méthodes](#concepts-clés--classes-objets-attributs-méthodes)

[Exemple en Python](#exemple-en-python-13)

[Constructeur (\_\_init\_\_)](#constructeur-__init__)

[Encapsulation, Héritage, Polymorphisme (concepts de base)](#encapsulation-héritage-polymorphisme-concepts-de-base)

[Polymorphisme](#polymorphisme)

[Exercices](#exercices-1)

# **Introduction à l'Algorithmique**

## **Qu'est-ce qu'un algorithme ?** 

Un algorithme est une suite finie et non ambiguë d'instructions ou d'opérations permettant de résoudre un problème spécifique ou d'atteindre un objectif donné.

- **Une recette** pour faire un gâteau est un algorithme. Elle liste les ingrédients (les entrées), les étapes précises à suivre dans un ordre spécifique (les instructions), et le résultat attendu est un délicieux gâteau (la sortie).

    - **Caractéristiques illustrées par la recette :**

* **Fini :** Une recette a un nombre défini d'étapes. Elle ne continue pas à l'infini.

* **Non ambigu :** Chaque étape doit être claire. "Ajouter un peu de farine" est ambigu ; "Ajouter 200g de farine" est précis.

* **Entrées :** Les ingrédients (farine, œufs, sucre).

* **Sorties :** Le gâteau.

* **Efficacité :** Une bonne recette permet de faire le gâteau sans gaspiller d'ingrédients ni de temps inutilement.

- **Exemple concret : Traverser une route en toute sécurité.**

1. S'approcher du bord du trottoir.

2. Regarder à gauche.

3. Si une voiture arrive, attendre. Sinon, continuer.

4. Regarder à droite.

5. Si une voiture arrive, attendre. Sinon, continuer.

6. Si la voie est libre des deux côtés, traverser.


## **La Pensée algorithmique**

C'est l'art de décomposer un problème complexe en sous-problèmes plus petits et plus faciles à gérer, puis de définir les étapes logiques pour résoudre chaque sous-problème.

- **Organiser un voyage.**

* Organiser un voyage Paris-Rome est un gros problème. La pensée algorithmique consiste à le décomposer :

1. Choisir les dates.

2. Définir le budget.

3. Réserver le transport (train ? avion ?).

4. Réserver l'hébergement.

5. Planifier les activités sur place.

6. Préparer les valises.

- Chacune de ces étapes peut elle-même être décomposée. Par exemple, "Réserver le transport" implique de comparer les prix, vérifier les horaires, effectuer le paiement.

* **Exemple concret : Faire une tasse de thé.**

- Problème : Je veux une tasse de thé.

- Décomposition et étapes logiques :

1. Prendre une bouilloire.

2. Remplir la bouilloire d'eau.

3. Mettre la bouilloire à chauffer.

4. Prendre une tasse.

5. Mettre un sachet de thé dans la tasse.

6. Attendre que l'eau bout.

7. Verser l'eau chaude dans la tasse.

8. Attendre quelques minutes pour l'infusion.

9. Retirer le sachet de thé.

10. (Optionnel) Ajouter du sucre ou du lait.


-----

## **Pseudo-code et organigrammes**

**Pseudo-code :** Une façon de décrire un algorithme en utilisant un langage simple, proche du langage naturel, mais avec une structure qui ressemble à celle d'un langage de programmation. Ce n'est pas un vrai code exécutable.

**Organigramme :** Une représentation graphique d'un algorithme, utilisant des symboles standardisés pour représenter les étapes et les décisions.

- **Un croquis avant de peindre ou un plan d'architecte.**

* Avant de peindre un tableau complexe, un artiste fait souvent un croquis pour définir la composition. Le pseudo-code est comme ce croquis.

* Un architecte dessine des plans détaillés (organigrammes) avant que les maçons ne construisent la maison, montrant où vont les murs, les portes, les fenêtres, et comment les pièces sont connectées.

- **Exemple concret (Jeu du "plus ou moins") :**

* **Pseudo-code :**

<!---->

    NOMBRE_SECRET = Choisir un nombre aléatoire entre 1 et 100

    A_TROUVE = Faux

    TENTATIVES = 0

    AFFICHER "Devinez le nombre entre 1 et 100."

    TANT QUE A_TROUVE est Faux:

        LIRE proposition_joueur

        TENTATIVES = TENTATIVES + 1

        SI proposition_joueur < NOMBRE_SECRET ALORS

            AFFICHER "C'est plus !"

        SINON SI proposition_joueur > NOMBRE_SECRET ALORS

            AFFICHER "C'est moins !"

        SINON

            AFFICHER "Bravo, vous avez trouvé en ", TENTATIVES, " tentatives !"

            A_TROUVE = Vrai

        FIN SI

    FIN TANT QUE

- **Organigramme (simplifié) :**

* Début -> Choisir NOMBRE\_SECRET -> Afficher "Devinez" -> Lire proposition -> (Losange de décision : proposition == NOMBRE\_SECRET ?)

- Oui -> Afficher "Bravo" -> Fin

- Non -> (Losange de décision : proposition < NOMBRE\_SECRET ?)

* Oui -> Afficher "C'est plus !" -> Retour à Lire proposition

* Non -> Afficher "C'est moins !" -> Retour à Lire proposition

en mermaid (MarkDown):

    ```mermaid

    graph TD;

        A[Début] --> B[Fixer NOMBRE_SECRET];

        B --> C[A_TROUVE = Faux];

        C --> D[TENTATIVES =];

        D --> E[Afficher 'Devinez le nombre'];

        E --> F_LOOP;  

        %% Connexion à la condition de boucle

        F_LOOP{A_TROUVE est Faux <br/>ET<br/> TENTATIVES < MAX_TENTATIVES?};

        %% Chemin si la condition de boucle est VRAIE (on continue dans la boucle)

        F_LOOP -- Oui --> G[Lire PROPOSITION];

        G --> H[TENTATIVES = TENTATIVES +];

        H --> I{PROPOSITION == NOMBRE_SECRET?};

        

        I -- Oui --> J[Afficher 'Bravo!'];

        J --> K[A_TROUVE = Vrai];

        K --> F_LOOP; %% Retour à la condition de boucle

        

        I -- Non --> L{PROPOSITION < NOMBRE_SECRET?};

        L -- Oui --> M[Afficher 'C'est plus!'];

        M --> F_LOOP; %% Retour à la condition de boucle

        

        L -- Non --> N[Afficher 'C'est moins!'];

        N --> F_LOOP; %% Retour à la condition de boucle

        

        %% Chemin si la condition de boucle est FAUSSE (on sort de la boucle)

        F_LOOP -- Non --> O{A_TROUVE est Vrai?};

        O -- Oui --> P[Fin - Gagné];

        O -- Non --> Q[Fin - Perdu, tentatives épuisées];

    ```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdC6hGuCEh7KEYjPCYQmZZELUA6qFQUxTliPdR-sXFSSYTh3FuJwEXlCXCL5SKEHJeGBb2qjQjKzr-RJ9BisGn_2BTwsut1duB0PVfsDxawRwqdqp_YP0VqdCJ4MynoYi5zutvR?key=imBr4Bp-sQmB_Z80Q2-akA)


-----

## **Complexité algorithmique (introduction simple : O(n), O(n²))**

C'est une façon de mesurer l'efficacité d'un algorithme, en particulier comment son temps d'exécution ou l'espace mémoire qu'il utilise augmente avec la taille des données en entrée.

- **Parabole de la vie réelle : Chercher un nom dans un annuaire.**

* **O(n) - Linéaire :** Vous avez un annuaire (liste de noms) non trié. Pour trouver "Dupont", vous devez potentiellement lire chaque nom, un par un, depuis le début. Si l'annuaire a 100 noms, cela peut prendre jusqu'à 100 étapes. S'il a 1000 noms (n=1000), jusqu'à 1000 étapes. Le temps augmente proportionnellement à la taille.

* **O(log n) - Logarithmique (plus efficace) :** Si l'annuaire est trié alphabétiquement. Vous ouvrez au milieu. Si "Dupont" est avant, vous prenez la première moitié et ouvrez à nouveau au milieu de cette section. Vous éliminez la moitié des possibilités à chaque étape. C'est beaucoup plus rapide pour les grands annuaires.

* **O(n²) - Quadratique :** Imaginez que pour chaque personne dans l'annuaire (n personnes), vous deviez comparer son nom avec celui de toutes les autres personnes (encore n personnes). Cela ferait n \* n comparaisons. Si vous avez 10 personnes, c'est 100 comparaisons. Si vous avez 100 personnes, c'est 10 000 comparaisons. Ça devient très lent très vite.

- **Exemple concret :**

* **Rechercher un élément dans une liste Python :**

- ma\_liste = \[1, 2, 3, ...,]

- Trouver x : for element in ma\_liste: if element == x: ... (dans le pire cas, on parcourt tout : O(n))

**Comparer chaque élément d'une liste avec chaque autre élément :**

    # Exemple de complexité O(n^2)
    # pour chaque element1 dans ma_liste:
    #     pour chaque element2 dans ma_liste:
    #         comparer(element1, element2)


-----

# **Bases de Python**

Python est le langage que nous utiliserons pour traduire nos algorithmes en instructions compréhensibles par l'ordinateur.


## **Installation de Python et d'un IDE (VS Code, PyCharm Community)**

Télécharger Python depuis python.org et installer VS Code avec l'extension Python ou PyCharm Community.


## **Variables, types de données (entiers, flottants, chaînes, booléens)**

**Variables :** Des "étiquettes" que l'on pose sur des "boîtes" pour stocker des informations. Le nom de la variable est l'étiquette, la valeur est ce qu'il y a dans la boîte.

**Types de données :** La nature de ce que l'on met dans les boîtes.

- **Dans la vie réelle : Des boîtes de rangement étiquetées.**

* age = 30 : Une boîte étiquetée "age" contenant le nombre entier 30. (Type : **entier** ou int)

* prix\_baguette = 1.10 : Une boîte "prix\_baguette" contenant le nombre décimal 1.10. (Type : **flottant** ou float)

* nom\_utilisateur = "Alice" : Une boîte "nom\_utilisateur" contenant le texte "Alice". (Type : **chaîne de caractères** ou str)

* est\_traitée = True : Une case à cocher "est\_traitée" indiquant si la tâches ou le dossier est traité (Type : **booléen** ou bool, peut être True ou False)


### **Exemple en Python**

    age = 25
    taille_cm = 175.5
    prenom = "Julien"
    aime_le_cafe = True


-----

## **Opérateurs (arithmétiques, de comparaison, logiques)**

- Ce sont les outils qui permettent de manipuler les valeurs dans vos boîtes (variables) ou de les comparer.

- **Parabole de la vie réelle : Les actions que vous faites avec le contenu des boîtes.**

* **Arithmétiques :** + (addition), - (soustraction), \* (multiplication), / (division). Comme calculer le coût total de vos courses.

* **De comparaison :** == (égal à), != (différent de), > (supérieur à), < (inférieur à), >= (supérieur ou égal), <= (inférieur ou égal). Comme vérifier si vous avez assez d'argent pour un achat.

* **Logiques :** and (ET), or (OU), not (NON). Comme décider de prendre un parapluie : SI (il pleut OU le ciel est menaçant) ET NON (j'ai oublié mon parapluie à la maison).


### **Exemple en Python**

    a = 10
    b = 5
    somme = a + b  # somme vaut 15
    est_plus_grand = a > b  # est_plus_grand vaut True
    peut_sortir = (temperature > 15) and (not pleut) # pleut doit être une variable booléenne


## **Entrées et sorties (input(), print())**

- Comment votre programme communique avec l'utilisateur ou le monde extérieur.

- **Parabole de la vie réelle : Parler et écouter.**

* input() : C'est comme poser une question à quelqu'un et attendre sa réponse. Le programme se met en pause et attend que l'utilisateur tape quelque chose.

* print() : C'est comme parler ou afficher un message sur un écran pour que l'utilisateur le voie.

- **Exemple en Python :**\
  `nom = input("Quel est votre nom ? ") # Pose la question et stocke la réponse dans 'nom'
  print("Bonjour, " + nom + " !")     # Affiche un message de bienvenue`

* **Structures de contrôle :** Elles dirigent le flux d'exécution de votre programme.

- **Conditions (if, elif, else)**

* Permettent d'exécuter différents blocs de code en fonction de si une condition est vraie ou fausse.

* **Parabole de la vie réelle : Prendre une décision à un carrefour.**

- if (Si) le feu est vert, alors traverser.

- elif (Sinon si) le feu est orange, alors ralentir et se préparer à s'arrêter.

- else (Sinon, donc si le feu est rouge), alors s'arrêter.


### **Exemple en Python**

    age_utilisateur = int(input("Quel âge avez-vous ? ")) # input() renvoie du texte, on le convertit en entier
    if age_utilisateur < 18:
        print("Vous êtes mineur.")
    elif age_utilisateur == 18:
        print("Vous venez d'atteindre la majorité !")
    else:
        print("Vous êtes majeur.")

- **Boucles (for, while)**

* Permettent de répéter un bloc de code plusieurs fois.

* **Parabole de la vie réelle : Des tâches répétitives.**

- **Boucle for (Pour) :** Utilisée quand on sait combien de fois on veut répéter, ou pour parcourir les éléments d'une collection.

* "Pour chaque invité sur ma liste (5 invités), préparer une assiette."

* "Pour chaque chanson dans ma playlist, jouer la chanson."

- **Boucle while (Tant que) :** Utilisée quand on veut répéter tant qu'une certaine condition reste vraie.

* "Tant que la casserole d'eau n'est pas pleine, continuer à verser de l'eau."

* "Tant que le joueur n'a pas trouvé le nombre secret, continuer à lui demander une nouvelle proposition." (Comme dans notre pseudo-code du "plus ou moins").


### **Exemple en Python**

    # Boucle for : afficher les chiffres de 0 à 4
    for i in range(5): # range(5) génère 0, 1, 2, 3, 4
        print(i)
    # Boucle for : parcourir une liste
    invites = ["Alice", "Bob", "Charlie"]
    for invite in invites:
        print("Bienvenue, " + invite + " !")
    # Boucle while : compter jusqu'à 3
    compteur = 0
    while compteur < 3:
        print("Le compteur est à", compteur)
        compteur = compteur + 1 # Important d'avoir une condition qui finira par rendre la boucle fausse!


### **Mini-projet 1 : Calculatrice simple, jeu du "plus ou moins".**

- **Calculatrice :**

* Demander à l'utilisateur deux nombres.

* Demander l'opération (+, -, \*, /).

* Utiliser if/elif/else pour effectuer le bon calcul.

* Afficher le résultat.

- **Jeu du "plus ou moins" :**

* L'ordinateur choisit un nombre aléatoire (module random).

* Utiliser une boucle while pour continuer tant que le joueur n'a pas trouvé.

* Dans la boucle, utiliser input() pour la proposition du joueur.

* Utiliser if/elif/else pour dire "plus", "moins" ou "gagné".


-----

# **Structures de Données Fondamentales en Python**

Ce sont des façons d'organiser et de stocker plusieurs données ensemble de manière structurée.


## **Listes (création, accès, modification, méthodes courantes)**

Une collection ordonnée et modifiable d'éléments. Les éléments peuvent être de différents types.

- **Parabole de la vie réelle : Une liste de courses.**

* Vous pouvez ajouter des articles (append), enlever des articles (remove), changer un article (ma\_liste\[] = "nouveau"), voir combien d'articles il y a (len), vérifier si un article est sur la liste (in). L'ordre des articles compte.


### **Exemple en Python**

    courses = ["pommes", "bananes", "lait"]
    print(courses[])  # Affiche "pommes" (l'indexation commence à 0)
    courses.append("pain") # Ajoute "pain" à la fin
    print(courses) # Affiche ['pommes', 'bananes', 'lait', 'pain']
    courses[] = "fraises" # Remplace "bananes" par "fraises"
    print(courses) # Affiche ['pommes', 'fraises', 'lait', 'pain']
    if "lait" in courses:
        print("N'oubliez pas le lait !")


## **Tuples (immutabilité, cas d'usage)**

Une collection ordonnée mais **non modifiable** (immuable) d'éléments. Une fois créé, on ne peut plus le changer.

- **Parabole de la vie réelle : Les coordonnées géographiques d'un lieu.**

* La latitude et la longitude d'un point fixe (ex: la Tour Eiffel) ne changent pas. coordonnees\_tour\_eiffel = (48.8584, 2.2945).

* Utile pour les données qui ne doivent pas être accidentellement modifiées.


### **Exemple en Python**

    point = (10, 20) # Un point avec des coordonnées x et y
    print(point[]) # Affiche 10
    # point[] = 15 # Cela provoquerait une erreur car les tuples sont immuables
    jours_semaine = ("Lundi", "Mardi", ..., "Dimanche")


## **Dictionnaires (clés-valeurs, accès, modification)**

Une collection non ordonnée (dans les anciennes versions de Python, ordonnée depuis Python 3.7+) de paires **clé-valeur**. Chaque clé doit être unique.

- **Parabole de la vie réelle : Un vrai dictionnaire ou un répertoire téléphonique.**

* Dans un dictionnaire de langue : la **clé** est le mot (ex: "ordinateur"), la **valeur** est sa définition.

* Dans un répertoire téléphonique : la **clé** est le nom de la personne (ex: "Alice Martin"), la **valeur** est son numéro de téléphone.


### **Exemple en Python**

    contact = {
        "nom": "Dupont",
        "prenom": "Jean",
        "telephone": "0123456789",
        "age": 42
    }
    print(contact["prenom"])  # Affiche "Jean"
    contact["email"] = "jean.dupont@email.com" # Ajoute une nouvelle paire clé-valeur
    contact["age"] = 43 # Modifie la valeur associée à la clé "age"
    print(contact)
    # Affiche {'nom': 'Dupont', 'prenom': 'Jean', 'telephone': '0123456789', 'age': 43, 'email': 'jean.dupont@email.com'}


## **Ensembles (sets) (unicité, opérations d'ensemble)**

- Une collection non ordonnée d'éléments **uniques**. Pas de doublons.

- **Parabole de la vie réelle : Une collection de timbres uniques ou les ingrédients uniques d'une recette.**

* Si vous avez une liste d'ingrédients pour plusieurs recettes et que vous voulez savoir quels sont tous les ingrédients distincts nécessaires, un ensemble est parfait. "farine, sucre, farine, oeufs, beurre" deviendrait {"farine", "sucre", "oeufs", "beurre"}.

* Utile pour vérifier l'appartenance et faire des opérations mathématiques d'ensemble (union, intersection).


### **Exemple en Python**

    ingredients_gateau_1 = {"farine", "sucre", "oeufs"}
    ingredients_gateau_2 = {"farine", "beurre", "chocolat"}
    # Union : tous les ingrédients uniques des deux gâteaux
    tous_ingredients = ingredients_gateau_1.union(ingredients_gateau_2)
    print(tous_ingredients) # Affiche quelque chose comme {'beurre', 'oeufs', 'farine', 'chocolat', 'sucre'} (l'ordre peut varier)

    # Intersection : ingrédients communs aux deux
    communs = ingredients_gateau_1.intersection(ingredients_gateau_2)
    print(communs) # Affiche {'farine'}


## **Exercices**

- Manipulation de listes : Créer une liste de tâches, ajouter des tâches, marquer une tâche comme faite (la supprimer ou la déplacer dans une autre liste), trier les tâches par priorité.

- Gestion d'un répertoire téléphonique simple avec un dictionnaire : Ajouter des contacts, rechercher un numéro par nom, supprimer un contact.


# **Fonctions**

Des blocs de code réutilisables qui effectuent une tâche spécifique.

**Définition :** C'est comme créer votre propre outil ou votre propre mini-recette que vous pourrez utiliser plusieurs fois. On utilise le mot-clé def.

**Appel :** C'est utiliser cet outil ou exécuter cette mini-recette.

**Dans la vie réelle : Une machine à café.**

- **Définition :** Quelqu'un a conçu et construit la machine à café (la fonction). Elle a un but précis : faire du café.

- **Appel :** Vous appuyez sur le bouton "Start" de la machine à café (vous appelez la fonction) pour obtenir un café.


### **Exemple en Python**

    # Définition de la fonction
    def saluer():
        print("Bonjour !")
        print("Comment allez-vous aujourd'hui ?")

    # Appel de la fonction
    saluer() # Affiche "Bonjour !" puis "Comment allez-vous aujourd'hui ?"
    saluer() # On peut l'appeler autant de fois qu'on veut


### **Paramètres et arguments**

**Paramètres :** Les variables listées entre parenthèses dans la définition d'une fonction. Ce sont les "emplacements" pour les données dont la fonction a besoin pour travailler.

**Arguments :** Les valeurs réelles que vous passez à la fonction lorsque vous l'appelez.

**Dans la vie réelle : Les ingrédients pour la machine à café.**

- La machine à café (fonction faire\_cafe) pourrait avoir besoin de savoir quel type de café (paramètre type\_cafe) et combien de sucre (paramètre quantite\_sucre).

- Quand vous l'utilisez (appel), vous fournissez les grains "Arabica" (argument pour type\_cafe) et "2 morceaux" (argument pour quantite\_sucre).


### **Exemple en Python**

    # Définition avec des paramètres
    def saluer_personne(nom, moment_journee):
        print(f"Bonjour {nom}, passez un excellent {moment_journee} !") # f-string pour formater

    # Appel avec des arguments
    saluer_personne("Alice", "matin") # Affiche "Bonjour Alice, passez un excellent matin !"
    saluer_personne("Bob", "après-midi") # Affiche "Bonjour Bob, passez un excellent après-midi !"


### **Valeurs de retour (return)**

Une fonction peut effectuer une tâche et "renvoyer" un résultat à l'endroit où elle a été appelée.

**Dans la vie réelle : Le café produit par la machine.**

- La machine à café ne se contente pas de travailler dans son coin ; elle _produit_ quelque chose : une tasse de café (la valeur de retour). Vous pouvez ensuite prendre cette tasse et la boire, ou la donner à quelqu'un.


### **Exemple en Python**

    def additionner(nombre1, nombre2):
        resultat = nombre1 + nombre2
        return resultat # La fonction renvoie la valeur de 'resultat'

    somme = additionner(5, 3) # 'somme' reçoit la valeur renvoyée par additionner (8)
    print(somme) # Affiche 8
    print(additionner(10, 20)) # Affiche 30 directement
    # Si une fonction n'a pas d'instruction return explicite, elle renvoie None par défaut.


-----

## **Portée des variables (locale, globale)**

Détermine où dans votre code une variable est accessible.

**Dans la vie réelle : Outils personnels vs. outils de l'atelier partagé.**

- **Variable locale :** Un outil que vous utilisez uniquement pour une tâche spécifique dans votre coin de l'atelier (à l'intérieur d'une fonction). Une fois la tâche terminée, l'outil est rangé et n'est pas accessible ailleurs.

- **Variable globale :** Un gros outil central dans l'atelier, accessible par tout le monde pour n'importe quelle tâche (déclarée en dehors de toute fonction). Il faut faire attention avec, car tout le monde peut le modifier.


### **Exemple en Python**

    variable_globale = "Je suis globale"

    def ma_fonction():
        variable_locale = "Je suis locale"
        print(variable_locale)
        print(variable_globale) # Peut accéder à la variable globale

    ma_fonction()
    # print(variable_locale) # ERREUR ! variable_locale n'existe qu'à l'intérieur de ma_fonction
    print(variable_globale)


-----

## **Fonctions anonymes (lambda)**

Des petites fonctions, souvent d'une seule ligne, sans nom formel. Utiles pour des opérations simples et rapides.

**Dans la vie réelle : Un petit outil jetable pour une tâche très spécifique et unique.**

- Imaginez que vous ayez besoin de serrer un type de vis très particulier une seule fois. Au lieu de fabriquer un tournevis sophistiqué (une fonction def complète), vous utilisez une petite clé simple et rapide (une lambda).


### **Exemple en Python**

    # Fonction normale
    def carre(x):
        return x * x

    # Fonction lambda équivalente
    carre_lambda = lambda x: x * x

    print(carre(5)) # Affiche 25
    print(carre_lambda(5)) # Affiche 25

    # Souvent utilisées avec des fonctions comme map() ou filter()
    nombres = [1, 2, 3,]
    carres = list(map(lambda x: x * x, nombres)) # map applique la lambda à chaque élément
    print(carres) # Affiche [1, 4, 9,]


-----

## **Mini-projet 2 : Modularisation du mini-projet 1 avec des fonctions.**

- Prendre la calculatrice ou le jeu du "plus ou moins".

- Identifier les parties du code qui effectuent une tâche spécifique et les transformer en fonctions.

- Exemple pour la calculatrice :

* def demander\_nombres(): ... return nombre1, nombre2

* def demander\_operation(): ... return operation

* def calculer(n1, n2, op): ... return resultat\_calcul

* def afficher\_resultat(res): …

- Le code principal devient alors une série d'appels à ces fonctions, ce qui le rend plus lisible et organisé.


-----

# **Programmation Orientée Objet (POO) en Python (Introduction)**

Un paradigme de programmation où l'on organise son code autour d'"objets", qui sont des instances de "classes". Les objets regroupent des données (attributs) et des comportements (méthodes).


## **Concepts clés : classes, objets, attributs, méthodes**

**Classe :** Un plan, un modèle, un "moule" pour créer des objets. Définit les caractéristiques (attributs) et les actions (méthodes) que tous les objets de cette classe auront.

**Objet :** Une instance spécifique d'une classe. C'est une "chose" concrète créée à partir du plan.

**Attributs :** Les données ou les propriétés associées à un objet. Ce sont les caractéristiques de l'objet.

**Méthodes :** Les fonctions qui appartiennent à un objet et qui peuvent agir sur les données de cet objet (ses attributs) ou effectuer des actions liées à l'objet.

**Dans la vie réelle : Le plan d'une voiture (Classe) et les voitures réelles (Objets).**

- **Classe Voiture :** Le plan de conception d'une voiture. Il spécifie qu'une voiture aura une couleur, une marque, un nombre de portes (attributs) et qu'elle pourra démarrer, accélérer, freiner (méthodes).

- **Objet ma\_voiture\_rouge :** Une voiture spécifique construite à partir du plan Voiture.

* **Attributs :** ma\_voiture\_rouge.couleur = "rouge", ma\_voiture\_rouge.marque = "Peugeot".

- **Objet la\_voiture\_bleue\_de\_bob :** Une autre voiture.

* **Attributs :** la\_voiture\_bleue\_de\_bob.couleur = "bleu", la\_voiture\_bleue\_de\_bob.marque = "Renault".

- **Méthodes :** Les deux voitures peuvent demarrer() ou accelerer(), même si leur couleur ou marque est différente.


### **Exemple en Python**

    class Chien:
        # Attribut de classe (partagé par tous les chiens)
        espece = "Canis familiaris"

        # Constructeur (méthode spéciale pour créer un objet)
        def __init__(self, nom_du_chien, race_du_chien):
            # Attributs d'instance (spécifiques à chaque chien)
            self.nom = nom_du_chien
            self.race = race_du_chien
            self.est_assis = False

        # Méthode d'instance
        def aboyer(self):
            return f"{self.nom} dit: Woof!"

        def asseoir(self):
            self.est_assis = True
            print(f"{self.nom} s'assoit.")

        def lever(self):
            self.est_assis = False
            print(f"{self.nom} se lève.")

    # Création d'objets (instances de la classe Chien)
    mon_chien = Chien("Médor", "Labrador")
    autre_chien = Chien("Rex", "Berger Allemand")

    print(mon_chien.nom)  # Affiche "Médor"
    print(autre_chien.race) # Affiche "Berger Allemand"
    print(mon_chien.aboyer()) # Affiche "Médor dit: Woof!"
    autre_chien.asseoir() # Affiche "Rex s'assoit."
    print(f"Est-ce que {autre_chien.nom} est assis ? {autre_chien.est_assis}") # Affiche True


## **Constructeur (\_\_init\_\_)**

Une méthode spéciale dans une classe qui est appelée automatiquement lorsqu'on crée un nouvel objet de cette classe. Son rôle principal est d'initialiser les attributs de l'objet.

**Dans la vie réelle : La chaîne de montage d'une voiture.**

- Quand une nouvelle voiture (objet) est créée sur la chaîne de montage (appel de la classe), le constructeur (\_\_init\_\_) est l'ensemble des opérations initiales : peindre la carrosserie dans la couleur demandée, installer le moteur spécifique, etc.

* Dans l'exemple Chien ci-dessus, \_\_init\_\_ prend nom\_du\_chien et race\_du\_chien et les assigne aux attributs self.nom et self.race de l'objet chien en cours de création. self fait référence à l'objet lui-même.


-----

## **Encapsulation, Héritage, Polymorphisme (concepts de base)**

Ce sont trois piliers importants de la POO.

**Encapsulation :**

L'idée de regrouper les données (attributs) et les méthodes qui opèrent sur ces données au sein d'un même objet, et de cacher les détails complexes de l'implémentation interne de l'objet. L'objet expose une interface claire pour interagir avec lui.

- **Exemple :** Une télécommande de télévision. Vous avez des boutons (interface) pour changer de chaîne ou de volume. Vous n'avez pas besoin de connaître les circuits électroniques internes (détails cachés) pour l'utiliser. L'encapsulation protège les données internes d'une modification accidentelle de l'extérieur.

**Héritage :**

- Permet à une nouvelle classe (classe fille ou sous-classe) d'hériter des attributs et méthodes d'une classe existante (classe mère ou super-classe). La classe fille peut ensuite ajouter ses propres attributs et méthodes spécifiques ou modifier ceux hérités.

- **Exemple :** Un Caniche (classe fille) est un type de Chien (classe mère). Il hérite de toutes les caractéristiques d'un chien (aboie, a une race, un nom) mais peut avoir des caractéristiques ou comportements spécifiques (ex: toiletter\_en\_boule()).

<!---->

    class Caniche(Chien): # Caniche hérite de Chien
        def __init__(self, nom_du_chien):
            super().__init__(nom_du_chien, "Caniche") # Appelle le constructeur de la classe Chien

        def faire_le_beau(self):
            return f"{self.nom} fait le beau !"

    mon_caniche = Caniche("Fifi")
    print(mon_caniche.nom)      # Hérité de Chien
    print(mon_caniche.race)     # Mis à "Caniche"
    print(mon_caniche.aboyer()) # Méthode héritée de Chien
    print(mon_caniche.faire_le_beau()) # Méthode spécifique à Caniche


## **Polymorphisme**

Signifie "plusieurs formes". En POO, cela signifie que des objets de différentes classes peuvent répondre au même appel de méthode, mais de manière différente, spécifique à leur classe.

**Dans la vie réelle :** Différents animaux peuvent tous avoir une méthode se\_deplacer(). Un Oiseau volera, un Poisson nagera, un Chien marchera/courra. L'action se\_deplacer() est la même, mais l'exécution (la forme) est différente.

    class Chat:
        def __init__(self, nom):
            self.nom = nom
        def parler(self):
            return f"{self.nom} dit: Miaou!"

    class Vache:
        def __init__(self, nom):
            self.nom = nom
        def parler(self):
            return f"{self.nom} dit: Meuh!"

    # Liste d'animaux de types différents
    animaux = [Chien("Pluto", "Basset"), Chat("Garfield"), Vache("Marguerite")]

    for animal in animaux:
        # On appelle la même méthode "parler()" mais chaque animal le fait à sa façon
        print(animal.parler())


## **Exercices**

- Créer une classe Voiture avec des attributs comme marque, modele, couleur, vitesse\_actuelle et des méthodes comme accelerer(valeur), freiner(valeur), afficher\_vitesse().

- Créer une classe Point avec des attributs x et y et une méthode pour calculer la distance par rapport à un autre point.


# **Projet Belote**

<https://github.com/Antoine-O/P2PBelote> 

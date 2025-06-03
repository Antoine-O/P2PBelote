import json
import pytest

# --- Données de Test (JSON complet de la partie) ---
# Dans un projet réel, ce JSON serait probablement dans un fichier séparé.
JSON_DATA = """
{
  "id_partie": "a1b2c3d4-e5f6-4a7b-8c2d-123456789abc",
  "date_debut": "2025-06-04T00:10:00Z",
  "joueurs": [
    { "id_joueur": "J1", "nom": "Alice", "position": 1 },
    { "id_joueur": "J2", "nom": "Bob", "position": 2 },
    { "id_joueur": "J3", "nom": "Charlie", "position": 3 },
    { "id_joueur": "J4", "nom": "Diana", "position": 4 }
  ],
  "equipes": {
    "equipe_A": { "joueurs": ["J1", "J3"], "score_total": 122 },
    "equipe_B": { "joueurs": ["J2", "J4"], "score_total": 60 }
  },
  "manches": [
    {
      "numero_manche": 1,
      "dealer_position": 1,
      "distribution": {
        "carte_retournee": { "valeur": "HUIT", "couleur": "COEUR" },
        "premier_tour": {
          "J1": [ { "valeur": "DAME", "couleur": "CARREAU" }, { "valeur": "DAME", "couleur": "COEUR" }, { "valeur": "VALET", "couleur": "COEUR" }, { "valeur": "NEUF", "couleur": "COEUR" }, { "valeur": "SEPT", "couleur": "COEUR" } ],
          "J2": [ { "valeur": "AS", "couleur": "COEUR" }, { "valeur": "DIX", "couleur": "COEUR" }, { "valeur": "ROI", "couleur": "COEUR" }, { "valeur": "AS", "couleur": "PIQUE" }, { "valeur": "SEPT", "couleur": "PIQUE" } ],
          "J3": [ { "valeur": "VALET", "couleur": "PIQUE" }, { "valeur": "DAME", "couleur": "PIQUE" }, { "valeur": "HUIT", "couleur": "PIQUE" }, { "valeur": "NEUF", "couleur": "CARREAU" }, { "valeur": "VALET", "couleur": "CARREAU" } ],
          "J4": [ { "valeur": "AS", "couleur": "CARREAU" }, { "valeur": "DIX", "couleur": "CARREAU" }, { "valeur": "ROI", "couleur": "CARREAU" }, { "valeur": "SEPT", "couleur": "CARREAU" }, { "valeur": "HUIT", "couleur": "CARREAU" } ]
        },
        "deuxieme_tour": {
          "J1": [ { "valeur": "NEUF", "couleur": "PIQUE" }, { "valeur": "DIX", "couleur": "PIQUE" }, { "valeur": "ROI", "couleur": "PIQUE" } ],
          "J2": [ { "valeur": "NEUF", "couleur": "TREFLE" }, { "valeur": "VALET", "couleur": "TREFLE" }, { "valeur": "SEPT", "couleur": "TREFLE" } ],
          "J3": [ { "valeur": "HUIT", "couleur": "TREFLE" }, { "valeur": "DIX", "couleur": "TREFLE" } ],
          "J4": [ { "valeur": "AS", "couleur": "TREFLE" }, { "valeur": "ROI", "couleur": "TREFLE" }, { "valeur": "DAME", "couleur": "TREFLE" } ]
        }
      },
      "contrat": { "preneur_id": "J1", "equipe_prenante": "A", "atout": "COEUR" },
      "plis": [
        { "numero_pli": 1, "meneur_id": "J2", "cartes_jouees": [ { "joueur_id": "J2", "carte": { "valeur": "AS", "couleur": "PIQUE" } }, { "joueur_id": "J3", "carte": { "valeur": "VALET", "couleur": "PIQUE" } }, { "joueur_id": "J4", "carte": { "valeur": "HUIT", "couleur": "CARREAU" } }, { "joueur_id": "J1", "carte": { "valeur": "ROI", "couleur": "PIQUE" } } ], "vainqueur_id": "J2" },
        { "numero_pli": 2, "meneur_id": "J2", "cartes_jouees": [ { "joueur_id": "J2", "carte": { "valeur": "SEPT", "couleur": "PIQUE" } }, { "joueur_id": "J3", "carte": { "valeur": "DAME", "couleur": "PIQUE" } }, { "joueur_id": "J4", "carte": { "valeur": "SEPT", "couleur": "CARREAU" } }, { "joueur_id": "J1", "carte": { "valeur": "NEUF", "couleur": "PIQUE" } } ], "vainqueur_id": "J1" },
        { "numero_pli": 3, "meneur_id": "J1", "cartes_jouees": [ { "joueur_id": "J1", "carte": { "valeur": "VALET", "couleur": "COEUR" } }, { "joueur_id": "J2", "carte": { "valeur": "SEPT", "couleur": "TREFLE" } }, { "joueur_id": "J3", "carte": { "valeur": "HUIT", "couleur": "PIQUE" } }, { "joueur_id": "J4", "carte": { "valeur": "AS", "couleur": "CARREAU" } } ], "vainqueur_id": "J1" },
        { "numero_pli": 4, "meneur_id": "J1", "cartes_jouees": [ { "joueur_id": "J1", "carte": { "valeur": "NEUF", "couleur": "COEUR" } }, { "joueur_id": "J2", "carte": { "valeur": "ROI", "couleur": "COEUR" } }, { "joueur_id": "J3", "carte": { "valeur": "NEUF", "couleur": "CARREAU" } }, { "joueur_id": "J4", "carte": { "valeur": "DIX", "couleur": "CARREAU" } } ], "vainqueur_id": "J1" },
        { "numero_pli": 5, "meneur_id": "J1", "cartes_jouees": [ { "joueur_id": "J1", "carte": { "valeur": "DAME", "couleur": "COEUR" } }, { "joueur_id": "J2", "carte": { "valeur": "AS", "couleur": "COEUR" } }, { "joueur_id": "J3", "carte": { "valeur": "VALET", "couleur": "CARREAU" } }, { "joueur_id": "J4", "carte": { "valeur": "ROI", "couleur": "CARREAU" } } ], "vainqueur_id": "J2" },
        { "numero_pli": 6, "meneur_id": "J2", "cartes_jouees": [ { "joueur_id": "J2", "carte": { "valeur": "DIX", "couleur": "COEUR" } }, { "joueur_id": "J3", "carte": { "valeur": "DIX", "couleur": "TREFLE" } }, { "joueur_id": "J4", "carte": { "valeur": "ROI", "couleur": "TREFLE" } }, { "joueur_id": "J1", "carte": { "valeur": "HUIT", "couleur": "COEUR" } } ], "vainqueur_id": "J2" },
        { "numero_pli": 7, "meneur_id": "J2", "cartes_jouees": [ { "joueur_id": "J2", "carte": { "valeur": "NEUF", "couleur": "TREFLE" } }, { "joueur_id": "J3", "carte": { "valeur": "HUIT", "couleur": "TREFLE" } }, { "joueur_id": "J4", "carte": { "valeur": "AS", "couleur": "TREFLE" } }, { "joueur_id": "J1", "carte": { "valeur": "DIX", "couleur": "PIQUE" } } ], "vainqueur_id": "J4" },
        { "numero_pli": 8, "meneur_id": "J4", "cartes_jouees": [ { "joueur_id": "J4", "carte": { "valeur": "DAME", "couleur": "TREFLE" } }, { "joueur_id": "J1", "carte": { "valeur": "DAME", "couleur": "CARREAU" } }, { "joueur_id": "J2", "carte": { "valeur": "VALET", "couleur": "TREFLE" } }, { "joueur_id": "J3", "carte": { "valeur": "DIX", "couleur": "CARREAU" } } ], "vainqueur_id": "J1" }
      ],
      "resultat_manche": { "contrat_reussi": true, "score_equipe_prenante": 122, "score_equipe_defense": 60, "annonces": [ { "joueur_id": "J1", "type": "BELOTE-REBELOTE", "valeur": 20 } ] }
    }
  ]
}
"""

# --- Constantes et Classes Utilitaires ---

POINTS_ATOUT = {"VALET": 20, "NEUF": 14, "AS": 11, "DIX": 10, "ROI": 4, "DAME": 3, "HUIT": 0, "SEPT": 0}
POINTS_NORMAL = {"AS": 11, "DIX": 10, "ROI": 4, "DAME": 3, "VALET": 2, "NEUF": 0, "HUIT": 0, "SEPT": 0}

class Carte:
    def __init__(self, data_dict):
        self.valeur = data_dict['valeur']
        self.couleur = data_dict['couleur']

    def __repr__(self):
        return f"{self.valeur} de {self.couleur}"

    def get_points(self, atout):
        return POINTS_ATOUT[self.valeur] if self.couleur == atout else POINTS_NORMAL[self.valeur]

# --- Fixture Pytest pour fournir les données ---

@pytest.fixture
def manche_test_data():
    """Charge et retourne les données de la première manche du JSON."""
    return json.loads(JSON_DATA)['manches'][0]

# --- Fonctions de Test Pytest ---

def test_recalcul_des_scores(manche_test_data):
    """
    TEST 1: Recalcule le score à partir des plis et le compare au score enregistré.
    Cette fonction est complète et devrait passer.
    """
    # Extraction des données de la fixture
    manche = manche_test_data
    partie = json.loads(JSON_DATA) # besoin des infos sur les equipes
    atout = manche['contrat']['atout']
    equipe_prenante_id = manche['contrat']['equipe_prenante']
    joueurs_equipe_prenante = partie['equipes'][equipe_prenante_id]['joueurs']

    # Calcul des points bruts
    points_bruts_prenants = 0
    points_bruts_defense = 0
    for pli in manche['plis']:
        points_du_pli = sum(Carte(c['carte']).get_points(atout) for c in pli['cartes_jouees'])
        if pli['vainqueur_id'] in joueurs_equipe_prenante:
            points_bruts_prenants += points_du_pli
        else:
            points_bruts_defense += points_du_pli

    # Ajout du Dix de Der
    if manche['plis'][-1]['vainqueur_id'] in joueurs_equipe_prenante:
        points_bruts_prenants += 10
    else:
        points_bruts_defense += 10

    # Calcul des annonces
    points_annonces_prenants = sum(a['valeur'] for a in manche['annonces'] if a['joueur_id'] in joueurs_equipe_prenante)
    points_annonces_defense = sum(a['valeur'] for a in manche['annonces'] if a['joueur_id'] not in joueurs_equipe_prenante)

    # Attribution finale des scores
    contrat_reussi = points_bruts_prenants >= 82
    score_final_prenant_calcule = 0
    score_final_defense_calcule = 0
    if contrat_reussi:
        score_final_prenant_calcule = points_bruts_prenants + points_annonces_prenants + points_annonces_defense
        score_final_defense_calcule = points_bruts_defense
    else:
        belote_prenante = sum(a['valeur'] for a in manche['annonces'] if a['joueur_id'] in joueurs_equipe_prenante and a['type'] == 'BELOTE-REBELOTE')
        score_final_prenant_calcule = belote_prenante
        score_final_defense_calcule = 162 + points_annonces_prenants + points_annonces_defense

    # Assertions Pytest
    resultat_json = manche['resultat_manche']
    assert contrat_reussi == resultat_json['contrat_reussi']
    assert score_final_prenant_calcule == resultat_json['score_equipe_prenante']
    assert score_final_defense_calcule == resultat_json['score_equipe_defense']

def test_legalite_des_plis(manche_test_data):
    """
    TEST 2: Vérifie que chaque carte jouée était un coup légal.
    Cette fonction nécessite l'implémentation de la logique de validation.
    """
    # Etape 1: Reconstituer les mains initiales
    manche = manche_test_data
    atout = manche['contrat']['atout']
    mains = {j_id: [Carte(c) for c in cartes] for j_id, cartes in manche['distribution']['premier_tour'].items()}
    for j_id, cartes in manche['distribution']['deuxieme_tour'].items():
        mains[j_id].extend([Carte(c) for c in cartes])
    preneur_id = manche['contrat']['preneur_id']
    mains[preneur_id].append(Carte(manche['distribution']['carte_retournee']))

    # Etape 2: Parcourir les plis et vérifier chaque coup
    for pli in manche['plis']:
        pli_en_cours_pour_validation = []
        for coup in pli['cartes_jouees']:
            joueur_id = coup['joueur_id']
            carte_jouee = Carte(coup['carte'])

            main_actuelle_du_joueur = mains[joueur_id]

            # L'assertion principale
            assert est_coup_legal(carte_jouee, main_actuelle_du_joueur, pli_en_cours_pour_validation, atout), \
                f"Coup illegal pour {joueur_id} au pli {pli['numero_pli']}: a joue {carte_jouee}"

            # Mise à jour de l'état pour le coup suivant
            pli_en_cours_pour_validation.append(carte_jouee)
            mains[joueur_id] = [c for c in main_actuelle_du_joueur if not (c.valeur == carte_jouee.valeur and c.couleur == carte_jouee.couleur)]

def est_coup_legal(carte_jouee, main_du_joueur, pli_en_cours, atout):
    """
    Fonction de validation. C'est ici que la logique complexe des règles doit être codée.
    Retourne True si le coup est légal, False sinon.
    """
    # TODO: Implémenter la logique du diagramme "Quelle Carte Jouer ?".
    # Pour ce canevas, on retourne True pour permettre au test de s'exécuter.
    # Une vraie implémentation analyserait le pli_en_cours et la main_du_joueur.

    # Vérification de base : le joueur possède-t-il la carte ?
    possede_la_carte = any(c.valeur == carte_jouee.valeur and c.couleur == carte_jouee.couleur for c in main_du_joueur)
    if not possede_la_carte:
        return False # Le joueur ne peut pas jouer une carte qu'il n'a pas.

    return True
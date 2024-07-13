import json

def chargerDonnees(fichier):
    try:
        with open(fichier, 'r') as f:
            data = json.load(f)
            global articles, vente
            articles = data['articles']
            vente = data['ventes']
            print("Données chargées avec succès!")
    except FileNotFoundError:
        print("Fichier non trouvé.")
    except json.JSONDecodeError:
        print("Erreur de décodage JSON.")

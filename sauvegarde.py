from articles import charger_articles
from vente import charger_ventes

def charger_donnees():
    charger_articles()
    charger_ventes()

    print("Données chargées avec succès.")

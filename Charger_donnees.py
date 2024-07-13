import json
def charger_donnees():
    with open ('Produit.json','r') as FICHIER: 
         LISTE_PRODUITS = json.load(FICHIER)
    with open('rapport_vente.json','r') as FICHIER:
        LISTE_RAPPORT = json.load(FICHIER)
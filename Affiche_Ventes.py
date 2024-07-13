import json

def afficher_vente():
    with open ('rapport_vente.json','r') as FICHIER: 
        LISTE_RAPPORT = json.load(FICHIER)
        print("\t\tVENTES ")
        j = 0
        
    for VENTE in LISTE_RAPPORT:
        print(f" ID VENTE : {VENTE[j]} | NOM CLIENT  : {VENTE[j+1]}  | PRODUIT  : {VENTE[j+2]} | QUANTITE  : {VENTE[j+3]} | DATE : {VENTE[j+4]} | HEURE : {VENTE[j+5]} ")
    
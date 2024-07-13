import json 

def Afficher_Produit_dispo(LISTE_PARAMETRE):
    with open ('Produit.json','r') as FICHIER: 
        LISTE_PARAMETRE = json.load(FICHIER)
        print("LES PRODUITS DISPONIBLES ")
    j = 0
    for PRODUIT in LISTE_PARAMETRE:
        if PRODUIT[j+3] > 0 :
            print(f"ID : {PRODUIT[j]} | NOM PRODUIT : {PRODUIT[j+1]}  | PRIX  : {PRODUIT[j+2]} | QUANTITE EN STOCK : {PRODUIT[j+3]}")
    return LISTE_PARAMETRE
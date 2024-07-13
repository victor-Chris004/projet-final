from datetime import datetime
import json 
def rapport ():
    print("RAPPORT JOURNALIER:")
    with open ('rapport_vente.json','r') as FICHIER: 
        LISTE_RAPPORT = json.load(FICHIER)
    with open ('Produit.json','r') as FICHIER: 
        LISTE_PARAMETRE = json.load(FICHIER)

    print("\tACHAT")
    j = 0 
    date = datetime.today().strftime('%d/%m/%Y')
    for ACHAT in LISTE_PARAMETRE:
                if ACHAT[j+4] == date:
                    print(f"NOM PRODUIT : {ACHAT[2]} | QUANTITE : {ACHAT[3]} | DATE : {ACHAT[4]} | HEURE {ACHAT[5]}")

    print("\tVENTES ")
            
    for VENTE in LISTE_RAPPORT:
        if VENTE[j+4] == date:
            print(f"ID VENTE : {VENTE[j]} | NOM CLIENT  : {VENTE[j+1]}  | PRODUIT  : {VENTE[j+2]} | QUANTITE  : {VENTE[j+3]} | DATE : {VENTE[j+4]} | HEURE : {VENTE[j+5]} ")
        
    
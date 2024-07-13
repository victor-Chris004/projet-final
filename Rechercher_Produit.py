import json 
from colorama import Fore,Style

def rechercher_produit():
    with open ('Produit.json','r') as FICHIER: 
        LISTE_PARAMETRE = json.load(FICHIER)
    VERIFICATEUR = 0
    while VERIFICATEUR == 0: 
        CHOIX_UTILISATEUR = input("Entrer le nom du produit : ")
        if CHOIX_UTILISATEUR.isnumeric():
            print(Fore.RED +f"Attention 🚨🚨 le nom du produit doit être une chaîne de carastères 😯"+Style.RESET_ALL)
        elif CHOIX_UTILISATEUR == "":
            print(Fore.RED +f"""
                   Attention  🚨🚨 le champs de nom du produit ne doit pas resté vide 
                   VEUILLEZ LE REMPLIR SVP  😯"""+Style.RESET_ALL)
        else:
            VERIFICATEUR = 1

    RESULTAT = []
    COMPTEUR = 0
    for PRODUIT in LISTE_PARAMETRE:
        if PRODUIT[1].lower() == CHOIX_UTILISATEUR.lower():
            COMPTEUR +=1
            RESULTAT.append(PRODUIT)
    if COMPTEUR == 0:
        print(Fore.RED +f"Aucun produit porte le nom  {CHOIX_UTILISATEUR} 😯"+Style.RESET_ALL)
    else:
        print (f"il ya {COMPTEUR} (s) Produits qui porte le nom  {CHOIX_UTILISATEUR} :")
        
        for PRODIT_DISP in RESULTAT:
            print(f"ID : {PRODIT_DISP[0]} | NOM PRODUIT : {PRODIT_DISP[1]} | PRIX : {PRODIT_DISP[2]} | QUANTITE EN STOCK :  {PRODIT_DISP[3]}")


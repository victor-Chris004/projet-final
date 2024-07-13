from enregistrer_vente import ouvrir_rapport
from colorama import Fore,Style
def vente_client ():
    
    LISTE_RAPPORT =  ouvrir_rapport()
    VERIFICATEUR  = 0
    while VERIFICATEUR == 0:
        REPONSE_UTILISATUER = input("Entrez le nom client : ")
        if REPONSE_UTILISATUER =="":
            print(Fore.RED +f"""
                   Attention  🚨🚨 le champs pour le nom client est obligatoire
                   VEUILLEZ LE REMPLIR SVP  😯"""+Style.RESET_ALL)
        elif  REPONSE_UTILISATUER.isnumeric():
              print(Fore.RED +f"Attention 🚨🚨 rien que une chaîne de caracters qui est valide pour le nom d'un produit 😯"+Style.RESET_ALL)
        elif  len(REPONSE_UTILISATUER) < 3 : 
             print(Fore.RED +f"MAUVAISE VALEUR 🚨🚨 😯"+Style.RESET_ALL)
        else : 
             VERIFICATEUR = 1 
        
    COMPTEUR = 0
    print(f"INFO POUR CLIENT {REPONSE_UTILISATUER} :")
    for CLIENT in LISTE_RAPPORT:
            if CLIENT[1].lower() == REPONSE_UTILISATUER.lower():
                COMPTEUR +=1
                print(f"NOM PRODUIT : {CLIENT[2]} | QUANTITE : {CLIENT[3]} | DATE : {CLIENT[4]} | HEURE {CLIENT[5]}")

    if COMPTEUR == 0: 
        print(Fore.RED +f"Aucun client porte le nom  {REPONSE_UTILISATUER} 😯"+Style.RESET_ALL)

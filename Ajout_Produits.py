import json 
from colorama import Fore,Style
from datetime import datetime
import time 

def ajouter_Produits(LISTE_PARAMETRE):
        LISTE_INTERMEDIAIRE = []
        id = len(LISTE_PARAMETRE)+1
        VERIFICATEUR  = 0
        while VERIFICATEUR == 0:    
            NOM_PRODUIT  = input("Entrez le nom du produit : ")
            PRIX_PRODUIT  = input("Entrez le prix du produit : ")
            QUANTITE_PRODUIT = int(input("Entrez la quantité du produit : "))
            if NOM_PRODUIT == "" or PRIX_PRODUIT == "" or  QUANTITE_PRODUIT == "":
                 print(Fore.RED +f"""
                       Attention 🚨🚨 touts les champs sont obligatoire  😯
                       RASSIREZ-VOUS D'AVOIR REMPLIR TOUTS LES CHAMPS """+Style.RESET_ALL)
            elif  len(NOM_PRODUIT) < 3 : 
                print(Fore.RED +f"MAUVAISE VALEUR 🚨🚨 😯"+Style.RESET_ALL)

            # elif  PRIX_PRODUIT.isnumeric() not or not  QUANTITE_PRODUIT.isnumeric():
            #      print(Fore.RED +f"""
            #            Attention 🚨🚨 le prix et la quantié du produit ne doit pas être une chaîne de carastères   😯
            #            VEUILLEZ LES MODIFFIERS SVP"""+Style.RESET_ALL)
            elif float(PRIX_PRODUIT) <= 0 or  QUANTITE_PRODUIT <= 0:
                 print(Fore.RED +f"Attention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯"+Style.RESET_ALL)
            else:
                 VERIFICATEUR = 1 
        PRIX_PRODUIT = float(PRIX_PRODUIT)  
        LISTE_INTERMEDIAIRE.append(id)
        LISTE_INTERMEDIAIRE.append(NOM_PRODUIT)
        LISTE_INTERMEDIAIRE.append(PRIX_PRODUIT)
        LISTE_INTERMEDIAIRE.append(QUANTITE_PRODUIT)
        heure = time.strftime('%H:%M:%S')
        date = datetime.today().strftime('%d/%m/%Y')
        LISTE_INTERMEDIAIRE.append(date)
        LISTE_INTERMEDIAIRE.append(heure)
        LISTE_PARAMETRE.append(LISTE_INTERMEDIAIRE)
        
        with open('Produit.json','w+') as FICHIER:
            json.dump(LISTE_PARAMETRE,FICHIER)
            print(Fore.GREEN +"Le produit à été bien ajouter en stock "+Style.RESET_ALL)
        return LISTE_PARAMETRE


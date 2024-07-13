from produits_dispo import * 
from datetime import datetime
import time 
# from main import LISTE_PRODUITS
from colorama import Fore,Style

def charger_rapport():
    with open ('Produit.json','r') as FICHIER: 
        LISTE_PRODUITS = json.load(FICHIER)
    return LISTE_PRODUITS

def ouvrir_rapport():
    with open('rapport_vente.json','r') as FICHIER:
        LISTE_RAPPORT = json.load(FICHIER)
    return LISTE_RAPPORT

def sauvegarder_rapport(LISTE_PARAMETRE):
      LISTE_RAPPORT_SAUVE = ouvrir_rapport()
      LISTE_RAPPORT_SAUVE.append(LISTE_PARAMETRE)
      
      with open('rapport_vente.json','w+') as FICHIER:
            json.dump(LISTE_RAPPORT_SAUVE,FICHIER)
            print(Fore.GREEN +"\t\tL'évément a été bien enregistré "+Style.RESET_ALL)
    

def Enregistrer_vente():
    LISTE_PRODUITS_RAPPORT = charger_rapport()
    RESULTAT = []
    COMPTEUR = 0
    VERIFICATEUR = 0
    Afficher_Produit_dispo(LISTE_PRODUITS_RAPPORT)
   
    while VERIFICATEUR == 0: 
        NOM_CLIENT  = input("Entrez le nom du client : ")
        NOM_PRODUIT = input("Entrez le nom du produit : ")
        QUANTITE_VENDU = int(input("Entrez la quantité : "))
        
        if NOM_PRODUIT.isnumeric():
            print(Fore.RED +f"Attention 🚨🚨 le nom du produit doit être une chaîne de carastères 😯"+Style.RESET_ALL)

        elif NOM_CLIENT.isnumeric():
             print(Fore.RED +f"Attention 🚨🚨 le nom du client  doit être une chaîne de carastères 😯"+Style.RESET_ALL)

        elif NOM_CLIENT=="" or NOM_PRODUIT =="" or QUANTITE_VENDU =="":
            print(Fore.RED +f"""
                   Attention  🚨🚨 tout les champs sont obligatoire
                   VEUILLEZ LES REMPLIR SVP  😯"""+Style.RESET_ALL)
        elif QUANTITE_VENDU <= 0:
                 print(Fore.RED +f"""Attention 🚨🚨 le nombre min pour la quantité  c'est 1 😯"""+Style.RESET_ALL)
        elif  len(NOM_CLIENT) < 3 or len(NOM_PRODUIT) < 3  : 
             print(Fore.RED +f"MAUVAISE VALEUR 🚨🚨 😯"+Style.RESET_ALL)
        else:
            VERIFICATEUR = 1

    for PRODUIT in LISTE_PRODUITS_RAPPORT:
        if PRODUIT[1] == NOM_PRODUIT and int(PRODUIT[2]) >= 0  and int(PRODUIT[3]) >= QUANTITE_VENDU :
            COMPTEUR +=1
            id = len(ouvrir_rapport())+1
            heure = time.strftime('%H:%M:%S')
            date = datetime.today().strftime('%d/%m/%Y')
            RESULTAT.append(id)
            RESULTAT.append(NOM_CLIENT.capitalize())
            RESULTAT.append(NOM_PRODUIT)
            RESULTAT.append(QUANTITE_VENDU)
            RESULTAT.append(date)
            RESULTAT.append(heure)
            PRODUIT[3] = (PRODUIT[3] - QUANTITE_VENDU)

            with open('Produit.json','w+') as FICHIER:
                json.dump(LISTE_PRODUITS_RAPPORT,FICHIER)

            sauvegarder_rapport(RESULTAT)

    if COMPTEUR == 0:
        print(Fore.RED +"""
              echec de vente 🚨 
              soit :
              le produit ne pas disponible,
              la quantité vendu est supérieure à la Quantité en stock pour ce produit, 
              """+Style.RESET_ALL)
      



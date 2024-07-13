import json
from colorama import Fore,Style
from datetime import datetime
import time 

def modification ():
    with open ('Produit.json','r') as FICHIER: 
        LISTE_MODIFICATION = json.load(FICHIER)
        

    VERIFICATEUR = 0
    while VERIFICATEUR == 0: 
        CHOIX_UTILISATEUR = input("Entrer le nom du produit à modifier : ")
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
    indice = 0
    for PRODUIT in LISTE_MODIFICATION:
        indice += 1 
        if PRODUIT[1].lower() == CHOIX_UTILISATEUR.lower():
            COMPTEUR +=1 
            RESULTAT.append(PRODUIT)   
    

    if COMPTEUR == 0:
        print(Fore.RED +f"Aucun produit porte le nom  {CHOIX_UTILISATEUR} 😯"+Style.RESET_ALL)
    else:
        print("VOILA LES INFORMATIONS SUR LE PRODUIT QUE VOUS SOUHAITEZ LE MODIFIER \n")
        for PRODIT_DISP in RESULTAT:
            
            print(f"ID : {PRODIT_DISP[0]} | NOM PRODUIT : {PRODIT_DISP[1]} | PRIX : {PRODIT_DISP[2]} | QUANTITE EN STOCK :  {PRODIT_DISP[3]}")
    print("ENTREZ LES NOUVELLES INFORMATIONS \n")
    VERIFICATEUR = 0
    while VERIFICATEUR == 0:    
            NOM_PRODUIT  = input("Entrez le nom du produit : ")
            PRIX_PRODUIT  = int(input("Entrez le prix du produit : "))
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
            elif PRIX_PRODUIT <= 0 or  QUANTITE_PRODUIT <= 0:
                 print(Fore.RED +f"Attention 🚨🚨 le nombre min pour le prix et la quantité c'est 1 😯"+Style.RESET_ALL)
            else:
                 VERIFICATEUR = 1 
    
    LISTE_MODIFICATION[indice-1][1] = NOM_PRODUIT
    LISTE_MODIFICATION[indice-1][2] = PRIX_PRODUIT
    LISTE_MODIFICATION[indice-1][3] =  QUANTITE_PRODUIT
    heure = time.strftime('%H:%M:%S')
    date = datetime.today().strftime('%d/%m/%Y')
    LISTE_MODIFICATION [indice-1][4] = date
    LISTE_MODIFICATION [indice-1][5]= heure 

    with open('Produit.json','w+') as FICHIER:
            json.dump(LISTE_MODIFICATION,FICHIER)

    print(Fore.GREEN +f"la modification du produit à été effectuée avec succès "+Style.RESET_ALL)

     



    

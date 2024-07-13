
import sys
from colorama import Fore,Style
from Ajout_Produits import *
from Afficher_Produits import *
from Rechercher_Produit import *
from enregistrer_vente import *
from Affiche_Ventes import *
from vente_client import *
from Rapport import *
from Charger_donnees import * 
from modiffier import * 


LISTE_PRODUITS = []

with open ('Produit.json','r') as FICHIER: 
     LISTE_PRODUITS = json.load(FICHIER)

MENU = """ MENU PRINCIPAL 
            1. Ajouter produit
            2. Afficher produits
            3. Rechercher produit
            4. Enregistrer vente
            5. Afficher ventes
            6. Ventes par client
            7. Générer rapport de ventes
            8. Modification produit
            9. Charger données
            10. Quitter
            ❓ Votre choix : """
MENU_CHOICES = ["1","2","3","4","5","6","7","8","9","10"]


while True:    
    CHOIX_UTILISATEUR = ""
    while CHOIX_UTILISATEUR not in MENU_CHOICES:
        CHOIX_UTILISATEUR = input(MENU)
        if CHOIX_UTILISATEUR not in MENU_CHOICES:
            print(Fore.RED +"\t\tVeuillez Choisir une option valide..."+Style.RESET_ALL)
    if CHOIX_UTILISATEUR == "1":
        ajouter_Produits(LISTE_PRODUITS)
    elif CHOIX_UTILISATEUR =="2":
        Afficher_Produit(LISTE_PRODUITS)
    elif CHOIX_UTILISATEUR == "3":
        rechercher_produit()
    elif CHOIX_UTILISATEUR =="4":
        Enregistrer_vente()
    elif CHOIX_UTILISATEUR  == "5":
        afficher_vente()
    elif CHOIX_UTILISATEUR =="6":
        vente_client ()
    elif CHOIX_UTILISATEUR == "7":
        rapport()
    elif CHOIX_UTILISATEUR =="8":
        modification()
    elif CHOIX_UTILISATEUR =="9":
        charger_donnees()
        print("\t\tchargement de données terminer")
    elif CHOIX_UTILISATEUR  == "10":
        print("\t\tÀ Bientôt ...")
        sys.exit()
    

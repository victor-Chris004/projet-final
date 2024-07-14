from articles import*
from vente import*
from sauvegarde import *

def menu_principal():
    print("1. Ajouter produit")
    print("2. Afficher produits")
    print("3. Rechercher produit")
    print("4. Supprimer produit")
    print("5. afficher ventes")
    print("6. ventes par client")
    print("7. Quitter")
    return input("Choisissez une option: ")

def main():
    #charger_donnees()
    while True:
        choix = menu_principal()
        if choix == '1':
            ajoutArticle()
        elif choix == '2':
            for articles in AfficherArticle():
                print(articles)
        elif choix == '3':
            Rechercher_par_Nom()
        elif choix == '4':
            supprimerDouble()
        elif choix == '5':
            afficher_ventes()
        elif choix == '6':
            ventes_par_client()
        elif choix == '7':
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
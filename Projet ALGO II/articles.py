import json
import os
articles = []

nom_fichier = "articles.json"
noms_articles_existants = []

if os.path.exists(nom_fichier):
    with open(nom_fichier,'r') as fichier:
        try:
            articles = json.load(fichier)
        except json.JSONDecodeError:
                articles = []

def validationNumArticle(idArt):
    #print("Ecrivez vous meme le code")
    list = idArt.isdecimal()
    while list == False:
        prixArt = input("Erreur du num")
        list = prixArt.isdecimal()
        if list == True:
           break

def validationNomArticle(nomArt):
    #print("Ecrivez vous meme le code")
    list = nomArt.isnumeric()
    while list == True:
        prixArt = input("Erreur de l'article")
        list = prixArt.isnumeric()
        if list == False:
            break    

def validationPrixArticle(prixArt):
    #print("Ecrivez vous meme le code")
    list = prixArt.isdecimal()
    while list == False:
        prixArt = input("Erreur du prix")
        list = prixArt.isdecimal()
        if list == True:
            break

def validationQteArticle(qteArt):
    #print("Ecrivez vous meme le code")
    list = qteArt.isnumeric()
    while list == False:
        prixArt = input("Erreur de la qte")
        list = prixArt.isnumeric()
        if list == True:
            break

def ajoutArticle():
    global idArt
    global nomArt
    global prixArt
    global qteArt

    idArt = input("saisir le numero de l'article: ")
    validationNumArticle(idArt)
    nomArt = input("saisir le nom de l'article: ")
    validationNomArticle(nomArt)
    prixArt = input("saisir le prix de l'article: ")
    validationPrixArticle(prixArt)
    qteArt = input("saisir la quantite de l'article: ")
    validationQteArticle(qteArt)

    article = {"Id":idArt , "nom":nomArt , "prix":prixArt , "quantite":qteArt}

    try:
        with open("articles.json","r") as fichier:
            articles = json.load(fichier)
    except FileNotFoundError:
        articles = []
    articles.append(article)
    with open("articles.json","w") as fichier:
        json.dump(articles,fichier, indent=3 )


def AfficherArticle():
    if len(articles) == 0:
        return "\nAucun article disponible ! \n"
    else:
        return articles

def Rechercher_par_Nom():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
    verification = input("saisir le nom de l'article rechecher: ")
    i = 0
    while (i <= len(articles) - 1):
        if verification == articles[i]["nom"]:
            print("nom:",articles[i]['nom'] ,"prix:",articles[i]['prix'] ,"quantité:",articles[i]["quantite"])
            return i
        elif (i != len(articles)-1):
            i += 1
        else:
            print("Erreur de l'articles")
            break

def Rechercher_par_ID():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
    verification = input("saisir l'ID de l'article rechecher: ")
    verification = validationQteArticle(verification)
    verification = int(verification)
    i = 0
    while (i <= len(articles) - 1):
        if verification == articles[i]["nomArt"]:
            print("nom:",articles[i]['nom'] ,"prix:",articles[i]['prix'] ,"quantité:",articles[i]["quantite"])
            return i - 1
        elif (i != len(articles)-1):
            i += 1
        else:
            print("Erreur du numero")
            break

def supprimerDouble():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
    supprimer = Rechercher_par_Nom()
    del articles[supprimer]
    with open("articles.json","w") as fichier:
        json.dump(articles,fichier, indent=1 ) 

def charger_produits():
    global produits
    try:
        with open('produits.json', 'r') as f:
            produits = json.load(f)
    except FileNotFoundError:
        produits = []

def mettre_a_jour_stock(produit_nom, quantite_vendue):
    for produit in produits:
        if produit['nom'].lower() == produit_nom.lower():
            produit['quantite'] -= quantite_vendue
            break

def verifier_stock(produit_nom, quantite_vendue):
    for produit in produits:
        if produit['nom'].lower() == produit_nom.lower():
            return produit['quantite'] >= quantite_vendue
    return False

def sauvegarder_produits():
    with open('produits.json', 'w') as f:
        json.dump(produits, f)

# Charger les produits au démarrage
charger_produits()
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

# Permet de verifier que le nom de l'articles ne contient pas des caractere numerique 
def validationNomArticle(nomArt):
    list = nomArt.isnumeric()
    while list == True:
        prixArt = input("Erreur de l'article")
        list = prixArt.isnumeric()
        if list == False:
            break    

# verifie que le prix de l'article ne contient pas des caractere alphabetique
def validationPrixArticle(prixArt):
    list = prixArt.isdecimal()
    while list == False:
        prixArt = input("Erreur du prix")
        list = prixArt.isdecimal()
        if list == True:
            break
# verifie que la quantite de l'articles ne contient pas des caractere alphabetique
def validationQteArticle(qteArt):
    list = qteArt.isnumeric()
    while list == False:
        prixArt = input("Erreur de la qte")
        list = prixArt.isnumeric()
        if list == True:
            break
# Permet d'ajouter un produit dans la base de donnee
def ajoutArticle():
    global articles
    global nomArt
    global prixArt
    global qteArt
    #incremente automatiquement le numero de produit
    idArt = 0
    idArt = len(articles) + 1
    nomArt = input("saisir le nom de l'article: ")
    validationNomArticle(nomArt)
    prixArt = input("saisir le prix de l'article: ")
    validationPrixArticle(prixArt)
    qteArt = input("saisir la quantite de l'article: ")
    validationQteArticle(qteArt)
    # Verifie si un produit qu'on veut ajouter existe deja
    if nomArt in articles :
        print(f"Le client {nomArt} existe deja dans la base de donnée")
    else:
        article = {
            "Id":idArt ,
            "nom":nomArt ,
            "prix":prixArt , 
            "quantite":qteArt
            }

    try:
        with open("articles.json","r") as fichier:
            articles = json.load(fichier)
    except FileNotFoundError:
        articles = []
    articles.append(article)
    with open("articles.json","w") as fichier:
        json.dump(articles,fichier, indent= 4 )

# Permet de vusualiser tous les articles que contient le fichier Json
def AfficherArticle():
    with open("articles.json","r") as fichier:
            articles = json.load(fichier)

    if (len(articles) == 0) and (articles == []):
        return "\n Aucun article disponible ! \n"
    else:
        with open('articles.json', 'r') as file :
            vu = json.load(file)
            print(vu)
# Fait une recherche de nom dans la base de donnee
def Rechercher_par_Nom():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
    verification = input("saisir le nom de l'article rechecher: ")
    i = 0
    while (i <= len(articles) - 1):
        if verification == articles[i]["nom"]:
            print("nom:",articles[i]['nom'] ,
            "prix:",articles[i]['prix'] ,
            "quantité:",articles[i]["quantite"])
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
# permet de supprimer le doublon de la base de donnee
def supprimerDouble():
    with open('articles.json','r') as fichier:
        articles = json.load(fichier)
    supprimer = Rechercher_par_Nom()
    del articles[supprimer]
    with open("articles.json","w") as fichier:
        json.dump(articles,fichier, indent=1 ) 

def charger_articles():
    global articles
    try:
        with open('articles.json', 'r') as f:
            articles = json.load(f)
    except FileNotFoundError: 
        articles = []
#Permet d'actualiser le donnees de la base de donnee
def mettre_a_jour_stock(produit_nom, quantite_vendue):
    for produit in articles:
        if produit['nom'].lower() == produit_nom.lower():
            produit['quantite'] -= quantite_vendue
            break

def verifier_stock(produit_nom, quantite_vendue):
    for produit in articles:
        if produit['nom'].lower() == produit_nom.lower():
            return produit['quantite'] >= quantite_vendue
    return False


# Charger les articles au démarrage
charger_articles()
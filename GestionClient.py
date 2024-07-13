import json
import os

Clients = {}

def validation_Nom(NomClient):
    if NomClient == '':
        NomClient = input("vous ne pouvez pas enregistrer des clients sans nom \nSaisir le Nom du client: ")
    # verifie si le Nom du client contient des caractere numerique 
    test = NomClient.isalpha()
    while test == False:
        NomClient = input("Veuillez entrer un nom du client sans caractère : ")
        test = NomClient.isalpha()
        if test == True:
            break

def validationNumClient(NumClient):
    if NumClient == 0:
        NumClient = input("Entrez la quantité de l'article enregistrer: ")
    # verifie que le numero du client ne contient pas des caractere alphabetique
    test = NumClient.isnumeric()
    while test == False:
        NumClient = input("Entrez une valeur numerique: ")
        test = NumClient.isnumeric()
        if test == True:
            break

def ajoutClient():
    MatClient = 0
    MatClient = len(Clients) + 1
    NomClient = input("Saisir le nom du client: ")
    NumClient = input("Saisir le numéro de telephone du client: ")
    AdresseClient = input("Saisir l'adresse du client: ")
    if NomClient in Clients and NumClient in Clients:
        print(f"Le client {NomClient} existe deja dans la base de donnée")
    else:
        Clients[NomClient] = {
            'MatClient' : MatClient,
            'NumClient' : NumClient,
            'AdresseClient' : AdresseClient
            }
    SauvegardeClients(Clients)
    return NomClient

def SauvegardeClients(Clients):
    with open('BDclients.json','w+') as file:
        json.dump(Clients, file, indent=3)

def ListeClient():
    with open('BDclients.json', 'r+') as file :
        data = json.load(file)
        print(data)
    
def deleteClient():
    with open('BDclients.json', 'r') as file :
        data = json.load(file)  
    NomClient = input("Saisir le Nom du client que vous souhaitez supprimer ")
    if NomClient in data == True:
        print("yes")
        del BDclients['NomClient']

    with open('BDclients.json','w+') as file:
        json.dump(Clients, file, indent=3)
    
def rechercherClientNOM():
    with open('BDclients.json', 'r') as db:
            data = json.load(db)
    verification = input("saisissez le nom de du client que vous rechercher : \n ")
    i=0
    while (i <= len(Clients)-1):
        if verification == data[i] ["NomClient"]:
              #print(" Quantité d'article : ", articles[i]['qteArticle'],"\n nom de l'article : ", articles[i]['nomArt'],"\n le prix de l'article : ", articles[i]['prix'])
              print('yes')
              return i
        elif (i != len(Clients)-1):
             i += 1
        else:    
            print("cet client n'y est pas ")
            break
 
def rechercherClientMat():
    with open('BDclient.json', 'r') as bd:
            articles = json.load(bd)
    verification = input("saisissez la valeur de le Matricule du client: ")
    verification= validationQteArticle(verification)
    verification=int(verification)
    i=0
    while (i <= len(articles)-1):
        if verification == articles[i] ['NumArticle']:
              print(" Quantité d'article : ", articles[i]['qteArticle'],"\n nom de l'article : ", articles[i]['nomArt'],"\n le prix de l'article : ", articles[i]['prix'])
              return i - 1
        elif (i != len(articles)-1):
             i += 1
        else:    
            print("le numéro de l'article n'y est pas ")
            break

#deleteClient()
#rechercherClientNOM()
# coding: utf8

import csv

def charger_usagers(nom_fichier):
    retour = {}
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        user   = {}
        iduser = ligne[0]
        user['nom']            = ligne[1]
        user['prenom']         = ligne[2]
        user['date_naissance'] = ligne[3]
        ## strip supprimme les caractères en trop en fin de chaine
        ## ('\0', '\n', ' ')
        user['emprunts']       = [x.strip() for x in ligne[4].split(',')]
        retour[iduser]         = user
    f.close()
    return retour

def charger_livres(nom_fichier):
    retour = {}
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        livre   = {}
        idlivre = ligne[0]
        livre['titre']     = ligne[1]
        livre['auteur']    = ligne[2]
        livre['mots_cles'] = [x.strip() for x in ligne[3].split(',')]
        retour[idlivre]    = livre
    f.close()
    return retour

def charger_emprunts(nom_fichier):
    retour = {}
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        emprunt     = {}
        idemprunt   = ligne[0]
        emprunt['livre']       = ligne[1]
        emprunt['dateEmprunt'] = ligne[2]
        emprunt['dateAttendu'] = ligne[3]
        emprunt['dateRetour']  = ligne[4]
        if emprunt['dateRetour'] == "Néant":
            emprunt['dateRetour'] = None
        retour[idemprunt] = emprunt
    f.close()
    return retour


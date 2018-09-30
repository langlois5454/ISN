# coding: utf8

##liste d'usagers
##id, nom, prénom, date naissance, liste des emprunts
##
##liste des emprunts = [id_emprunt,id_livre,debut,fin_attendue,fin_reelle = None]*
##
##
##livres
##(id, titre, auteur, liste_mots_cles)
##
##
##Exos
##Y- charger à partir de fichier (csv) x3
##D- changer le nom d'un usager à partir de son id
##Y- ajoyter un mot clé à un livre
##D- les majeurs (1 liste)
##Y- les en retard (1 liste)
##D- les livres sur un mot clé en paramètre (1 liste)
##Y- titres des livres actuellement empruntés (2 listes)
##D- le livre le plus récemment rendus de X (2 listes)
##Y- liste des personnes ayant emprunté le livre d'iditifiant X (2 listes)
##D- liste des personnes ayant emprunté le livre de titre X (3 listes)
##Y- la liste des mots clés (sans doublon) emprunté par X --> enjeu sociétaux
##DY- (bonus) le nombre max de livres empruntés en même temps par quelqu'un
##Y- fiche identité usager (3 listes)

from datetime import datetime
import utils
import csv

## chargement

def charger_usagers(nom_fichier):
    retour = []
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        ligne[0] = int(ligne[0])
        ligne.append([])
        retour.append(ligne)
    f.close()
    return retour

def charger_livres(nom_fichier):
    retour = []
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        livre = ligne[0:-3]
        livre[0] = int(livre[0])
        motscles = [x for x in ligne[-3:] if x != "Néant"]
        livre.append(motscles)
        retour.append(livre)
    f.close()
    return retour
    
def charger_emprunts(nom_fichier):
    retour = []
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        ligne[0] = int(ligne[0])
        ligne[1] = int(ligne[1])
        if ligne[-1] == "Néant":
            ligne[-1] = None
        retour.append(ligne)
    f.close()
    return retour

def charger_emprunts_usagers(usagers,nom_fichier):
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        id_usager = int(ligne[0])
        id_emprunt = int(ligne[1])
        for i in range(len(usagers)):
            if usagers[i][0] == id_usager:
                usagers[i][-1].append(id_emprunt)
    f.close()








def changer_nom_usager(liste_usagers,id_usager,nv_nom):
    """
    change le nom de l'usage d'id id_usager en nv_nom
    """
    for i in range(len(liste_usagers)):
        if liste_usagers[i][0] == id_usager:
            liste_usagers[i][1] =  nv_nom



def lister_usagers_majeurs(usagers):
    """
    retourne la liste des identifiants des usagers
    majeurs
    """
    return [u[0] for u in usagers if utils.majeur(u[3])]
        
def lister_livres_sur_mot_cle(livres,mot_cle):
    """
    retourne la liste des identifiants des livres
    associés au mot-clé mot_cle
    """
    return [l[0] for l in livres if mot_cle in l[3]]

def livre_plus_recemment_rendu(emprunts,liste_usagers,id_usager):
    """
    retourne l'id du livre le plus récemment rendu par l'usager d'id id_usager
    """
    usager = None
    for u in liste_usagers:
        if u[0] == id_usager:
            usager = u
    liste_emprunts = usager[4]
    ##(id_livre,debut,fin_attendue,fin_reelle = None)
    dernier_emprunt_rendu = None
    for id_e in liste_emprunts:
        ## (id_emprunt,id_livre,debut,fin_attendue,fin_reelle = None)
        for e in emprunts:
            if e[0] == id_e:
                if e[-1] != None:
                    if dernier_emprunt_rendu == None:
                        dernier_emprunt_rendu = e
                    else:
                        if utils.date_posterieure(dernier_emprunt_rendu[-1],e[-1]):
                            dernier_emprunt_rendu = e

    if dernier_emprunt_rendu == None:
        return None
    else:
        return dernier_emprunt_rendu[1]             
                

## liste des personnes ayant emprunté le livre de titre X               
def liste_usagers_ayant_emprunte_livre_titre_X(usagers,livres,emprunts,titre):
    """
    retourne la liste des id des usagers ayany emprunté le livre de titre 'titre'
    """
    ## recherche du livre
    id_livre = [l[0] for l in livres if l[1] == titre][0]
    ## recherche des emprunts
    emps = [e[0] for e in emprunts if e[1] == id_livre]
    ## recherche des usagers
    usgs = []
    for u in usagers:
        emprunts_u = u[4]
        for e in emprunts_u:
            if e in emps:
                usgs.append(u[0])
    return list(set(usgs)) ## pour supprimer les doublons
            

## main

usagers = charger_usagers("usagers.csv")
livres = charger_livres("livres.csv")
emprunts = charger_emprunts("emprunts.csv")
charger_emprunts_usagers(usagers,"emprunts_usagers.csv")

print("Les usagers")
print("=================================")
for u in usagers:
    print("   ",u)
print("")
print("Les livres")
print("=================================")
for l in livres:
    print("   ",l)
print("")
print("Les emprunts")
print("=================================")
for e in emprunts:
    print("   ",e)
print("")



changer_nom_usager(usagers,2,"Bine")
print(usagers)

print(lister_usagers_majeurs(usagers))

print(lister_livres_sur_mot_cle(livres,"Policier"))

print(livre_plus_recemment_rendu(emprunts,usagers,1))

print(liste_usagers_ayant_emprunte_livre_titre_X(usagers,livres,emprunts,"Le chien de Baskerville"))

      

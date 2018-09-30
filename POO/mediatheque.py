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
    retour = {}
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        user   = {}
        iduser = ligne[0]
        user['nom']            = ligne[1]
        user['prenom']         = ligne[2]
        user['date_naissance'] = ligne[3]
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
        idlivre = int(ligne[0])
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
        emprunt['livre']       = int(ligne[1])
        emprunt['dateEmprunt'] = ligne[2]
        emprunt['dateAttendu'] = ligne[3]
        emprunt['dateRetour']  = ligne[4]
        if emprunt['dateRetour'] == "Néant":
            emprunt['dateRetour'] = None
        retour[idemprunt] = emprunt
    f.close()
    return retour

def changer_nom_usager(liste_usagers,id_usager,nv_nom):
    """
    change le nom de l'usage d'id id_usager en nv_nom
    """
    liste_usagers[id_usager]['nom'] = nv_nom
    
def lister_usagers_majeurs(usagers):
    """
    retourne la liste des identifiants des usagers
    majeurs
    """
    return [u for u,v in usagers.items() if utils.majeur(v['date_naissance'])]
        
def lister_livres_sur_mot_cle(livres,mot_cle):
    """
    retourne la liste des identifiants des livres
    associés au mot-clé mot_cle
    """
    return [l for l,m in livres.items() if mot_cle in m['mots_cles']]

def livre_plus_recemment_rendu(emprunts,liste_usagers,id_usager):
    """
    retourne l\'identifiant du livre le plus récemment rendu par l'usager d'id id_usager
    """
    liste_emprunts = liste_usagers[id_usager]['emprunts']
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
                

# ## liste des personnes ayant emprunté le livre de titre X               
# def liste_usagers_ayant_emprunte_livre_titre_X(usagers,livres,emprunts,titre):
#     """
#     retourne la liste des id des usagers ayany emprunté le livre de titre 'titre'
#     """
#     ## recherche du livre
#     id_livre = [l[0] for l in livres if l[1] == titre][0]
#     ## recherche des emprunts
#     emps = [e[0] for e in emprunts if e[1] == id_livre]
#     ## recherche des usagers
#     usgs = []
#     for u in usagers:
#         emprunts_u = u[4]
#         for e in emprunts_u:
#             if e in emps:
#                 usgs.append(u[0])
#     return list(set(usgs)) ## pour supprimer les doublons
            

def nb_livres_empruntes(usagers,id_usager):
    return len(usagers[id_usager]['emprunts'])

## main
if __name__ == '__main__':
    usagers_test = {'user1': {'nom':'Nonyme', 'prenom':'Alphonse', 'date_naissance':'01/01/2003', 'emprunts':['emprunt_1','emprunt_2','emprunt_3']}, 'user2': {'nom' : 'Camion', 'prenom':'Bo', 'date_naissance':'18/03/1954', 'emprunts':['emprunt_4']}}
    for user in usagers_test:
        print(nb_livres_empruntes(usagers_test,user))

    usagers = charger_usagers("usagers.csv")
    livres = charger_livres("livres.csv")
    emprunts = charger_emprunts("emprunts.csv")

    print("Les usagers")
    print("=================================")
    for u,v in usagers.items():
        print("   ",u,v)
    print("")

    print("Les livres")
    print("=================================")
    for l,m in livres.items():
        print("   ",l,m)
    print("")

    print("Les emprunts")
    print("=================================")
    for e,f in emprunts.items():
        print("   ",e,f)
    print("")

    changer_nom_usager(usagers,'user2','Bine')
    print(usagers)

    print(lister_usagers_majeurs(usagers))

    print(lister_livres_sur_mot_cle(livres,"Policier"))

    # print(livre_plus_recemment_rendu(emprunts,usagers,1))

    # print(liste_usagers_ayant_emprunte_livre_titre_X(usagers,livres,emprunts,"Le chien de Baskerville"))

      

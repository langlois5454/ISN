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
##Y- ajouter un mot clé à un livre
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

def changer_nom_usager(dict_usagers,id_usager,nv_nom):
    """
    change le nom de l'usage d'id id_usager en nv_nom
    """
    dict_usagers[id_usager]['nom'] = nv_nom

def ajouter_mot_cle(dict_livres,id_livre,nv_mot_cle):
    """
    ajoute le mot cle nv_mot_cle au livre d'id id_livre
    """
    dict_livres[id_livre]['mots_cles'].append(nv_mot_cle)

def lister_usagers_majeurs(dict_usagers):
    """
    retourne la liste des identifiants des usagers
    majeurs
    """
    return [u for u,v in dict_usagers.items() if utils.majeur(v['date_naissance'])]
        
def lister_prets_en_retard(dict_emprunts):
    """
    retourne la liste des identifiants des prêts en retard
    """
    auj = datetime.today()
    sauj= str(auj.day) + "/" + str(auj.month) + "/" + str(auj.year)
    return [e for e,f in dict_emprunts.items() if f['dateRetour'] == None and utils.date_posterieure(sauj,f['dateAttendu'])]

def lister_livres_sur_mot_cle(dict_livres,mot_cle):
    """
    retourne la liste des identifiants des livres
    associés au mot-clé mot_cle
    """
    return [l for l,m in dict_livres.items() if mot_cle in m['mots_cles']]

def livres_empruntes(dict_emprunts,dict_livres):
    """
    retourne la liste des titres livres en cours d'emprunt
    """
    return [dict_livres[f['livre']]['titre'] for f in dict_emprunts.values() if f['dateRetour'] == None]

def livre_plus_recemment_rendu(emprunts,liste_usagers,id_usager):
    """
    retourne l\'identifiant du livre le plus récemment rendu par l'usager d'id id_usager
    """
    liste_emprunts = liste_usagers[id_usager]['emprunts']
    ##(id_livre,debut,fin_attendue,fin_reelle = None)
    liste_emprunts_tries = sorted(liste_emprunts, key=lambda e: datetime.strptime(emprunts[e]['dateEmprunt'], '%d/%m/%Y'), reverse=True)
    return liste_emprunts_tries[0]

## liste des personnes ayant emprunté le livre d'id X               
def usagers_emprunts_id_livre(dict_usagers,dict_emprunts,id_livre):
    """
    retourne la liste des id des usagers ayant emprunté le livre d'id \'id_livre\'
    """
    ## recherche des emprunts
    emps = [e for e in dict_emprunts.keys() if dict_emprunts[e]['livre'] == id_livre]
    ## recherche des usagers
    usgs = []
    for u in dict_usagers: #equivalent a usagers.keys()
        for e in dict_usagers[u]['emprunts']:
            if e in emps:
                usgs.append(u)
    return list(set(usgs)) ## pour supprimer les doublons

## liste des personnes ayant emprunté le livre de titre X               
def usagers_emprunts_titre_livre(dict_usagers,dict_emprunts,dict_livres,titre):
    """
    retourne la liste des id des usagers ayant emprunté le livre de titre \'titre\'
    """
    ## recherche du livre
    id_livre = [l for l in dict_livres.keys() if dict_livres[l]['titre'] == titre][0]
    ## recherche des emprunts
    emps = [e for e in dict_emprunts.keys() if dict_emprunts[e]['livre'] == id_livre]
    ## recherche des usagers
    usgs = []
    for u in dict_usagers: #equivalent a usagers.keys()
        for e in dict_usagers[u]['emprunts']:
            if e in emps:
                usgs.append(u)
    return list(set(usgs)) ## pour supprimer les doublons

## liste des mots cles
def liste_mots_cles(usagers, emprunts, livres, idusager):
    motscles = []
    for emp in usagers[idusager]['emprunts']:
        motscles.extend(livres[emprunts[emp]['livre']]['mots_cles'])
    return list(set(motscles))

##DY- (bonus) le nombre max de livres empruntés actuellement
def max_emprunts_actuellement(dict_usagers,dict_emprunts):
    ## recherche des emprunts
    emps = [e for e in dict_emprunts.keys() if dict_emprunts[e]['dateRetour'] == None]
    ## recherche du nombre de livres par utilisateur
    users = []
    for u,v in dict_usagers.items():
        nblivres = 0
        for e in v['emprunts']:
            if e in emps:
                nblivres += 1
        users.append((u,nblivres))
    return sorted(users, key=lambda x:x[1], reverse=True)[0][0]

##Y- fiche identité usager (3 listes)
def afficher(usagers, emprunts, livres, idusager):
    res = ''
    res += usagers[idusager]['nom'] + '\n'
    res += usagers[idusager]['prenom'] + '\n'
    res += 'né(e) le: ' + usagers[idusager]['date_naissance'] + '\n'
    res += 'emprunts :\n'
    for e in sorted(usagers[idusager]['emprunts'], key= lambda e: datetime.strptime(emprunts[e]['dateEmprunt'], '%d/%m/%Y')):
        res += livres[emprunts[e]['livre']]['titre'] + ' emprunté le ' + emprunts[e]['dateEmprunt'] + ' '
        if emprunts[e]['dateRetour'] == None:
            res += 'en cours de prêt\n'
        else:
            res += 'rendu le ' + emprunts[e]['dateRetour'] +'\n'
    return res

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

    ajouter_mot_cle(livres,2,"toto")
    print(livres)
    
    print(lister_usagers_majeurs(usagers))

    print(lister_prets_en_retard(emprunts))

    print(lister_livres_sur_mot_cle(livres,"Policier"))

    print(livres_empruntes(emprunts,livres))

    print(livre_plus_recemment_rendu(emprunts,usagers,"user1"))

    print(usagers_emprunts_id_livre(usagers,emprunts,4))

    print(usagers_emprunts_titre_livre(usagers,emprunts,livres,"Le chien de Baskerville"))

    print(liste_mots_cles(usagers,emprunts,livres,"user1"))

    print(afficher(usagers,emprunts,livres,"user1"))

    print(afficher(usagers,emprunts,livres,max_emprunts_actuellement(usagers,emprunts)))

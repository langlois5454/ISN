# coding: utf8

##liste d'usagers
## nom, prénom, date naissance, identifiants des emprunts
##
##liste des emprunts
## id_livre, debut, fin_attendue, fin_reelle = None
##
##liste des livres
## titre, auteur, liste_mots_cles
##

import utils

def nb_livres_empruntes(usagers,id_usager):
    return len(usagers[id_usager]['emprunts'])

if __name__ == '__main__':
    usagers_test = {'user1': {'nom':'Nonyme', 'prenom':'Alphonse', 'date_naissance':'01/01/2003', 'emprunts':['emprunt_1','emprunt_2','emprunt_3']}, 'user2': {'nom' : 'Camion', 'prenom':'Bo', 'date_naissance':'18/03/1954', 'emprunts':['emprunt_4']}}
    for user in usagers_test:
        print(nb_livres_empruntes(usagers_test,user))

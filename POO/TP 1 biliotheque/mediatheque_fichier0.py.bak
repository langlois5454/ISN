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

import utils

def nb_livres_empruntes(usagers,id_usager):
    for u in usagers:
        if u[0] == id_usager:
            return len(u[4])

if __name__ == '__main__':
    usagers_test = [[1,"Nonyme","Alphonse","01/01/2003",[1,2,4]],[2,"Camion","Bo","18/03/1954",[3]]]
    ids = [u[0] for u in usagers_test]
    for id in ids:
        print(nb_livres_empruntes(usagers_test,id))


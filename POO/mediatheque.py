

##liste d'usagers
##id, nom, prénom, date naissance, liste des emprunts
##
##liste des emprunts = (id_livre,debut,fin_attendue,fin_reelle = None)*
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


def changer_nom_usager(liste_usagers,id_usager,nv_nom):
    """
    change le nom de l'usage d'id id_usager en nv_nom
    """
    for i in range(len(liste_usagers)):
        if liste_usagers[i][0] == id_usager:
            liste_usagers[i][1] =  nv_nom

			
			


## main

usagers_test = [[1,"Nonyme","Alphonse","01/01/2000",[1,2]],[2,"Camion","Bo","18/03/1954",[3]]]
emprunts_test = [[1,"12/07/2018","12/08/2018","10/08/2018"],[2,"01/09/2018","01/11/2018",None],[3,"01/09/2018","01/11/2018","01/10/2018"]]
livres_test = [[1,"Nana","Zola Emile",["Drame","Classique","Troisième Empire"]],[2,"La parfum de la dame en noir","Leroux Gaston",["Policier","Rouletabille"]],[3,"Le chien de Baskerville","Doyle Conan",["Policier","Sherlock Holmes"]]]

print(usagers_test)
changer_nom_usager(usagers_test,2,"Bine")
print(usagers_test)

            

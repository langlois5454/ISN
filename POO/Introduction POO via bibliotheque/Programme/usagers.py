# coding utf-8

import csv

class Usagers:
  def __init__(self,nom_fichier):
    self.usagers = {}
    f = open(nom_fichier,"r")
    csv_reader = csv.reader(f,delimiter=';')
    for ligne in csv_reader:
        iduser = ligne[0]
        nom            = ligne[1]
        prenom         = ligne[2]
        date_naissance = ligne[3]        
        self.usagers[iduser] = Usager.Usager(nom,prenom,date_naissance)
        ## les emprunts ne sont pas intégrés
        ## une fois qu'on connaîtra les emprunts, il faudra relire
        ## le fichier afin d'ajouter les emprunts
        ## chaque élément de self.emprunts sera une référence sur un
        ## Emprunt
    f.close()

  def changer_nom_usager(self,idus,nvnom):
    self.usagers[idus].changer_nom(nvnom)



  

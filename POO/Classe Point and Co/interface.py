
#coding utf-8

import feuille
import point

class Interface:
  def __init__(self,f):
    self.feuille = f
    self.etat_dialogue = "menu principal"

  def demander_reponse(self,deb,fin):
    rep = int(input("Que voulez-vous faire ? >>> "))
    while rep < deb or rep > fin:
      print("Mauvais choix !!! Donnez une valeur entre",deb," et",fin)
      rep = int(input("Que voulez-vous faire ? >>> "))
    return rep

  def menu_principal(self):
    ordre = None
    print("")
    print("==== MENU PRINCIPAL ====")
    print("1. Creer point")
    print("2. Bouger point")
    print("3. Créer polygone")
    print("4. Lister contenu feuille")
    print("5. Affichage")
    print("6. Supprimer point")
    print("7. Supprimer polygone")
    print("8. Translater polygone")
    print("9. Nettoyer feuille")
    print("10. Quitter")
    print("========================")
    print("")
    ordre = self.demander_reponse(1,10)

    if ordre == 1:
      self.etat_dialogue = "creer point"
    elif ordre == 2:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 3:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 4:
      print("")
      print(self.feuille)
    elif ordre == 5:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 6:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 7:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 8:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 9:
      print("Désole, cette fonctionnalité n'est pas encore implémentée")
    elif ordre == 10:
      self.etat_dialogue = "fin"
    
    
  def menu_creer_point(self):
    nom = input("Quel nom ? >>> ")
    x = float(input("Abscisse ? >>> "))
    y = float(input("Ordonnée ? >>> "))
    ## il faudrait vérifier que le nom n'a pas été déjà choisi
    self.feuille.ajoute_point(point.PointNomme(x,y,nom))
    self.etat_dialogue = "menu principal"

  def AfficheMenu(self):
    if self.etat_dialogue == "menu principal":
      self.menu_principal()
    elif self.etat_dialogue == "creer point":
      self.menu_creer_point()      

  def Quitter():
    self.etat_dialogue = "fin"


if __name__ == "__main__":
  i = Interface(feuille.Feuille())

  while i.etat_dialogue != "fin":
    i.AfficheMenu()

  print("Bye bye...")
    

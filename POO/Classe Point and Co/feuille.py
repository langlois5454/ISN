import point
import polygone


class Feuille:
  def __init__(self):
    self.points = []
    self.polygones = []

  def ajoute_point(self,p):
    self.points.append(p)

  def ajoute_polygone(self,p):
    self.polygone.append(p)

  def __str__(self):
    res = "Liste des points : \n"
    for p in self.points:
      res = res + "   " + str(p) + " " + super(point.PointNomme,p).__str__()

    res += "\n"

    res += "Liste des polygones :\n"

    for p in self.polygones:
      res += "   " + str(p)

    return res
    

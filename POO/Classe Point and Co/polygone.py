import point

class Polygone:
  def __init__(self,lp):
    self.points = [p for p in lp]

  def __str__(self):
    return "Polygone("+"".join([p.nom for p in self.points])+")"

class Rectangle(Polygone):
  def __init__(self,lp):
    Polygone.__init__(self,lp)

  def __str__(self):
    return "Rectangle("+"".join([p.nom for p in self.points])+")"

class Carre(Rectangle):
  def __init__(self,lp):
    Rectangle.__init__(self,lp)

  def __str__(self):
    return "Carre("+"".join([p.nom for p in self.points])+")"


class Triangle(Polygone):
  def __init__(self,lp):
    Rectangle.__init__(self,lp)

  def __str__(self):
    return "Triangle("+"".join([p.nom for p in self.points])+")"
  

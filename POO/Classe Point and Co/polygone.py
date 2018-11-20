import point

class Polygone:
  def __init__(self,lp):
    self.points = [p for p in lp]

  def __str__(self):
    return "Polygone("+"".join([p.nom for p in self.points])+")"

  def perimetre(self):
      p = 0
      for i in range(len(self.points)-1):
          p += self.points[i].distance(self.points[i+1])
      p += self.points[-1].distance(self.points[0])
      return p

class Rectangle(Polygone):
  def __init__(self,lp):
    Polygone.__init__(self,lp)

  def __str__(self):
    return "Rectangle("+"".join([p.nom for p in self.points])+")"

class Carre(Rectangle):
  def __init__(self,a,c):
    ## centre de rotation = milieu de ac
    x_centre_rotation = (a.x+c.x)/2
    y_centre_rotation = (a.y+c.y)/2
    ## on décale les points pour les centrer sur 0,0
    a_decal = point.Point(a.x-x_centre_rotation,a.y-y_centre_rotation)
    c_decal = point.Point(c.x-x_centre_rotation,c.y-y_centre_rotation)
    ## on opère la rotation
    a_decal_rotate = point.Point(-a_decal.y,a_decal.x)
    c_decal_rotate = point.Point(-c_decal.y,c_decal.x)
    ## on annule le décalage
    b = point.PointNomme(c_decal_rotate.x+x_centre_rotation,c_decal_rotate.y+y_centre_rotation,"#")
    d = point.PointNomme(a_decal_rotate.x+x_centre_rotation,a_decal_rotate.y+y_centre_rotation,"#")
    Rectangle.__init__(self,[a,b,c,d])

  def __str__(self):
    return "Carre("+"".join([p.nom for p in self.points])+")"

  def perimetre(self):
    return self.points[0].distance(self.points[0])*4

  def aire(self):
    return self.points[0].distance(self.points[0])**2


class Triangle(Polygone):
  def __init__(self,lp):
    Polygone.__init__(self,lp)

  def __str__(self):
    return "Triangle("+"".join([p.nom for p in self.points])+")"
  

if __name__ == "__main__":
    x = point.PointNomme(1,0,"A")
    y = point.PointNomme(0,1,"B")
    z = point.PointNomme(-1,0,"C")
    t = point.PointNomme(0,-1,"D")
    p = Polygone([x,y,z,t])
    print(p)
    print(p.perimetre())
    c = Carre(point.PointNomme(0,1,"E"),point.PointNomme(1,0,"G"))
    print(c.points[3].x,c.points[3].y)
                         

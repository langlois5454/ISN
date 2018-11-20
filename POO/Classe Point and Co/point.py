import math

class Point:
    '''Classe Point permettant de manipuler un point 2D'''
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
    
    def copie(self):
        return Point(self.x,self.y)

    def distance(self,p):
        return math.sqrt((self.x-p.x)**2+(self.y-p.y)**2)
    
    def symetrique_origine(self):
        '''Point.symetrique_origine() --> Point -- renvoie le symétrique d'un Point par rapport à l'origine '''
        return Point(-self.x,-self.y)

class PointNomme(Point):
    def __init__(self,x,y,nom):
        Point.__init__(self,x,y)
        self.nom = nom
        
    def __str__(self):
        return self.nom
    
if __name__ == "__main__":
    A = PointNomme(1,2,"Mon nom est A")
    print(A)
    print(A.nom)
    print(A.x)
    print(super(PointNomme,A).__str__())
    l = [Point(2.3,5.6),PointNomme(2,8,"Z"),Point(5,9)]
    for x in l:
        print(x)

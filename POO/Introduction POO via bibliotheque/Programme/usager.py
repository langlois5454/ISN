# coding utf-8

class Usager:
    def __init__(self,nom,prenom,naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = naissance
        self.emprunts = []

if __name__ == '__main__':
    u1 = Usager("Nonyme","Albert","17/09/2000")
    print(u1.nom)
    u1.nom = "Toto"
    print(u1.nom)
    u1.emprunts.append("23")
    print(u1.emprunts)
    

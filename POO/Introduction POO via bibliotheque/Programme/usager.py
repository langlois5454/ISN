# coding utf-8

from datetime import datetime


class Usager:
    def __init__(self,nom,prenom,naissance,dn):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = naissance
        self.date_renouvellement = dn
        self.emprunts = []

    def age(self):
        """ retour l'age de l'usager """
        aujourdhui = datetime.now()
        dn = datetime.strptime(self.date_naissance, '%d/%m/%Y')
        retour = aujourdhui.year - dn.year
        ## on enlève 1 an si la date actuelle est antérieure à
        ## celle de l'anniversaire
        if aujourdhui.month < dn.month:
            retour -= 1
        else:
            if aujourdhui.month == dn.month and aujourdhui.day < dn.day:
                retour -= 1
        return retour

    def renouveller(self):
        aujourdhui = datetime.now()
        self.date_renouvellement = str(aujourdhui.day) +"/" + str(aujourdhui.month) + "/" + str(aujourdhui.year + 1)

    def changer_nom(self,nvnom):
        self.nom = nbnom

if __name__ == '__main__':
    u1 = Usager("Nonyme","Albert","17/09/2000","11/12/2018")
    print(u1.nom)
    u1.nom = "Toto"
    print(u1.nom)
    u1.emprunts.append("23")
    print(u1.emprunts)
    print("L'usager, né le {}, a {} an(s)".format(u1.date_naissance,u1.age()))
    print(u1.date_renouvellement)
    u1.renouveller()
    print(u1.date_renouvellement)
     

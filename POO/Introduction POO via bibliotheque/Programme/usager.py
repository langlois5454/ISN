# coding utf-8

from datetime import datetime


class Usager:
    def __init__(self,nom,prenom,naissance):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = naissance
        aujourdhui = datetime.now()
        self.date_renouvellement = "{}/{}/{}".format(aujourdhui.day,aujourdhui.month,aujourdhui.year)
        self.renouveller()
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

    def renouvellement(self):
        aujourdhui = datetime.now()
        d = datetime.strptime(self.date_renouvellement, '%d/%m/%Y')
        if aujourdhui > d:
            return True
        else:
            return False

    def renouveller(self):
        """ décale la date de renouvellement d'un an """
        dr = self.date_renouvellement
        annee = int(dr[-4:])
        jour_mois = dr[:-4]
        self.date_renouvellement = jour_mois + str(annee + 1)

    def changer_nom(self,nvnom):
        self.nom = nvnom

    def ajouter_emprunt(self,emp):
        self.emprunts.append(emp)

    def majeur(self):
        dn = datetime.strptime(self.date_naissance, '%d/%m/%Y')
        date_majeur = datetime(dn.year+18,dn.month,dn.day)
        aujourdhui = datetime.now()
        duree = aujourdhui-date_majeur
        return duree.days >= 0       



if __name__ == '__main__':
    u1 = Usager("Nonyme","Albert","17/09/2000")
    print(u1.nom)
    u1.nom = "Toto"
    print(u1.nom)
    u1.emprunts.append("23")
    print(u1.emprunts)
    print("L'usager, né le {}, a {} an(s)".format(u1.date_naissance,u1.age()))
    print(u1.date_renouvellement)
    u1.renouveller()
    print(u1.date_renouvellement)
     

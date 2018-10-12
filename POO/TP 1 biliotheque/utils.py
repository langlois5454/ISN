# coding: utf8

from datetime import datetime

def majeur(date_naissance):
    """
    renvoie True si, aujourd'hui une personne née le date_naissance
    est majeure, False, sinon
    La date est donnée sous la fourme "JJ/MM/AAAA"
    """
    date_naissance = datetime.strptime(date_naissance, '%d/%m/%Y')
    date_majeur = datetime(date_naissance.year+18,date_naissance.month,date_naissance.day)
    aujourdhui = datetime.now()
    duree = aujourdhui-date_majeur
    return duree.days >= 0

def date_posterieure(d1,d2):
    """
    renvoie True si la date d2 (sous la forme "DD/MM/YYYY")
    est postérieure (ou égale) à la date d1
    """
    da1 = datetime.strptime(d1, '%d/%m/%Y')
    da2 = datetime.strptime(d2, '%d/%m/%Y')
    return da2 >= da1

if __name__ == '__main__':
    aujourdhui = datetime.now()
    deb = aujourdhui.year - 20
    fin = aujourdhui.year - 16
    courant = deb
    while courant <= fin:
        d = "12/09/"+str(courant)
        m = majeur(d)
        if m:
            print("Une personne née le",d," est majeure")
        else:
            print("Une personne née le",d," est mineure")
        courant += 1

    d1 = "10/12/2018"
    d2 = "01/01/2019"

    print("{} vient après {} : {}".format(d2,d1,date_posterieure(d1,d2)))
    print("{} vient après {} : {}".format(d1,d2,date_posterieure(d2,d1)))


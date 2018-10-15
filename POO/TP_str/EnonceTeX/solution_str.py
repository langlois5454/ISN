#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv

def nbchar(fichier):
    resultat = 0
    with open(fichier, 'r') as f:
        contenu = csv.reader(f, delimiter=';')
        for tableau_ligne in contenu :
            resultat += len(''.join(tableau_ligne))
    return resultat

def suffixe(fichier, suf):
    resultat = []
    with open(fichier, 'r') as f:
        contenu = csv.reader(f, delimiter=';')
        for tableau_ligne in contenu :
            for cellule in tableau_ligne :
                if cellule.endswith(suf):
                    resultat.append(cellule)
    return resultat

def nbmot(fichier, mot):
    with open(fichier, 'r') as f:
        contenu = f.read()
    return contenu.count(mot)

def present(fichier, mot, debut, fin):
    with open(fichier, 'r') as f:
        contenu = f.read()
    return ( contenu.find(mot, debut, fin) != -1)

def position(fichier, mot, debut, fin):
    with open(fichier, 'r') as f:
        contenu = f.read()
    return contenu.find(mot, debut, fin)

def lignes(fichier, mot):
    resultat = []
    with open(fichier, 'r') as f:
        contenu = f.read()
    lignes = contenu.split('\n')
    for ligne in lignes:
        if ligne.startswith('CHAPITRE'):
            resultat.append(ligne)
    return resultat

def detabifier(fichier):
    with open(fichier, 'r') as f:
        contenu = f.read()    
    return contenu.expandtabs(4)

def tabifier(fichier):
    with open(fichier, 'r') as f:
        contenu = f.read()    
    return contenu.replace('    ','\t')


if __name__=='__main__':
    print(nbchar('usagers.csv'))
    print(suffixe('usagers.csv','ion'))
    print(nbmot('pg13951.txt','Artagnan'))
    print(present('pg13951.txt','Artagnan',1000,2000))
    print(position('pg13951.txt','Artagnan',5000,8000))
    print(lignes('pg13951.txt','CHAPITRE'))
    print(detabifier('solution_str.py'), file = open('a.out', 'w'))
    print(tabifier('a.out'))
    

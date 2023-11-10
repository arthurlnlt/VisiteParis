import random

def rechercherparprix(tab, prix):
    sortie = []
    if prix == 1:
        for i in range(len(tab)):
            if tab[i][2]==0:
                sortie.append(tab[i])
    else:
        for i in range(len(tab)):
            if tab[i][2]!=0:
                sortie.append(tab[i])
    return sortie

def rechercherparlieu(tab, lieu):
    sortie = []
    for i in range(len(tab)):
        if lieu ==1:
            if tab[i][3] ==1:
                sortie.append(tab[i])
        if lieu ==2:
            if tab[i][3] ==2:
                sortie.append(tab[i])
        if lieu ==3:
            if tab[i][3] ==3:
                sortie.append(tab[i])
        if lieu ==4:
            if tab[i][3] ==4:
                sortie.append(tab[i])
    return sortie


def rechercherpartransport(tab, transport):
    sortie = []
    for i in range(len(tab)):
        if transport == 1:
            if tab[i][4] == 1:
                sortie.append(tab[i])
        else:
            if tab[i][4] == 0:
                sortie.append(tab[i])
    return sortie

def rechercherpararrondissement(tab, arrondissement):
    sortie = []
    for i in range(len(tab)):
        if tab[i][5] == arrondissement:
            sortie.append(tab[i])
    if len(sortie) == 0:
        return 0
    return sortie


def selectionnerRandom(tab, nombre):
    sortie = []
    nombres = []
    for i in range(nombre):
        nombres.append(random.randint(0, len(tab)-1))
    for j in range(nombre):
        sortie.append(tab[nombres[j]])
    return sortie


def afficherlieux(tab):
    for i in range(len(tab)):
        print("Nom : ", tab[i][0])
        print("Lien de localisation : ",tab[i][1])
        print("Arrondissement : ", tab[i][5])
        print("Prix : ", tab[i][2], "€")
        print("Type : ", end='')
        if tab[i][3] == 1:
            print("Musée")
        elif tab[i][3] == 2:
            print("Restaurant")
        elif tab[i][3] == 3:
            print("Escape Game")
        else:
            print("Lieu")
        print("Accès en transport: ", end='')
        if tab[i][4] == 1:
            print("Oui")
        else:
            print("Non")
        print("\n")
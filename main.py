
from fonctions import *
import random
tableau = []


tab_jeune = [
    #modèle: nom, lien localisation, prix, type(1=musee 2=restaurant 3=escapegrame 4=lieu), accès transport: oui=1 non=0, arrondissement
    ["Musée du Louvre", "https://maps.app.goo.gl/KzE59zeDLkq7ynZj7", 0, 1, 1, 1],
    ["La Felicita", "https://maps.app.goo.gl/y6WyLUWbWdcWTegK8", 20, 2, 1, 13],
    ["Musée de la vie romantique", "https://maps.app.goo.gl/oy2V78AHan9aMrYb8", 0, 1, 1, 9],
    ["PATROL", "https://maps.app.goo.gl/4HCCXaoNRKN98GkCA", 26, 2, 1, 6],
    ["Jardin du Luxembourg", "https://maps.app.goo.gl/9x6BRUKptKbwfvAz8", 0, 4, 1, 6],
]

tab_moyen = [
    [],
    [],
    [],
    [],
    [],
]

tab_vieux = [
    [],
    [],
    [],
    [],
    [],
]





boucle = 0
while boucle !=1:
    print("Bienvenue sur le dénicheur de bon plans à Paris !\n")
    print("Saisissez votre âge:")
    age = int(input())
    if 0 < age < 30:
        tableau = tab_jeune
    if 30 < age < 50:
        tableau = tab_moyen
    if 50 < age < 150:
        tableau = tab_vieux
    print("Choisissez:\n"
          "1- Vous souhaitez vous laisser surprendre avec un lieu aléatoire choisi dans notre base de données selon vos critères\n"
          "2- Vous souhaitez rechercher plusieurs lieux selon différents critères")
    choix = int(input())
    while choix < 1 and choix >2:
        choix = int(input())

    if choix == 1:
        print("Sélectionnez le paramètre que vous souhaitez filtrer:\n"
              "1- Prix\n"
              "2- Type de lieu\n"
              "3- Accessible en transports en communs\n"
              "4- Par arrondissement")
        filtre = int(input())
        while 1 < filtre > 4:
            filtre = int(input())
        if filtre == 1:
            print("Saisissez si vous souhaitez un lieu gratuit ou payant:\n"
                  "1- Lieu Gratuit\n"
                  "2- Lieu Payant")
            prix = int(input())
            while 1 < prix > 2:
                prix = int(input())
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherparprix(tableau, prix)
            tableau = selectionnerRandom(tableau, nombre)
            afficherlieux(tableau)

        if filtre == 2:
            print("Saisissez le type de lieu que vous souhaitez:\n"
                  "1- Musée\n"
                  "2- Restaurant\n"
                  "3- Escape Game\n"
                  "4- Lieu")
            lieu = int(input())
            while 1 < lieu > 4:
                lieu = int(input())
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherparlieu(tableau, lieu)
            tableau = selectionnerRandom(tableau, nombre)
            afficherlieux(tableau)

        if filtre == 3:
            print("Saisissez si vous souhaitez un lieu accessible en transports en commun ou non:\n"
                  "1- Oui\n"
                  "2- Non")
            transport = int(input())
            while 1 < transport > 2:
                transport = int(input())
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherpartransport(tableau, transport)
            tableau = selectionnerRandom(tableau, nombre)
            afficherlieux(tableau)

        if filtre == 4:
            print("Saisissez l'arrondissement :")
            arrondissement = int(input())
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherpararrondissement(tableau, arrondissement)
            if tableau == 0:
                print("Aucun lieu trouvé avec l'arrondissement saisi !")
            else:
                tableau = selectionnerRandom(tableau, nombre)
                afficherlieux(tableau)











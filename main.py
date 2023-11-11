import os

from fonctions import *

tableau = []

tab_jeune = [
    # modèle: nom, lien localisation, prix, type(1=musee 2=restaurant 3=escape game 4=lieu), accès transport : oui=1
    # non=0, arrondissement
    ["Musée du Louvre", "https://maps.app.goo.gl/KzE59zeDLkq7ynZj7", 0, 1, 1, 1],
    ["La Felicita", "https://maps.app.goo.gl/y6WyLUWbWdcWTegK8", 20, 2, 1, 13],
    ["Musée de la vie romantique", "https://maps.app.goo.gl/oy2V78AHan9aMrYb8", 0, 1, 1, 9],
    ["PATROL", "https://maps.app.goo.gl/4HCCXaoNRKN98GkCA", 26, 2, 1, 6],
    ["Jardin du Luxembourg", "https://maps.app.goo.gl/9x6BRUKptKbwfvAz8", 0, 4, 1, 6],
    ["Petit Palais", "https://maps.app.goo.gl/ujsUpFMH2ByUrYNV6", 0, 1, 1, 8],
    ["Musée de l'illusion", "https://maps.app.goo.gl/iGCYdT3hRNzvMPcB7", 18, 1, 1, 1],
    ["Jeu de piste engagé à Odéon", "https://maps.app.goo.gl/xnqozN1RG2h7YFq38", 30, 3, 1, 6],
    ["Escape game Le Bureau des Légendes", "https://maps.app.goo.gl/4pQst7wPh1AqKUjg6", 60, 3, 1, 6],

]

tab_moyen = [
    ["Musée d'Orsay", "https://maps.app.goo.gl/ku7TEfj2TDL2KwYo9", 16, 1, 1, 7],
    ["Crypte archéologique de l'île de la Cité", "https://maps.app.goo.gl/G637hJoo6CEJtApt5", 9, 1, 1, 4],
    ["Sainte Chapelle", "https://maps.app.goo.gl/8AGTEF2HUhcDR234A", 12, 1, 1, 1],
    ["Visite du quartier Latin", "https://maps.app.goo.gl/JoE6rrbaD4iACHhG7", 0, 4, 1, 5],
    ["Ballade en 2CV dans Paris", "Adresse choisie au préalable", 110, 4, 1, 75],
    ["Jeu de piste au musée de la magie et des automates", "https://maps.app.goo.gl/jn5U1rRP7RQ5fkbc9", 27, 3, 1, 4],
    ["Visite guidée des Berges de Seine en vélo", "https://maps.app.goo.gl/m23jTBuLFBUnLYFE7", 42, 4, 1, 3]

]

tab_vieux = [
    ["Musée de Cluny - Musée national du Moyen Âge", "https://maps.app.goo.gl/ivuxSnJCiNtkurDW6", 12, 1, 1, 5],
    ["Musée national de la Légion d’honneur et des ordres de chevalerie", "https://maps.app.goo.gl/CC42DjRdnMcAmSps9",
     0, 1, 1, 7],
    ["Dégustation de fromages", "https://maps.app.goo.gl/dj2VxW7Pk4fMvWv59", 70, 2, 1, 5],
    ["Atelier oenologie des cafés d'exception", "https://maps.app.goo.gl/o7wJSSqGB93WohMN8", 190, 2, 1, 6],
    ["Dégustation fromages & vins Cave du Louvre", "https://maps.app.goo.gl/4FFJj4JBk9Fk8vxW7", 109, 2, 1, 1],
    ["Visite en DS dans Paris", "Adresse choisie au préalable", 110, 4, 1, 75]

]

boucle = 0
while boucle != 1:
    print("Bienvenue sur le dénicheur de bon plans à Paris !\n")
    print("Souhaitez-vous appliquer un filtre d'âge pour les activités ?\n"
          "1- Oui\n"
          "2- Non")
    filtre_age = int(input())
    while 1>filtre_age>2:
        filtre_age = int(input())
    if filtre_age == 1:
        print("Saisissez votre âge:")
        age = int(input())
        if 0 < age < 30:
            tableau = tab_jeune
        if 30 < age < 50:
            tableau = tab_moyen
        if 50 < age < 150:
            tableau = tab_vieux
    else:
        tableau = tab_jeune + tab_moyen + tab_vieux
    print("Choisissez:\n"
          "1- Vous souhaitez vous laisser surprendre avec une activité aléatoire choisi dans notre base de données "
          "selon vos critères\n"
          "2- Vous souhaitez rechercher plusieurs activités selon différents critères")
    choix = int(input())
    while 1 > choix < 2:
        choix = int(input())

    if choix == 1:
        print("Sélectionnez le paramètre que vous souhaitez filtrer:\n"
              "1- Prix\n"
              "2- Type d'activité\n"
              "3- Accessible en transports en communs\n"
              "4- Par arrondissement\n"
              "5- Aucun")
        filtre = int(input())
        while 1 > filtre > 5:
            filtre = int(input())
        if filtre == 1:
            print("Saisissez si vous souhaitez une activité gratuite ou payante:\n"
                  "1- Gratuit\n"
                  "2- Payant")
            prix = int(input())
            while 1 < prix > 2:
                prix = int(input())
            print(
                "Indiquez le nombre d'activités que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherparprix(tableau, prix)
            tableau = selectionnerRandom(tableau, nombre)
            afficherlieux(tableau)

        if filtre == 2:
            print("Saisissez le type d'activité que vous souhaitez:\n"
                  "1- Musée\n"
                  "2- Restaurant\n"
                  "3- Escape Game\n"
                  "4- Lieu")
            lieu = int(input())
            while 1 < lieu > 4:
                lieu = int(input())
            print("Indiquez le nombre d'activités que vous souhaitez générer (à partir de 2, les activités peuvent se "
                  "répéter")
            nombre = int(input())
            tableau = rechercherparlieu(tableau, lieu)
            tableau = selectionnerRandom(tableau, nombre)


        if filtre == 3:
            print("Saisissez si vous souhaitez une activité accessible en transports en commun ou non:\n"
                  "1- Oui\n"
                  "2- Non")
            transport = int(input())
            while 1 < transport > 2:
                transport = int(input())
            print("Indiquez le nombre d'activités que vous souhaitez générer (à partir de 2, les activités peuvent se "
                  "répéter")
            nombre = int(input())
            tableau = rechercherpartransport(tableau, transport)
            tableau = selectionnerRandom(tableau, nombre)


        if filtre == 4:
            print("Saisissez l'arrondissement :")
            arrondissement = int(input())
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherpararrondissement(tableau, arrondissement)
            if tableau == 0:
                print("Aucune activité trouvée avec l'arrondissement saisi !")
            else:
                tableau = selectionnerRandom(tableau, nombre)


        if filtre == 5:
            print("Indiquez le nombre de lieux que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = selectionnerRandom(tableau, nombre)
        afficherlieux(tableau)
    else:
        stop = 1
        tableau_filtre = []
        while stop == 1:
            print("Sélectionnez le filtre souhaité:\n"
                  "1- Prix\n"
                  "2- Type d'activité\n"
                  "3- Accessibilité en transports en communs\n"
                  "4- Par arrondissement")
            choix1 = int(input())
            while 1 > choix1 > 4:
                choix1 = int(input())
            if choix1 == 1:
                print("Sélectionnez la fourchette de prix pour les activités souhaitée:\n"
                      "1- Gratuit\n"
                      "2- Entre 1 et 50€\n"
                      "3- 50€ et plus")
                prix1 = int(input())
                while 1 > prix1 > 3:
                    prix1 = int(input())
                tableau = trierparprix(tableau, prix1)
                stop = verificationtableau(tableau)
            if choix1 ==2:
                print("Saisissez l'activité que vous souhaitez réaliser :\n"
                      "1- Musée\n"
                      "2- Restaurant\n"
                      "3- Escape Game\n"
                      "4- Lieu")
                activite = int(input())
                while 1>activite>4:
                    activite = int(input())
                tableau = rechercherparlieu(tableau, activite)
                stop = verificationtableau(tableau)

            if choix1 == 3:
                print("Saisissez si vous souhaitez que l'activité soit accessible en transports en communs :\n"
                      "1- Oui\n"
                      "2- Non")
                transport1 = int(input())
                while 1>transport1 >2:
                    transport1 = int(input())
                tableau = rechercherpartransport(tableau, transport1)
                stop = verificationtableau(tableau)

            if choix1 == 4:
                print("Saisissez l'arrondissement dans lequel vous souhaitez faire l'activité :")
                arrondissement1 = int(input())
                tableau = rechercherpararrondissement(tableau, arrondissement1)
                stop = verificationtableau(tableau)

        print("Voici les activités restantes après avoir appliqué les filtres :")
        afficherlieux(tableau)



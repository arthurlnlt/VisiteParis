import os
from tkinter import N

from fonctions import *

tableau = []

tab_jeune = [
    # modèle: nom, lien localisation, prix, type(1=musee 2=restaurant 3=escape game 4=lieu), accès transport : oui=1, non=0, arrondissement, halal
    ["Musée du Louvre", "https://maps.app.goo.gl/KzE59zeDLkq7ynZj7", 0, 1, 1, 1, 0],
    ["La Felicita", "https://maps.app.goo.gl/y6WyLUWbWdcWTegK8", 20, 2, 1, 13, 0],
    ["Musée de la vie romantique", "https://maps.app.goo.gl/oy2V78AHan9aMrYb8", 0, 1, 1, 9, 0],
    ["PATROL", "https://maps.app.goo.gl/4HCCXaoNRKN98GkCA", 26, 2, 1, 6, 0],
    ["Jardin du Luxembourg", "https://maps.app.goo.gl/9x6BRUKptKbwfvAz8", 0, 4, 1, 6, 0],
    ["Petit Palais", "https://maps.app.goo.gl/ujsUpFMH2ByUrYNV6", 0, 1, 1, 8, 0],
    ["Musée de l'illusion", "https://maps.app.goo.gl/iGCYdT3hRNzvMPcB7", 18, 1, 1, 1, 0],
    ["Jeu de piste engagé à Odéon", "https://maps.app.goo.gl/xnqozN1RG2h7YFq38", 30, 3, 1, 6, 0],
    ["Escape game Le Bureau des Légendes", "https://maps.app.goo.gl/4pQst7wPh1AqKUjg6", 60, 3, 1, 6, 0],
    ["Initiation au Street-Art", "https://maps.app.goo.gl/Wo6Bswm8L4GhKn4C7",50,4,1,3, 0],
    ["DAYA", "https://maps.app.goo.gl/CvAakDQ4WiQhaGwK7",30, 2, 1, "Ivry sur Seine", 1],
    ["Siena Paris", "https://maps.app.goo.gl/6E2SfUvAMggTAQth9",25,2,1,1,0],
    ["EL&N London", "https://maps.app.goo.gl/KVydoMX1yUcT9UWTA",10, 2, 1, 9, 1],
    ["Mad Golf", "https://maps.app.goo.gl/7TG4zqXqpGuDAuH36",16,4,1,2,0],
    ["Ballon de Paris Generali","https://maps.app.goo.gl/8h8A5vg281mNswYMA",18,4,1,15,0],
    ["Catacombes de Paris","https://maps.app.goo.gl/ZSvGf5KSEivDLLaK8",35,1,1,14,0],
    ["Paradox Museum","https://maps.app.goo.gl/BHkUwahCENL1e1by6",22,1,1,9,0],
    ["Musée Carnavalet","https://maps.app.goo.gl/71ES9TWcBXcdAaee9",0,1,1,3,0],
    ["Musée d'Art Moderne de Paris","https://maps.app.goo.gl/LXdAYmWZGoK1wTqn8",0,1,1,16,0],
    ["Institut du Monde Arabe","https://maps.app.goo.gl/BLjuwT4hL4CtgDZr5",8,1,1,5,0]
    
    

]

tab_moyen = [
    ["Musée d'Orsay", "https://maps.app.goo.gl/ku7TEfj2TDL2KwYo9", 16, 1, 1, 7, 0],
    ["Crypte archéologique de l'île de la Cité", "https://maps.app.goo.gl/G637hJoo6CEJtApt5", 9, 1, 1, 4, 0],
    ["Sainte Chapelle", "https://maps.app.goo.gl/8AGTEF2HUhcDR234A", 12, 1, 1, 1, 0],
    ["Visite du quartier Latin", "https://maps.app.goo.gl/JoE6rrbaD4iACHhG7", 0, 4, 1, 5, 0],
    ["Ballade en 2CV dans Paris", "Adresse choisie au préalable", 110, 4, 1, 75, 0],
    ["Jeu de piste au musée de la magie et des automates", "https://maps.app.goo.gl/jn5U1rRP7RQ5fkbc9", 27, 3, 1, 4, 0],
    ["Visite guidée des Berges de Seine en vélo", "https://maps.app.goo.gl/m23jTBuLFBUnLYFE7", 42, 4, 1, 3, 0],
    ["Rue Dénoyez : Street-Art", "https://maps.app.goo.gl/Sb5xrCQQHAmnV9Fa6",0,4,1,20, 0],
    ["Parc de Montsouris","https://maps.app.goo.gl/DkNrN2tEZe3UhT8W7",0,4,1,14, 0],
    ["Notre Dame du Travail","https://maps.app.goo.gl/hpUYzDZ2HDcCLonB9",0,1,1,14, 0],
    ["Cedric Grolet Opéra","https://maps.app.goo.gl/cSHRQbtiFApZe1Gi8",30,2,1,2, 0],
    ["Ciel de Paris", "https://maps.app.goo.gl/ZtRcFHg6f9XuovJLA",35,2,1,1,0],
    ["Bambini Paris", "https://maps.app.goo.gl/RPqTmhSt4msrqLNZ8", 35,2,1,16,0],
    ["Kalamata Paris","https://maps.app.goo.gl/i5VJ4RsiRBFHFekL6",35,2,1,8,0],
    ["Le Grand Amalfi","https://maps.app.goo.gl/xKvfbkmY549Nxc678",35, 2, 1, 5, 1],
    ["Vitrines de Noël de la Samaritaine", "https://maps.app.goo.gl/KnTuk9ioPHpA6sKL9",0,4,1,1,0],
    ["Grandes Serres du jardin des Plantes","https://maps.app.goo.gl/QdVh52NxndW6Hyqq7",7,4,1,5,0],
    ["Rex Studios","https://maps.app.goo.gl/fZU2cc1TsCWRdnUb6",11,4,1,2,0],
    ["Virtual Room Paris","https://maps.app.goo.gl/PpamoBYsJwt4jjgx6",30,3,1,11,0],
    ["Musée Picasso","https://maps.app.goo.gl/Jbyu8HoERFBS7K4Q6",14,1,1,3,0],
    ["Musée de l'Orangerie","https://maps.app.goo.gl/A8Xfo7i2peZZw97PA",13,1,1,1,0],
    ["Exposition Parfums d'Orient","https://maps.app.goo.gl/BLjuwT4hL4CtgDZr5",13,1,1,5,0],
    ["Musée des Arts décoratifs","https://maps.app.goo.gl/foNgp96ah9Mrx7T2A",14,1,1,1,0],
    ["Exposition le Japon en couleur","https://maps.app.goo.gl/foNgp96ah9Mrx7T2A",14,1,1,1,0]
    

]

tab_vieux = [
    ["Musée de Cluny - Musée national du Moyen Âge", "https://maps.app.goo.gl/ivuxSnJCiNtkurDW6", 12, 1, 1, 5, 0],
    ["Musée national de la Légion d’honneur et des ordres de chevalerie", "https://maps.app.goo.gl/CC42DjRdnMcAmSps9",
     0, 1, 1, 7, 0],
    ["Dégustation de fromages", "https://maps.app.goo.gl/dj2VxW7Pk4fMvWv59", 70, 2, 1, 5, 0],
    ["Atelier oenologie des cafés d'exception", "https://maps.app.goo.gl/o7wJSSqGB93WohMN8", 190, 2, 1, 6, 0],
    ["Dégustation fromages & vins Cave du Louvre", "https://maps.app.goo.gl/4FFJj4JBk9Fk8vxW7", 109, 2, 1, 1, 0],
    ["Visite en DS dans Paris", "Adresse choisie au préalable", 110, 4, 1, 75, 0],
    ["La plus vieille maison de Paris","https://maps.app.goo.gl/Ei917pMc7WCa5LHU8",0,4,1,3, 0],
    ["Musée du Quai Branly","https://maps.app.goo.gl/ZckHYWeb3vgLRJZU7",12,1,1,7, 0],
    ["Place des Vosges","https://maps.app.goo.gl/mBkScgf2PS5vT86aA",0,4,1,4, 0],
    ["Giulia Paris","https://maps.app.goo.gl/jNxnsVpcSDJRRMXZA",60,2,1,8,0],
    ["Big Love Caffé","https://maps.app.goo.gl/DRusY56QyhenfcLi7",15,2,1,3,0],
    ["Wagyu Paris", "https://maps.app.goo.gl/Bw1qq4c7WdN3YWzRA",25,2,1,19,1],
    ["Le Bebrant", "https://maps.app.goo.gl/7xkj3NuDDMDq7Uei7", 30,2,1,9,0],
    ["Cabaret Canaille","https://maps.app.goo.gl/bsq9LdGWvjTNX5jg9",35,4,1,8,0],
    ["Observatoire de la Sorbonne","https://maps.app.goo.gl/p4eZsYJh9NNVPF3w9",10,4,1,5,0],
    ["Le Moulin Rouge","https://maps.app.goo.gl/yZeDgFnHbaWhp4F29",170,2,1,18,0],
    ["Grande mosquée de Paris","https://maps.app.goo.gl/Mhge3Upu18nrStZ3A",3,1,1,5,0],
    ["Musée Rodin","https://maps.app.goo.gl/twS9KczwNQvZz6Va9",14,1,1,7,0],
    ["Exposition George Hugo","https://maps.app.goo.gl/kWbcGihiWNwNQf566",9,1,1,4,0],
    ["Exposition Claude Gillot","https://maps.app.goo.gl/BvZxAjyvHoMSpmeT7",17,1,1,1,0],
    ["Exposition Chagall à l'Oeuvre","https://maps.app.goo.gl/kKEbNXyQ6Q8idSDF8",15,1,1,4,0],
    ["Exposition Nicolas de Staël","https://maps.app.goo.gl/LXdAYmWZGoK1wTqn8",15,1,1,16,0],
    ["Exposition Amedeo Modigliani","https://maps.app.goo.gl/A8Xfo7i2peZZw97PA",13,1,1,1,0]
    
    


]

boucle = 0
while boucle != 1:
    print("Bienvenue sur le dénicheur de bon plans à Paris !\n")
    print("actuellement",len(tab_jeune)+len(tab_moyen)+len(tab_vieux),"activités dans notre base de données\n")
    print("Appuyez sur 1 pour commencer:\n")
    a = int(input())
    os.system("cls")
    while a !=1:
        a = int(input())
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
    os.system("cls")
    print("Choisissez:\n"
          "1- Vous souhaitez vous laisser surprendre avec une activité aléatoire choisi dans notre base de données "
          "selon vos critères\n"
          "2- Vous souhaitez rechercher plusieurs activités selon différents critères")
    choix = int(input())
    while 1 > choix < 2:
        choix = int(input())

    if choix == 1:
        os.system("cls")
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
            os.system("cls")
            print("Saisissez si vous souhaitez une activité gratuite ou payante:\n"
                  "1- Gratuit\n"
                  "2- Payant")
            prix = int(input())
            while 1 < prix > 2:
                prix = int(input())
            os.system("cls")
            print(
                "Indiquez le nombre d'activités que vous souhaitez générer (à partir de 2, les lieux peuvent se répéter")
            nombre = int(input())
            tableau = rechercherparprix(tableau, prix)
            tableau = selectionnerRandom(tableau, nombre)
            afficherlieux(tableau)

        if filtre == 2:
            os.system("cls")
            print("Saisissez le type d'activité que vous souhaitez:\n"
                  "1- Musée\n"
                  "2- Restaurant\n"
                  "3- Escape Game\n"
                  "4- Lieu")
            lieu = int(input())
            while 1 < lieu > 4:
                lieu = int(input())
            os.system("cls")
            halal = 0
            if lieu == 2:
               print("Souhaitez-vous un restaurant Halal ?\n 1- Oui\n 2- Non\n 3- Peu importe")
               halal = int(input())
               while 1 > halal > 3:
                    halal = int(input())
            os.system('cls')
            print("Indiquez le nombre d'activités que vous souhaitez générer (à partir de 2, les activités peuvent se "
                  "répéter")
            nombre = int(input())
            tableau = rechercherparlieu(tableau, lieu, halal)
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
                halal = 0
                if activite == 2:
                    print("Souhaitez-vous un restaurant Halal ?\n 1- Oui\n 2- Non\n 3- Peu importe")
                    halal = int(input())
                    while 1 > halal > 3:
                        halal = int(input())
                tableau = rechercherparlieu(tableau, activite,halal)
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



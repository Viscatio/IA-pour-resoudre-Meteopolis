# Créé par victo, le 16/04/2024 en Python 3.7
import MeteoPolis
import api
from graphe_projet3 import Graphe
import random
import os


### Code pour récupérer les matrices de météo de chaque saisons ###
Meteo = {
    'Soleil': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Nuageux': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Pluie': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Vent': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Tempête': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Neige': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    },

    'Brouillard': {
        'Soleil': 0,
        'Nuageux': 0,
        'Pluie': 0,
        'Vent': 0,
        'Tempête': 0,
        'Neige': 0,
        'Brouillard': 0
    }
}

meteos = ['Soleil', 'Nuageux', 'Pluie', 'Vent', 'Tempête', 'Neige', 'Brouillard']

def recuperer_proba(saison_voulue):
    ville = MeteoPolis.Meteopolis()
    ville.saison = saison_voulue
    for meteo in meteos:
        liste = []
        for i in range(1000):
            Graphe.ville_de_demain(ville)
            if ville.chaos != True:
                liste.append(ville.temps)
            else:
                ville.chaos = False
        remplir_dictionnaire(meteo, liste)

def remplir_dictionnaire(meteo, liste):
    for i in liste:
        Meteo[meteo][i] += 1
    for j in meteos:
        Meteo[meteo][j] = Meteo[meteo][j] / 10
    print(Meteo)

#recuperer_proba('Printemps')

######################################


### Code de l'IA ###

#Un peu plus compliqué

def compter_cases(carte):
    residence = 0
    emploi = 0
    nature = 0
    energie = 0
    for i in carte:
        for k in i:
            if k.typecase == 'Residence':
                residence += 1
            elif k.typecase == 'Emploi':
                emploi += 1
            elif k.typecase == 'Nature':
                nature += 1
            elif k.typecase == 'Energie':
                energie += 1
    return([residence, emploi, nature, energie])

def get_pire_case(carte, typecase):
    score_mini = 400
    min = (0, 0)
    for i in range(len(carte)):
        for j in range(len(i)):
            if carte[i][j].typecase == typecase and carte[i][j].vie < score_mini:
                score_mini = carte[i][j].vie
                min = (i, j)
    return min

def ameliorer_carte(carte):
    type = ['Residence', 'Emploi', 'Nature', 'Energie']

    for i in range(random.randint(2, 120)):
        carte[random.randint(0, 9)][random.randint(0, 9)].new_type(random.choice(type))

        ok = compter_cases(carte)
        if ok[0] == 0:
            carte[random.randint(0, 9)][random.randint(0, 9)].new_type('Residence')
        if ok[1] == 0:
            carte[random.randint(0, 9)][random.randint(0, 9)].new_type('Emploi')
        if ok[2] == 0:
            carte[random.randint(0, 9)][random.randint(0, 9)].new_type('Nature')
        if ok[3] == 0:
            carte[random.randint(0, 9)][random.randint(0, 9)].new_type('Energie')

    for i in carte:
        for j in i:
            j.set_vie(100)

    return carte

def recherche_de_maximum(liste_de_tuples):
    if not liste_de_tuples:
        return None, None

    maximum = liste_de_tuples[0]
    indice_maximum = 0
    for i, element in enumerate(liste_de_tuples[1:], start=1):
        if element[1] > maximum[1]:
            maximum = element
            indice_maximum = i

    return maximum, indice_maximum
'''
def generation1(liste):
    liste_cartes = []
    for i in liste:
        liste_cartes.append(i)
        for j in range(9):
            liste_cartes.append(ameliorer_carte(i))

    scores = []

    for map in liste_cartes:
        ville = MeteoPolis.Meteopolis()
        ville.carte = map

        ok = api.Application('Ete', 'Carte.csv')
        ok = ok.lancer_simulation()
        scores.append((map, ok))

    max = []
    for i in range(4):
        maximum = recherche_de_maximum(scores)
        scores.pop(maximum[1])
        max.append(maximum[0])

    return max

liste = []
ok = api.lecture_fichier('Carte.csv')
for i in range(4):
    liste.append(ok)

def IA(liste, nb_generations):
    for i in range(nb_generations):
        essai = generation(liste)

        liste = []
        for i in range(4):
            print(essai[i][1])
            liste.append(essai[i][0])
    print('céfini')
    api.ecriture_fichier(essai[0][0], 'ok.csv')


IA(liste, 5)
'''




########

def afficher(carte):
    for i in carte:
        ligne = ""
        for j in i:
            ligne += str(j.get_vie()) + " "
        print(ligne)

def generation(liste):
    cartes = []
    for i in range(len(liste)):
        cartes.append(liste[i])

        api.ecriture_fichier2(liste[i], 'trash.csv')
        for j in range(10):
            carte = api.lecture_fichier('trash.csv')
            cartes.append(ameliorer_carte(carte))


    for i in range(len(cartes)):
        score = 0
        j = 0
        api.ecriture_fichier2(cartes[i], 'trash.csv')
        while j < 10:
            carte = api.lecture_fichier('trash.csv')
            ok = api.Application('Ete', 'Carte.csv')
            ok.meteopolis.carte = carte
            ok = ok.lancer_simulation()
            if ok < 5000:
                j = 10
            score += ok
            #print(" -" + str(j) + "->" + str(ok))
            j += 1
        moyenne = score//10
        print(moyenne)
        cartes[i] = (cartes[i], moyenne)


    prochaine_generation = []
    '''
    for i in range(len(cartes)):
        maximum = recherche_de_maximum(cartes)
        if maximum[0][1] > 28000:
            prochaine_generation.append(cartes.pop(maximum[1]))
    '''
    for i in range(10):
        maximum = recherche_de_maximum(cartes)
        prochaine_generation.append(cartes.pop(maximum[1]))
    return prochaine_generation


'''
Méthode d'IA (liste de 10 cartes):
	Liste = liste de 10 cartes
	Génération = 0
	Tant que la date limite n'est pas dépassée:
		Liste = Méthode qui teste une génération(Liste)
		Je créé un dossier avec le numéro de la génération
Dans ce dossier j'enregistre les 10 cartes dans la Liste
'''



def IA(liste, nb_generation):
    cartes = []
    for i in range(len(liste)):
        cartes.append(liste[i])

    for i in range(len(cartes)):
        score = 0
        j = 0
        api.ecriture_fichier2(cartes[i], 'trash.csv')
        while j < 100:
            carte = api.lecture_fichier('trash.csv')
            ok = api.Application('Ete', 'Carte.csv')
            ok.meteopolis.carte = carte
            ok = ok.lancer_simulation()
            if ok < 5000:
                j = 10
            score += ok
            #print(" -" + str(j) + "->" + str(ok))
            j += 1
        moyenne = score//100
        print(moyenne)
        cartes[i] = (cartes[i], moyenne)



liste = []



# Chemin du dossier contenant les fichiers
dossier = 'maps_V3/2426/'

# Liste des noms de fichiers dans le dossier
fichiers = os.listdir(dossier)


# Affichage des noms de fichiers
for fichier in fichiers:
    map = api.lecture_fichier(dossier+f"{fichier}")
    liste.append(map)




IA(liste, 200000)
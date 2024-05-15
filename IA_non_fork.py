import MeteoPolis
import api
from graphe import Graphe
import random
import os
import time
from multiprocessing import Process, Queue, freeze_support
import numpy as np
import gc
import modules_IA

def generation(liste):
    cartes = []
    for i in range(len(liste)):
        cartes.append(liste[i])

        api.ecriture_fichier2(liste[i], 'trash.csv')
        for j in range(19):
            carte = api.lecture_fichier('trash.csv')
            cartes.append(modules_IA.ameliorer_carte(carte))


    for i in range(len(cartes)):
        score = 0
        j = 0
        api.ecriture_fichier2(cartes[i], 'trash.csv')
        while j < 20:
            carte = api.lecture_fichier('trash.csv')
            ok = api.Application('Ete', 'trash.csv')
            ok.meteopolis.carte = carte
            ok = ok.lancer_simulation()
            if ok < 5000:
                j = 20
            elif ok > 46000:
                dossier_script = os.path.dirname(os.path.abspath(__file__))
                chemin_fichier = os.path.join(dossier_script, "record_" + str(ok) + '.csv')
                api.ecriture_fichier2(cartes[i], chemin_fichier)
            score += ok
            #print(" -" + str(j) + "->" + str(ok))
            j += 1
        moyenne = score//20
        print(moyenne)
        cartes[i] = (cartes[i], moyenne)

    prochaine_generation = []

    for i in range(10):
        maximum = modules_IA.recherche_de_maximum(cartes)
        prochaine_generation.append(cartes.pop(maximum[1]))
    return prochaine_generation


def IA(liste, nb_generation, numero):
    liste_de_dix_cartes = liste
    numero_generation = numero
    for i in range(nb_generation):
        # Début du chronomètre
        start_time = time.time()
        while len(liste_de_dix_cartes) < 10:
            if len(liste_de_dix_cartes)!=0:
                liste_de_dix_cartes.append(liste_de_dix_cartes[0])
            else:
                liste_de_dix_cartes.append(api.lecture_fichier("ok.csv"))
        liste_de_dix_cartes = generation(liste_de_dix_cartes)



        # Récupérer le chemin du dossier où se trouve le script actuel
        dossier_script = os.path.dirname(os.path.abspath(__file__))

        # Chemin du dossier à créer
        chemin_dossier = os.path.join(dossier_script, "maps_V1/", str(numero_generation))

        # Vérifier si le dossier n'existe pas déjà
        if not os.path.exists(chemin_dossier):
            # Créer le dossier
            os.makedirs(chemin_dossier)
            print("Le dossier a été créé avec succès !")
        else:
            print("Le dossier existe déjà.")

        for i in range(len(liste_de_dix_cartes)):
            nom_fichier = str(liste_de_dix_cartes[i][1]) + '.csv'
            chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
            api.ecriture_fichier2(liste_de_dix_cartes[i][0], chemin_fichier)

        for i in range(len(liste_de_dix_cartes)):
            liste_de_dix_cartes[i] = liste_de_dix_cartes[i][0]

        numero_generation += 1

        # Fin du chronomètre
        end_time = time.time()

        # Calcul du temps écoulé en secondes
        execution_time = end_time - start_time

        print("Temps d'exécution:", execution_time, "secondes")

    return numero_generation



def main(ok):

    liste = []

    # Chemin du dossier contenant les fichiers
    dossier = 'maps_V1/' + str(ok) + '/'

    # Liste des noms de fichiers dans le dossier
    fichiers = os.listdir(dossier)


    # Affichage des noms de fichiers
    for fichier in fichiers:
        map = api.lecture_fichier(dossier+f"{fichier}")
        liste.append(map)

    IA(liste, 200000, ok + 1)
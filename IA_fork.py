import MeteoPolis
import api
from graphe import Graphe
import random
import os
import numpy as np
import gc
import multiprocessing
import IA_non_fork
import time
from multiprocessing import Process, Queue, freeze_support
import sys
import modules_IA

def worker(queue):
    '''Lance une simulation et renvoi le score obtenu'''

    #Créé la ville et lance la simulation en récupérant le score
    ville = api.Application('Ete', 'trash.csv')
    score = ville.lancer_simulation()

    #Supprime les variables
    del ville
    gc.collect()

    #Renvoie le score
    queue.put(score)


def generation(liste):
    '''Met une generation à l'épreuve'''

    #J'initialise une liste de cartes à vide
    cartes = []

    #Je parcours la liste de cartes donnée en arguments
    for i in range(len(liste)):
        #J'ajoute la carte courante à la liste carte
        cartes.append(liste[i])
        #Je stocke la carte courante dans un fichier csv
        api.ecriture_fichier2(liste[i], 'trash.csv')
        #Je répète 19 fois
        for j in range(19):
            #Je récupère la carte enregistrée
            carte = api.lecture_fichier('trash.csv')
            #J'ajoute une version modifiée de la carte à la liste
            cartes.append(modules_IA.ameliorer_carte(carte))

    #Je supprime les variables
    del i, j, carte
    gc.collect()

    #Je lance l'évaluation des cartes
    for i in range(len(cartes)):
        #J'enregistre la carte courante dans un fichier csv
        api.ecriture_fichier2(cartes[i], 'trash.csv')

        #Je défini le nombre de simulations lancées en simultané
        num_tasks = 2

        #Je créé une file de processus
        queue = Queue()
        processes = []

        #Je lance les processus enfants
        for _ in range(num_tasks):
            p = Process(target=worker, args=(queue,))
            p.start()
            processes.append(p)

        #Je récupère les résultats des processus enfants
        results = []
        for _ in range(num_tasks):
            result = queue.get()
            results.append(result)

        #J'attends que tout les processus se terminent
        for p in processes:
            p.join()

        #Je supprime la file de processus
        queue.close()

        #Je calcul la moyenne de toutes les simulations
        moyenne = sum(results) // (num_tasks)
        cartes[i] = (cartes[i], moyenne)

    #J'initialise à vide la liste des meilleures cartes
    prochaine_generation = []

    #Je récupère les 10 meilleures
    for i in range(10):
        maximum = modules_IA.recherche_de_maximum(cartes)
        prochaine_generation.append(cartes.pop(maximum[1]))

    #Je supprime toutes les variables
    del num_tasks, queue, processes, results, moyenne, cartes, p, result, maximum, dossier_script, chemin_fichier
    gc.collect()

    #Je renvoie les 10 meilleures cartes
    return prochaine_generation


def IA(liste, nb_generation, gen):
    '''Lance nb_generation générations'''

    #J'ajoute freeze_support pour des raisons de multiprocessing (python râle sans)
    freeze_support()

    #Je dit dans quel dossier je génère
    dossier = 'maps_V1/'

    #Je récupère la liste de cartes
    liste_de_dix_cartes = liste

    #J'initialise le numéro de la génération de départ
    numero_generation = gen

    #Je simule nb_generation générations
    for o in range(nb_generation):

        #Je démarre un chronomètre
        start_time = time.time()

        #Tant que je n'ai pas 10 cartes
        while len(liste_de_dix_cartes) < 10:
            #Si la liste n'est pas vide
            if len(liste_de_dix_cartes)!=0:
                #Je duplique la première carte de la liste
                liste_de_dix_cartes.append(liste_de_dix_cartes[0])
            #Si la liste est vide
            else:
                #Je récupère la dernière carte
                liste_de_dix_cartes.append(api.lecture_fichier("trash.csv"))

        #Je lance une génération
        liste_de_dix_cartes = generation(liste_de_dix_cartes)

        #Je récupère le dossier courant
        dossier_script = os.path.dirname(os.path.abspath(__file__))
        chemin_dossier = os.path.join(dossier_script, dossier, str(numero_generation))

        #Je créé le nouveau dossier
        if not os.path.exists(chemin_dossier):
            os.makedirs(chemin_dossier)
            print("Le dossier a été créé avec succès !")
        else:
            print("Le dossier existe déjà.")

        #J'enregistre les 10 cartes dans le nouveau dossier
        for i in range(len(liste_de_dix_cartes)):
            nom_fichier = str(liste_de_dix_cartes[i][1]) + '.csv'
            chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
            api.ecriture_fichier2(liste_de_dix_cartes[i][0], chemin_fichier)

        #Je supprime les variables
        del liste_de_dix_cartes, nom_fichier, chemin_fichier
        gc.collect()


        #Je récupère les cartes
        liste = []
        dossier = dossier + str(numero_generation)

        # Liste des noms de fichiers dans le dossier
        fichiers = os.listdir(dossier)

        # Affichage des noms de fichiers et ajout dans la nouvelle liste
        for fichier in fichiers:
            map = api.lecture_fichier(dossier+f"{numero_generation}"+'/'+f"{fichier}")
            print(dossier+f"{numero_generation}"+'/'+f"{fichier}")
            liste.append(map)

        liste_de_dix_cartes = liste

        #Suppression des variables
        del liste, fichiers, dossier, chemin_dossier, dossier_script, map, i, fichier
        gc.collect()

        #J'arrête le chronomètre
        end_time = time.time()

        #Je calcul le temps écoulé
        execution_time = end_time - start_time

        #J'affiche le temps qu'a pris la génération à se faire
        print("Temps d'exécution:", execution_time, "secondes")

        #Je passe à la génération suivante
        numero_generation += 1
    return numero_generation

def main(gen):
    freeze_support()

    liste = []

    # Chemin du dossier contenant les fichiers
    dossier = "maps_V1/" + str(gen)

    # Liste des noms de fichiers dans le dossier
    fichiers = os.listdir(dossier)

    # Affichage des noms de fichiers
    for fichier in fichiers:
        map = api.lecture_fichier(dossier+'/'+f"{fichier}")
        liste.append(map)

    #SUppression des variables
    del fichiers, dossier, map
    gc.collect()

    #Je lance l'IA pour 2 générations
    ok = IA(liste, 2, gen + 1)

    #Je continue avec l'IA qui ne pose pas de soucis pour la ram
    IA_non_fork.main(ok-1)

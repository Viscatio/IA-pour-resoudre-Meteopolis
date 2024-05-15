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
    ok = api.Application('Ete', 'ok.csv')
    michel = ok.lancer_simulation()
    del ok
    gc.collect()
    queue.put(michel)

import matplotlib.pyplot as plt

def graphique(carte, nom):

    # Votre liste de valeurs
    valeurs = []

    # Définir les intervalles pour l'histogramme (dans ce cas, chaque intervalle a une largeur de 250)
    intervalles = range(30000, 50200, 200)

    # Créer l'histogramme avec des données vides
    fig, ax = plt.subplots()
    hist, bins, _ = ax.hist(valeurs, bins=intervalles, color='blue', alpha=0.5)

    # Ajouter des étiquettes et un titre
    ax.set_xlabel('Intervalles')
    ax.set_ylabel('Fréquence')
    ax.set_title('Histogramme des valeurs entre 30000 et 50000')

    plt.ion()  # Activer le mode interactif

    total = 0
    nb_resultats = 0

    for i in range(100000000):
        num_tasks = 4
        queue = Queue()
        processes = []

        for _ in range(num_tasks):
            p = Process(target=worker, args=(queue,))
            p.start()
            processes.append(p)

        # Récupération des résultats
        results = []
        for _ in range(num_tasks):
            result = queue.get()
            print(result)
            valeurs.append(result)
            results.append(result)
            total += result
            nb_resultats += 1

        # Mettre à jour les données de l'histogramme
        hist, _ = np.histogram(valeurs, bins=bins)
        for rectangle, height in zip(ax.patches, hist):
            rectangle.set_height(height)

        # Redessiner le graphique avec des axes redimensionnés
        ax.clear()  # Effacer le contenu de l'axe
        hist, bins, _ = ax.hist(valeurs, bins=intervalles, color='blue', alpha=0.5)
        ax.set_xlabel('Intervalles')
        ax.set_ylabel('Fréquence')
        ax.set_title('Histogramme des valeurs entre 30000 et 50000')
        ax.set_xlim(min(intervalles), max(intervalles))
        ax.set_ylim(0, max(hist) * 1.1)  # Redimensionner l'axe des y pour contenir toutes les valeurs
        plt.draw()

        # Attendre un court laps de temps pour permettre à la mise à jour d'être affichée
        plt.pause(0.1)

        if max(hist) * 1.1 > 3000:
            # Sauvegarder l'histogramme
            nom = total // nb_resultats
            plt.savefig(nom + '.png')
            nom_fichier = str(nom) + '.csv'
            nom = os.path.join(chemin_dossier, nom_fichier)
            api.ecriture_fichier2(carte, nom)
            return

        # Fermer la file d'attente
        queue.close()

    plt.ioff()  # Désactiver le mode interactif à la fin



if __name__ == '__main__':
    freeze_support()

    graphique(api.lecture_fichier('ok.csv'), str(43329))
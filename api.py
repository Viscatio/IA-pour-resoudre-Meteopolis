import tkinter as tk
from PIL import Image, ImageTk
from Cases import Case
import os
import numpy as np
import gc
import csv
import MeteoPolis as MeteoPolis
from graphe_projet3 import Graphe


def lecture_fichier(nom_fichier : str) -> list :
    """Lire et Appliquer un fichier csv sur une carte"""
    with open(nom_fichier, newline= "", encoding= 'utf-8') as f :
        fichier = csv.reader(f, delimiter = ';')
        carte = []
        for ligne in fichier :
            ligne=conversion_ligne(ligne)
            ligne2=[]
            for item in ligne:
                item=Case(item[0], item[1])
                ligne2.append(item)
            carte.append(ligne2)
        gc.collect()
        return carte

# /!\ ne pas toucher à ces méthodes! /!\ #

def conversion_ligne(liste : str) -> list:
    """Fonction permettant de bien charger le fichier csv"""
    liste2=[]

    for case in liste:
        temp,tempnb="",""
        for lettre in case:
            if lettre in "1234567890":
                tempnb+=lettre
            if lettre in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                temp+=lettre
            if lettre == ")":
                liste2.append((int(tempnb),temp))
                tempnb=""
                temp=""
    return liste2

# /!\ ne pas toucher à ces méthodes! /!\ #

def ecriture_fichier(carte : list, nom_fichier : str) -> None :
    """Sauvegarder la carte dans un fichier csv"""
    with open(nom_fichier,'w',newline="",encoding='utf-8') as f :
        csv.writer(f, delimiter = ';').writerows(carte)

def ecriture_fichier2(carte: list, nom_fichier: str) -> None:
    """Sauvegarder la carte dans un fichier csv"""
    chemin_complet = nom_fichier
    with open(chemin_complet, 'w', newline="", encoding='utf-8') as f:
        csv.writer(f, delimiter=';').writerows(carte)
    del chemin_complet
    gc.collect()

# /!\ ne pas toucher à ces méthodes! /!\ #
##########################################

#Qu'on soit d'accord, vous n'avez aucune raison de modifier le code!
#Néanmoins, si vous le modifiez et que cela ne fonctionne plus:
#Sauvegardez vos cartes autre part (que dans le dossier) et retéléchargez la bonne version

##### Classe Application, gérant tout l'affichage #####

class Application:

    ## Fonction d'initialisation de la classe ##
    def __init__(self, saison_de_depart : str = 'Printemps', nom_fichier : str = '') -> None:

        #Je créé la ville et la stocke en attribut de la classe
        self.meteopolis = MeteoPolis.Meteopolis(10, 10, 'Nature', 1)


        #Je charge la carte depuis le fichier si nom_fichier n'est pas vide
        if nom_fichier != "":
            carte = lecture_fichier(nom_fichier)
            #Je remplace la carte par défaut par la carte chargée
            self.meteopolis.carte=carte

        #Je stocke la saison de départ, et le nom du fichier au cas où
        self.saison_de_depart = saison_de_depart
        self.nom_fichier = nom_fichier

    ## Méthode lançant la simulation ##
    def lancer_simulation(self):
        #Je passe à True le booléen stipulant que la simulation est lancée
        self.simulation = True

        #Je définis la saison de départ de la simulation
        self.meteopolis.set_saison(self.saison_de_depart)

        #J'initialise le compteur de saisons à 1
        self.nb_saison = 1 #Je crois que c'est devenu inutile, mais ça fonctionne, donc on touche à rien

        #Je simule une année
        return self.simuler_une_annee()


    ## Méthode lançant une simulation d'un an ##
    def simuler_une_annee(self):
        #Condition d'arrêt, quand la saison 4 est dépassée, on retourne le score de la simulation
        for i in range(122):
            if self.meteopolis.get_jour() > 120:
                #J'essaie de scorer la carte
                try:
                    resultat = Graphe.calcul_score(self.meteopolis)
                except Exception as e:
                    resultat = 5
                    ecriture_fichier(self.meteopolis.carte, 'bug.csv')
                return resultat

            #Je calcule la ville de demain
            Graphe.ville_de_demain(self.meteopolis) # Calcul de la ville du lendemain
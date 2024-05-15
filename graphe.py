# Créé par victo, le 07/05/2024 en Python 3.7
# uncompyle6 version 3.5.0
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.2 (default, Dec 29 2018, 06:19:36)
# [GCC 7.3.0]
# Embedded file name: P:\Documents\2023-2024\Term\Projet 3\Code application\graphe_projet3.py
# Size of source mod 2**32: 23574 bytes
from random import randint
from MeteoPolis import Meteopolis
saisons = ['Printemps', 'Ete', 'Automne', 'Hiver', 'Chaos']
temps = ['Soleil', 'Nuageux', 'Pluie', 'Vent', 'Tempête', 'Neige', 'Brouillard']
temps_chaotique_classique = {'Printemps':'Pluie',  'Ete':'Soleil',  'Automne':'Vent',  'Hiver':'Neige'}
temps_chaotique_catastrophique = ['Séisme', 'Inondation', 'Pluie de météorites', 'Tornade', 'Canicule', 'Fatal-foudre', 'Epidémie', 'Volcan', 'Antre du démon', 'Attaque OVNI']
printemps = [
 [
  50, 30, 20, 0, 0, 0, 0],
 [
  20, 30, 30, 20, 0, 0, 0],
 [
  10, 40, 30, 10, 5, 0, 5],
 [
  60, 0, 0, 35, 5, 0, 0],
 [
  10, 40, 20, 10, 0, 0, 20],
 [
  0, 100, 0, 0, 0, 0, 0],
 [
  50, 10, 0, 0, 0, 0, 40]]
ete = [
 [
  60, 10, 30, 0, 0, 0, 0],
 [
  40, 20, 20, 10, 10, 0, 0],
 [
  20, 20, 40, 5, 15, 0, 0],
 [
  50, 0, 15, 20, 15, 0, 0],
 [
  0, 10, 50, 0, 20, 0, 20],
 [
  0, 0, 0, 0, 100, 0, 0],
 [
  100, 0, 0, 0, 0, 0, 0]]
automne = [
 [
  10, 30, 20, 20, 0, 0, 20],
 [
  20, 50, 20, 10, 0, 0, 0],
 [
  0, 10, 40, 30, 0, 0, 20],
 [
  10, 0, 20, 40, 25, 0, 5],
 [
  10, 0, 0, 50, 20, 20, 0],
 [
  0, 50, 20, 0, 0, 10, 20],
 [
  0, 10, 0, 50, 0, 0, 40]]
hiver = [
 [
  50, 20, 0, 20, 0, 10, 0],
 [
  10, 30, 10, 0, 0, 40, 10],
 [
  0, 50, 0, 20, 0, 30, 0],
 [
  30, 0, 0, 40, 10, 20, 0],
 [
  0, 0, 0, 50, 10, 40, 0],
 [
  20, 10, 10, 0, 10, 50, 0],
 [
  0, 30, 0, 0, 0, 0, 70]]
chaos = []
meteos = {saisons[0]: printemps, saisons[1]: ete, saisons[2]: automne, saisons[3]: hiver, saisons[4]: chaos}
impact_printemps = {'Soleil':{'Residence':6,
  'Emploi':4,  'Energie':6,  'Nature':8,  'Out':6},
 'Nuageux':{'Residence':5,
  'Emploi':6,  'Energie':5,  'Nature':5,  'Out':5},
 'Pluie':{'Residence':3,
  'Emploi':3,  'Energie':6,  'Nature':6,  'Out':5},
 'Vent':{'Residence':2,
  'Emploi':2,  'Energie':6,  'Nature':6,  'Out':6},
 'Tempête':{'Residence':2,
  'Emploi':0,  'Energie':1,  'Nature':2,  'Out':0},
 'Neige':{'Residence':0,
  'Emploi':2,  'Energie':-2,  'Nature':-7,  'Out':3},
 'Brouillard':{'Residence':4,
  'Emploi':1,  'Energie':3,  'Nature':3,  'Out':4}}
impact_ete = {'Soleil':{'Residence':7,
  'Emploi':-1,  'Energie':1,  'Nature':3,  'Out':3},
 'Nuageux':{'Residence':3,
  'Emploi':4,  'Energie':4,  'Nature':4,  'Out':4},
 'Pluie':{'Residence':1,
  'Emploi':7,  'Energie':5,  'Nature':5,  'Out':7},
 'Vent':{'Residence':-1,
  'Emploi':1,  'Energie':4,  'Nature':1,  'Out':3},
 'Tempête':{'Residence':-3,
  'Emploi':-8,  'Energie':0,  'Nature':-3,  'Out':2},
 'Neige':{'Residence':-8,
  'Emploi':-3,  'Energie':4,  'Nature':-3,  'Out':1},
 'Brouillard':{'Residence':2,
  'Emploi':-1,  'Energie':3,  'Nature':4,  'Out':7}}
impact_automne = {'Soleil':{'Residence':4,
  'Emploi':4,  'Energie':4,  'Nature':4,  'Out':0},
 'Nuageux':{'Residence':0,
  'Emploi':2,  'Energie':-1,  'Nature':-1,  'Out':0},
 'Pluie':{'Residence':-2,
  'Emploi':-3,  'Energie':-2,  'Nature':0,  'Out':-3},
 'Vent':{'Residence':1,
  'Emploi':2,  'Energie':1,  'Nature':2,  'Out':-1},
 'Tempête':{'Residence':-6,
  'Emploi':-4,  'Energie':-4,  'Nature':-6,  'Out':-1},
 'Neige':{'Residence':-1,
  'Emploi':-6,  'Energie':-6,  'Nature':-4,  'Out':-2},
 'Brouillard':{'Residence':-2,
  'Emploi':-2,  'Energie':-2,  'Nature':0,  'Out':0}}
impact_hiver = {'Soleil':{'Residence':2,
  'Emploi':1,  'Energie':-2,  'Nature':2,  'Out':2},
 'Nuageux':{'Residence':-2,
  'Emploi':0,  'Energie':-3,  'Nature':0,  'Out':1},
 'Pluie':{'Residence':-3,
  'Emploi':-4,  'Energie':-2,  'Nature':-1,  'Out':0},
 'Vent':{'Residence':-4,
  'Emploi':-1,  'Energie':-2,  'Nature':-1,  'Out':-1},
 'Tempête':{'Residence':-11,
  'Emploi':-7,  'Energie':-8,  'Nature':-2,  'Out':-1},
 'Neige':{'Residence':1,
  'Emploi':-2,  'Energie':-5,  'Nature':-1,  'Out':-1},
 'Brouillard':{'Residence':-4,
  'Emploi':-1,  'Energie':-4,  'Nature':0,  'Out':-1}}
impact_chaos = {'Soleil':{'Residence':5,
  'Emploi':-3,  'Energie':-1,  'Nature':1,  'Out':1},
 'Pluie':{'Residence':0,
  'Emploi':0,  'Energie':3,  'Nature':3,  'Out':2},
 'Vent':{'Residence':2,
  'Emploi':3,  'Energie':2,  'Nature':3,  'Out':1},
 'Neige':{'Residence':2,
  'Emploi':0,  'Energie':-2,  'Nature':-1,  'Out':-1}}
impact_meteos = {saisons[0]: impact_printemps, saisons[1]: impact_ete, saisons[2]: impact_automne, saisons[3]: impact_hiver, saisons[4]: impact_chaos}
meteo_origine_printemps = [
 'Soleil', 'Nuageux', 'Pluie', 'Vent', 'Neige', 'Brouillard']
meteo_origine_ete = ['Soleil', 'Nuageux', 'Pluie', 'Vent', 'Tempête', 'Brouillard']
meteo_origine_automne = ['Nuageux', 'Pluie', 'Vent', 'Tempête', 'Neige', 'Brouillard']
meteo_origine_hiver = ['Soleil', 'Nuageux', 'Pluie', 'Vent', 'Tempête', 'Neige']
meteo_origine = {'Printemps':meteo_origine_printemps,
 'Ete':meteo_origine_ete,  'Automne':meteo_origine_automne,  'Hiver':meteo_origine_hiver}

class Graphe:

    def __init__(self, saison: str, temps_du_jour: str) -> None:
        self.saison = saison
        self.temps = temps_du_jour
        self.meteo = meteos[saison]
        self.impact_meteo = impact_meteos[saison]

    def __str__(self) -> str:
        s = 'Nous sommes en ' + self.saison + '.\n'
        s += 'Le temps est : ' + self.temps + '.'
        return s

    def indice_temps(self) -> int:
        return temps.index(self.temps)

    def prevision_meteo_chaotique(self) -> str:
        if self.temps == temps_chaotique_classique[self.saison]:
            if randint(1, 100) <= 30:
                return temps_chaotique_classique[self.saison]
            else:
                return temps_chaotique_catastrophique[randint(0, 9)]
        else:
            return temps_chaotique_classique[self.saison]

    def prevision_meteo(self) -> str:
        assert not randint(1, 100) == 100
        alea = randint(1, 100)
        i = -1
        while 1:
            if alea > 0:
                i += 1
                alea -= self.meteo[self.indice_temps()][i]

        return temps[i]

    def comptage_types(liste_cases: list):
        compteur = {type:0 for type in ('Residence', 'Emploi', 'Energie', 'Nature',
                                        'Out')}
        for case in liste_cases:
            compteur[case.get_type()] += 1

        return compteur

    def impact_voisinage(self, type: str, voisins: list) -> int:
        compteur = Graphe.comptage_types(voisins)
        if type == 'Residence':
            if compteur['Emploi'] > 0:
                pass
        if compteur['Energie'] > 0:
            if compteur['Nature'] > 0:
                return 10
            return -5
        elif type == 'Emploi':
            nb = compteur['Emploi']
            if nb == 0 or nb == 4:
                return -5
            elif nb == 2:
                return 5
            else:
                return 10
        elif type == 'Energie':
            if compteur['Nature'] >= 2:
                return 5
            else:
                return -10
        elif type == 'Nature':
            if compteur['Nature'] >= 1:
                return 5
            else:
                return -5
        else:
            return 10

    def liste_coordonnees_proches_voisins(i, j):
        return [
         (
          i, (j + 1) % 10), (i, (j - 1) % 10), ((i - 1) % 10, j), ((i + 1) % 10, j)]

    def liste_coordonnees_voisins(i, j):
        liste = Graphe.liste_coordonnees_proches_voisins(i, j)
        liste += [((i - 1) % 10, (j - 1) % 10), ((i - 1) % 10, (j + 1) % 10), ((i + 1) % 10, (j - 1) % 10), ((i + 1) % 10, (j + 1) % 10)]
        liste += [((i - 2) % 10, j), ((i + 2) % 10, j), (i, (j - 2) % 10), (i, (j + 2) % 10)]
        return liste

    def liste_coordonnees_banlieue(i, j):
        liste = Graphe.liste_coordonnees_voisins(i, j)
        liste += [((i - 1) % 10, (j - 2) % 10), ((i - 1) % 10, (j + 2) % 10), ((i + 1) % 10, (j - 2) % 10), ((i + 1) % 10, (j + 2) % 10)]
        liste += [((i - 2) % 10, (j - 1) % 10), ((i - 2) % 10, (j + 1) % 10), ((i + 2) % 10, (j - 1) % 10), ((i + 2) % 10, (j + 1) % 10)]
        liste += [((i - 2) % 10, (j - 2) % 10), ((i - 2) % 10, (j + 2) % 10), ((i + 2) % 10, (j - 2) % 10), ((i + 2) % 10, (j + 2) % 10)]
        return liste

    def impact_zone(self, ville, i, j, modifications) -> None:
        carte = ville.get_carte()
        type = carte[i][j].get_type()
        if type == 'Residence':
            coordo = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in coordo:
                type = carte[x][y].get_type()
                if type == 'Residence':
                    modifications[x][y] += 1
                elif type == 'Nature':
                    modifications[x][y] -= 1

        elif type == 'Emploi':
            coordo = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in coordo:
                type = carte[x][y].get_type()
                if type == 'Nature':
                    modifications[x][y] -= 1
                elif type == 'Emploi':
                    modifications[x][y] += 1

            coordo = Graphe.liste_coordonnees_proches_voisins(i, j)
            for x, y in coordo:
                if carte[x][y].get_type() != 'Residence':
                    modifications[x][y] -= 2

        elif type == 'Energie':
            coordo = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in coordo:
                if carte[x][y].get_type() != 'Energie':
                    modifications[x][y] -= 1

        elif type == 'Nature':
            coordo = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in coordo:
                modifications[x][y] -= 1

            coordo = Graphe.liste_coordonnees_banlieue(i, j)
            for x, y in coordo:
                if carte[x][y].get_type() in ('Nature', 'Out'):
                    modifications[x][y] += 2

    def autour_la_nature(carte: list, i: int, j: int) -> bool:
        if carte[i][((j + 1) % 10)].get_type() != 'Nature' or carte[i][((j - 1) % 10)].get_type() != 'Nature':
            return False
        elif carte[((i - 1) % 10)][j].get_type() != 'Nature' or carte[((i + 1) % 10)][j].get_type() != 'Nature':
            return False
        elif carte[((i + 1) % 10)][((j + 1) % 10)].get_type() != 'Nature' or carte[((i - 1) % 10)][((j - 1) % 10)].get_type() != 'Nature':
            return False
        elif carte[((i - 1) % 10)][((j + 1) % 10)].get_type() != 'Nature' or carte[((i + 1) % 10)][((j - 1) % 10)].get_type() != 'Nature':
            return False
        else:
            return True

    def chaos_seisme(ville: Meteopolis, modifications: list) -> None:
        for i in range(len(modifications)):
            for j in range(len(modifications[i])):
                if ville.get_carte()[i][j].get_type() in ('Residence', 'Emploi'):
                    modifications[i][j] -= 20

    def chaos_inondation(ville: Meteopolis, modifications: list) -> None:
        for i in range(len(modifications)):
            for j in range(len(modifications[i])):
                if ville.get_carte()[i][j].get_type() in ('Nature', 'Energie'):
                    modifications[i][j] -= 20

    def chaos_meteorites(ville: Meteopolis, modifications: list) -> None:
        for i in range(5):
            x = randint(0, 9)
            y = randint(0, 9)
            modifications[x][y] -= 50
            liste = Graphe.liste_coordonnees_proches_voisins(x, y)
            for a, b in liste:
                modifications[a][b] -= 10

    def chaos_tornade(modifications: list) -> None:
        alea = randint(0, len(modifications) - 1)
        if randint(0, 1) == 0:
            for j in range(len(modifications[alea])):
                modifications[alea][j] -= 30

        else:
            for i in range(len(modifications)):
                modifications[i][alea] -= 30

    def chaos_canicule(modifications: list) -> None:
        for i in range(len(modifications)):
            for j in range(len(modifications[i])):
                modifications[i][j] -= 5

    def chaos_foudre(ville: Meteopolis, modifications: list) -> None:
        for i in range(len(modifications)):
            for j in range(len(modifications[i])):
                if ville.get_carte()[i][j].get_type() in ('Energie', 'Emploi'):
                    modifications[i][j] -= 20

    def chaos_epidemie(ville: Meteopolis, modifications: list) -> None:
        for i in range(len(modifications)):
            for j in range(len(modifications[i])):
                if ville.get_carte()[i][j].get_type() in ('Residence', 'Nature'):
                    modifications[i][j] -= 20

    def chaos_volcan(modifications: list) -> None:
        alea = randint(1, 4)
        if alea == 1:
            x, y = (0, 0)
        elif alea == 2:
            x, y = (0, 9)
        elif alea == 3:
            x, y = (9, 0)
        else:
            x, y = (9, 9)
        modifications[x][y] -= 100
        liste = Graphe.liste_coordonnees_voisins(x, y)
        for a, b in liste:
            modifications[a][b] -= 10

    def chaos_demon(modifications: list) -> None:
        alea = randint(1, 4)
        if alea == 1:
            x, y = (4, 4)
        elif alea == 2:
            x, y = (4, 5)
        elif alea == 3:
            x, y = (5, 4)
        else:
            x, y = (5, 5)
        modifications[x][y] -= 100
        liste = Graphe.liste_coordonnees_voisins(x, y)
        for a, b in liste:
            modifications[a][b] -= 10

    def chaos_ovni(modifications: list) -> None:
        liste = [(2, 3), (2, 4), (2, 5), (2, 6), (3, 2), (4, 2), (5, 2), (6, 2), (7, 3), (7, 4), (7, 5), (7, 6), (3, 7), (4, 7), (5, 7), (6, 7)]
        for x, y in liste:
            modifications[x][y] -= 20

    def gestion_meteo_catastrophique(self, ville: Meteopolis, modifications: list) -> None:
        meteo = self.temps
        if meteo == temps_chaotique_catastrophique[0]:
            Graphe.chaos_seisme(ville, modifications)
        elif meteo == temps_chaotique_catastrophique[1]:
            Graphe.chaos_inondation(ville, modifications)
        elif meteo == temps_chaotique_catastrophique[2]:
            Graphe.chaos_meteorites(ville, modifications)
        elif meteo == temps_chaotique_catastrophique[3]:
            Graphe.chaos_tornade(modifications)
        elif meteo == temps_chaotique_catastrophique[4]:
            Graphe.chaos_canicule(modifications)
        elif meteo == temps_chaotique_catastrophique[5]:
            Graphe.chaos_foudre(ville, modifications)
        elif meteo == temps_chaotique_catastrophique[6]:
            Graphe.chaos_epidemie(ville, modifications)
        elif meteo == temps_chaotique_catastrophique[7]:
            Graphe.chaos_volcan(modifications)
        elif meteo == temps_chaotique_catastrophique[8]:
            Graphe.chaos_demon(modifications)
        else:
            Graphe.chaos_ovni(modifications)

    def meteo_originelle(self) -> str:
        alea = randint(0, 5)
        return meteo_origine[self.saison][alea]

    def maj_case(ville: Meteopolis, i: int, j: int) -> bool:
        case = ville.get_carte()[i][j]
        vie = case.get_vie()
        type = case.get_type()
        if vie == 0 or type == 'Out':
            return True
        else:
            if vie < 100:
                pass
            if case.magnifique:
                return True
            if vie == 100:
                if not case.magnifique:
                    comptage = {'Residence':0,
                     'Emploi':0,  'Nature':0,  'Energie':0,  'Out':0}
                    carte = ville.get_carte()
                    if type == 'Residence':
                        alentours = Graphe.liste_coordonnees_banlieue(i, j)
                        for x, y in alentours:
                            comptage[carte[x][y].get_type()] += 1

                        return comptage['Emploi'] >= 2 and comptage['Energie'] >= 2 and comptage['Nature'] >= 2
                    if type == 'Emploi':
                        alentours = Graphe.liste_coordonnees_proches_voisins(i, j)
                        for x, y in alentours:
                            comptage[carte[x][y].get_type()] += 1

                        if comptage['Emploi'] not in (2, 3):
                            return False
                        comptage = {'Residence':0,  'Emploi':0,  'Nature':0,  'Energie':0,  'Out':0}
                        alentours = Graphe.liste_coordonnees_banlieue(i, j)
                        for x, y in alentours:
                            comptage[carte[x][y].get_type()] += 1

                        return comptage['Residence'] >= 7
                    if type == 'Energie':
                        alentours = Graphe.liste_coordonnees_voisins(i, j)
                        for x, y in alentours:
                            comptage[carte[x][y].get_type()] += 1

                        if comptage['Nature'] not in (3, 4, 5):
                            return False
                        alentours = Graphe.liste_coordonnees_banlieue(i, j)
                        for x, y in alentours:
                            if carte[x][y].get_type() == 'Energie':
                                return True

                        return False
                    if type == 'Nature':
                        alentours = Graphe.liste_coordonnees_proches_voisins(i, j)
                        for x, y in alentours:
                            if carte[x][y].get_type() == 'Energie':
                                return False

                        alentours = Graphe.liste_coordonnees_voisins(i, j)
                        for x, y in alentours:
                            comptage[carte[x][y].get_type()] += 1

                        if comptage['Emploi'] > 1:
                            return False
                        comptage = 0
                        alentours = Graphe.liste_coordonnees_banlieue(i, j)
                        for x, y in alentours:
                            if carte[x][y].get_type() == 'Nature':
                                comptage += 1

                        return comptage >= 5
            return False

    def ville_de_demain(ville: Meteopolis) -> Meteopolis:
        change_saison = False
        if ville.get_jour() % 30 == 0:
            if ville.get_jour != 0:
                change_saison = True
                ville.set_saison()
            graphe = Graphe(ville.get_saison(), ville.get_temps())
            if ville.get_chaos() % 7 != 0:
                ville.incremente_chaos()
                new_meteo = graphe.prevision_meteo_chaotique()
            elif ville.est_chaos:
                ville.est_chaos = False
                new_meteo = graphe.meteo_originelle()
        if change_saison:
            new_meteo = graphe.meteo_originelle()
        else:
            try:
                new_meteo = graphe.prevision_meteo()
            except ValueError:
                ville.est_chaos = True
                ville.incremente_chaos()
                new_meteo = graphe.prevision_meteo_chaotique()

            ville.incremente_jour()
            ville.set_temps(new_meteo)
            graphe.temps = new_meteo
            modifications = [[0 for j in range(len(ville.get_carte()[i]))] for i in range(len(ville.get_carte()))]
            if graphe.temps in temps_chaotique_catastrophique:
                graphe.gestion_meteo_catastrophique(ville, modifications)
            else:
                for i in range(len(ville.get_carte())):
                    for j in range(len(ville.get_carte()[i])):
                        case = ville.get_carte()[i][j]
                        modifications[i][j] += graphe.impact_meteo[graphe.temps][case.get_type()]

            for i in range(len(ville.get_carte())):
                for j in range(len(ville.get_carte()[i])):
                    case = ville.get_carte()[i][j]
                    voisins = ville.voisinage(i, j)
                    modifications[i][j] += graphe.impact_voisinage(case.get_type(), voisins)
                    graphe.impact_zone(ville, i, j, modifications)

            for i in range(len(ville.get_carte())):
                for j in range(len(ville.get_carte()[i])):
                    case = ville.get_carte()[i][j]
                    case.modif_vie(modifications[i][j])
                    if Graphe.maj_case(ville, i, j):
                        case.verif_case()

            for i in range(len(ville.get_carte())):
                for j in range(len(ville.get_carte()[i])):
                    carte = ville.get_carte()
                    if carte[i][j].get_type() == 'Nature':
                        if Graphe.autour_la_nature(carte, i, j):
                            carte[i][j].new_type('Energie')
                            carte[i][j].set_vie(50)

            return ville

    def calcul_score(ville: Meteopolis) -> int:
        carte = ville.get_carte()
        somme = {'Residence':0,  'Emploi':0,  'Nature':0,  'Energie':0}
        comptage = {'Residence':0,  'Emploi':0,  'Nature':0,  'Energie':0}
        for i in range(len(carte)):
            for j in range(len(carte[i])):
                case = carte[i][j]
                type = case.get_type()
                if type != 'Out':
                    somme[type] += case.get_vie()
                    comptage[type] += 1

        score = 0
        multiplicateur = 1
        while somme != {}:
            type_max = ''
            nbre_max = 0
            for type in comptage:
                if comptage[type] > nbre_max or comptage[type] == nbre_max and somme[type] > somme[type_max]:
                    type_max = type
                    nbre_max = comptage[type]

            score += somme.pop(type_max) * multiplicateur
            multiplicateur += 1
            comptage.pop(type_max)

        return score


    #J'ai rajouté cette méthode pour savoir si une case peut devenir magnifique ou non en fonction de son entourage.
    def peu_devenir_magnifique(ville, i, j):
        case = ville[i][j]
        vie = case.get_vie()
        type = case.get_type()
        comptage = {'Residence':0, 'Emploi':0,  'Nature':0,  'Energie':0,  'Out':0}
        carte = ville
        if type == 'Residence':
            alentours = Graphe.liste_coordonnees_banlieue(i, j)
            for x, y in alentours:
                comptage[carte[x][y].get_type()] += 1

            return comptage['Emploi'] >= 2 and comptage['Energie'] >= 2 and comptage['Nature'] >= 2
        if type == 'Emploi':
            alentours = Graphe.liste_coordonnees_proches_voisins(i, j)
            for x, y in alentours:
                comptage[carte[x][y].get_type()] += 1

            if comptage['Emploi'] not in (2, 3):
                return False
            comptage = {'Residence':0,  'Emploi':0,  'Nature':0,  'Energie':0,  'Out':0}
            alentours = Graphe.liste_coordonnees_banlieue(i, j)
            for x, y in alentours:
                comptage[carte[x][y].get_type()] += 1

            return comptage['Residence'] >= 7
        if type == 'Energie':
            alentours = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in alentours:
                comptage[carte[x][y].get_type()] += 1

            if comptage['Nature'] not in (3, 4, 5):
                return False
            alentours = Graphe.liste_coordonnees_banlieue(i, j)
            for x, y in alentours:
                if carte[x][y].get_type() == 'Energie':
                    return True

            return False
        if type == 'Nature':
            alentours = Graphe.liste_coordonnees_proches_voisins(i, j)
            for x, y in alentours:
                if carte[x][y].get_type() == 'Energie':
                    return False

            alentours = Graphe.liste_coordonnees_voisins(i, j)
            for x, y in alentours:
                comptage[carte[x][y].get_type()] += 1

            if comptage['Emploi'] > 1:
                return False
            comptage = 0
            alentours = Graphe.liste_coordonnees_banlieue(i, j)
            for x, y in alentours:
                if carte[x][y].get_type() == 'Nature':
                    comptage += 1

            return comptage >= 5
        return False
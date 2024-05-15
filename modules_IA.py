import random
from graphe import Graphe
import gc

### Code de l'IA ###

def compter_cases(carte):
    '''Compte le nombre de cases de chaque type dans une carte'''
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

def afficher(carte):
    '''Affiche la carte en argument'''
    for i in carte:
        ligne = ""
        for j in i:
            ligne += str(j.get_vie()) + " "
        print(ligne)


def ameliorer_carte(carte):
    '''Améliore la carte en changeant le type de cases qui ne peuvent devenir magnifique de manière aléatoire'''
    type = ['Residence', 'Emploi', 'Nature', 'Energie']

    for i in range(random.randint(2, 70)):
        x, y = random.randint(0, 9), random.randint(0, 9)
        if not Graphe.peu_devenir_magnifique(carte, x, y):
            carte[x][y].new_type(random.choice(type))

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

    del i, j, x, y, type

    gc.collect()

    return ameliorer_carte_deuxieme_etape(carte)

def ameliorer_carte_deuxieme_etape(carte):
    '''Fait la même chose que la méthode précédente, mais modifie n'importe qu'elle case'''
    type = ['Residence', 'Emploi', 'Nature', 'Energie']

    for i in range(random.randint(0, 10)):
        x, y = random.randint(0, 9), random.randint(0, 9)
        carte[x][y].new_type(random.choice(type))

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

    gc.collect()

    return carte


def recherche_de_maximum(liste_de_tuples):
    '''Retourne la carte avec le meilleur score'''
    if not liste_de_tuples:
        return None, None

    maximum = liste_de_tuples[0]
    indice_maximum = 0
    for i, element in enumerate(liste_de_tuples[1:], start=1):
        if element[1] > maximum[1]:
            maximum = element
            indice_maximum = i

    del liste_de_tuples, i, element

    gc.collect()

    return maximum, indice_maximum
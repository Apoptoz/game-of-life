from substrat import TAILLE_GRILLE
from random import randint


class Population:
    #pop_list : [nb_white,nb_blue,nb_black,nb_red,nb_green]
    def __init__(self,pop_list):
        self.pop = init_pop(pop_list)



def init_pop(pop_list):
    pos_list = []
    cell_population=[]
    for white_cell in range(pop_list[0]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(CelluleBlanche((x,y)))
    for blue_cell in range(pop_list[1]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(CelluleBleue((x,y)))
    for black_cell in range(pop_list[2]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(CelluleNoire((x,y)))
    for red_cell in range(pop_list[3]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(CelluleRouge((x,y)))
    for green_cell in range(pop_list[4]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(CelluleVerte((x,y)))
    return cell_population


def random_pos(pos_list):
    (x,y) = (randint(0,TAILLE_GRILLE),randint(0,TAILLE_GRILLE))
    while (x,y) not in pos_list:
        (x,y) = (randint(0,TAILLE_GRILLE),randint(0,TAILLE_GRILLE))
    return (x,y)

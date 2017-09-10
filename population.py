from main import NB_LIGNE,NB_COLONNE
from random import randint
import cellule

class Population:
    #pop_list : [nb_white,nb_blue,nb_black,nb_red,nb_green]
    def __init__(self,pop_list):
        self.pop = init_pop(pop_list)

    def __getitem__(self,key):
        return self.pop[key]

    def __setitem__(self,key,item):
        self.pop[key] = item

    def __len__(self): return len(self.pop)
    def __delitem__(self,key): del self.pop[key]

    def __iter__(self): return iter(self.pop)
    def __next__(self): return next(self.pop)


def init_pop(pop_list):
    pos_list = []
    cell_population=[]
    for white_cell in range(pop_list[0]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(cellule.CelluleBlanche((x,y)))
    for blue_cell in range(pop_list[1]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(cellule.CelluleBleue((x,y)))
    for black_cell in range(pop_list[2]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(cellule.CelluleNoire((x,y)))
    for red_cell in range(pop_list[3]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(cellule.CelluleRouge((x,y)))
    for green_cell in range(pop_list[4]):
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(cellule.CelluleVerte((x,y)))
    return cell_population

TAILLE_GRILLE =  20

def random_pos(pos_list):
    (x,y) = (randint(0,TAILLE_GRILLE),randint(0,TAILLE_GRILLE))
    while (x,y) in pos_list:
        (x,y) = (randint(0,TAILLE_GRILLE),randint(0,TAILLE_GRILLE))
    return (x,y)

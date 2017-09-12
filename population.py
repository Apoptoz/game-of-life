from main import NB_LIGNE,NB_COLONNE
from random import randint
from substrat import grille
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


def init_pop(self):
    pos_list = []
    cell_population=[]
    for white_cell in range(pop_list[0]):
        new_cell = cellule.CelluleBlanche((x,y))
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(new_cell)
        grille[x,y].cells_on_case = new_cell
    for blue_cell in range(pop_list[1]):
        new_cell = cellule.CelluleBleue((x,y))
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(new_cell)
        grille[x,y].cells_on_case = new_cell
    for black_cell in range(pop_list[2]):
        new_cell = cellule.CelluleNoire((x,y))
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(new_cell)
        grille[x,y].cells_on_case = new_cell
    for red_cell in range(pop_list[3]):
        new_cell = cellule.CelluleRouge((x,y))
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(new_cell)
        grille[x,y].cells_on_case = new_cell
    for green_cell in range(pop_list[4]):
        new_cell = cellule.CelluleVerte((x,y))
        (x,y) = random_pos(pos_list)
        pos_list.append((x,y))
        cell_population.append(new_cell)
        grille[x,y].cells_on_case = new_cell
    return cell_population

#Défini une position aléatoire non existante dans la grille.
def random_pos(pos_list):
    (x,y) = (randint(0,NB_COLONNE-1),randint(0,NB_LIGNE-1))
    while (x,y) in pos_list:
        (x,y) = (randint(0,TAILLE_GRILLE),randint(0,TAILLE_GRILLE))
    return (x,y)

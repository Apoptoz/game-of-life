import random
from substrat import grille,cases_adjacentes

MAX_AGE = 10
BASE_ENERGY = 3


class Cellule:
    def __init__(self,colour,age,max_age,energy,coord):
        self.age = age
        self.energy = energy
        self.max_age = max_age
        self.colour = colour
        self.coord_x = coord[0]
        self.coord_y = coord[1]

    def __str__(self):
        return "coord :"+str(self.coord_x)+" "+str(self.coord_y)

    def eat(self):
       self.energy += 2
           #Survie : toute cellule seule dans une case comportant de la nourriture voit son niveau d'énergie augmenter de 2 et le niveau d'énergie de la case diminué de 1.
    def fight(self):
        self.energy -= 1
        #Affrontement : toute case occupée par deux cellules de couleur différente voit le niveau d'énergie de chaque cellule diminué d'1 point (sauf capacité spéciale propre à chaque couleur de cellule, cf. définition des cellules).

    #CelluleBlanche : cellule immunisée à l'une des 4 autres couleurs,choisie au hasard pour chaque instance de CelluleBlanche
    #CelluleBleue : celle-ci comporte une autre couleur à sa naissance, qu'elle fournira à une cellule d'une autre couleur que bleue. Si la couleur correspond, elle subit la règle de dommage lors de l'affrontement mais elle peut se reproduire et donner naissance à une cellule bleue
    #CelluleNoire : cellule ayant 25% de chance de réapparaître sur lieu de sa mort avec un niveau d'énergie maximum i.e 3 mais en conservant l'âge qu'elle avait au moment de sa mort
    #CelluleRouge : cellule enlevant 1 point d'énergie supplémentaire à une cellule d'une autre couleur (en plus du point de dommage lors de l'affrontement)
    #CelluleVerte : cellule ayant un niveau d'énergie supplémentaire (3 points de plus que les autres couleurs)

    def death(self):
        print("mort")

    def reproduce(self):
        print("reproduce")

    def move(self):
        cases_autour = cases_adjacentes(self.coord_x,self.coord_y)
        if self.energy => 1:
            self.energy -= 1
            if(grille[self.coord_x][self.coord_y].nb_food >= 1):
                #rien ?

            elif(is_food_and_friend(cases_autour)):
                for case in cases_autour:
                    if grille[case.coord_x][case.coord_y].nb_food > 0:
                        self.coord_x = case.coord_x
                        self.coord_y = case.coord_y
            elif(3):
            elif(4):
            elif(5):
            elif(6):
            elif(7):
            else:


class CelluleBlanche(Cellule):
    def __init__(self,coord):
        Cellule.__init__(self,"W",0,MAX_AGE+10,BASE_ENERGY,coord)
        self.immune = random_colour("W") #définir la fonction random_colour
class CelluleBleue(Cellule):
    def __init__(self,coord):
        Cellule.__init__(self,"B",0,MAX_AGE,BASE_ENERGY,coord)
        self.chromia = random_colour("B")

    def move(self):
        print("déplacement bleue")
class CelluleNoire(Cellule):
    def __init__(self,coord):
        Cellule.__init__(self,"N",0,MAX_AGE,BASE_ENERGY,coord)

    def mort(self):
        print("mort noire")

    def reproduce(self):
        print("reproduction noire")
class CelluleRouge(Cellule):
    def __init__(self,coord):
        Cellule.__init__(self,"R",0,MAX_AGE,BASE_ENERGY,coord)

    def fight(self):
        print("affrontement rouge")
class CelluleVerte(Cellule):
    def __init__(self,coord):
        Cellule.__init__(self,"G",0,MAX_AGE,BASE_ENERGY+3,coord)


def random_colour(colour_to_remove):
    colour_set={"W","B","G","N","R"} - {colour_to_remove}
    chosen_colour = random.sample(colour_set,1)
    return chosen_colour

def is_food_and_friend(cases_atour,cell_colour):
    for case in cases_autour:
        case_grille = grille[case.coord_x][case.coord_y]
        if case_grille.nb_food > 0:
            if len(case_grille.cells_on_case) == 1 and case_grille.cells_on_case.colour == cell_colour):
                return case.coord_x,case.coord_y
    return False

def is_only_friend(cases_autour):


blanche = Cellule("B",0,20,3,(10,10))

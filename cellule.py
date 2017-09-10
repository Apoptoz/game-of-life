
MAX_AGE = 10
BASE_ENERGY = 3


class Cellule:
    def __init__(self,colour,age,max_age,energy,coord_x,coord_y):
        self.age = age
        self.energy = energy
        self.colour = colour
        self.coord_x = coord_x
        self.coord_y = coord_y

	def eat(self,energy):
		self.energy =+ 2
#Survie : toute cellule seule dans une case comportant de la nourriture voit son niveau d'énergie augmenter de 2 et le niveau d'énergie de la case diminué de 1.

	def fight(self,energy):
		self.energy =- 1
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
        print("move")



class CelluleBlanche(Cellule):
    def __init__(self,coord_x,coord_y):
        Cellule.__init__(self,"W",0,MAX_AGE+10,BASE_ENERGY,coord_x,coord_y)
        self.immune = random_colour("W") #définir la fonction random_colour


class CelluleBleue(Cellule):
    def __init__(self,coord_x,coord_y):
        Cellule.__init__(self,"B",0,MAX_AGE,BASE_ENERGY,coord_x,coord_y)
        self.chromia = random_colour("B")

    def move(self):
        print("déplacement bleue")

class CelluleNoire(Cellule):
    def __init__(self,coord_x,coord_y):
        Cellule.__init__(self,"N",0,MAX_AGE,BASE_ENERGY,coord_x,coord_y)

    def mort(self):
        print("mort noire")

    def reproduce(self):
        print("reproduction noire")

class CelluleRouge(Cellule):
    def __init__(self,coord_x,coord_y):
        Cellule.__init__(self,"R",0,MAX_AGE,BASE_ENERGY,coord_x,coord_y)

    def fight(self):
        print("affrontement rouge")

class CelluleVerte(Cellule):
    def __init__(self,coord_x,coord_y):
        Cellule.__init__(self,"G",0,MAX_AGE,BASE_ENERGY+3,coord_x,coord_y)


def random_colour(colour_to_remove):
    colour_set={"W","B","G","N","R"}
    


blanche = Cellule("B",0,20,3,10,10,immune=random_colour)

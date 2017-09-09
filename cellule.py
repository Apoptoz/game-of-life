

class Cellule:
    def __init__(self,colour,age,max_age,energy,coord_x,coord_y,immune=None):
        self.age = age
        self.energy = energy
        self.colour = colour
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.immune = immune

	def survie(self,energy):
		self.energy =+ 2
#Survie : toute cellule seule dans une case comportant de la nourriture voit son niveau d'énergie augmenter de 2 et le niveau d'énergie de la case diminué de 1.

	def affrontement(self,energy):
		self.energy =- 1
#Affrontement : toute case occupée par deux cellules de couleur différente voit le niveau d'énergie de chaque cellule diminué d'1 point (sauf capacité spéciale propre à chaque couleur de cellule, cf. définition des cellules).


    #CelluleBlanche : cellule immunisée à l'une des 4 autres couleurs,choisie au hasard pour chaque instance de CelluleBlanche
    #CelluleBleue : celle-ci comporte une autre couleur à sa naissance, qu'elle fournira à une cellule d'une autre couleur que bleue. Si la couleur correspond, elle subit la règle de dommage lors de l'affrontement mais elle peut se reproduire et donner naissance à une cellule bleue
    #CelluleNoire : cellule ayant 25% de chance de réapparaître sur lieu de sa mort avec un niveau d'énergie maximum i.e 3 mais en conservant l'âge qu'elle avait au moment de sa mort
    #CelluleRouge : cellule enlevant 1 point d'énergie supplémentaire à une cellule d'une autre couleur (en plus du point de dommage lors de l'affrontement)
    #CelluleVerte : cellule ayant un niveau d'énergie supplémentaire (3 points de plus que les autres couleurs)



blanche = Cellule("B",0,20,3,10,10,immune=random_colour)

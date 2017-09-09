

class Cellule:
    def __init__(self,colour,age,max_age,energy,coord_x,coord_y,immune=None):
        self.age = age
        self.energy = energy
        self.colour = colour
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.immune = immune


    def death(self):
        print("mort")

    def reproduce(self):
        print("reproduce")

    def move(self):
        print("move")


blanche = Cellule("B",0,20,3,10,10,immune=random_colour)

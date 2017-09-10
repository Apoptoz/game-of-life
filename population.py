


class Population:
    #pop_list : [nb_white,nb_blue,nb_black,nb_red,nb_green]
    def __init__(self,pop_list):
        self.pop = init_pop(pop_list)



def init_pop(pop_list):
    cell_population=[]
    for white_cell in range(pop_list[0]):
        print("Faut lier la grille pour voir si y a pas deja une cell ?")
        print("Ou bien créer une liste des cellules déja ajoutées ?")

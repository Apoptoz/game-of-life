from main import LARGEUR_GRILLE,HAUTEUR_GRILLE

class Substrat:

	def __init__(self, cells_on_case,coord,nb_food=0):
		#Liste des cellules présentes
		self.cells_on_case = cells_on_case
		self.coord_x = coord[0]
		self.coord_y = coord[1]
		self.nb_food = nb_food

#Y a pas besoin de faire une classe grille en fait ????
class Grille:
	def __init__(self,TAILLE_GRILLE):
		self.grille = [Substrat(None,(i,j)) for i in range(HAUTEUR_GRILLE) for j in range(LARGEUR_GRILLE)]


grille = [[Substrat(None,(i,j)) for i in range(TAILLE_GRILLE)] for j in range(TAILLE_GRILLE)]

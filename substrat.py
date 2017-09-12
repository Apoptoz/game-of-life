from main import NB_LIGNE,NB_COLONNE

class Substrat:

	def __init__(self, cells_on_case,coord,nb_food=0):
		#Liste des cellules présentes
		self.cells_on_case = cells_on_case
		self.coord_x = coord[0]
		self.coord_y = coord[1]
		self.nb_food = nb_food


grille = [[Substrat(None,(i,j)) for i in range(HAUTEUR_GRILLE)] for j in range(LARGEUR_GRILLE)]

#Défini les cases adjacentes à (i,j)
def cases_adjacentes(i,j):
	def is_inside(x,y):
		return x>=0 && x<LARGEUR_GRILLE && y>=0 && y<HAUTEUR_GRILLE
	cases_adjacentes = [(i-1,j-1),(i,j-1),(i+1,j-1),
	(i-1,j),(i+1,j),
	(i-1,j+1),(i,j+1),(i+1,j+1)]
	return [cases_inside for cases_inside in cases_adjacentes if is_inside(cases_inside)]

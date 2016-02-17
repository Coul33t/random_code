# Labyrinth generation

import random as rn

#TODO : display of the labyrinth

LABYRINTH_X = 10
LABYRINTH_Y = 10

class Tile:
	
	def __init__(self):
		self._visited = False
		self._openState = [0,0,0,0] # clockwise, starting at the top

	def _getVisited(self):
		return self._visited

	def _getOpenState(self):
		return self._openState

	def _setVisited(self, visited):
		self._visited = visited

	def _setOpenState(self, openState):
		self._openState = openState

	visited = property(_getVisited, _setVisited)
	openState = property(_getOpenState, _setOpenState)

	def openPath(self, orientation):
		self._openState[orientation] = 1

	



def initializeLabyrinth():
	labyrinth = [[Tile() for y in range(LABYRINTH_Y)] for x in range(LABYRINTH_X)]
	return labyrinth

def checkNeighboors(x, y, labyrinth):
	available_neighboors = [0,0,0,0] # clockwise, starting at the top
	
	if(x > 0):
		if not labyrinth[x-1][y].visited:
			available_neighboors[3] = 1

	if(y > 0):
		if not labyrinth[x][y-1].visited:
			available_neighboors[0] = 1

	if(x < LABYRINTH_X-1):
		if not labyrinth[x+1][y].visited:
			available_neighboors[1] = 1

	if(y < LABYRINTH_Y-1):
		if not labyrinth[x][y+1].visited:
			available_neighboors[2] = 1

	return available_neighboors


def constructLabyrinth(labyrinth):
	walls_to_open = (LABYRINTH_X * LABYRINTH_Y) - 1
	tiles_coordinates_stack = []

	current_x = rn.randint(0, LABYRINTH_X - 1)
	current_y = rn.randint(0, LABYRINTH_Y - 1)

	while(walls_to_open > 0):
		tiles_coordinates_stack.append([current_x, current_y])
		available_neighboors = checkNeighboors(current_x, current_y, labyrinth)

		#If there's an avaible neighboor
		if sum(available_neighboors) > 0:

			#Assure that we take an available neighboor
			rand_neighboor = rn.randint(0,3)
			while not available_neighboors[rand_neighboor]:
				rand_neighboor = rn.randint(0,3)

			labyrinth[current_x][current_y].openPath(rand_neighboor)

			if rand_neighboor == 0:
				current_y -= 1

			elif rand_neighboor == 1:
				current_x += 1

			elif rand_neighboor == 2:
				current_y += 1

			elif rand_neighboor == 3:
				current_x -= 1

			walls_to_open -= 1



		#We go back
		else:
			if len(tiles_coordinates_stack) > 0:
				current_x, current_y = tiles_coordinates_stack.pop()

			else:
				print('We shouldn\'t be there.')

	return labyrinth



		


if __name__=="__main__":
	labyrinth = initializeLabyrinth()
	labyrinth = constructLabyrinth(labyrinth)

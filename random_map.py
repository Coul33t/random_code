# Random map generation
import math
import random as rn
import pygame
from pygame.locals import *
import pdb


MATCHING = ['.','#']
X_SIZE = 640
Y_SIZE = 640
TILE_SIZE = 8

def generate_random_map(x, y):
	return [[rn.randint(0,1) for i in range(x)] for j in range(y)]


# Rule :
# if a water tile is surrounded by 3 or more land tile, it becomes a land tile.
def refine_inner_land(game_map):
	game_map_tmp = game_map
	for x in range(len(game_map)):
		for y in range(len(game_map[x])):
			if(game_map[x][y] == 0):
				if(sum(get_four_neighboors(game_map, x, y)) > 2):
					game_map_tmp[x][y] = 1


	return game_map_tmp


# Rule :
# if a land tile is surrounded by 2 or less land tile, it becomes a water tile.
def refine_outer_land(game_map):
	game_map_tmp = game_map
	for x in range(len(game_map)):
		for y in range(len(game_map[x])):
			if(game_map[x][y] == 1):
				if(sum(get_eight_neighboors(game_map, x, y)) < 3):
					game_map_tmp[x][y] = 0
	

	return game_map_tmp

#Rule :
# if a land tile is surrounded (16 tiles) by 6 or less tile, it becomes a water tile.
def erase_isolated_land(game_map):
	game_map_tmp = game_map
	for x in range(len(game_map)):
		for y in range(len(game_map[x])):
			if(game_map[x][y] == 1):
				if(sum(get_sixteen_neighboors(game_map, x, y)) < 7):
					game_map_tmp[x][y] = 0
	

	return game_map_tmp

#TODO : connected components
#if water:
#	explore around
#	mark explored
#	when no more water not explored:
#	if size list < 10% tile number:
#		water = land

def explore(game_map,x,y,explored):
	valid_neighboors = 4
	if game_map[x][y] == 0 and not explored[x][y]:
		explored[x][y] = True
		for coordinates in get_four_neighboors(game_map, x, y):
			pdb.set_trace()
			if explored[coordinates[0]][coordinates[1]] == False:
				coord_lst.append(explore(game_map, coordinates[0], coordinates[1]))
			else:
				valid_neighboors -= 1

		if valid_neighboors == 0:
			return(x,y)



def erase_inner_water(game_map):
	explored = [[False for i in range(len(game_map[j]))] for j in range(len(game_map))]
	tile_list = []

	for x in range(len(game_map)):
		for y in range(len(game_map)):
			if game_map[x][y] == 0 and not explored[x][y]:
				tile_list = explore(game_map,x,y,explored)

	return tile_list



def get_sixteen_neighboors(grid, x, y):	
	xi = [0, -1, -2, 1, 2] if 1 < x < len(grid) - 2 else ([0, -1, 1] if 0 < x < len(grid)-1 else ([0, -1] if x > 0 else [0, 1]))
	yi = [0, -1, -2, 1, 2] if 1 < y < len(grid[0]) - 2 else ([0, -1, 1] if 0 < y < len(grid[0])-1 else ([0, -1] if y > 0 else [0, 1]))

	for a in xi:
		for b in yi:
			if a == b == 0:
				continue
			yield grid[x + a][y + b]

# return the 8 neigbhoors of a tile
def get_eight_neighboors(grid, x, y):	
	xi = [0, -1, 1] if 0 < x < len(grid) - 1 else ([0, -1] if x > 0 else [0, 1])
	yi = [0, -1, 1] if 0 < y < len(grid[0]) - 1 else ([0, -1] if y > 0 else [0, 1])

	for a in xi:
		for b in yi:
			if a == b == 0:
				continue
			yield grid[x + a][y + b]



# return the 4 neigbhoors of a tile (up, down, left, right)
def get_four_neighboors(grid, x, y):
	xi = [0, -1, 1] if 0 < x < len(grid) - 1 else ([0, -1] if x > 0 else [0, 1])
	yi = [0, -1, 1] if 0 < y < len(grid[0]) - 1 else ([0, -1] if y > 0 else [0, 1])

	for a in xi:
		for b in yi:
			if math.fabs(a) == math.fabs(b):
				continue
			yield grid[x + a][y + b]



def display_map(game_map):
	print('\n\n')
	for x in range(len(game_map)):
		print('')
		for y in range(len(game_map[x])):
			print(MATCHING[game_map[x][y]], end='')
	print('\n\n')
	


def display_map(screen, terrain):
	for x in range(len(terrain)):
		for y in range(len(terrain[x])):
			color = (255,255,255)
			if terrain[x][y] == 0:
				color = (100, 100, 255)
			elif terrain[x][y] == 1:
				color = (100, 255, 100)
			pygame.draw.rect(screen, color, pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, x+TILE_SIZE, y+TILE_SIZE))

	pygame.display.flip()


def generate_fake_list():
	return [[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,1,1,1,0,0,0,0],
			[0,0,0,0,1,1,0,0,0,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,0,0,0,0,0,0,0,1,0],
			[0,0,0,0,0,0,0,1,1,0],
			[0,0,0,0,0,0,0,0,0,0],
			[0,1,0,0,0,0,0,0,0,0]]

if __name__ == '__main__':

	pygame.init()
	screen = pygame.display.set_mode((Y_SIZE,X_SIZE))

	game_map = generate_random_map((int)(X_SIZE/TILE_SIZE),(int)(Y_SIZE/TILE_SIZE))

	continued = 1

	display_map(screen, game_map)

	#yo = generate_fake_list()
	#print(erase_inner_water(yo))
	#pdb.set_trace()

	while continued:
		for event in pygame.event.get():
        
			if event.type == QUIT:
				continued = 0
	        
			if event.type == KEYDOWN:   
				
				if event.key == pygame.K_1:
					game_map = refine_outer_land(game_map)
					
				if event.key == pygame.K_2:
					game_map = refine_inner_land(game_map)

				if event.key == pygame.K_3:
					game_map = erase_isolated_land(game_map)

				display_map(screen, game_map)

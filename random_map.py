# Random map generation

import random as rn
import pdb

CORRES = ['.','#']

def generate_random_map(x, y):
	return [[rn.randint(0,1) for i in range(x)] for j in range(y)]

def refine_inner_land(game_map):
	game_map_tmp = game_map
	for x in range(len(game_map)):
		for y in range(len(game_map[x])):
			if(game_map_tmp[x][y] == 0):
				if(sum(get_four_neighboors(game_map_tmp, x, y)) > 2):
					game_map[x][y] = 1
	
	return game_map_tmp


def refine_outer_land(game_map):
	game_map_tmp = game_map
	for x in range(len(game_map)):
		for y in range(len(game_map[x])):
			if(game_map_tmp[x][y] == 1):
				if(sum(get_eight_neighboors(game_map_tmp, x, y)) < 3):
					game_map[x][y] = 0
	
	return game_map_tmp


def refine_map(game_map):
	for i in range(3):
		game_map = refine_outer_land(game_map)
		display_map(game_map)

	for i in range(3):
		game_map = refine_inner_land(game_map)
		display_map(game_map)
		
	return game_map

def get_eight_neighboors(grid, x, y):	
	xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
	yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))

	for a in xi:
		for b in yi:
			if a == b == 0:
				continue
			yield grid[x + a][y + b]

def get_four_neighboors(grid, x, y):	
	xi = (-1, 1) if 0 < x < len(grid) - 1 else ([-1] if x > 0 else [1])
	yi = (-1, 1) if 0 < y < len(grid[0]) - 1 else ([-1] if y > 0 else [1])

	for a in xi:
		for b in yi:
			yield grid[x + a][y + b]


def display_map(game_map):
	print('\n\n')
	for x in range(len(game_map)):
		print('')
		for y in range(len(game_map[x])):
			print(CORRES[game_map[x][y]], end='')
	print('\n\n')

if __name__ == '__main__':
	game_map = generate_random_map(70,10)
	display_map(game_map)
	game_map = refine_map(game_map)
	pdb.set_trace()

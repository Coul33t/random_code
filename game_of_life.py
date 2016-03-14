import random as rn
import pygame
import pdb

X_SIZE = 80
Y_SIZE = 100
X_DISPLAY = 40
Y_DISPLAY = 50
TILE_SIZE = 8

COLOR = [(50,50,50),(225,225,255)]

def initialize_array():
	return [[rn.randint(0,1) for x in range(Y_SIZE)] for y in range(X_SIZE)]



def display_array(array):
	offset = (int)(X_DISPLAY/2)
	for x in range(offset,X_SIZE-offset):
		for y in range(offset,Y_SIZE-offset):
			pygame.draw.rect(screen, (COLOR[array[x][y]]),((x-offset)*TILE_SIZE,(y-offset)*TILE_SIZE,TILE_SIZE, TILE_SIZE), 0)
	
	pygame.display.flip()



def get_eight_neighboors(grid, x, y):	
	xi = (0, -1, 1) if 0 < x < len(grid) - 1 else ((0, -1) if x > 0 else (0, 1))
	yi = (0, -1, 1) if 0 < y < len(grid[0]) - 1 else ((0, -1) if y > 0 else (0, 1))

	for a in xi:
		for b in yi:
			if a == b == 0:
				continue
			yield grid[x + a][y + b]


def update_array(array):
	tmp_array = array
	for x in range(X_SIZE):
		for y in range(Y_SIZE):
			
			neighboors_sum = sum(get_eight_neighboors(array,x,y))
			
			if array[x][y] == 0 and neighboors_sum == 3:
				tmp_array[x][y] = 1
			elif array[x][y] == 1 and not 2 <= neighboors_sum <= 3:
				tmp_array[x][y] = 0

	return tmp_array

if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode([TILE_SIZE*X_DISPLAY, TILE_SIZE*Y_DISPLAY])
	array = initialize_array()

	while True:
		pygame.time.wait(50)
		array = update_array(array)
		display_array(array)
		
pygame.quit()
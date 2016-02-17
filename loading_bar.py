# Console loading bar

import os
import time


def list_init(size_of_list):
	
	str = []

	for i in range (0,size_of_list+2):
		if(i == 0):
			str.append('[')
		elif(i == size_of_list+1):
			str.append(']')
		else:
			str.append(' ')

	return str


size_of_list = 50

while(True):
	str = list_init(size_of_list)
	for i in range (0,size_of_list):
		str[i+1] = '#'
		os.system('cls')
		print(''.join(str))
		time.sleep(0.15)


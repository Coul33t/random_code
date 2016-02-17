# adaboost implementation (not finished yet)

import random as rnd
import pdb

EXAMPLE_NUMBER = 10

def Adaboost(xi, yi, iterations):
	for i in range(iterations):
		threshold = 0
		subset = []

		# Subset construction
		for subs_iter in range(EXAMPLE_NUMBER):
			sample = rnd.ranint(0,EXAMPLE_NUMBER-1)
			subset.append([xi[sample], yi[sample]])

		# Threshold finding
		for ths_iter in range(EXAMPLE_NUMBER):
			tmp_threshold = ths_iter + 0.5

			# Iterating all samples
			for sample_iter in range(EXAMPLE_NUMBER):
				if()




if __name__ == '__main__':
	
	iterations = 50
	
	xi = [x for x in range(EXAMPLE_NUMBER)]
	yi = [rnd.randint(0,1) for x in range(EXAMPLE_NUMBER)]
	pi = [1/EXAMPLE_NUMBER for x in range(EXAMPLE_NUMBER)]


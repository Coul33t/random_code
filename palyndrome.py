# Palyndrome checker

def check(input):
	idx = 0
	for letter in input:
		#print(letter + ' vs ' + input[len(input) - 1 - idx])
		if(letter != input[len(input) - 1 - idx]):
			return False
		idx += 1

	return True

def faster_check(input):
	return input == input[::-1]

if __name__=='__main__':
	str_to_check = ['bonjour', 'kayak', 'juhhuj', 'chat']
	for word in str_to_check:
		print('Is ' + word + ' a palyndrom ? ' + str(faster_check(word)))
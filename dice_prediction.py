# ' Game ' about guessing how many throws are needed to reach 100 (6 faced dice)

import random as rn
import time

print('How much throw to reach 100 ?')

while True:
	guess = input()
	try:
		guess = int(guess)
	except ValueError as error:
		print('Value error : %s' % (error))

	if(guess > 16):
		break
	else:
		print('You\'re not very bright, aren\'t you ? (16 x 6 = 96)')

score = 0
throw = 0

while(score < 100):
	throw += 1
	throw_value = rn.randint(1,6)
	score += throw_value
	print('throw n°%i : %i |  %i' % (throw, throw_value, score))
	time.sleep(0.1)

print('Number of throw : %i vs %i (your guess)' % (throw, guess))
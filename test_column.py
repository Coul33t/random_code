# Column-wise value modification (not working)

import random as rn
import pdb

class Test_Class:
	def __init__(self):
		_value = rn.randint(0,100)

	def _get_value(self):
		return _value

	def _set_value(self, value):
		self._value = value

	value = property(_get_value, _set_value)


def column_change(l, n=1, m=100):
	l[n]._set_value(m)


	return l

test_array = [[1,2,3],[4,5,6],[7,8,9]]
test_array_class = [[Test_Class for i in range(3)] for j in range(3)]

pdb.set_trace()
print(list(map(column_change,test_array_class)))
import pytest
from utils import *

'''Unit tests for funcs in utils.py'''



def testGcd():
	assert gcd(16,10) == 2
	assert gcd(42,56) == 14
	assert gcd(0,9) == 9

def testDiv():
	assert div(8,9) == 0
	assert div(4, 2) == 2
	assert div(578, 24) == 24

def testextendedGcd():
	assert extended_gcd(35, 12) == (1, -1, 3)
	assert extended_gcd(16, 10) == (2, 2, -3)
	assert extended_gcd(437, 3) == (1,-1, 146)



testGcd()
testDiv()
testextendedGcd()
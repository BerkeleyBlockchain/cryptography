"""secret-sharing.py"""

import sys
sys.path.append('../utils')

from primes import *
from mod import *

class SecretShare:

	def __init__(self,secret,minimum,num_shares):
		self.secret = secret
		self.minimum = minimum
		self.num_shares = num_shares
		generate_random_shares(secret, minimum, num_shares)

    def poly_eval(poly, x):
        '''Evaluate a polynomial (represented as a list) at x
        >>> poly_eval([1, 2, 3], 4)
        57
        >>> poly_eval([50, 60, 70], 2)
        450
        '''
        total, i = 0, 0
        for coef in poly:
            total += coef * pow(x, i)
            i += 1
        return total

    def poly_add(a, b):
        '''

        '''
        result = max((a,b), key=len)
        for i in range(min(len(a), len(b))):
            result[i] = (a[i] + b[i])
        return result

    print(poly_add([1, 2], [3, 4]))
    print(poly_add([1, 2, 3, 4], [5, 6]))

    def poly_scalar_mul(p, c):
        for i in range(len(p)):
            p[i] = p[i] * c

    def poly_mul(a, b):
        i, z = 0, []
        for x in b:
            n = []
            for i in range(i):
                n.append(0)
            for j in range(len(a)):
                n.append(x * a[j])
            z.append(n)
            i += 1
        v = []
        for x in z:
            v = poly_add(v, x)
        return v

    print(poly_mul([1, 2], [2, 3]))

    print(poly_mul([1, 2, 3, 4], [8, 9]))

        #[1,2]      [2, 3]
        #1 + 2x     2 + 3x

        #2 + 7x + 6x^2

    def lagrange_interpolation(pairs):
        '''Find the polynomial P, with degree i -1 given a set of i number of points in pairs'''
        list_of_x = []
        list_of_y = []
        for x in len(pairs):
            list_of_x = list_of_x + x[0]
        for y in len(pairs):
            list_of_y = list_of_y + y[1]

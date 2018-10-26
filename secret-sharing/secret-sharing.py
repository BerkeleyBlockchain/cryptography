"""secret-sharing.py"""

import sys
sys.path.append('../utils')

from primes import *
from mod import *
from random import randint

class SecretSharingScheme:
    """
    SecretSharingScheme class

    Attributes:
        secret (int): The secret number/code that you want to safely distribute.
        minimum (int): The minimum number of individuals/shares that need to come
                       together in order to access the secret.
        num_shares (int): The number of shares distributed.
        polynomial (list): The secret polynomial P(x) that has randomly chosen
                           coefficients and P(0) = secret.
        shares (list): A list of tuples that contains the shares (1, P(1)), (2, P(2)), ..., (n, P(n))
                       where n = num_shares.
    """
    def __init__(self, secret, minimum, num_shares):
        self.secret = secret
        self.minimum = minimum
        self.num_shares = num_shares
        self.polynomial = [secret] + [randint(1, 100) for i in range(minimum)]
        self.shares = self.generate_shares()

   def generate_shares(self):
        """
        Returns a list of shares (points) that correspond to the secret polynomial
        such that at least `minimum` people can come together and reconstruct the
        polynomial P(x) and evaluate the secret P(0) = s.
        """
        return [(i, poly_eval(self.polynomial, i)) for i in range(1, self.num_shares + 1)]

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
    '''Add two polynomials, represented as lists.
    >>> print(poly_add([1, 2], [3, 4]))
    [4, 6]
    >>> print(poly_add([1, 2, 3, 4], [5, 6]))
    [6, 8, 3, 4]
    '''
    result = max((a,b), key=len)
    for i in range(min(len(a), len(b))):
        result[i] = (a[i] + b[i])
    return result

def poly_scalar_mul(p, c):
    '''Multiply a polynomial, represented as a list, by a scalar.
    >>> print(poly_scalar_mul([1, 2], 5))
    [5, 10]
    '''
    x = []
    for i in range(len(p)):
        x.append(p[i] * c)
    return x

def poly_mul(a, b):
    '''Multiply two polynomials, represented as lists
    >>> print(poly_mul([1, 2], [2, 3]))
    [2, 7, 6]
    >>> print(poly_mul([1, 2, 3, 4], [8, 9]))
    [8, 25, 42, 59, 36]
    '''
    i, z = 0, []
    for x in b:
        n = []
        for i in range(i):
            n.append(0)
        n.extend(poly_scalar_mul(a, x))
        z.append(n)
        i += 1
    v = []
    for x in z:
        v = poly_add(v, x)
    return v

def lagrange_interpolation(pairs):
    '''Find the polynomial P, with degree i - 1 given a set of i number of points in pairs'''

    poly_list = []
    for i in range(1, len(pairs)):
        new_list = generate_polynomial(i, pairs)
        poly_list = poly_add(poly_list,new_list)
    return poly_list

if __name__ == '__main__':
    secret = input('Enter a secret code (as an integer): ')
    num_shares = input('Enter the number of shares you want to give out: ')
    minimum = input('Enter the minimum number of people needed to access the secret: ')

    s = SecretSharingScheme(secret, minimum, num_shares)

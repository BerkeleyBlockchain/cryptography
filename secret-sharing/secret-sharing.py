"""secret-sharing.py"""

import numpy as np

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
        self.polynomial = [randint(1, 100) for i in range(minimum - 1)] + [secret]
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

def generate_polynomial(i, pairs):
    denominator = 1
    xS = [a[0] for a in pairs]
    yS = [a[1] for a in pairs]
    xI = xS[i-1]
    factors = []
    for x in xS[0:i-1]+xS[i:]:
        denominator *= (xI - x)
        factors.append([1,-x])

    numerator = poly_mul(factors)
    answer = numerator / denominator
    return answer

def lagrange_interpolation(pairs):
    '''Find the polynomial P, with degree i - 1 given a set of i number of points in pairs'''

    poly = []
    yS = [a[1] for a in pairs]
    for i in range(1, len(pairs)+1):
        new = generate_polynomial(i, pairs)
        print(new)
        poly = np.polyadd(poly, yS[i-1]*new)

    return poly

def recover_secret(shares):
    poly = lagrange_interpolation(shares)
    return poly[len(poly)-1]
    """figure out if polynomial is forward or backward ie is the first coefficient the coefficient of the 0th degree or of the nth degree"""

def poly_mul(factors):
    '''Multiply two polynomials, represented as lists
    >>> print(poly_mul([1, 2], [2, 3]))
    [2, 7, 6]
    >>> print(poly_mul([1, 2, 3, 4], [8, 9]))
    [8, 25, 42, 59, 36]
    '''
    v = None
    for a in factors:
        if v is None:
            v = a
        else:
            v = np.polymul(v, a)

    return v


if __name__ == '__main__':
    secret = int(input('Enter a secret code (as an integer): '))
    num_shares = int(input('Enter the number of shares you want to give out: '))
    minimum = int(input('Enter the minimum number of people needed to access the secret: '))

    s = SecretSharingScheme(secret, minimum, num_shares)
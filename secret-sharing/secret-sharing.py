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
        self.polynomial = [secret] + [randint(1, 100) for i in range(minimum - 1)]
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
        factors.append([1, -x])

    numerator = poly_mul(factors)
    answer = numerator / denominator
    return answer

def lagrange_interpolation(points):
    """
    Find the polynomial P, with degree d given a list of d + 1 points.
    The argument `points` needs to contain at least 2 points.

    >>> points = [(1, 1), (2, 2), (3, 4)]
    >>> lagrange_interpolation(points)
    array([ 1. , -0.5,  0.5])
    """
    assert isinstance(points, list) and len(points) > 1, 'Error: argument needs to contain at least two points'

    poly = []
    y = [point[1] for point in points]
    for i in range(1, len(points) + 1):
        new = generate_polynomial(i, points)
        poly = np.polyadd(poly, y[i - 1] * new)
    return poly[::-1]

def recover_secret(shares):
    poly = lagrange_interpolation(shares)
    return int(poly[0])

def poly_mul(factors):
    """

    """

    v = None
    for a in factors:
        if v is None:
            v = a
        else:
            v = np.polymul(v, a)
    return v

if __name__ == '__main__':
    secret = 314159
    num_shares = random.randint(5, 10)
    minimum = num_shares - 2

    s = SecretSharingScheme(secret, minimum, num_shares)
    print("Hello! " + str(num_shares) + " shares have been handed out.")

    m = int(input('How many of you are here? '))

    while m < minimum:
        print("Lagrange interpolation failed. More people are needed to unlock secret.")
        m = int(input('How many of you are here? '))

    print("Performing Lagrange interpolation with your inputs...")
    test = s.shares[:m]
    print("Inputs: " + str(test))
    print("SECRET: " + str(recover_secret(test)))
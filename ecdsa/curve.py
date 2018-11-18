"""curve.py"""

import sys
sys.path.append('../utils')

from mod import *
from random import randint

class Curve:
    """
    Class definition for an elliptic curve
    Attributes:
        a, b: coefficients in equation: y^2 = x^3 + ax + b
        G: generator point as a tuple
    """
    def __init__(self, a, b, G):
        self.a = a
        self.b = b
        self.G = G
        self.history = [self.G]

    def get_point(self, x):
        y = pow(pow(x, 3) + self.a * x + self.b, 0.5)
        return (x, y)

    def point_double(self):
        point = self.history[len(self.history) - 1]
        m = (3 * pow(point[0], 2) + self.a) / (2 * point[1])
        x = pow(m, 2) - point[0] - point[0]
        y = -(point[1] + m * (x - point[0]))
        point = (x, y)
        self.history.append(point)
        return point

    def point_add(self):
        point1 = self.history[0]
        point2 = self.history[0]
        m = 0

        if len(self.history) == 1:
            m = (3 * pow(point1[0], 2) + self.a) / (2 * point1[1])
        else:
            point2 = self.history[len(self.history) - 1]
            m = (point1[1] - point2[1]) / (point1[0] - point2[0])

        x = pow(m, 2) - point1[0] - point2[0]
        y = -(point1[1] + m * (x - point1[0]))

        point = (x, y)
        self.history.append(point)

    def point_double_mod(self, p):
        self.point_double()
        return self.point_mod(p)

    def point_add_mod(self, p):
        self.point_add()
        return self.point_mod(p)

    def scalar_mul(self, k):
        while k > 1:
            point = self.point_add()
            k += -1
        return point

    def point_exp(self, k):
        if k == 1:
            return self.history[len(self.history) - 1]
        if k % 2 == 1:
            self.point_double()
            self.point_exp((k - 1) / 2)
            return self.point_add()
        else:
            self.point_double()
            return self.point_exp(k/2)

    def point_mod(self, p):
        point = self.history[len(self.history) - 1]
        mod_point = (point[0] % p, point[1] % p)
        self.history[len(self.history) - 1] = mod_point
        return mod_point

class FiniteCurve(Curve):
    """
    Class definition for a finite elliptic curve, which performs operations
    such as point addition and scalar multiplication with respect to a modulus P.
    """
    def __init__(self, a, b, G, P, N):
        Curve.__init__(self, a, b, G)
        self.P = P
        self.N = N

    @property
    def current_point(self):
        assert len(self.history) > 0, 'Error: no generator point'
        return self.history[len(self.history) - 1]

    @current_point.setter
    def current_point(self, point):
        self.history.append(point)

    def point_add(self):
        """
        Performs elliptic curve addition using the given generator point.

        >>> c = FiniteCurve(0, 7, (13, 19), 97, 79)
        >>> c.point_add()
        (27, 75)
        >>> c.point_add()
        (73, 32)
        """
        if len(self.history) == 1:
            return self.point_double()
        p1, p2 = self.current_point, self.G
        m = ((p2[1] - p1[1]) * mod_inverse(self.P, p2[0] - p1[0])) % self.P
        x = (pow(m, 2) - p1[0] - p2[0]) % self.P
        y = (m * (p1[0] - x) - p1[1]) % self.P
        added_point = (x, y)
        self.current_point = added_point
        return added_point

    def point_double(self):
        """
        Doubles a point on an elliptic curve, which is equivalent to finding
        the inverse of the point intersected by the line tangent to the current
        point.

        >>>
        """
        point = self.current_point
        m = ((3 * pow(point[0], 2) + self.a) * mod_inverse(self.P, 2 * point[1])) % self.P
        x = (pow(m, 2) - 2 * point[0]) % self.P
        y = (m * (point[0] - x) - point[1]) % self.P
        doubled_point = (x, y)
        self.current_point = doubled_point
        return doubled_point

    def scalar_mul(self, k):
        """
        Performs point addition k times, using double-and-add to speed up computation.
        """
        k_bin = str(bin(k))[2:]
        n_bits = len(k_bin)
        print(n_bits)
        for i in range(1, n_bits):
            print('Double')
            self.point_double()
            if k_bin[i] == "1":
                print('Add')
                self.point_add()
        return self.current_point



























"""
# Specs for secp256-k1
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
_Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
_r = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

curve_secp256k1 = Curve(_p, _a, _b)
generator_secp256k1 = ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)

SECP256k1 = finiteCurve("SECP256k1", curve_secp256k1,
                  ecdsa.generator_secp256k1,
                  (1, 3, 132, 0, 10), "secp256k1")

class finiteCurve:
    ''' A class storing the SECP256k1 curve. Attributes
    include name, the curve given from..., the generator
    that returns the initial point, oid??
    '''
    def __init___(name, curve, generator, oid):
        self.name = name
        self.curve = curve
        self.generator = generator
        self.oid = oid

"""


c = Curve(-7, 10)

print(c.point_add_mod(19))

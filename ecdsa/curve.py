

from random import randint

class Curve:

    """
    Attributes:
        a, b: coefficients in equation: y^2 = x^3 + ax + b

    """

    def __init__(self, a , b):
        self.a = a
        self.b = b
        self.history = [self.get_point(randint(1, 100))]


    def get_point(self, x):
        y = pow(pow(x, 3) + a*x + b, 0.5)
        return (x, y)

    def add_point():

        if len(history) == 1:
            ...

        else:
            point1, point2 = self.history[0], self.history[len(self.history - 1)]
            slope = (point1[0] - point2[0]) / (point1[1] - point2[1])

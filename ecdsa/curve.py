

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
        y = pow(pow(x, 3) + self.a * x + self.b, 0.5)
        return (x, y)

    def add_point(self):
        point1 = self.history[0]
        point2 = self.history[0]
        m = 0

        if len(self.history) == 1:
            m = (3 * pow(point1[0], 2) + self.a) / (2 * point1[1])
        else:
            point2 = self.history[len(self.history - 1)]
            m = (point1[1] - point2[1]) / (point1[0] - point2[0])

        x = pow(m, 2) - point1[0] - point2[0]
        y = -(point1[1] + m * (x - point1[0]))

        point = (x, y)
        self.history.append(point)
        return point

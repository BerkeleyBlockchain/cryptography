

class Curve:

    """
    Attributes:
        a, b: coefficients in equation: y^2 = x^3 + ax + b

    """

    def __init__(self, a , b):
        self.a = a
        self.b = b

    def get_point(self, x):

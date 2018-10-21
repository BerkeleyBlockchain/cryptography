"""mod.py"""

def gcd(x, y):
    """
    Computes the greatest common divisor of x and y.

    >>> gcd(16, 10)
    2
    >>> gcd(3, 3)
    3
    >>> gcd(35, 12)
    1
    """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def div(x, y):
    """
    Returns the number of times a number y divides x.

    >>> div(5, 4)
    1
    >>> div(28, 5)
    5
    """
    return (x - x % y) // y

def extended_gcd(x, y):
    """Computes d, the greatest common divisor as well as integers
    a and b such that gcd(x, y) = ax + by. Returns (d,a,b).

    >>> extended_gcd(35, 12)
    (1, -1, 3)
    >>> extended_gcd(16, 10)
    (2, 2, -3)
    """
    if y == 0:
        return x, 1, 0
    else:
        d, a, b = extended_gcd(y, x % y)
        return d, b, a - div(x, y) * b

def is_coprime(a, b):
    """
    Returns whether or not two integers are coprime
    (which means that a and b only share 1 as a common divisor).

    >>> is_coprime(2, 3)
    True
    >>> is_coprime(16, 10)
    False
    """
    return gcd(a, b) == 1

def find_inverse(m, x):
    """
    Find the inverse of x mod m, if m and x are coprime.

    >>> find_inverse(35, 12)
    3
    >>> print(find_inverse(16, 10))
    None
    """
    if not is_coprime(m, x):
        return None
    d, _, inv = extended_gcd(m, x)
    while inv < 0:
        inv += m
    return inv

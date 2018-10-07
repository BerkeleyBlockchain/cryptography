
def gcd(x, y):
    '''Computes the greatest common divisor of x and y.

    >>> gcd(16, 10)
    2
    >>> gcd(3, 3)
    3
    >>> gcd(35, 12)
    1
    '''
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def div(x, y):
    '''Returns the number of times a number y divides x.
    '''
    return (x - x % y) // y

def extended_gcd(x, y):
    '''Computes the greatest common divisor, as well as integers
    a and b such that gcd(x, y) = ax + by.

    >>> extended_gcd(35, 12)
    (1, -1, 3)
    >>> extended_gcd(16, 10)
    (2, 2, -3)
    '''
    if y == 0:
        return x, 1, 0
    else:
        d, a, b = extended_gcd(y, x % y)
        return d, b, a - div(x, y) * b


import random

def div_mod(num, denom, p):
    '''Compute num / denom in modulo p

    >>> div_mod(3, 5, 2)
    1

    '''

    inv = find_inverse(p, denom)
    return num * inv


def generate_random_shares(secret, minimum, num_shares):

    assert minimum < shares, "Minimum shares must be less than total shares)"
    poly = [secret] + [generate_prime() for i in range(minimum)]

    shares = [(i, poly_eval(poly, i)) for i in range(1, num_shares + 1)]

    return shares


def poly_eval(poly, x):
    '''Evaluate a polynomial (represented as a list) at x

    >>> poly_eval([1, 2, 3], 4)
    57

    >>> poly_eval([50, 60, 70], 2)
    450

    '''

    sum, i = 0, 0
    for coef in poly:
        sum += coef * pow(x, i)
        i += 1
    return sum

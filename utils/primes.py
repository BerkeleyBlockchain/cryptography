"""primes.py"""

from random import getrandbits
import random
from mod import is_coprime

def is_prime(n, k=50):
    """
    Returns whether a number is prime or not using the Miller-Rabin
    primality check.

    >>> is_prime(100005091)
    True
    >>> is_prime(3)
    True
    """
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits=512):
    """
    Returns a random prime number with a specified number of bits.

    >>> is_prime(generate_prime(2))
    True
    """
    prime = int(getrandbits(bits))
    while not is_prime(prime):
        prime = int(getrandbits(bits))
    return prime

def generate_coprime(x, max_num=None):
    """
    Returns a number that is relatively prime to x.
    """
    check_num = generate_prime()
    while not is_coprime(x, check_num):
        if max_num and check_num > max_num:
            return None
        else:
            check_num = generate_prime()
    return check_num

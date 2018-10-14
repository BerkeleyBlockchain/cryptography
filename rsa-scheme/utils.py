'''utils.py'''

from math import sqrt
from random import getrandbits

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

def is_coprime(a, b):
    '''Returns whether or not two integers are coprime
    (which means that a and b only share 1 as a common divisor).

    >>> is_coprime(2, 3)
    True
    >>> is_coprime(16, 10)
    False
    '''
    return gcd(a, b) == 1

def find_inverse(m, x):
    '''Find the inverse of x mod m, if m and x are coprime.

    >>> find_inverse(35, 12)
    3
    >>> print(find_inverse(16, 10))
    None
    '''
    if not is_coprime(m, x):
        return None
    d, _, inv = extended_gcd(m, x)
    while inv < 0:
        inv += m
    return inv

def is_prime_naive(x):
    '''Returns whether or not a number x is prime. O(sqrt(n)).

    >>> is_prime_naive(2)
    True
    >>> is_prime_naive(89)
    True
    >>> is_prime_naive(100)
    False
    '''
    if x <= 1:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def generate_prime(bits=512):
    '''Returns a random prime number with a specified number of bits.

    >>> is_prime_naive(generate_prime(2))
    True
    '''
    prime = int(getrandbits(bits))
    while not is_prime_naive(prime): # change this to is_prime
        prime = int(getrandbits(bits))
    return prime

def generate_coprime(x, max_num=None):
    '''Returns the smallest number that is relatively prime to x.

    >>> generate_coprime(40)
    3
    >>> generate_coprime(21312)
    5
    '''

    check_num = 3
    while not is_coprime(x, check_num):
        if max_num and check_num > max_num:
            return None
        elif not is_prime_naive(check_num):
            check_num += 1
            continue
        else:
            check_num += 1
    return check_num

def miller_rabin(n, k):


    if n == 2:
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


        # if n & 1 == 0:
        #     return False
        #
        # """Write n - 1 as 2^r·d with d odd by factoring powers of 2"""
        # d = n - 1
        # r = 0
        # while d % 2 == 0:
        #     d = d / 2
        #     r += 1
        # for i in range(k):
        #     a = np.random.random_integers(2, n - 2)
        #     x = (a**d) % n
        #
        #
        #     if x == 1 or x == n - 1:
        #         continue
        #     for j in range(1, r - 1):
        #         x = (x**2) % n
        #         if x == 1:
        #             return False #composite for sure
        #         elif x == n - 1:
        #             a = 0 #tracks that loop didn't continue to end
        #             break
        #     if a:
                # return False

            # """implementation #2"""
            # if x != 1:
            #     i = 0
            #     while x != (n-1):
            #         if i == r - 1:
            #             return False
            #         else:
            #             i += 1
            #             x = (x**2) % n

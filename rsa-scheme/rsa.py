'''rsa.py'''

from utils import *
from random import getrandbits

class RSA:
    '''Class definition for an RSA scheme.

    Attributes:

    '''

    def __init__(self):
        self.p, self.q = self.generate_keys()
        self.N = self.p * self.q

        self.public_key = (self.N, self.e)
        # Totient function (p - 1) * (q - 1) is the # of primes below N = p * q
        self.totient = (self.p - 1) * (self.q - 1)

        self.e = 3 # Arbitrary small prime that is coprime with self.totient

        self.d = find_inverse(self.totient, self.e)


    def encrypt(self, message):
        '''Returns the encryption of a given message:
            E(x) = x^e mod N
        '''
        assert type(message) == int, 'Must provide an integer message'
        return (message ** self.e) % self.N

    def decrypt(self, encrypted):
        '''Returns the decryption of a given encryption with the same
        public/private key pair.
            D(y) = y^d mod N
        '''
        assert type(encrypted) == int, 'Must provide an integer encrypted message'
        return (encrypted ** self.d) % self.N

    def generate_keys(self):
        num_bits = 10
        p = generate_prime(num_bits)
        q = generate_prime(num_bits)
        while p == q:
            q = generate_prime(num_bits)
        return p, q

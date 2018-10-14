'''rsa.py'''

from utils import *
from random import getrandbits

class RSA:
    '''RSA scheme.
    '''

    def __init__(self, user):
        self.user = user
        self.p, self.q = self.generate_keys()
        self.N = self.p * self.q

        # Totient function (p - 1) * (q - 1) is the # of primes below N = p * q
        self.totient = (self.p - 1) * (self.q - 1)

        # Arbitrary small prime that is coprime with self.totient
        self.e = generate_coprime(self.totient, max_num=self.totient)
        self.public_key = (self.N, self.e)

        self.d = find_inverse(self.totient, self.e)

    def encrypt(self, message):
        '''Returns the encryption of a given message:
            E(x) = x^e mod N
        '''
        assert type(message) == int, 'Must provide an integer message'
        return pow(message, self.e, self.N)

    def decrypt(self, encrypted):
        '''Returns the decryption of a given encryption with the same
        public/private key pair.
            D(y) = y^d mod N
        '''
        assert type(encrypted) == int, 'Must provide an integer encrypted message'
        return pow(encrypted, self.d, self.N)

    def generate_keys(self):
        num_bits = 50
        p = generate_prime(num_bits)
        q = generate_prime(num_bits)
        while p == q:
            q = generate_prime(num_bits)
        return p, q

    def __str__(self):
        return "{0}'s RSA: \nPublic key pair (N, e) = {1}".format(self.user, self.public_key)

if __name__ == '__main__':
    name = input('What is your name? ')
    print('Generating your RSA keys...\n')
    your_rsa = RSA(name)
    print(your_rsa)
    another_rsa = RSA('John DeNero')

    while True:
        msg = input('What is your message (as an integer)? ')
        try:
            msg = int(msg)
            break
        except:
            print('Please enter an integer.')
            continue
    encrypted = your_rsa.encrypt(msg)
    print('Your encrypted message is:', encrypted)

    # Other people can't decrypt your message!
    wrong_decrypt = another_rsa.decrypt(encrypted)

    print(another_rsa)
    print(another_rsa.user + ' cannot decrypt your message! He does not have the correct private key pair.')
    print(wrong_decrypt)

    print('Only you are able to decrypt the message.')
    print('Your decrypted (original) message is:', your_rsa.decrypt(encrypted))


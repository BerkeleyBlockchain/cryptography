# RSA Scheme Implementation

## Planning

Good intro readings/videos:
- [Original RSA paper](http://people.csail.mit.edu/rivest/Rsapaper.pdf)
- https://www.youtube.com/watch?v=wXB-V_Keiu8
- [Medium article](https://hackernoon.com/how-does-rsa-work-f44918df914b)
- [UW notes](https://sites.math.washington.edu/~morrow/336_09/papers/Yevgeny.pdf)

Functionality that we need ([Example for reference](https://gist.github.com/JonCooperWorks/5314103)):
- `gcd(x, y)`: Implement a function to find the GCD for use in determining if two numbers x, y are coprime `gcd(x, y) == 1`
- `generate_large_prime`
    - `generate_seed`: Be able to generate a random seed from 0 to some large number. This seed will determine the primes generated. We can also implement a way for the user to regenerate a seed.
- `is_prime(x)`: (Efficiently) checks whether or not a given number is prime.
    - Implement Miller-Rabin algorithm for efficiency. Read into why it's more efficient.
    - Create a list of "small primes" to check through before running Miller-Rabin to save time in a lot of cases.
    - Reading: [Implementation Example](https://langui.sh/2009/03/07/generating-very-large-primes/), [another article](https://medium.com/@prudywsh/how-to-generate-big-prime-numbers-miller-rabin-49e6e6af32fb)
- `encrypt(keypair, unencrypted)`: Encrypt a message with a public/private key pair.
- `decrypt(keypair, encrypted)`: Decrypt an encrypted message with a corresponding key pair.

Read into Dev's suggestions:
- OAEP padding to prevent attacks based on homomorphic properties
    - [Article on OAEP and example impelementation](https://medium.com/blue-space/improving-the-security-of-rsa-with-oaep-e854a5084918)
- Chinese Remainder Theorem
    - https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    - https://www.di-mgt.com.au/crt_rsa.html
    - https://crypto.stackexchange.com/questions/2575/chinese-remainder-theorem-and-rsa
- Protections for different random specialized factoring (attacks trying to find p and q through factoring N = pq)
- Constant time Montgomery form exponentiation
    - https://en.wikipedia.org/wiki/Montgomery_modular_multiplication

## High Level Summary

Goal: You want to receive ecrypted messages that only you can read.

To do this, you publish a public "lock" that anyone can use to encrypt their message.
Only you have the private "key" needed to decrypt this "locked" message to access the sender's original message.
The encrypted message is meaningless to anyone else trying to read it.

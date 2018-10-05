# RSA Scheme Implementation

## Planning

Functionality that we need:
- `gcd`: Implement a function to find the GCD for use in determining if two numbers x, y are coprime `gcd(x, y) == 1`
- `generate_large_prime`:
    - `generate_seed`: Be able to generate a random seed from 0 to some large number. This seed will determine the primes generated. We can also implement a way for the user to regenerate a seed.
- `is_prime`:
    - Implement Miller-Rabin algorithm for efficiency. Read into why it's more efficient.
- `encrypt(keypair, unencrypted)`: Encrypt a message with a public/private key pair.
- `decrypt(keypair, encrypted)`: Decrypt an encrypted message with a corresponding key pair.
- Read into Dev's suggestions:
    - OAEP padding to prevent attacks based on homomorphic properties
    - Chinese Remainder Theorem
    - Protections for different random specialized factoring (attacks trying to find p and q through factoring N = pq)
    - Constant time Montgomery form exponentiation

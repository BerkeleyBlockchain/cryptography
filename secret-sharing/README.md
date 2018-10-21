# Secret Sharing Scheme Implementation

## Planning

Reading:
- [CS70 Note #8](http://www.eecs70.org/static/notes/n8.pdf)
- Chinese Remainder Theorem and exponentiation (http://web.eecs.umich.edu/~akamil/teaching/fa03/101003.pdf)
- Attacks with random different specialized factoring algorithms (http://www.tcs.hut.fi/Studies/T-79.5501/2008SPR/lectures/out08.pdf).
- Shamir's Secret Sharing Scheme (https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing)

Functionality:
- `lagrange_interpolation`: Find the corresponding y value of a given x, given a certain number of x, y points which represent a polynomial.=
    - `div_mod` Computes the result of dividing a number by another number in a given modulo.
    - `extended_GCD` Computes the inverse of a number in a modulo. To be used in `div_mod`.
- `generate_random_shares`: generate random shares that each represent a point on a polynomial.
    - `generate_polynomial`: generate a random polynomial f such that f(0) = secret.
- `recover_secret`: recover the secret using the given share points, employing `lagrange_interpolation`.

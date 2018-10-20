# Secret Sharing Scheme Implementation

## Planning

Reading:
- [CS70 Note #8](http://www.eecs70.org/static/notes/n8.pdf)
- Chinese Remainder Theorem and exponentiation (http://web.eecs.umich.edu/~akamil/teaching/fa03/101003.pdf)
- Attacks with random different specialized factoring algorithms (http://www.tcs.hut.fi/Studies/T-79.5501/2008SPR/lectures/out08.pdf).

Functionality:
- `lagrange_interpolation`: Find the corresponding y value of a given x, given a certain number of x, y points which represent a polynomial.
- `generate_random_shares`: generate random shares that each represent a point on a polynomial.
- `recover_secret`: recover the secret using the given share points, employing `lagrange_interpolation`.

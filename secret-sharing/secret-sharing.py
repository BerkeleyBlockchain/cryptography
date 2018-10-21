
def div_mod(num, denom, p):
    '''Compute num / denom in modulo p

    >>> div_mod(3, 5, 2)
    1

    '''

    inv = find_inverse(p, denom)
    return num * inv


def generate_random_shares(secret, minimum, shares):

    assert minimum < shares, "Minimum shares must be less than total shares)"
    poly = [secret] + [randomint() for i in range(minimum)]

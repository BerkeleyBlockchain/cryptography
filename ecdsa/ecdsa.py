"""ecdsa.py"""

from curve import Curve, FiniteCurve
from random import randrange
import hashlib
from hashlib import sha256
import base58check

# Params for secp256-k1 (Curve that Bitcoin uses)
# http://www.secg.org/sec2-v2.pdf
_a = 0x0000000000000000000000000000000000000000000000000000000000000000
_b = 0x0000000000000000000000000000000000000000000000000000000000000007
_p = 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f
_Gx = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
_Gy = 0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8
_n = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

curve_secp256k1 = FiniteCurve(_a, _b, (_Gx, _Gy), _p, _n)

# https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses

private_key = 0x3969E7AF7D041E2E8527972682E805DF63EFA7841828171C769CB3AD5FD23330
public_key = curve_secp256k1.scalar_mul(private_key)
public_key = hex(public_key[0]) # The x-coord is the compressed public key.
public_key = '02' + str(public_key)[2:]

print(public_key)

s1 = sha256(public_key.encode('utf-8')).hexdigest()
r = '00' + hashlib.new('ripemd160', s1.encode('utf-8')).hexdigest()
s2 = sha256(r.encode('utf-8')).hexdigest()
s3 = sha256(s2.encode('utf-8')).hexdigest()
checksum = s3[:8]
binary_address = r + checksum

print(s1)
print(r)
print(s2)
print(s3)
print(checksum)
print(binary_address)

"""
curve_secp256k1 = Curve(_p, _a, _b)
generator_secp256k1 = ellipticcurve.Point(curve_secp256k1, _Gx, _Gy, _r)

SECP256k1 = finiteCurve("SECP256k1", curve_secp256k1,
                  ecdsa.generator_secp256k1,
                  (1, 3, 132, 0, 10), "secp256k1")

"""




class ECDSA:
    """
    ECDSA (Elliptic Curve Digital Signature Algorithm)
    Implementation of an ECDSA key generation scheme.
    """

    def __init__(self,curve):
         this.curve = Curve
         this.d = d.randrange(1, curve.p)

    def verify(pubkey, privkey):
    	"""Some function to verify that this priv key
    	and this pubkey can be used to sign/verify transactions etc..
    	"""

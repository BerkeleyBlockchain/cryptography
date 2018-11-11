# ECDSA Implementation
Elliptic Curve Digital Signature Algorithm

## Planning

Reading:
- https://docs.google.com/presentation/d/1gfB6WZMvM9mmDKofFibIgsyYShdf0RV_Y8TLz3k1Ls0/edit#slide=id.g443ebc39b4_0_275
- https://blog.cloudflare.com/ecdsa-the-digital-signature-algorithm-of-a-better-internet/
- https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/
- https://www.youtube.com/watch?v=dCvB-mhkT0w&t=9s

![](https://blog.cloudflare.com/content/images/image02.gif)

Notes:
- Keys can be fewer bits, but same security as RSA
- Create an elliptic curve, equation `y^2 = x^3 + ax + b`
- Properties of the elliptic curve
    - Symmetry about the x axis
    - Any non-vertical line will intersect the curve at three points.



Functions:
- ECDSA Class
    - Point_add
    - Point_scalar_mul
 
- Curve class
    - Attributes:
        - a
        - b
    -in_it:
        - check 4a^3 + 27b^2 =! 0
    - Subclass Finite_curve:
        - Attribute mod
        - Max = mod
        
        
      

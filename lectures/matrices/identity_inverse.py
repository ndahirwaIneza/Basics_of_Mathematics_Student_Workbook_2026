

"""
Inverse of 2x2 matrix
A = [[a,b] , [c,d]]
is 
inv_A = 1/det(A)[[d, -b], [-c, a]]

if det(A) is 0 then we have no inverse

To verify that we got the right inverse:
A * inv_A = I which is identity matrix

I = [[1,0], [0,1]]


Inverse of 3x3 matrix
B = [[a11, a12, a13], [a21, a22, a23], [a31, a32, a33]]
 only when det(B) is different from 0

 inv_B = 1/det(B)* Adj(B) -> Adjoint = system of cofactors
Adj(B) = C^T
C^T = matrix(Cij) -> system of cofactors
cij = ((-1)^(i+j)) * Mij -> this means minors

Mij example
M11 = det([[b22, b32], [b23, b33]])

"""
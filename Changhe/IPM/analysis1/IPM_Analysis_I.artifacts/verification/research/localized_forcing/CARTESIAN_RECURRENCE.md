# Cartesian differentiation from independent polar jets

Written before the checker. Put t=log r, E=exp(-t), z=exp(i theta),
C=(z+z^-1)/2 and S=(z-z^-1)/(2i). For a sufficiently differentiable scalar
field f, denote J_ij=partial_t^i partial_theta^j f. The two Cartesian
operators are D_x=E(C partial_t-S partial_theta) and
D_y=E(S partial_t+C partial_theta).

For arbitrary polar derivatives of a Cartesian derivative, Leibniz gives
partial_t^i partial_theta^j(D_x f)=sum_{a<=i,b<=j} C(i,a)C(j,b)
[(-1)^a E cos(theta+b pi/2) J_(i-a+1,j-b)
 -(-1)^a E sin(theta+b pi/2) J_(i-a,j-b+1)],
and the analogous plus/swap formula for D_y. This proves the producer's
recursive identity for every smooth f by induction on Cartesian order.
Separate input jets, not differentiated remainder intervals, are needed.
For weak derivatives the same identities hold locally away from r=0 by
density and the smooth change of coordinates.

An independent full symbolic check works in the Laurent polynomial ring
Q[i][z,z^-1,E] acting linearly on formal jet symbols J_ij. If a term after
d Cartesian differentiations is E^d A(theta)J_ij, direct differentiation
gives
D_x term = E^(d+1){C[-d A J_ij+A J_(i+1,j)]
                         -S[A' J_ij+A J_(i,j+1)]},
D_y term = E^(d+1){S[-d A J_ij+A J_(i+1,j)]
                         +C[A' J_ij+A J_(i,j+1)]}.
For A=z^n, A'=i n z^n. Thus all coefficients are Gaussian rationals and
all comparisons can be exact. Compare these independently constructed
operators with the frozen producer recursion for every derivative of
total order<=4, on the formal jet family. Equality of coefficient maps
is an identity for all functions with the required jets, not a finite
point sample. Check the Laplacian separately:
Delta f=E^2(J20+J02), which also detects a missing radial first derivative
when t=log r. Check Delta^2 f=E^4[J40-4J30+4J20+2J22-4J12+4J02+J04]
by applying Delta to E^2(J20+J02). These are exact identities.
This check does not validate any floating Taylor coefficient, remainder,
canonical input or norm constant.

# The single-tail family is the first compensated row

Written before the new checking code. This is a corollary of topics105,
106 and114, with their mandatory addenda and finalized verdicts. It does
not alter any frozen result. It concerns one explicit family and cannot
exclude a surrounding uncertainty neighborhood.

Let rho0, k, c0=1/k, R_b, L, the original source P and the canonical
full-plane velocity be exactly as in those topics. Set a1=2k-1. Topic105
uses the correction H=k Epsilon/(1-k), where the exact leading exterior
residual is

 Epsilon=(a1/k-1)D1+B_(k,k)(D0,D0).

Since a1-k=k-1, multiplication by k/(1-k) gives exactly

 H=-D1+k B_(k,k)(D0,D0)/(1-k)=A1-D1=H1.                  (1)

This is an identity of finite angular functions, not equality inferred
from overlapping coefficient intervals. Both constructions use the same
b(s)=(s-1)^8(2-s)^8 on(1,2), the same normalized integral cutoff chi, and
the same J_b=integral_1^2 s b(s)ds. Their angular scalar is precisely the
sin(3theta) coefficient h_(1,1), and their radial moment is
J_(a1,1)=integral_1^infinity chi(s)s^(a1-2)ds. Hence the complete105 density
correction, including its exact strain compensator, is

 chi(r/T)r^a1 H1(theta)
 -(4 h_(1,1)J_(a1,1)/J_b) T^(a1-3) x^2 y b(r/T).          (2)

It is exactly row1 of106 and114 for every T>=max(R_b,L,1).
Each row separately has zero canonical center strain. Thus all the
individual row1 interior-velocity estimates of114 apply to105 without
adding the second and d rows. This also follows directly from the finite
Green formula in114, whose proof was rowwise before summation.

For R=9 the two independently audited row1 majorants at comparison scale
T=3000 are contained strictly below, respectively for derivative orders
j=0,1,2,3,

 (1.523891e-12, 5.139245e-13, 1.184002e-13, 1.590300e-14).    (3)

The new finite check must verify each of these rational ceilings against
both existing audited row1 interval outputs. It reuses those two complete
computations and does not claim a third convolution or a new full tail
calculation. The positive terms decrease with T. The previously audited
exact input gives R_b>3412.96685816>3000 and R_b>=L>1. Consequently(3)
bounds every velocity component and each Cartesian partial of orderj
on the closed disk of radius9, uniformly over every admissible105 cutoff.

The density and its derivatives near P are unchanged. Parity and the
canonical normalization give the exact identity

 F_y(rho_T,c0)(P)-F_y(rho0,c0)(P)
 =rho0_y(P) partial_y U[h_T]_2(P)+rho0_xy(P) U[h_T]_1(P).

The independently accepted source bounds are
|F_y(rho0,c0)(P)|>6.70197e-7 and
|rho0_y(P)|+|rho0_xy(P)|<30.0230, with |P|<9. The j=1 ceiling is smaller
than the j=0 ceiling, so the triangle inequality yields

 |F_y(rho_T,c0)(P)|
 >6.70197e-7-30.0230*(1.523891e-12)>6.7015e-7>6.70e-7.       (4)

The final comparison is exact rational arithmetic and must be checked
independently with intervals as well. This strengthens the earlier
3.69e-7 lower bound for the single-tail family. It neither assumes that
P is still a source of the new velocity nor supplies an inverse estimate,
a global residual norm ceiling, stationarity, or a decisive task endpoint.

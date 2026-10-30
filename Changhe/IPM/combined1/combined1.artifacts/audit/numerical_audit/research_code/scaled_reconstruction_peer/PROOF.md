# Independent acceptance of candidate017 gradient reconstruction

## Exact statement

Fix c=4076476460239181/2251799813685248, delta=1-1/c, and the exact
potential chi in C1-N1-017-legqs50-quot013 with raw SHA256
7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Let rho=-partial_y Delta chi. Put t=r^2/(1+r^2), v=1-t,
w=v^(delta/2), z=cos(2theta), and D(t)=(1+2499(1-t))^19.
The retained exact rational polynomials with compressed SHA256
6887cdc6cdcc02fd0a7733d0343188df67c42c653e1a82ec033b2a207a08e872
satisfy on r>0

    rho_x=sin(2theta) sum_(ell=1)^8 w^ell P_(x,ell)(t,z)/D(t),
    rho_y=             sum_(ell=1)^8 w^ell P_(y,ell)(t,z)/D(t).

They extend continuously to the origin and to the compactified t=1
endpoint. There are40082 nonzero exact rational coefficients, with
maximum separate degrees103 in t and80 in z. This statement establishes
an identity, not an interval range, coercivity, inverse or existence.
The full candidate017 cover N4-309 remains a separate calculation.

## Generator meaning and independent polar reconstruction

A raw branch j contributes v^(-p_j) A(t) cos(2m theta), where
p_j=2-(j+1)delta/2. A legqs generator with specification
(w0,n,q,R) has exact radial numerator

    A(t)=sum_(k=0)^n (-1)^(n+k) binom(n,k)binom(n+k,k)
         R^(2q) t^(m+w0+k) v^q / (1+(R^2-1)v)^(w0+q+k).

All coefficients multiply the exact rational JSON amplitudes. Ordinary
Legendre terms use q=0,R=1, and monomials use n=0,q=0,R=1. This is the
finite shifted-Legendre identity; candidate017 has R=1 or50. All radial
denominators are strictly positive on [0,1], and the factors t^m with
cos(2m theta) make the Cartesian potential smooth at the origin.

Write E_p A=2t(1-t)A'+2ptA. Since r partial_r t=2t(1-t),
r partial_r(v^(-p)A)=v^(-p)E_p A. The polar Laplacian of the
mode n=2m is r^-2 v^(-p)(E_p^2-n^2)A cos(n theta). Apply
-partial_y using partial_y=sin(theta)partial_r+cos(theta)r^-1
partial_theta and the exact sine/cosine product identities. Each
resulting rational numerator has an exact factor t^2, checked by
polynomial division. Because

    r^-3 t^2 v^(-p_j)=r v^((j+1)delta/2),

this gives rho=r sum_(j,n) v^((j+1)delta/2) A_(j,n)(t)sin(n theta).
This is the independent polar density route of T4-366, already
accepted through N4-303. The original N4-284 route instead takes the
fourth Cartesian derivatives of the potential directly.

For a density branch r v^a A(t)sin(n theta), put
B=(1-2at)A+2t(1-t)A'. Its x derivative has sine coefficients
(B-nA)/2 at n+1 and (B+nA)/2 at n-1. Its y derivative has cosine
coefficients -(B-nA)/2 at n+1 and (B+nA)/2 at n-1. These follow by
substituting the polar derivative formulas and folding negative modes
using sine oddness and cosine evenness. They retain the derivative of
the full rational coefficient A. All gradient frequencies are even,
and the sine zero mode vanishes.

## Common denominator and angular polynomial identities

The independent rational representation stores separate multiplicities
for 1+624v and1+2499v. The exact candidate gradient requires no624
factor and at most19 factors of1+2499v. For every coefficient P_A/D_A,
form P_A D/D_A by exact polynomial division and check
(P_A D/D_A)D_A=P_A D. Positivity of D introduces no singularity.
There are728 such complete identities,360 for rho_x and368 for rho_y.

For z=cos(2theta), cos(2k theta)=T_k(z) and
sin(2k theta)=sin(2theta) U_(k-1)(z). N4-284 uses their recurrence;
T4-378 independently uses the exact closed coefficients

    T_0=1,
    T_k=(k/2) sum_(a=0)^floor(k/2)
        (-1)^a (k-a-1)! (2z)^(k-2a) / [a!(k-2a)!], k>0,
    U_k=sum_(a=0)^floor(k/2) (-1)^a binom(k-a,a)(2z)^(k-2a).

The recurrence T_(k+1)=2zT_k-T_(k-1), and the same recurrence for U,
with T_0=U_0=1,T_1=z,U_1=2z, proves the formulas by induction. The
closed formulas were also checked through80, giving158 recurrence
identities. Multiply each cleared radial coefficient by its complete
angular polynomial and add all branches exactly. T4-378 checks equality
of every complete sparse coefficient map with the N4-284 data, including
all cancellations and absence of extra coefficients. Therefore the
identities hold for every r>0 and angle, rather than only at sample points.

## Origin and compactified infinity

An independent fourth-order raw Cartesian expansion in u=r^2 has
coefficients b_m of u^2 cos(2m theta), m=0,1,2. Only generators
m+w0<=2 contribute. For each k<=min(n,2-m-w0), put L=2-m-w0-k.
Its contribution is its JSON amplitude times

    (-1)^(n+k)binom(n,k)binom(n+k,k) R^(-2(w0+k))
       sum_(i=0)^L binom(p_j-m,i)binom(-w0-q-k,L-i)R^(-2(L-i)).

This is the coefficient of u^L in
(1+u)^(p_j-m)(1+u/R^2)^(-w0-q-k). The identities
u^2=(x^2+y^2)^2, u^2 cos2theta=x^4-y^4 and
u^2 cos4theta=x^4-6x^2y^2+y^4 give
a22=2b0-6b2, a04=b0-b1+b2, rho_y(0)=-4a22-24a04.
The strain is4a22. The exact raw calculation agrees with the independent
N4 local jet in all four quantities, and c+4a22=1.

The full rational polynomials satisfy
sum_ell P_(x,ell)(0,z)=0 and
sum_ell P_(y,ell)(0,z)=rho_y(0)D(0). Because w tends to1 at the origin,
these are precisely the continuous Cartesian limits. At t=1, D(1)=1
and every w^ell tends to0, giving the continuous compactified limit.
No finite tail is omitted, but this observation supplies no bound on
intermediate values.

## Verification and scope

The checker binds N4-284, accepted303 and the entire independent
T4-378 input graph. Existing identical own files are retained without
unnecessary large copies. It recomputes all sixteen complete coefficient
digests and40082 nonzero coefficients from the retained compressed
polynomials, verifies the exact denominator and origin identities,
compares each branch count and all six point balls, and checks the
recorded independent clearing and recurrence counts. Peer code is read
but not executed. The acceptance depends on the analytic argument and
complete independent coefficient comparison, not on six point values.
The final record accepts the reconstruction only. The range theorem is
accepted separately by N4-310; actual cover arithmetic is still separate.

# The second nonlinear exterior row of the single-tail repair

Status: complete informal argument before the new numerical coefficient evaluation.
All nonvanishing conclusions below require the stated interval check. This is
not a profile-existence theorem or a neighborhood exclusion.

## Exact statement and imported definitions

Use the exact modal trial rho0, c0=1/k, k=1615536043799051/9007199254740992,
R=exp(tplus), and the single-tail repaired rho_T of topic105, including its
mandatory addendum. The exact Green law, normalization and finite exterior
expansion are those proved in topics15,42,104,105,106 and109. In this document
only the already proved expansion of109 is used; its separate nonvanishing
coefficient and externally unreviewed conclusion are not premises.

Set beta=2k-1, a2=3k-2, d=k-2, a3=4k-3. The original leading density rows
D0,D1,D2 multiply r^k,r^beta,r^a2. In the single-tail repair the beta row is
A1=k/(1-k) B_(k,k)(D0,D0)=D1+k/(1-k) Epsilon, where Epsilon is the physical
leading residual coefficient of rho0 at exponent beta. These are exact angular
functions; enclosures do not redefine them. Topic42 independently computed all
522 odd-sine coefficients e_j of Epsilon in the coordinate r/R, so the physical
coefficients are R^(-beta)e_j.

For each of D0,D1,D2, let b_(i,j) denote the coefficient of sin((2j+1)theta)
in cos^2(theta)sin(theta) sum_(m=0)^259 A_(m,i)cos(2m theta). For i=0 include
the exact normalization correction z in A_(0,0). Thus the physical sine rows
are d_(i,j)=R^(3-a_i)b_(i,j), with a_0=k,a_1=beta,a_2=a2. Every missing
coefficient is zero. Let h_j=d_(1,j)+k/(1-k)R^(-beta)e_j, the sine coefficients
of A1. The desired real scalar is

 C20=(a2/k-1)d_(2,0)
           + Q_(k,beta)(d_0,h) + Q_(beta,k)(h,d_0).             (1)

If an independently audited interval for C20 excludes zero, then for every
fixed admissible cutoff T the coefficient of r^a2 sin(theta) in F(rho_T,c0)
is C20 and is nonzero. It is independent of T. Within the finite exterior
class of106, after fixing D0 and the required A1, the r^a2 target must be A2
from106 if r F(rho,c0) is in L2. In particular the actual correction H2=A2-D2
then has a nonzero first sine coefficient k C20/[2(1-k)]. This is a necessary
counterterm in this finite class, not a statement about arbitrary exterior
expansions. No finite-radius numerical lower bound follows from C20 alone.

## Independent reconstruction of the projection

For an angular density row A=sum_j A_j sin((2j+1)theta) at exponent a, put

 F_n=((a+1-2n)A_(n-1)+(a+1+2n)A_n)/2,
 Delta_n=4n^2-(a+1)^2,
 v_n=-2n F_n/Delta_n, w_n=(a+1)F_n/Delta_n.

Applying -Delta to r^(a+1)sin(2n theta) proves these particular Green factors.
They are radial and tangential velocity coefficients because U_r=-psi_theta/r
and U_theta=psi_r. All required Delta_n are positive for a=k or beta.
For another density row B at exponent b, direct product-to-sum gives the
frequency-one coefficient of b V_a[A]B+W_a[A]B' as

 Q_(a,b)(A,B)=sum_(n>=1) {b v_n(B_n-B_(n-1))
                +w_n[(2n-1)B_(n-1)-(2n+1)B_n]}/2.             (2)

Indeed cos(2n theta)sin((2j+1)theta) contributes only for j=n-1,n,
with coefficients -1/2,+1/2. The differentiated density times sin(2n theta)
contributes +1/2,-1/2 for the same two indices. Collecting (2) gives the
independent algebraic form

 Q_(a,b)(A,B)=sum_n F_n/(2 Delta_n)
  { [2n(a+b+1)-(a+1)]B_(n-1)
                      -[2n(a+b+1)+(a+1)]B_n }.                (3)

For both products in(1) only n<=261 contributes. In the first, D0 has stream
support through261; in the second, the density D0 has odd-sine support
j<=260. Consequently only h_0,...,h_261 are needed. Higher A1 coefficients
cannot contribute to frequency one. Omitting them here is exact support
algebra, not a numerical truncation.

The projection of each original row can be independently computed by either
signed expansion of the four frequencies 1+2m,1-2m,3+2m,3-2m, each with
weight1/8, or Laurent multiplication of cos(theta)^2,2i sin(theta), and the
finite cosine series. The m=0 normalization contributes z/4 to j=0,1.

## Why this is the residual coefficient

Outside2T, rho_T=r^k D0+r^beta A1+r^a2 D2+r^d Dd plus the finite remainder
of order r^a3 times a fixed logarithmic polynomial. A compact strain
compensator and the inner cutoff change only exterior homogeneous velocity
terms r^(-2n-1); their products with the leading density derivative have
exponent at most k-4<a3. The only particular products at a2 are (k,beta)
and(beta,k), since a+b-1=a2 exactly for these ordered pairs. All other
products except(k,k) have exponent at most a3, and the beta residual
already cancels exactly. Thus (1) is the first sine coefficient of the
residual's a2 row, independent of T.

For a general proposed r^a2 row B2 with D0,A1 fixed, the residual row is
-2(1-k)B2/k + B_(k,beta)(D0,A1)+B_(beta,k)(A1,D0). Its vanishing uniquely
requires B2=A2 as in106. A nonzero row at a2>-2 makes r F fail L2 by the
radial integral integral r^(2a2+3)dr; a smaller d or a3 row cannot cancel it.
This proves the stated necessity. In particular C20=2(1-k)H2_0/k.

There is also a dot H^-1 obstruction from this row alone. For nonnegative
smooth nonzero g supported in(1,2), phi_S(X)=g(|X|/S)sin(arg X) has constant
gradient L2 norm. The residual pairing is
pi C20 S^(3k) integral_1^2 g(s)s^(3k-1)ds + o(S^(3k)), which is unbounded
if C20 is nonzero. All tests are compactly supported away from the origin.
This uses 3k>0 and d+2=k<3k, without a numerical asymptotic threshold.

## Planned independent computation and scope

Arb512 will decode exact JSON dyadics, use four-frequency row projections,
the primary522-coefficient leading residual, physical row scales and(3).
mpmath.iv180 will decode the original NPZ, construct Laurent row projections,
the independent522-coefficient residual, coordinate-scaled Green sums(2).
Each separately encloses C20. An exact rational audit will compare all original
row data, verify support/projection algebra, both strict public bounds, every
imported file hash and the normalization brackets. Overlap alone is not proof.
No actual second-model acceptance is assumed. The current Opus5.5 availability
limitation must be preserved, and the overall result stays OPEN until an actual
independent mathematical review is obtained. No request will bypass a refusal.

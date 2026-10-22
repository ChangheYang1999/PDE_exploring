# A remaining exterior row obstructs homogeneous H^{-1} for the single-tail repair

Status: complete informal proof before the new coefficient computation.
This is a statement about the explicit topic105 trial, not a neighborhood
exclusion or a stationary-profile endpoint.

## 1. Exact definitions and statement

Use the normalized modal rho0, exact k,L,R_b=exp(tplus), canonical
velocity, c0=1/k and the single-tail repair rho_T of
normalized_tail_repair/PROOF.md with its mandatory addendum. The exact
input k=1615536043799051/9007199254740992 obeys 0<k<1/4. Put

 beta=2k-1, a2=3k-2, d=k-2, a3=4k-3.

The density's original exterior pair(j,l)=(0,1) is column6 of the exact
260 by10 array Aout. Its physical coefficient is

 Dd(theta)=R_b^(3-d) cos^2(theta)sin(theta)
                      sum_(m=0)^259 A_(m,6) cos(2m theta).       (1)

The exact center normalization changes column0 and a fast joined row,
not column6. Define the rational coefficient

 b_d=(2 A_(0,6)-A_(2,6))/8,
 L_d=(-2/k) R_b^(5-k) b_d.                                     (2)

A new two-method computation will verify b_d!=0 and enclose L_d strictly
on one side of zero. Until that check passes, the following assertions
are conditional on b_d!=0. Subject to it, for every fixed
T>=max(R_b,L,1), the residual epsilon_T=F(rho_T,c0) satisfies:

(a) The coefficient of r^d sin(theta) in its exterior expansion is
exactly L_d, independent of T. It is nonzero.

(b) epsilon_T is not in dot H^-1(R2), despite being in L2 and therefore
H^-1. Also r epsilon_T is not in L2.

(c) Within the finite exterior class consisting of the leading r^k
row, an arbitrary r^beta row, an arbitrary r^a2 row, an r^d row and
only further density powers at most a3, with the same canonical law
and c0, the condition r epsilon in L2 forces the r^d density row to
vanish. Thus the topic106 cancellation Hd=-Dd removes a necessary
nonzero row within this class. No necessity claim is made about its
a2 correction, and no classification of arbitrary other tail types,
logarithmic leading terms, or all weighted function spaces is asserted.

## 2. Reconstruction of the exterior residual

The finite density powers of rho0 are k-j(1-k)-2l for
(j,l)=(0,0),(1,0),...,(5,0),(0,1),(1,1),(2,1),(0,2),
and the joined power3-bo with bo>120 and logarithmic degree at most6.
These exact inputs and all nonresonant Green denominators are separately
audited in topic106. The single-tail repair replaces only the beta
row by A1, the row which cancels the residual at beta. Its compact
strain compensator contributes only decaying homogeneous velocity
outside2T. Thus for fixed T and sufficiently large r,

 rho_T=r^k D0+r^beta A1+r^a2 D2+r^d Dd
                         +O(r^a3(1+log r)^6).                  (3)

All displayed rows are finite sine polynomials, without logarithms.
Every canonical particular velocity for r^a A has exponent a; its
homogeneous velocities are r^(-2n-1), n>=1. This is the exact finite
Green expansion, not a local Poisson inverse with a free harmonic term.
An ordered product U[r^a A].grad(r^b B) has exponent a+b-1.
The only pairs above a3 are (k,k) at beta, and (k,beta),(beta,k) at a2.
Every pair involving d has exponent at most 2k-3<a3, and homogeneous
velocity-density products have exponent at most k-4<a3. The comparisons
use k>0. In particular no nonlinear term has exponent d. Since

 a3<d<a2<-1,  d>-2, a3<-2,

and the beta row was exactly canceled, the residual has the uniform
finite expansion

 epsilon_T=r^a2 C2(theta)+r^d Cd(theta)
                              +O(r^a3(1+log r)^12),             (4)
 Cd=(d/k-1)Dd=(-2/k)Dd.

C2 is an exactly defined finite sine polynomial which need not be
computed for this theorem. It does not depend on T either, although
the smaller remainder constants may depend on T. Compact annular
sources cannot change a particular coefficient at d.

For the frequency-one projection, use
cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4.
Multiplication by cos(2m theta) contributes to sin(theta) only when
m=0,1,2; the two m=1 contributions cancel, m=0 contributes A_(0,6)/4,
and m=2 contributes -A_(2,6)/8. This proves b_d and (2).
A distinct Laurent multiplication of the two cos factors and one sin
factor will check all column6 sine coefficients from the original NPZ.

## 3. Negative norm obstruction without computing C2

Let g be a nonnegative, nonzero smooth function supported in (1,2),
phi(Y)=g(|Y|)sin(arg Y), Phi_S(X)=phi(X/S). Then
||grad Phi_S||2=||grad phi||2, independent of S. Let C_{2,0}
be the sin(theta) coefficient of C2; this coefficient is finite, and
its value or sign is not assumed. From (4),

 <epsilon_T,Phi_S>
   =pi C_{2,0} S^(a2+2) integral_1^2 g(s)s^(a2+1)ds
    +pi L_d S^(d+2) integral_1^2 g(s)s^(d+1)ds
    +O(S^(a3+2)(1+log S)^12).                                 (5)

Here a2+2=3k>d+2=k>0, while a3+2=4k-1<0. If C_{2,0}!=0,
the first term dominates and the pairing is unbounded. If C_{2,0}=0,
the second dominates and is unbounded since L_d!=0. These two exhaustive
cases prove that epsilon_T is not a bounded functional on dot H^1.
All tests are smooth, supported away from zero and have zero integral.
No pointwise realization of the homogeneous completion is assumed.

The same expansion proves r epsilon_T not in L2. If C2 is nonzero,
its larger power a2>-2 already gives divergence. If C2 is identically
zero, the nonzero Cd at d>-2 gives divergence. Uniform angular
convergence and nonzero angular L2 norm reduce this to
integral r^(2a+3)dr with a>-2. The remainders in (4) are strictly
smaller; they cannot cancel the leading nonzero angular function.
Alternatively, the angular primitive argument of topic106 proves that
r epsilon_T in L2 would imply epsilon_T in dot H^-1, contradicting(5).
The existing topic105 L2 membership remains valid because a2,d<-1.

## 4. Necessity in the stated finite exterior class

For the class in(c), the exponent enumeration is unchanged. Its linear
coefficient at d is (-2/k) times its density row there; there is no
nonlinear contribution at d. If the beta or a2 residual row is nonzero,
it already obstructs r epsilon in L2. After those rows vanish, a
nonzero d row still obstructs it because d>-2. Therefore every such
profile with r epsilon in L2 must have zero d density row.

This forces Hd=-Dd for the given rho0 whenever the repair retains the
other listed exponent types. It says nothing about the actual a2 row's
being nonzero. The nonzero test uses only the exact stored column6,
the exact c0 and radius. The cutoff radius can change lower homogeneous
terms but cannot alter this conclusion.

## 5. Verification, dependencies and limits

Before publication: check all260 column6 coefficients against their
exact JSON export, recompute the frequency-one projection in two ways,
check the exponent comparisons using rational arithmetic, and enclose
R_b^(5-k) with Arb and mpmath.iv independently. The first method uses
the closed projection(2), the second constructs the Laurent product
from the original binary64 dyadics. Record exact endpoints, source
hashes, outward rounding and the current complete dependency verdicts.
A numerical interval containing zero would leave the theorem unproved.

The higher-tail repair in topic106 resolves this particular codomain
obstruction by canceling d and a2. This theorem does not prove that its
forcing norm is small, and the separate topic108 annular argument shows
asymptotic growth as T tends to infinity. No inverse, nonlinear closing
inequality, exclusion neighborhood of X3 or decisive endpoint follows.

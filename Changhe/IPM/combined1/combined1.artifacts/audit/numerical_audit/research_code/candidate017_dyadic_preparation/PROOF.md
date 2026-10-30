# Candidate017: two projected Laplacian norms and the conditional seven-cell test

## Statement, objects and hypotheses

Fix c=4076476460239181/2251799813685248, gamma=1/c, delta=1-gamma,
S=1+r^2, t=r^2/S and v=1/S. The exact candidate is
C1-N1-017-legqs50-quot013, raw SHA256
 7dc30181e2d29c8c9706cf396a1be2334f53b2a19ca00e4fad756ff98ec59114.
Its rational JSON defines a finite smooth potential chi by the generator
convention of ../joint_scaled_factored_weak/PROOF.md. Put
rho=-partial_y Delta chi, u=(-chi_xyy,chi_xxy) and
F=(cX+u).grad rho-rho. All source coefficients, exact origin identities
and forbidden sectors must agree with the earlier accepted017 audit.

For an odd positive n let Pi_n be the orthogonal full-circle sine
projection, normalized by pi^(-1) integration over0<=theta<=2pi. Define

 J(a)^2=sum_(n=1,3) integral_R2 S^(2-a) |Delta Pi_n F|^2 dX,
 N_a(F)=||S^((2-a)/2) Delta F||_2,  a>=0.

This note proves an exact algorithm for J(1/4) and J(7/4). Actual
containing intervals require its finite checker to pass. The selected
modes give J(a)<=N_a(F), even when the latter is infinite. No omitted
angular mode is set to zero and no full upper norm is asserted.

The conditional consequence concerns only the registered
NC-T-ORIGIN-INV scalar criterion. Assume1<c<2, a0=rho_y(0)>=5c-4,
chi_xxyy(0)=1-c, and the criterion

 5^((a-2)/2) N_a(F)<H(c-1)(1+c-ca)/(1+a),  0<a<Astar=1+1/c,
 H(d)=max_(0<s<d) (d-s)sqrt(4 pi s(1+s)).                 (1)

When interpreted as an obstruction to the registered dyadic existence
scheme, additionally assume the exact realization, input hyperplane,
canonical velocity, dyadic partition, plateau and absorption hypotheses
of the origin inverse theorem and its retained Opus reviews in
../origin_dyadic_ceiling/. Specifically these supply0<s<c-1,
M>=1/(c-1-s), beta<=1+c-ca and C_U>=1. This computation supplies no
new inverse theorem. A violation of(1) excludes that criterion at this
reference, not a stationary solution or a different proof scheme.

## Exact projection and two derivative constructions

The generators are H_m S^(p_j-m) t_R^w v_R^q P_N(2t_R-1), where
H_m=Re(x+iy)^(2m), p_j=(3+gamma-j delta)/2,
t_R=r^2/(R^2+r^2), v_R=R^2/(R^2+r^2), and P_N is the Legendre
polynomial with P_N(1)=1. All indices are nonnegative integers and
R belongs to{1,10,25,50,100}. The017 input uses only1 and50.
After factoring the branch power, the radial functions are exact
rational functions of t with denominator

 product_(b in{99,624,2499,9999}) (1+b(1-t))^k_b,  k_b>=0.

All denominators are positive on[0,1]. Sums, products and derivatives
therefore stay in this class. The accepted Cartesian generator
recurrence computes all rho,u,grad rho fields. The identity
cos(l theta)sin(m theta)=[sin((m+l)theta)+sin((m-l)theta)]/2,
with the sign of negative frequencies retained, selects every input
pair contributing to each requested output mode. Together with the
exact drift this yields

 Pi_n F=r sum_ell v^(ell delta/2) P_(ell,n)(t) sin(n theta).       (2)

Every background mode contributing to(2) is retained. This is the
same exact projection used in the accepted whole-plane weak tests.

For z=ell delta/2 set T_z P=(1-2zt)P+2t(1-t)P'. Since
r partial_r t=2t(1-t) and r partial_r v=-2tv, direct differentiation
of(2) gives

 Delta[r v^z P(t)sin(n theta)]
      =r v^(z+1) L(t)sin(n theta),
 t L=T_z(T_z P)-n^2 P.                                  (3)

The numerator on the right is divided by t only after its exact zero
is checked. Independently apply the Cartesian recurrence to(2) twice.
For order d, represent a field by r^(1-d) v^(ell delta/2) B(t) times
its trigonometric factor. Its radial derivative numerator is
(1-d-ell delta t)B+2t(1-t)B'. In the smooth normalization used by the
code B=t^floor(d/2) Q, and the new coefficient is divided by
t^floor((d+1)/2), with exact divisibility required. Multiplication by
cos(theta),sin(theta) and angular differentiation gives the adjacent
frequencies. Both mixed derivatives must coincide exactly, and xx+yy
must equal(3) coefficient by coefficient. These identities include
all derivatives of the positive denominator factors.

## Endpoint cancellations and complete moments

For each nonzero L write its numerator in v, extract its exact order
q at0, and write L(1-v)=v^q Q(v)/D(v). Require
ell delta+2q-2>0 for every nonzero branch. Because D(0)=1, these
conditions make every diagonal integral finite at a=0; the mixed
integrals are finite by the arithmetic mean of their exponents.
For one mode, angular orthogonality, r dr=dt/(2v^2), and(3) give

 (pi/2) sum_(ell,k) integral_0^1
   v^(a+(ell+k)delta/2+q_ell+q_k-3) (1-v)
             Q_ell(v) Q_k(v)/(D_ell(v) D_k(v)) dv.        (4)

Every unordered branch pair is counted, twice off the diagonal.
Exactly combine pairs with equal exponents before integration. Partial
fractions over the distinct negative auxiliary poles are exact rational
identities, replayed by multiplication by their common denominator.
The same decomposition is valid at both a values because it depends
only on the rational factor. Polynomial terms integrate rationally;
principal terms are evaluated by the accepted outward Arb positive-pole
moment algorithm in ../rational_pole_moments/PROOF.md. All integration
exponents must be greater than-1. Sum complete finite terms before
taking a positive square root. More than150 reliable bits are required.
No quadrature, finite spatial cutoff, or leading-term replacement occurs.

Calibration precedes017: apply the new four-pole representation to007,
compare its exact projections and all five Cartesian derivative maps
with the accepted polynomial implementation, and compare the two
complete energies for each mode with the retained007 records. This
calibration does not by itself certify017; the actual017 calculation
and its comparison with the separate N3 construction are still required.

## Seven cells from only two evaluations

J(a) is nonincreasing, since S^(2-a) decreases pointwise and the
integrand is nonnegative. Put endpoints
0,1/4,1/2,3/4,1,5/4,3/2,Astar; exact3/2<Astar<7/4.
For the first cell use e=1/4. For each of the six other cells use e=7/4.
In every case e is at least the cell's right endpoint. For[l,h],

 5^((a-2)/2)N_a(F)>=5^((l-2)/2)J(e),
 H(c-1)(1+c-ca)/(1+a)<=H(c-1)(1+c-cl)/(1+l).             (5)

The first factor increases and the last ratio decreases with a.
Thus a strict positive gap between the two bounds in(5) contradicts(1)
throughout that cell. This two-evaluation test is weaker than evaluating
at all seven right endpoints, but it suffices if every gap is positive.
It does not assert reproduction of the five unused N3 endpoint values.

For completeness, the unique maximizing point for H(d) is
sstar=(2d-3+sqrt((2d-3)^2+16d))/8. Indeed the derivative of
(d-s)^2 s(1+s) equals(d-s)[d+(2d-3)s-4s^2]; the bracket has exactly
one root in(0,d), with opposite signs at its endpoints. The endpoint
values are zero. This proves the maximum formula without numerical
optimization. The checker encloses sstar,H(d), all seven gaps and their
ratios. The low-rate condition separately fails when Astar<=a<2.

## Evidence and scope

Frozen N3 seven-cell output and source are comparison inputs, never
executed. Only the complete J(1/4),J(7/4) squares are compared. Decimal
lower-endpoint strings printed by N3 are not treated as exact interval
centers. The wide containing squared-norm displays can be compared to
the own100-digit balls. No independent reproduction of internal1024-bit
N3 endpoints is claimed.

Exact JSON records bind all source files, own calibration inputs, raw017,
its accepted origin/sector audit, exact derivative identities, complete
group counts, moment decompositions and interval outputs. Own017 work
is OPEN until it passes and agrees with the independent N3 construction.
The final conditional scalar implication inherits the stated analytic
hypotheses; neither a residual upper norm nor an existence result follows.

## Implemented algorithm and provenance

The checker adapts the accepted016 finite algorithm to raw017 and
recomputes both complete projected modes, every derivative and both
positive-endpoint energies. Its candidate-specific source is bound by
the raw hash above, its own origin/sector record, and the frozen N3
source identity. The four-pole arithmetic includes pole2499 for radius50.
A fresh007 calibration precedes017. No017 numerical value or certificate
is inherited from016. Actual acceptance remains OPEN until the checker
and its source-binding wrapper finish successfully.

The wrapper follows own imported module objects, including dynamically
loaded helpers, and records their hashes before and after execution.
It also checks the moment implementations against the previously
accepted source-bound016 weak calculation, which supplies only source
identity, not a017 value. All outputs are new write-once files. The
complete framework and limitation statements above remain in force.

# Sixteen-mode dual and divergence-free certificate for candidate016

## Statement, exact inputs and dependencies

Let chi be the canonical exact potential C1-N1-016-legqs25-quot013 with raw
SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42.
Put c=4076476460239181/2251799813685248, delta=1-1/c,
rho=-partial_y Delta chi, U=(-chi_xyy,chi_xxy), and
F=(cX+U).grad rho-rho on R^2. All norms use full-plane Lebesgue measure.
Write F=sum_n f_n(r)sin(n theta), with its complete accepted 160 odd
frequencies n=1,3,...,319. The accepted exact residual construction has
1360 radial branches. Set G0=||F||_2, G1=||grad F||_2,
P2=||(1+4r^2)^(2/5)D^2 F||_2 and S=||rF||_2^2, all finite. Define

 H(F)=sup{|integral F phi|: phi in C_c^infinity(R^2), ||grad phi||_2<=1},
 E2(F)^2=P2^2+2^14 G1^2+2^18 G0^2+(20/21)2^18 H(F)^2.

The imported exact trial coefficients are mathematical data whose labels
and energies must be checked. For each n=1,3,...,31 set

 psi_n=u_n(r)sin(n theta),
 u_n=sum_i x_i r^3(1+r^2)^(-beta_i)(r^2/(1+r^2))^(k_i).

Every beta_i>3/2, k_i>=-1 and 3+2k_i-n is a nonnegative even integer.
All x_i are exact rationals. Define d_n=||grad psi_n||_2^2,
p_n=integral F psi_n, a_n=||Z_n||_2^2 and b_n=<A_F,Z_n>, where
A_G=-e_theta sum_n r g_n(r)cos(n theta)/n and
Z_n=A_(Delta psi_n)-grad psi_n. Require d_n,a_n>0.
For strict rational floors 0<l_n<|p_n|/sqrt(d_n) and
0<j_n<b_n^2/a_n the conclusion is

 sum_n l_n^2 < H(F)^2 < B-sum_n j_n,                         (1)

where B is any accepted complete upper bound for
M2=pi sum_(all160 n) n^(-2) integral_0^infinity r^3 f_n^2 dr.
One may choose the larger of two already accepted floors in a given
frequency, separately for l_n and j_n. One may not add both same-frequency
floors. The inequalities concern actual H and E2 under the accepted source
soundness premises; they imply no correction distance or existence.

The complete B used here is the exact positive-coefficient prefix bound
from T4-480, research/candidate016_prefix31_hardy_audit. Its derivation is
accepted under T4-477 and T4-481. The prior deep n=1,3 floors and 650digit
replay are T4-472, research/candidate016_cross_archive_audit. G0,G1,P2 and
S are accepted by T4-467. Each input and its upstream source graph is
bound in data/manifest.json and data/initial_sources.json. Numerical
claims remain OPEN until the complete new producer result and this
checker pass. The formal-sources directory contains reviewed Python
certificate source as text, not a Lean formalization.

## Ordinary integrals, domain and orthogonality

At the origin each r^(3+2k)sin(n theta) is a homogeneous Cartesian
harmonic polynomial times a nonnegative integer power of r^2. The rest
of the radial factor is smooth in r^2, including when k=-1. Thus each
trial is smooth. At infinity its first two logarithmic radial derivatives
are O(r^(3-2 beta_min)). Gradient and r Delta psi are square integrable.
Smooth radial cutoffs converge in the gradient norm: the squared error
is O(R^(6-4 beta_min)), tending to zero. Every grouped forcing pairing
below has exponent plus its exact numerator zero order greater than -1
at the infinite endpoint. Its denominator is positive on the compact
coordinate interval. This proves absolute convergence and identifies
the functional pairing with its ordinary integral by dominated convergence.

On annuli, div A_F=F by angular differentiation. Its radial flux is zero,
so local integrability extends the identity across the origin. Its L2
norm squared is M2. Consequently |integral F phi|<=sqrt(M2)||grad phi||_2,
and the functional extends to the gradient completion. Angular
orthogonality makes the sixteen grad psi_n mutually orthogonal. Testing
with sum_n(p_n/d_n)psi_n gives H(F)^2>=sum_n p_n^2/d_n.

The same distribution calculation gives div Z_n=0. Its explicit form is

 Z_n=-u_n'(r)sin(n theta)e_r
       -(r u_n''(r)+u_n'(r))cos(n theta)e_theta/n.

Distinct Z_n are orthogonal. A_F+sum_n t_n Z_n has divergence F and
squared norm M2+sum_n(2t_n b_n+t_n^2 a_n). Minimization at the exact
value t_n=-b_n/a_n gives H(F)^2<=M2-sum_n b_n^2/a_n. Strict rational
floors and complete M2<=B give (1). Nonzero decaying u_n gives a_n>0,
since vanishing Z_n first forces u_n' to vanish. A positive exact d_n
also verifies nonzero trials. Choice of different tests for the lower
and upper inequality causes no conflict: these are separate arguments.

## Independent exact energy calculation

Let t=r^2/(1+r^2), v=1-t, b=beta-1 and
P_b(t)=sum_(i:beta_i-1=b) x_i t^(k_i+1). Then
u_n=r sum_b v^b P_b(t). With y=log r define
D_b P=(1-2bt)P+2t(1-t)P'. Direct differentiation gives
u_y=r sum_b v^b D_b P_b and u_yy=r sum_b v^b D_b^2 P_b.
The polar integral and dr/r=dt/(2t(1-t)) yield

 d_n/pi=(1/2)sum_(b,c) integral_0^1 v^(b+c-2)
             [(D_bP_b)(D_cP_c)+n^2 P_bP_c]dt,
 a_n/pi=(1/2)sum_(b,c) integral_0^1 v^(b+c-2)
             [(D_bP_b)(D_cP_c)+(D_b^2P_b)(D_c^2P_c)/n^2]dt.

All 81 ordered pairs of the nine beta classes are retained. Every
exponent e=b+c-2>-1. Independently of the producer's substitution
into powers of v, integrate monomials t^j using the exact beta moments
M_0=1/(e+1), M_j=j M_(j-1)/(e+j+1). This recurrence follows by integration
by parts, or the convergent beta integral. Each energy group is one half
the exact coefficient sum against M_j. Match every grouped value and
the total with the producer and the original vector's exact d_n/pi.

## Signed moment replay and complete-field binding

The producer reconstructs f_n=r sum_ell v^(ell delta/2) A_(ell,n)(t)
from the raw potential. Exact denominator raising or exact polynomial
division with zero remainder identifies each A with the accepted complete
Cartesian-checked residual representation, coefficient hash by coefficient
hash. The checker here checks the full component sets and identities.
It does not reconstruct the residual again. The pairing integrals are

 p_n=(pi/2)sum_(ell,b) integral_0^1
                 v^(ell delta/2+b-3) t A_(ell,n)P_b dt,
 b_n=(pi/(2n^2))sum_(ell,b) integral_0^1
                 v^(ell delta/2+b-3) t A_(ell,n)D_b^2P_b dt.

The cross group numerator already includes 1/n^2. Group all equal
exponents before integrating, retain the exact zero order q at v=0,
and require ell delta/2+b-3+q>-1. The accepted positive-pole moment
routine checks the exact partial-fraction identity and containing Arb
intervals. We retain this source-specific soundness and execution premise.
Reparse every saved 650digit group interval and independently add the
signed intervals. Check finite values, exact exponent/order, positive
pole factors, reconstruction flags, accumulated absolute radius below
10^-200 and final relative accuracy above 600 bits. Compare the replay
with the full-precision source serialization and peer containing balls;
overlap of two containing final displays alone is not the proof of a
floor. Prove each directed floor against the independently resummed
interval and the independently computed positive exact energy.

## Full tail and scalar assembly

Let Q_n=pi integral r^3 f_n^2 dr. With complete S<=S_U and independently
accepted Q_n<=U_n for n=1,...,31, odd, the exact bound is

 B=S_U/33^2+sum_(n<33,odd)(1/n^2-1/33^2)U_n.

It retains every omitted mode, since 1/n^2<=1/33^2 for n>=33. All
coefficients are positive. The accepted T4-480 source provides this
exact rational B. No new tail estimate or frequency truncation is made.
Write L=sum selected_l_n^2 and J=sum selected_j_n. Exact positive
component bounds G0_L/U,G1_L/U,P2_L/U then give

 E2_L_squared=P2_L^2+2^14 G1_L^2+2^18 G0_L^2+(20/21)2^18 L,
 E2_U_squared=P2_U^2+2^14 G1_U^2+2^18 G0_U^2+(20/21)2^18(B-J).

For positive rational printed endpoints, exact squaring supplies strict
directed bounds. Compare with accepted candidate007 upper E2=606.820219
and lower H>0.635524376000091 only in the same norm definition. The
result records exact squares and conservative decimal endpoints.

## Scope and verification evidence

The checker runs only our own finite arithmetic and interval replay.
No foreign program, candidate moment integral, solver, quadrature,
finite-radius cutoff approximation or sampled angular transform runs.
All 1224 trial labels, all radial branches at all sixteen selected
frequencies and every saved signed group must pass. Complete source
hashes are frozen before arithmetic and rechecked. The finite exact
coefficients do not assert solver optimality or basis completeness.
The gradient completion does not silently add a strain-trace evaluation;
no c[h] or origin normalization theorem is needed for these forcing norm
bounds. Existing existence and inverse claims retain all their separate
normalization, contact-term, domain, range and regularity hypotheses.
No pair changes closure verdict on the strength of these norm comparisons.

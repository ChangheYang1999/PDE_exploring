# Candidate016 cross energies and a finite replay of four complete pairings

## Exact statement and hypotheses

This audit fixes the real S1 snapshot C1-N1-016-legqs25-quot013,
raw SHA256 a0345b4eee060ea8f6b0b6e21719cf606b04174704e0a26f516c645081208f42,
c=4076476460239181/2251799813685248 and its canonical complete residual
F=(cX+U[rho]).grad rho-rho. The canonical velocity includes its local
contact term. F has finitely many positive odd sine modes f_n sin(n theta)
and ||rF||2 is finite by the independently accepted complete component
certificate T4-467. Lebesgue measure is used on the whole plane. Define
H(F)=sup{|int F phi|:phi smooth compactly supported,||grad phi||2<=1}.
All exact trial coefficients below are frozen in the JSON accepted by
T4-470; no FLOAT optimizer or finite-basis completeness is a premise.

For n=1,3 take precisely those nonzero tests psi_n=u_n(r)sin(n theta).
Put d_n=||grad psi_n||2^2, p_n=int F psi_n and
A_F=-e_theta r sum f_n cos(n theta)/n,
Z_n=A_(Delta psi_n)-grad psi_n,
a_n=||Z_n||2^2, b_n=<A_F,Z_n>.
This audit independently proves the exact rational values a_n/pi>0
from the full trial coefficients and replays the four pairings p_1,p_3,
b_1,b_3 by adding all their source-certified group intervals. It confirms

 b_1^2/a_1 > 103604969053537790023083/500000000000000000000000,
 b_3^2/a_3 > 15724609172740789414523/500000000000000000000000.

Their sum is strictly above
59664789113139289718803/250000000000000000000000.
The individual moment enclosures retain N4's complete projection,
positive-pole integration and directed-tail certificates as premises.
This audit independently re-sums those enclosures; it does not perform
a new numerical integration of F or execute a peer program.

The dual floors of T4-470 and its actual identical-energy comparison
E2(016)>608.392385921614>606.820219>E2(007) are recovered from the saved
groups, with H(016)>0.529469576110512066428681. This discharges the
intermediate-display precision limitation identified in T4-470 for the
new archive. The old 200-digit group records remain insufficient and
are preserved unchanged. No complete numerical upper bound for H
follows until the full M2=||A_F||2^2 has been independently accepted.
The general upper theorem T4-469 remains pending Opus review at writing.

## Admissibility and exact positive trial energy

Each term of u_n is x r^3(1+r^2)^(-beta)t^k, t=r^2/(1+r^2),
where x,beta are exact rationals, beta>3/2, k is an integer at least -1,
and 3+2k-n is nonnegative and even. All 663 labels are checked.
At the origin this is a smooth Cartesian polynomial times a smooth
radial factor. At infinity its size and first two logarithmic radial
derivatives are O(r^(3-2 beta)). The gradient is square integrable;
smooth outer cutoffs have squared gradient error O(R^(6-4 beta_min)),
which tends to zero. Hence psi_n belongs to the gradient completion of
compact smooth functions and r Delta psi_n is in L2. Angular Hardy
gives ||psi_n/r||2<=||grad psi_n||2, so int |F psi_n| is finite.
These facts justify the dual test without a boundary or origin term.

Let y=log r and v(y)=u(exp y). Polar differentiation gives

 Z_n=-u' sin(n theta)e_r-(r u''+u')cos(n theta)e_theta/n,
 a_n/pi=int [v'^2+v''^2/n^2]dy,
 b_n=(pi/n^2)int_0^infinity r f_n(r) u_yy(r)dr.

The first identity follows by subtracting the gradient from the angular
right inverse of Delta psi. The latter two follow by direct scalar
products and integration of sine or cosine squares, each equal to pi.
The positive energy a_n vanishes only when v' is zero. Decay then forces
v=0, whereas the exact computed positive energy proves the current test
is nonzero even if a redundant parametrization could cancel a vector.

For w=1-t, group b=beta-1 and P_b(t)=sum x_(beta,k)t^(k+1).
Define D_b P=(1-2bt)P+2t(1-t)P'. Then
u_y=r sum w^b D_bP_b and u_yy=r sum w^b D_b(D_bP_b).
Substitution of dy=dt/(2t(1-t)) yields

 a_n/pi=(1/2)sum_(b,c) int_0^1 (1-t)^(b+c-2)
             [D_bP_b D_cP_c+D_b^2P_b D_c^2P_c/n^2]dt.

The notation D_b^2 is operator composition. Every one of the 169 ordered
pairs for each mode is included and b+c-2>-1. For a polynomial sum_j q_j t^j,
its integral with exponent e is exactly
sum_j q_j j!/product_(i=1)^(j+1)(e+i). This beta-moment computation in t
is independent of N4's expansion in w followed by monomial antiderivatives.
Check all 82 exponent groups and the exact complete totals. The same
calculation also checks d_n against T4-470's accepted denominator.

## Pairing groups and their rigorous finite replay

The source serialization is
f_n=r sum_ell w^(ell delta/2)A_(ell,n)(t), delta=1-1/c,
with exact rational functions A. Its positive denominator factors are
(1+s w)^j, s in {99,624,2499,9999}, j a positive integer.
Thus the two pairings use complete grouped integrals

 p_n=(pi/2)sum_e int_0^1 w^e L_e(t)dt,
 b_n=(pi/2)sum_e int_0^1 w^e C_e(t)dt,

where e=ell delta/2+b-3, L_e=sum t A P_b and
C_e=sum t A D_b^2P_b/n^2 at that exponent. Exact numerator powers w^q
are cancelled before integration; e+q>-1 is checked for every group.
The denominator has no zero on [0,1]. No divergent separated term is
assigned analytic continuation. The positive-pole moment soundness and
complete Cartesian source projection are the already accepted production
dependencies. Equal group exponents, vanishing orders, numerator hashes,
factors and projection hashes bind the 650-digit sidecar to both old
complete productions. All 58 mode1 and 73 mode3 groups occur twice,
for a total of 262 complete integral enclosures.

If I_j contains the exact integral, then sum I_j contains their sum
regardless of cancellation. Reparse each decimal ball from the compressed
JSON, sum at sufficient precision, then multiply by a containing pi/2.
Independently bound the sum of absolute input radii by 10^-250 and check
that the signed sum has more than 700 bits of relative accuracy. These
are checked outcomes, not assumptions based on the count of printed
digits. The positive dual and negative cross signs are certified.
The new sum must lie strictly inside the previously saved final 200-digit
pairing ball and agree with the new complete-runtime final enclosure.
This verifies the source-to-pairing composition using only the new archive.

From a containing p interval and exact positive d/pi, compute
|p|/sqrt(pi*(d/pi)); from b and positive a/pi compute b^2/(pi*(a/pi)).
Every saved rational lower floor must be strictly below the appropriate
lower endpoint. Orthogonality of the test modes in the gradient norm gives
H(F)^2>=p_1^2/d_1+p_3^2/d_3. Combining the exact quotient floors and
T4-467's positive lower G0,G1,P2 endpoints gives the same exact square
E2^2=P2^2+2^14G1^2+2^18G0^2+(20/21)2^18H^2 as T4-470.
Its independently certified 007 upper endpoint yields the stated strict
pairwise ordering. No actual H-only or correction-distance ordering follows.

## Conditional use of the cross improvement and scope

Since div Z_n=0 and the two frequencies are orthogonal,
||A_F+t_1 Z_1+t_3 Z_3||2^2=M2+2sum t_n b_n+sum t_n^2 a_n.
An L2 field with divergence F bounds H by its norm. Minimizing each
quadratic gives H(F)^2<=M2-b_1^2/a_1-b_3^2/a_3. Thus an independently
accepted full M2 upper U, including all 160 modes, would give the upper
H(F)^2<U-59664789113139289718803/250000000000000000000000.
This calculation cannot replace the missing U. In particular the omitted
mode energy is not estimated as zero. Independent analytic review of
T4-469 and its positive-pole extension is kept separate from the finite
coefficient and interval acceptance here.

Proofs, source programs for inspection only, compressed numerical inputs,
all source-hash receipts and verification evidence accompany this proof.
Only the finite own checker is executed. The work neither proves a
stationary inverse or existence theorem nor establishes optimality of a
trial basis, an exact H value or an optimal candidate. The Opus5.5
collaboration uses the existing T1/T2 lanes; actual provider identity is
not observable here and no substitute remote model is called.

# Independent density-moment verification of modal Green boundaries

Date: 2026-10-20. Status: CONFIRMED for the selected180 entries and all7810 log-boundary enclosures, source and exact-output audit completed 2026-10-20T15:33:40Z. This verifies the canonical Poisson inverse of the exact modal trial, not its transport residual.

## Exact object and density projection

The exact trial, its common knot endpoints and exact scalar-dependent coefficient are defined in ../modal_repair/PROOF.md. Its input is data_exact/modal_v2.json and its scalar correction is enclosed by the independent certificate in ../modal_repair/evidence/independent_gauss_iv.json. Do not use rounded dependent coefficient strings as definitions.

Write rho(r,theta)=r^3 sum_{j>=0} R_j(log r) sin((2j+1)theta). The finite cosine factor modes a_m give the exact projection

R_j=sum_m P_jm a_m,
P_jm=(1/8) sum_{f in {1+2m,1-2m,3+2m,3-2m}} sign(f) 1_{|f|=2j+1}.

Indeed cos^2(theta)sin(theta)=(sin(theta)+sin(3theta))/4, and 2sin(p theta)cos(q theta)=sin((p+q)theta)+sin((p-q)theta). Repeated frequencies are counted separately. This construction includes every low-mode sign and every endpoint mode, rather than guessing index shifts.

## Density moments and Green identities

For an even angular frequency m=2n, let a_L(r)=r^3 R_{n-1}(log r) and a_U(r)=r^3 R_n(log r). Direct differentiation of the sine series gives the sin(m theta) coefficient of partial_x rho as

f_m=(a_L'-(m-1)a_L/r+a_U'+(m+1)a_U/r)/2.

Set

I_m(r)=r^(-m-1) integral_0^r s^m a_L(s) ds,
J_m(r)=r^(m-1) integral_r^infinity s^(-m) a_U(s) ds.

Integration by parts in the canonical Green formula yields

A_m(r)=r(a_L+a_U)/2-mr I_m,
B_m(r)=mr J_m-r(a_L+a_U)/2,
psi_m=(A_m+B_m)/(2m).

The sign is for the task convention -Delta psi=partial_x rho. The angular radial Laplacian acting on this Green solution is -f_m, so the displayed plus sign is the required one.

The inner boundary term vanishes because a_L,a_U=O(r^3). The outer boundary term r^(1-m)(a_L+a_U) vanishes because k<1 and m>=2. These follow from the exact modal trial's center and far-field bounds. This independent route never differentiates fitted density modes to build f_m, and does not use the numerics lane's exponential primitive subtraction.

## Scaled density recurrences

For t=log r define i_m(t)=exp(-3t)I_m(exp t) and j_m(t)=exp(-3t)J_m(exp t). On a middle polynomial interval [a,b], h=b-a,

i_m(b)=exp(-(m+4)h)i_m(a)
 +integral_0^h exp(-(m+4)v) R_{n-1}(b-v) dv,

j_m(a)=exp((4-m)h)j_m(b)
 +integral_0^h exp((4-m)v)R_n(a+v) dv.

These follow by splitting the defining density integrals at the two endpoints and changing variables. Reversing the first polynomial uses R(b-v), including its odd-power signs. The second uses R(a+v). No growing global exponential primitive is subtracted.

The exact endpoint values are obtained from the finite inner and outer exponential-polynomial formulas. For a projected inner core C+sum D_l exp(2(l+1)tau)+exp(bi tau)sum Ei_l tau^l,

i_m(t_-)=C/(m+4)+sum_l D_l/(m+6+2l)
 +sum_l Ei_l (-1)^l l!/(m+4+bi)^(l+1).

For a projected outer expression sum_q A_q exp(alpha_q tau)+exp(-bo tau)sum Eo_l tau^l,

j_m(t_+)=sum_q A_q/(m-4-alpha_q)
 +sum_l Eo_l l!/(m-4+bo)^(l+1).

Every denominator has the sign required for convergence, checked exactly. The scalar correction z is inserted in the leading outer coefficient and in the six-jet correction before projection; all interval evaluations are uniform over its independently certified enclosure.

Recover the Green boundaries by

A_m(exp t)=exp(4t)[(R_{n-1}(t)+R_n(t))/2-m i_m(t)],
B_m(exp t)=exp(4t)[m j_m(t)-(R_{n-1}(t)+R_n(t))/2].

## Enclosure and artifact comparison

Each selected log boundary is reconstructed exactly from the original rational knots and the exported integer parent grouping. The grouping is checked to cover every original span once in order; each span is partitioned into its declared number of equal rational subintervals. Every exported tb midpoint-radius interval must contain the corresponding exact rational boundary. This checks both the claimed comparison point and full boundary coverage.

Middle spline polynomials are reconstructed by the independently audited exact rational Cox routine. Density projections are exact rational combinations. Polynomial coefficients are converted outward to Arb, and all moments use the scaled Taylor series with proved geometric tails in ../exponential_moments/PROOF.md. The implementation uses 128 Taylor terms and checks |lambda h|<129 on every exact integration interval. A failed hypothesis aborts the run. It does not automatically subdivide these intervals. The scaling avoids subtraction of growing primitives; for m=2 the backward multiplier is exp(2h)>1, so no contraction of accumulated errors is claimed. The original numerics Green arrays are only comparison data; none enters the reconstruction of I_m or J_m.

For selected stream modes and selected boundaries, compare the independent enclosures to the exact dyadic intervals described by A_mid,A_rad and B_mid,B_rad. Containment of a whole independently proved interval is sufficient to confirm that selected exported ball. An overlap alone is weaker and must be reported separately. A failure of containment is not automatically a refutation if the independent enclosure is wider; disjointness is decisive evidence of a disagreement. The full input and source hashes and tested indices must accompany the verdict.

Only the selected finite set is audited by this procedure. No statement about untested array entries, Taylor residual products, global residual norms or an inverse theorem follows.

## Pre-run source checks

The exact modal definition has inner constant delta_(mode,0), hence its density projection is P_(j,0), exactly `ws.get(0)` in the checker. The correction z changes only the leading outer coefficient of cosine mode zero and its dependent outer six-jet; the stored middle spline and inner formula are unchanged. The independently audited `exact_poly` constructs its polynomial variable about `(a+b)/2`, as its Cox factors explicitly use `mid-t_i` plus the polynomial variable. The proved `phi(j,z,N)` is the enclosure of integral_0^1 exp(z v) v^j dv; therefore h^(j+1)phi(j,lambda h,N) is the required monomial moment. These facts address the actual Opus 5.5 pre-run questions. Its warning about a noncontractive m=2 backward step is adopted in the wording above.

## Completed verification record

The run completed at 2026-10-20T15:17:14Z in48.24seconds at320bits. It tested stream indices1,2,3,4,16,64,128,260,261 and log-boundary indices0,147,1414,2761,3925,4102,4211,5622,7038,7809. All180 A/B comparisons were CONTAINED; none was overlap-only or disjoint. All7810 exported abscissae contained their exact rational definitions.

The comparison artifact SHA256 was c2c2e4f73f5ac6ee49fd0052b81700fc88ee68d01a5a526691cf03c2b82c2ef1 before and after the run. A separate exact Fraction checker rechecked all interval containments, index coverage and accepted dependency hashes, with PASS in evidence/output_audit.json. The full calculation and review evidence are preserved; this confirms no untested array entries.

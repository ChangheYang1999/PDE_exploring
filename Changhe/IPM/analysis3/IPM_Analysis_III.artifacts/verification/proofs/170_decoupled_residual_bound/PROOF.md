# A certified residual upper bound in the decoupled family

## Statement and comparison

Let F=(ell X+U[rho]).grad rho-rho be the exact residual of the normalized original-data modal trial. Let Y_old be the strong target of V164, with angular exponent 17/4, inner radial exponent 17/2, and outer radial exponent 5/4. Let Y_a be the target in proof 168, where 18/5<=a<=4, the inner radial exponent is unchanged, and the outer radial exponent is 37/20.

Use the same exact axis/remainder decomposition

 F=p gamma(log r)+u, p=x^2 y,
 u=p cos(theta)^2 Q(log r,theta).

No angular modes are truncated. For each t define the squared angular energy of the old target by

 N_old(t)^2=|gamma(t)|^2
  +integral_0^(2pi)|cos(theta)|^(-1/2)sin(theta)^2 |Q(t,theta)|^2 dtheta.

For the new target the angular power is 8-2a. Since 8-2a>=0>-1/2 and |cos(theta)|<=1,

 N_a(t)^2<=N_old(t)^2.                                  (1)

The radial density changes by the exact factor

 g_new(t)/g_old(t)=1 for t<0, exp(-3t/5) for t>=0.        (2)

Consequently the new norm can be bounded using the full-angular envelope already certified in V164, with only scalar exponential integrations. The comparison is uniform for a in the stated interval. It does not purport to compute the exact new angular norm, and it gives no lower bound.

## Finite intervals

The accepted residual journal partitions [-40,20] into 1860 disjoint intervals [l_j,r_j], with the weight join split at zero. Its separately audited Taylor argument proves on each entire interval

 N_old(t)<=C_j+V_j,

where C_j is the center_norm enclosure and V_j the variation_bound enclosure, including the full angular remainder. Their upper endpoints are exact rationals in the journal. Write M_j for the sum of those upper endpoints. Then (1) gives

 integral_(l_j)^(r_j) N_a(t)^2 g_new(t)dt
   <=M_j^2 exp(b_j l_j) expm1(b_j(r_j-l_j))/b_j,          (3)

where b_j=-1/2 for a negative interval and b_j=123/20 for a positive interval. No integration of a sampled residual is used. The scalar expression in (3) is evaluated with outward Arb enclosures.

## The two infinite ends

The accepted V164 inner tail bound applies unchanged by (1)-(2), including the independent enlargement retained in its final certificate. On t>=20 the factor in (2) is at most exp(-12). Thus

 new_inner_tail<=old_inner_tail,
 new_outer_tail<=exp(-12) old_outer_tail.                (4)

Both old tail bounds cover their entire half-lines, use every angular mode, and come from the same original-data residual. Equations (3)-(4), summed with directed arithmetic, prove the upper bound reported in the evidence below.

## Verification and scope

The checker validates the original NPZ hash, the accepted residual journal and metadata hashes, exact partition endpoints and adjacency, and the V164 final certificate. It independently recomputes all scalar integrals at 384 and 768 bits, checks overlapping enclosures, and retains the exact outward endpoint for their sum. A decimal upper bound is accepted by a rational square comparison. These operations reuse an already verified original-data coefficient certificate; they do not import numerical estimates from another team.

This is a norm bound for the exact normalized trial in the specified low targets. It is not a bound in the high target, a bound for the raw X3 profile, or an inverse estimate. The actual nonlinear smallness condition still requires its high residual norm and the inverse and nonlinear constants.

## Accepted numerical result

The independent scalar recomputation at 384 and 768 bits gives a total squared-norm upper enclosure below (60704/125)^2. Therefore

 ||F||_(Y_a)<485.632 for every 18/5<=a<=4.

The upper enclosure before rounding is approximately 485.631156158809 for the norm. The finite spline contribution to its squared upper bound is approximately 83458.9462, the finite outer contribution is 152377.4237, and the remaining outer half-line contributes at most 1.250013. These displayed components are explanatory approximations; the exact outward endpoints and the rational square comparison are in evidence/check.json.

Verdict: CONFIRMED as a uniform low-target upper bound, derived from the independently verified original-data residual. No positive lower bound in the new target is asserted here.

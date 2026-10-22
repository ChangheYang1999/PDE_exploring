# N8 source coefficient bounds: coverage audit and conditional consequence

Status: OPEN numerical certificate. The exact metadata obstruction and the conditional algebra below are proved. No coefficient supremum is independently accepted here.

## Statement, notation and dependencies

Let P=(p,0), with 8.60006380515688 <= p <= 8.600063805157474. Write B_R(P) for the Euclidean disc. The local source estimate in topic77, with the canonical correction in topic80, has kappa=1687/500 and E <= delta*C_V, where C_V=(417/10) M_V+3 M_rho. The numbers M_V and M_rho must be certified upper bounds for the appropriate second derivative Frobenius norms on all of B_(3delta)(P). Merely bounding a smaller set does not satisfy this hypothesis.

The frozen N8 fine output has delta_max=0.0165, radial cover approximately [8.549454755209684,8.656430245964334], and nevertheless includes result entries delta=0.05,0.1,0.2. These three entries do not have coverage of their stated discs. This rejects their interpretation as complete disc certificates. It does not prove that the numerical upper bounds themselves are false.

If the reported fine C_V < 13.34 is independently proved on B_(3*0.0165)(P), then E < 22011/100000 and kappa-E > 315389/100000. Consequently K_1=1/(kappa-E) < 318/1000. If the full-run C_V < 18.634 is independently proved on B_(3*0.05)(P), then E < 9317/10000, kappa-E > 24423/10000, and K_1 < 41/100.

## Proof of coverage obstruction

For each of the three larger deltas, the point X=P+(delta,0) is strictly inside B_(3delta)(P). Its radius is p+delta. Even for delta=0.05, this is at least 8.65006380515688, which alone does not exceed the declared radial endpoint. Instead take X=P+(2*delta,0), also strictly inside the disc. Its radius is at least 8.70006380515688, greater than 8.656430245964334. The same inequality holds for larger delta. This point is outside the entire radial cover. Angular overinclusion cannot restore missing radii. Hence the reported fine certificate domains cannot cover the larger discs. The exact dyadic comparison in the evidence avoids relying on the displayed rounded approximations.

## Proof of conditional coercivity consequence

Substitute delta=33/2000 and C_V<667/50 into E<=delta*C_V. Their product is 22011/100000. Subtracting this from 1687/500 gives 315389/100000. The exact positive comparison 100000/315389 < 159/500 proves the first bound. For delta=1/20 and C_V<9317/500, the product is 9317/10000 and the remaining margin is 24423/10000. The inequality 10000/24423 < 41/100 proves the second. These are conditional statements, not interval enclosures of the derivatives.

## Additional open arithmetic obligations

The frozen producer takes hk=succ(h_up/K) for Bernstein recentering, but uses the exact Arb value h_up/K for the coordinate-factor cells. The resulting radial subintervals are not identically defined. Its coefficient uncertainties may cover the discrepancy, but this needs a proof for every subinterval; none is supplied by the code comment claiming merely a longer interval. The geometric cell filter uses floating distances and a 1e-6 relative safety allowance. That allowance requires a proved error bound, or an independent interval inclusion audit. The Green anchors, derivative Taylor remainders, Cartesian derivative recursion, all midpoint-radius operations and Frobenius sums also remain to be checked with an independent method.

The producer's module docstring calls its output rigorous. That description is an input claim, not a verifier conclusion. The exact coercivity arithmetic above is useful once the coefficient certificate is complete. There is no decisive endpoint.

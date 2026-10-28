# Numerical upper endpoints from the strict radial coupling

## Statement and source bounds

Use the homogeneous Euclidean Holder seminorm and the diagonal transform R_1^2=T_xx-I/2 on real or complex functions, defined modulo constants by circular principal values. Let U_alpha be the accepted upper endpoint selected as follows:

- Atalpha=1/1000 and1/100, use the exact rational upper endpoint of J_D at its saved rational radiusrho in the V118 rational_cutoffs.json certificate.
- Atalpha=1/20 and1/10, use the V045 exterior-circle upper endpoint in data/circle_composite_upper_n768.json.
- Atalpha=1/5 and99/100, use the interpolated diagonal recombinations accepted in V179.
- Atalpha=3/10,1/2,3/4,9/10, use the diagonal phase interpolation bounds accepted in V177.

The standalone analytic proofs in ../PROOF.md and ../cutoff_plan/PROOF.md propose

    D_alpha <= U_alpha - eta_alpha,

where eta_alpha is eta_cut(alpha,rho) for the first two rows and eta_rad(alpha,1/2) for all other rows. All source bounds in the latter group use a local radius equal to half the increment length. Their positive remainder of mass1/2 is outside the phase interpolation. The cutoff rows instead use the guaranteed surviving measure after perturbation, so their gain includes the explicit lost-density correction.

This numerical statement is conditional on a CONFIRMED analytic acceptance that binds both proofs and their independent cross-read. No numerical endpoint exists until the accompanying acceptance file is written. No transport geometry or plan is optimized or changed in this calculation.

## Independent evaluation and rounding

The coefficient is J=653/288-(63/8)log(4/3). Evaluate each gain as a ball at384 bits, preserving the exact rational exponent and radius. The gain lower endpoint l_alpha yields the valid upper endpoint U_alpha-l_alpha. Round it upward to ten decimal places.

Independently enclose log(4/3) by its positive atanh series, with q=1/7:

    log(4/3)=2 sum_(n>=0) q^(2n+1)/(2n+1).

ForN terms, the omitted tail lies between zero and

    2q^(2N+1)/[(2N+1)(1-q^2)].

The calculation uses256 terms and exact rational arithmetic, with no floating logarithm in this independent coefficient enclosure. The resulting rational J interval must lie inside its384-bit logarithmic enclosure and have positive lower endpoint greater than7/4608. A separate768-bit calculation of the power by exp((alpha-2)log(1+s/2)) verifies that both fresh gain endpoints lie inside the first enclosure. The cutoff density correction rho^4/[512(1-rho)^2] is exact rational arithmetic. Its positivity and the admissible radiusrho<=1/3 are checked before evaluation.

The final upward decimal is checked against the exact rational difference U_alpha-l_alpha. Every input acceptance, source hash, proof and cross-read is bound in the output. The accepted V045 scalar values are inherited with their original source and comparison hashes. This is a new scalar certificate for a proved gain; it does not relabel a numerical observation as an operator theorem.

# Exact leading data of Candidate 007

## Statement

The authoritative Candidate 007 coefficient file has

\[
c=\frac{4076476460239181}{2251799813685248},\quad
\gamma=\frac{2251799813685248}{4076476460239181},\quad
\delta=\frac{1824676646553933}{4076476460239181}.
\]

Its leading density coefficient is the ten-term sine polynomial

\[
f_1(\theta)=\sum_{m\in\{1,3,\ldots,19\}}a_m\sin(m\theta).
\]

The exact rational coefficients are in `data/leading_exact.json`. Rounded values, for identifying the profile only, are:

| m | a_m, rounded |
|---|---:|
| 1 | 18.56782229754644 |
| 3 | 2.107321631475442 |
| 5 | 0.6247347944872613 |
| 7 | 0.1511119117034160 |
| 9 | -0.1016674009550197 |
| 11 | 0.02814322689785034 |
| 13 | 0.002309093254678445 |
| 15 | 0.0003658523972799070 |
| 17 | -0.0008585850168560336 |
| 19 | 0.001896735774558059 |

All ten coefficients are nonzero. The profile has the stated S1 symmetry and is strictly positive for 0 < theta < pi. On the first quadrant it increases to exactly one interior maximum, then decreases to theta = pi/2. Thus it is not monotone on that quadrant. Its first-quadrant L2 norm satisfies

\[
16.5710002630288<\|f_1\|_{L^2(0,\pi/2)}<16.5710002630289.
\]

The extraction is not a verification of Candidate 007 as an exact stationary solution. It supplies leading data for a new formal recursion.

## Extraction from the source

The source JSON describes generators

\[
\chi=\sum A_{m,j,h}\,H_m(x,y)(1+r^2)^{P_j-m}T_h(t),
\quad t=\frac{r^2}{1+r^2},\quad
H_m=r^{2m}\cos(2m\theta),
\]

where 2P_j = 3+gamma-j delta. The two generator types present are T_h(t)=t^h and T_h(t)=t^w P_h(2t-1), with P_h a Legendre polynomial. Both tend to one as r tends to infinity. Since delta > 0, only branch j=0 contributes to the leading potential degree 3+gamma. Its coefficient at cos(2m theta) is therefore the exact sum of the stored rational coefficients with that m and j=0. There are 416 branch-zero generators and ten nonzero leading potential moments.

Applying rho=-d_y Delta chi to this leading homogeneous potential gives the displayed sine polynomial. This differentiation is implemented with exact homogeneous Cartesian operators, without importing a source-project routine. The source SHA256 equals the manifest value

`ed4962328d88fa141fd1a08276a9bcbece0c07b4dcda1aa8a49d493f26053d21`.

The manifest and sector-table hashes are recorded in the extracted JSON. The rounded density coefficients agree with the sector table, but the sector table's floating-point coefficients are not used as inputs.

## Positivity

For any integer m >= 1 and 0 <= theta <= pi,

\[
|\sin(m\theta)|\le m\sin\theta.
\]

One proof writes sin(m theta)/sin(theta) as the sum of m complex numbers of modulus one, using the geometric-series identity; the endpoint values follow by continuity. Hence

\[
f_1(\theta)\ge
\left(a_1-\sum_{m\ge3}m|a_m|\right)\sin\theta.
\]

Exact rational arithmetic on the extracted coefficients gives the parenthesized quantity greater than 27/4. Its value rounded to identify the margin is 6.7536780210151885. This proves strict positivity on the open upper semicircle. Oddness under y reflection gives the sign on the lower semicircle.

## Monotonicity

Put t=sin^2(theta). The elementary expansion of the imaginary part of (cos(theta)+i sin(theta))^m gives

\[
\frac{\sin(m\theta)}{\sin\theta}
=\sum_{j=0}^{(m-1)/2}(-1)^j\binom{m}{2j+1}
(1-t)^{(m-1)/2-j}t^j.
\]

Thus f_1(theta)=sin(theta) P(t), for an explicitly stored rational polynomial P of degree nine, and

\[
f_1'(\theta)=\cos\theta\,Q(t),\qquad Q=P+2tP'.
\]

The exact Sturm sequence of Q has five sign variations at t=0 and four at t=1, and neither endpoint is a root. It follows that Q has exactly one distinct root in (0,1). Moreover Q(0)>0 and Q(1)<0. Therefore f_1 increases and then decreases on (0,pi/2), with precisely one interior maximum. The exact rational isolating bracket for its sin-squared coordinate is stored in `verification/properties.json`; that coordinate is approximately 0.9791431770159187. As a simpler independent obstruction to monotonicity, exact arithmetic gives

\[
4.4495<f_1''(\pi/2)<4.4496,
\]

while f_1'(0)>0. The endpoint theta=pi/2 is a strict local minimum in the reflected profile.

The Sturm conclusion uses the standard exact real-polynomial root-counting theorem. The retained code computes the signed remainder sequence in rational arithmetic; the JSON records the endpoint signs and polynomial coefficients for reproduction. This is not a proof-assistant certificate.

## Norm enclosure

Orthogonality of distinct odd sine functions on the first quadrant yields

\[
\|f_1\|_{L^2(0,\pi/2)}^2=\frac\pi4\sum_m a_m^2.
\]

The rational factor sum(a_m^2)/4 is retained exactly. Arb evaluation at 256 bits encloses its product with pi and the positive square root strictly between the two displayed decimal rationals. This is a validated ball-arithmetic enclosure, not an estimate from angular sampling.

## Dependencies and verification

The source generator definition, exact rational parsing, the homogeneous differentiation identities in `../01_recurrence/PROOF.md`, elementary trigonometry, Sturm's theorem and the Arb implementation are the dependencies. `../../code/cartesian_verify.py` reproduces the extraction and verifies the new stationary recursion through order five by returning to the potential and its Cartesian derivatives. `../../code/candidate_properties.py` reproduces the sign, root count and norm certificate. None of these finite checks decides convergence of the infinite recursion.

## All eight stored pure branches

The independent exact Cartesian recursion was extended through N=8. For each source branch j=0,...,7, sum its generator coefficients at each angular mode; both generator families tend to one in their compactified radial variable. This is its pure homogeneous potential coefficient at q_{j+1}=4-(j+1)delta. Direct Cartesian differentiation gives the source pure density coefficient, which agrees exactly with the newly computed f_{j+1} in every Fourier mode.

The check is recorded in `verification/source_branches_N8.json`, with exact coefficients and source/implementation hashes. At these eight nonexceptional exponents the pure potential map is injective, so equality of the density also gives equality of the pure potential and stream branches. This verifies the stored pure branch recurrence through order eight. The source generators additionally contain r^(-2) corrections; neither this check nor the leading extraction proves that the full Candidate 007 function is an exact stationary solution.

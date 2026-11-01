# Explicit three-mode resonant responses at c=3

Status: PROVED. The independent Cartesian certificates and the theory part's separate Fourier and rational computations agree. The independent review dated 2026-10-31T11:06Z is recorded in V284. All conclusions retain the exact hypotheses and scope stated below.

## Statement and exact definition

Let c=3, delta=2/3 and f_1=sin(theta)+b sin(3theta)+tau sin(5theta), with real or complex parameters b,tau. Define f_2,f_3,g_1,g_2 by the nonresonant pure recurrence. For n=3k, k>=2, put e=sin((2k-2)theta) at stream radial power p_n+1. Define

    phi_1=T(e,f_1)/(2n),
    phi_2=[T(e,f_2)+T(g_1,phi_1)+T(Pi_(n+1)phi_1,f_1)]/[2(n+1)],
    phi_3=[T(e,f_3)+T(g_1,phi_2)+T(Pi_(n+2)phi_2,f_1)
                    +T(g_2,phi_1)+T(Pi_(n+1)phi_1,f_2)]/[2(n+2)].

Here T is the signed Cartesian advection of119, equivalently the angular advection with the displayed radial orders. Let sigma_k be the coefficient of sin((2k-1)theta) in phi_3. These formulas are valid whether or not O6(b,tau)=0.

The computation will retain exact bivariate polynomials for2<=k<=14 and one rational function in k with bivariate polynomial coefficients valid for every integer k>=10. It also gives an exact cubic limiting polynomial sigma_infinity(b,tau). Its restriction tau=0 must agree with119. Its resultant with the exact O6 from125 must be a nonzero polynomial; any real zero of sigma_infinity on the compatibility curve projects to a real root of that resultant. Resultant roots alone do not identify a real common root or its connected branch.

## Why the symbolic formula is valid

The signed Laurent Cartesian representation has independent monomial labels (a,h), representing frequency a k+h. The unit harmonic has labels (2,-2) and(-2,2). Multiplication adds these labels; Cartesian differentiation shifts h by1 and multiplies by the corresponding affine exponent. The three response equations contain exactly one varying harmonic, so their nonzero frequency slopes remain2 or-2.

For B=6, the successive positive-branch frequency windows around m=2k-2 have offsets at most5,6,11,12,17 for phi1, its Poisson inverse, phi2, its Poisson inverse, and phi3 respectively. At k>=10, m>=18, so these windows never meet zero or the opposite branch. Every signed-label operation then specializes to the physical Fourier operation with no folding ambiguity. The two intermediate orders3k+1 and3k+2 are nonresonant. Their factored Poisson divisors and all stationary divisors are nonzero. The symbolic algebra therefore proves one rational formula for all such integer k, not merely for sampled k. Direct comparisons at k10through14 check implementation consistency.

Each response is of degree at most3 in(b,tau), by the homogeneous response proof. The uniform cubic bound in122 implies that every rational coefficient in k is bounded for large k. Its numerator degree is therefore at most its denominator degree. Dividing leading coefficients, or taking zero when the numerator degree is smaller, gives its exact limit. This proves coefficientwise and locally uniform convergence to the retained cubic polynomial. Substitution tau=0 supplies a separate exact comparison with the earlier two-mode calculation.

Finally,135 proves that the normalized compatibility polynomial is irreducible over Q[b,tau], while sigma_infinity is nonzero and has lower degree. They are therefore coprime as univariate polynomials in b over Q(tau), so their resultant is nonzero. At any common zero the resultant vanishes. As O6 is monic up to a nonzero constant in b, the fiber has at most6 points. Thus only finitely many compatibility points have zero limiting response, without interpreting every real projected root as an actual real profile.

Dependencies:119for exact response and Cartesian calculus,122for the uniform cubic bound,125for the exact three-mode compatibility polynomial,129for uniform limiting responses, and135for the independent algebraic genericity argument. No infinite convergence claim is inferred from finite numerical response samples.

## Completed exact calculation

The limiting response is

    -(254100*b**3 + 8113875*b**2*tau + 22818180*b**2 - 3679500*b*tau**2 - 12142680*b*tau - 9909900*b + 8130900*tau**2 + 1353264*tau + 1063832)/439084800

The exact degree18 resultant has two real roots, approximately -3.0164889488602338 and98.60390338118108. Their exact isolating intervals are retained. These are candidate projected parameters only. In particular, no compatible profile with -3<=tau<=98 has a zero limiting response. Direct responses at k10through14 and the tau0 specialization agree exactly with the symbolic formula.

## Independent determinant and real-root certificate

V272 checks the stored resultant without using the original resultant or Sturm implementation. Clear denominators in O and sigma_infinity by d_O=6436703590689275904000000 and d_S=439084800. Their b-degrees are6and3 and total degrees at most6and3. The Sylvester determinant has3rows drawn from O and6from S. In any nonzero determinant term, the sum of selected b-powers is18: the selected column powers minus the row shifts give this fixed total. Each coefficient of b^i has tau-degree at most6-i or3-i, respectively. Thus every determinant term has tau-degree at most3*6+6*3-18=18. This proves the resultant degree bound.

A polynomial of degree at most18 is determined by19distinct values. Integer Bareiss determinants at tau=0,...,18 agree exactly with d_O^3 d_S^6 times the retained resultant. This proves the entire identity. A separate primitive rational-remainder Sturm sequence has variations10at negative infinity and8at positive infinity, one variation drop on each recorded isolating interval, and equal variations9at-3and98. Both endpoints are nonzeros. It proves exactly two simple real projected roots and none in[-3,98]. The determinant samples and complete integer Sturm sequence are retained in JSON. Separate finite-field arithmetic also verifies the P6mod19 and P10mod11 irreducibility inputs used in135.

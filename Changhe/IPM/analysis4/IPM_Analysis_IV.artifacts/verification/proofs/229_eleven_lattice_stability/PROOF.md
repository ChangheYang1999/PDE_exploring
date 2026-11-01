# Stability within a high-harmonic lattice

Status: PROVED. The conditional stability theorem was independently reviewed at17:14Z and admitted in V480; its center hypothesis was established in V484, and the resulting open family is admitted in V485.

## Statement

Fix delta=4/9 and c=9/5. Let J be a finite set of positive odd integers containing1, and define

    f_1(theta;a)=sum_(j in J) a_j sin(11j theta),
    a^0_1=1, a^0_j=0 for j!=1.

Assume that the single-eleventh-harmonic center satisfies

    inf_(k>=1)|sigma_k(a^0)|>0,

where sigma_k is the response of the order9(k+1) compatibility coefficient to the free stream harmonic at order9k. Then an open neighborhood U_J of a^0 in R^J and a finite R_J exist such that every a in U_J has a unique compatible pure density and stream series, convergent with every appropriately weighted derivative on r>=R_J. The series has a common potential with the same convergence property, consisting of the pure-power series and one finite logarithmic correction at order9. This logarithmic coefficient is nonzero throughout a possibly smaller U_J. The profiles and solutions are nontrivial.

The coefficients depend real analytically on a, and the sums do so on every slightly larger strict exterior. No explicit size for U_J or R_J is asserted. The neighborhood is open in this fixed finite-dimensional lattice subspace, not in the full space of odd sine profiles. Delta is fixed.

## First compatibility is an identity on this subspace

Write Lambda={plus or minus11j : j in J}. Each element of Lambda is11 times an odd integer. The signed-support induction of197 and201 gives

    supp f_r subset r Lambda+E_(r-1), 1<=r<=9,

where r Lambda is the r-fold sumset and E_m={-m,-m+2,...,m}. There are no earlier stream resonances. A sum of nine odd integers is odd, hence nonzero; every element of9 Lambda has absolute value at least11. Since E_8 has absolute value at most8, every possible frequency of f_9 has absolute value at least3. Its frequency-one coefficient therefore vanishes identically for every real or complex a. This is exactly the first compatibility condition.

In particular, changing a_j within this subspace does not require solving an additional compatibility equation. The calculation uses an upper bound on support, not an inference from a numerically small coefficient.

## A uniform response bound in a neighborhood

Set B=11 max J+1, a fixed even integer. Before the first resonance each low coefficient is a polynomial in a, because only fixed nonzero rational divisors occur. Each sigma_k(a) is consequently a homogeneous polynomial of degree9. Topic144 proves that these polynomials converge locally uniformly, also for complex a, to the polynomial sigma_infinity(a). This conclusion is independent of any normalization of the frequency-one coefficient.

Let c0=inf_k|sigma_k(a^0)|>0. Taking the limit gives |sigma_infinity(a^0)|>=c0. First choose a small closed complex polydisk P about a^0 on which |sigma_infinity(a)|>=3c0/4. Local uniform convergence supplies K such that

    |sigma_k(a)-sigma_infinity(a)|<c0/4

for every a in P and every k>=K. Thus all tail responses have absolute value at least c0/2. Shrink P to control the finitely many continuous responses with k<K, each nonzero at a^0, by the same c0/2 lower bound. This proves

    inf_(a in P,k>=1)|sigma_k(a)|>=c0/2.

This argument needs both the nonzero limit and the finite nonzero responses. It would not be justified by continuity of each response separately.

## Uniform convergence and parameter dependence

For each a in P, tune the harmonics in order by H_(9k)=-R_k/sigma_k(a). The affine response identity and the support compatibility just proved give the unique compatible sequence. Since every denominator is nonzero on P, all its coefficients are holomorphic functions of a.

The leading Fourier norm is uniformly bounded on P, its bandwidth is at most B, and the response bound is uniform. Apply the scalar majorant of145 with these common bounds. The same nonnegative majorant then controls the density, stream and potential for every a in P. Choose an exterior radius strictly beyond its geometric threshold. Polynomial factors from each fixed derivative are absorbed by this strict geometric ratio, so every weighted derivative converges uniformly on the closed exterior. Increasing the radius once gives one R_J valid for all derivative orders, with a derivative-dependent multiplicative constant.

Uniform convergence on compact parameter polydisks and the common strict exterior proves holomorphic dependence of the sums on the complexified parameters. Restriction to real parameters proves real analytic dependence. The common potential and termwise identities give the stationary IPM equation there by145. Shrinking the real neighborhood to a_1>1/2 makes the leading profile and hence the solution nonzero.

## The finite logarithm persists

At order9 the density exponent is-3 and the potential exponent is zero. Topic228 gives the logarithmic coefficient

    lambda(a)=beta_pure(a)-H_9(a),

where beta_pure is the stream amplitude forced by the pure degree-zero potential. The finite back substitution for beta_pure is linear in f_9 and hence polynomial in a; H_9 is holomorphic on P. Thus lambda is continuous there. The exact center calculation in36 and228 gives lambda(a^0)>0. After shrinking U_J again, lambda(a)>0 throughout it. A constant gauge cannot remove this term.

For delta=4/9 the general common-potential reconstruction in145 has only this finite logarithmic correction; later resonant harmonics have pure potential representatives. The summed potential therefore has the asserted form.

## Dependencies and scope

This is a local stability consequence of the proved support and response-limit theorems197,201,144 and the conditional convergence theorem145. It does not use the irreducibility or frequency-one normalization hypotheses of147. The extra hypothesis at the center is precisely the all-integer certificate being checked in227. No neighborhood in delta, no genericity in the ambient profile space, and no whole-plane stationary extension is claimed.

## Discharged center hypothesis

Topic227 proves inf_k |sigma_k(a^0)|>2^-29 by a complete integer-response certificate and independent replay. Thus the open family stated above exists unconditionally with respect to the center hypothesis. The neighborhood size and common family radius remain qualitative; the explicit center bound alone is not asserted for the whole neighborhood.

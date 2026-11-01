# Exact resonances, compatibility and explicit obstructions

## Statements

Let c>1, delta=1-1/c, p_n=1-n delta, and use the S1 Fourier spaces and pure-power recursion of the prompt.

1. A stream Poisson resonance at order n and sine frequency 2j occurs precisely when n delta=2(j+1), j>=1. It is compatible precisely when the coefficient of sin((2j-1)theta) in f_n is zero. If compatible, the resonant stream coefficient is free.
2. If delta=A/B is reduced and 0<A<B, put d=gcd(A,2), n_0=2B/d and r=A/d. The first stream resonance is at n_0 if r>=2, and at 2n_0 if r=1. The first even-exponent potential exception occurs at n_0; it can be earlier than the first stream resonance when r=1.
3. For c=9/5 and f_1=a sin(theta), a real and nonzero, the uniquely defined nonresonant recursion through order eight has an incompatible Poisson equation at order nine. There is no all-order pure density/stream series of the stipulated form with these leading data.
4. For c=2 and f_1=a sin(theta), a real and nonzero, the density/stream recursion through order seven has an incompatible Poisson equation at order eight. Already at order four its density cannot be produced by a smooth pure homogeneous potential of degree two. Thus a pure potential series fails earlier.

These are obstructions to the specified pure ansatz. They do not exclude an expansion with logarithms or added exponent channels, nor prove universal divergence.

## Resonance and arithmetic location

The stream denominator is 4j^2-(2-n delta)^2. Since n delta>0, the branch 2-n delta=2j is impossible for j>=1. The other branch gives n delta=2(j+1). At that exponent the numerator forcing at frequency 2j is

\[
\tfrac12[(p_n-2j+1)a_{n,j-1}+(p_n+2j+1)a_{n,j}]
=-2j a_{n,j-1}.
\]

The periodic Fourier equation therefore has a solution if and only if a_(n,j-1)=0. Its kernel is the one-dimensional sine mode sin(2j theta).

For rational delta=A/B in lowest terms, n delta is an even integer exactly when n is a multiple of 2B/gcd(A,2). At the first such multiple n_0, its value is 2r. The stream condition requires this even integer to be at least four, which gives the stated formula. The potential map is already exceptional when n delta=2; see `../01_recurrence/PROOF.md`.

For the exact stored Candidate 007 parameter this gives

\[
n_{\rm first}=8152952920478362,\qquad
j_{\rm first}=1824676646553932.
\]

The stream frequency is 3649353293107864, and compatibility tests density frequency 3649353293107863. This is only the exact arithmetic location. No coefficient at this enormous order has been computed. In particular neither compatibility nor incompatibility for the Candidate 007 leading data is inferred from the rational denominator alone.

## The c=9/5 obstruction

Here delta=4/9. Every stream and pure-potential inverse through order eight is nonsingular on its finite Fourier support. Starting from f_1=sin(theta), exact rational Cartesian differentiation and ordered multiplication determine these orders uniquely. At order nine, p_9=-3 and the stream frequency 2 is resonant. The forcing coefficient in d_x(r^(p_9) f_9), after removing its radial factor, is exactly

\[
h_{9,1}=
-\frac{37109215993375012065093034946875}
{443877619295577935692260192337640030208}\ne0.
\]

The complete exact f_9 polynomial and the preceding exact coefficients are retained in `verification/exact_probes.json` and `../01_recurrence/verification/single_mode_c9_5_N8.json`. The computation follows this finite proof: reconstruct each of the first eight potentials, differentiate it to obtain the two Cartesian velocity components, form the sum of u_i dot grad(rho_j) for i+j=9, divide by 8(c-1), then apply d_x and inspect sine frequency 2. Every operation is an addition, multiplication or division of exact rationals, with the nonzero divisors recorded in the recursion. The displayed rational is nonzero, so the resonant Fourier equation 0*b=h has no solution.

For f_1=a sin(theta), homogeneity of the nonresonant recursion multiplies f_n by a^n. The obstruction becomes a^9 h_(9,1), still nonzero for every real a!=0. This extends the finite certificate to the stated one-parameter family.

## The c=2 obstruction and the earlier potential exception

Here delta=1/2. The stream equations are nonsingular through order seven, although the pure-potential map is singular at order four. Computing through the stream route gives at order eight, p_8=-3,

\[
h_{8,1}=-\frac{126709539517}{484849833302016000}\ne0.
\]

The same finite rational procedure as above proves incompatibility; the exact density/stream polynomials through seven and the order-eight forcing are in `verification/exact_probes.json`.

At order four, p_4=-1, exact evaluation gives

\[
f_4(\pi/2)=\frac{359}{401310}\ne0
\]

for unit leading amplitude. For any smooth even potential coefficient C, a pure chi=r^2 C(theta) has Delta chi=H(theta), so

\[
-\partial_y\Delta\chi=-r^{-1}\cos\theta\,H'(\theta).
\]

Its density coefficient vanishes at theta=pi/2. Hence the computed f_4 cannot come from such a pure potential, even if infinitely many angular modes are permitted in C. A logarithmic potential channel is required if one is to continue representing this density/stream pair by a potential.

For nonzero leading amplitude a, the two nonzero quantities are multiplied by a^8 and a^4 respectively. Neither obstruction is removed by choosing a smaller nonzero amplitude.

## Logarithmic repair and limits of the conclusion

At a failed resonance, a term proportional to r^(-2j) log(r) sin(2j theta) solves the forced Poisson equation. Its coefficient is h/(4j), as checked in `../01_recurrence/PROOF.md`. Subsequent nonlinear interactions may generate further powers of log(r). The pure recurrence does not describe those terms. No all-order convergence or obstruction theorem for that generalized expansion is proved here.

## Dependencies and verification

The formal identities in `../01_recurrence/PROOF.md`, rational arithmetic and the elementary nonvanishing of the displayed numerators are the dependencies. The finite certificates are reproduced by `../../code/resonance_probes.py` using the independent Cartesian implementation. Source hashes and real execution dates are retained in the output. No theorem-prover formalization or numerical extrapolation is used.

## Additional independently recomputed obstructions

The same exact Cartesian algorithm was run separately on five further reported cases. The Candidate profile below is exactly the independently extracted leading density in topic 02; only its parameter is changed. Every resonant coefficient and forcing agrees exactly with the numerical experiments' retained rational report. The displayed decimals are descriptive, while the nonzero verdict uses the retained exact numerator.

| Leading profile | c | First stream order | Resonant j | kappa, approximately |
|---|---:|---:|---:|---:|
| Extracted Candidate 007 | 5/3 | 10 | 1 | 31343.40056048673 |
| Extracted Candidate 007 | 9/5 | 9 | 1 | -859.6172263959526 |
| sin(theta) | 20/11 | 40 | 8 | -2.381673640372098e-21 |
| sin(theta) | 5/3 | 10 | 1 | -1.1701076840965914e-7 |
| sin(theta)+sin(3theta)/2 | 5/3 | 10 | 1 | -0.0059636256002700535 |

Here `kappa` is the coefficient of `sin((2j-1)theta)` in the density at the first stream resonance, and the Poisson forcing is exactly `-2j*kappa`. All five values are nonzero, so each corresponding pure density/stream ansatz is obstructed at the indicated order. At `c=5/3` the earlier potential exception at order five does not prevent defining the pure density/stream recursion up to its first stream resonance; it does mean that a compatible potential already needs logarithms.

Executable source: `../../code/first_resonance_audit.py`. The complete exact density/stream prefixes, final density, source snapshot, input identity check and hashes are in `verification/independent_first_resonances/`. Each listed nonzero leading amplitude can also be scaled by any nonzero real factor, multiplying its first obstruction by that factor to the stated order. This does not prove density of incompatible rational parameters.

# Analytic leading profiles and the exact topology of stability

## Statement

Let 0<delta<1, c=1/(1-delta), and assume that alpha=delta/2 has finite Brjuno sum Bcal, defined in the preceding topic. For sigma>=0 let A_sigma be the Wiener space with norm

\[
\|h\|_\sigma=\sum_{m\in\mathbb Z}|\widehat h(m)|e^{\sigma|m|}.
\]

Let sigma_0>0 and let f_1 be a nonzero S1 sine series with F=||f_1||_(sigma_0)<infinity. With lambda_delta as in the preceding topic, define

\[
K'=\frac{2e^{\sigma_0}(1+\sigma_0)\lambda_\delta}{c-1},
\qquad A'=8K'e^{2\mathcal B}F/\delta.
\]

Then the pure stationary recursion and its original potential reconstruction are defined as analytic angular functions at every order. For n>=1 and 0<=sigma<sigma_0,

\[
\frac{n\|f_n\|_\sigma}{d_n}
 \le\frac{A'^n}{8K'(\sigma_0-\sigma)^{n-1}}.
\tag{1}
\]

For every R>(A'/sigma_0)^(1/delta), the density, stream and potential series converge absolutely and uniformly on r>=R, with all fixed Cartesian derivatives in their natural radial weights. Their sums form a nonzero real-analytic exterior solution of the original stationary potential equation.

For fixed delta, bounded sets of data in A_(sigma_0) have a common exterior radius, and the solution depends real analytically on the data there. The coefficient map f_1 -> f_n is a continuous homogeneous polynomial of degree n from A_(sigma_0) to every smaller-strip space A_sigma, sigma<sigma_0. The smaller-strip codomain is part of the statement. No assertion that f_n belongs to the original endpoint space A_(sigma_0) is needed.

On a compact interval [delta_-,delta_+] in (0,1), with a common upper bound on Bcal(delta/2), the radius may be chosen uniformly for bounded data. With the leading radial powers factored out, the series and each fixed weighted derivative depend continuously on delta and the data on that restricted parameter set. This is relative continuity, not a claim of an open interval of admissible exponents.

## The derivative estimate with shrinking strip

Suppose an analytic angular function h satisfies

\[
\|h\|_{\sigma'}\le\nu(\sigma_0-\sigma')^{-k}
\quad(0\le\sigma'<\sigma_0),
\]

where k is a nonnegative integer. Let s=sigma_0-sigma. For epsilon>0 with epsilon<s,

\[
\|h'\|_\sigma\le\frac1{e\epsilon}\|h\|_{\sigma+\epsilon},
\]

because |m|exp(-epsilon |m|)<=1/(e epsilon). If k>=1, set epsilon=s/(k+1). Then

\[
\|h'\|_\sigma\le
 \frac{k+1}{e}s^{-k-1}(1+1/k)^k\nu
 \le(k+1)s^{-k-1}\nu.
\tag{2}
\]

For k=0, let epsilon increase to s. This gives the still stronger bound nu/(e s), hence (2). Thus the endpoint k=0 does not require substituting into an undefined expression (1+1/k)^k.

Set

\[
\nu_n=\sup_{0\le\sigma<\sigma_0}
 (\sigma_0-\sigma)^{n-1}\|f_n\|_\sigma.
\]

In particular nu_1=F by monotone convergence of the nonnegative Fourier-norm sum. Inductively, (2) gives ||f_j'||_sigma<=j nu_j s^(-j). The stream estimate from the preceding topic gives

\[
\max(|P_i|\|g_i\|_\sigma,\|g_i'\|_\sigma)
 \le e^{\sigma_0}\lambda_\delta\frac i{d_i}
 \nu_i s^{-(i-1)}.
\]

Since |p_j|<=j, the two ordered nonlinear terms are bounded together by

\[
e^{\sigma_0}\lambda_\delta\frac{ij}{d_i}
 \nu_i\nu_j(1+s)s^{-(n-1)}.
\]

Here the derivative term has power s^(-(n-1)), and the radial-exponent term has power s^(-(n-2)); retaining the latter factor s gives the displayed 1+s. Since s<=sigma_0,

\[
(n-1)(c-1)\nu_n\le
 e^{\sigma_0}(1+\sigma_0)\lambda_\delta
 \sum_{i+j=n}\frac{ij}{d_i}\nu_i\nu_j.
\]

Thus Z_n=n nu_n/d_n obeys the same scalar tree recurrence as before, with K replaced by K'. The audited tree product estimate proves Z_n<=A'^n/(8K'), which is (1).

## Completing the infinite-angular potential inverse

The density-to-Laplacian equations are, with x=(n delta-2)/2>-1,

\[
a_0=2x d_0+(1-x)d_1,
\qquad a_m=(m+x)d_m+(m+1-x)d_{m+1}\quad(m\ge1).
\tag{3}
\]

For irrational delta, x is not zero and q_n=4-n delta is not an even integer. The decaying solution of (3) has

\[
d_m=\sum_{k=m}^{\infty}
 \frac{(-1)^{k-m}a_k}{k+x}
 \prod_{l=m}^{k-1}\frac{l+1-x}{l+x}
\quad(m\ge1),
\tag{4}
\]

and d_0=(a_0-(1-x)d_1)/(2x).

First consider n delta>=3, so x>=1/2. Each absolute product in (4) is at most one. The proof of the potential estimate in the preceding topic extends to any analytic input: for sigma>=0,

\[
e^{2m\sigma}|d_m|
 \le\frac{\|f_n\|_\sigma}{m+x}\quad(m\ge1),
\qquad |d_0|\le3\|f_n\|_\sigma.
\]

The same summable Laplacian denominators therefore give

\[
\|C_n\|_\sigma\le
 (3/|4-n\delta|+1)\|f_n\|_\sigma/d_n.
\tag{5}
\]

This is uniform in the angular bandwidth, so finite Fourier support is unnecessary here.

It remains to justify the finitely many orders with -1<x<1/2. Set h=1-2x, so 0<h<3. The product in (4) has positive factors 1+h/(l+x). For l>=2, l+x>l-1. The first factor, if present, is (2-x)/(1+x), finite because x>-1. Consequently

\[
\prod_{l=m}^{k-1}\left|\frac{l+1-x}{l+x}\right|
 \le C_x k^3,
\quad C_x=e^3\max(1,(2-x)/(1+x)).
\tag{6}
\]

This follows by taking logarithms, using log(1+t)<=t and the elementary bound on the harmonic sum; an empty product is one. Also k+x>=min(1,1+x)k. Thus

\[
|d_m|\le C_x'\sum_{k\ge m}k^2|a_k|.
\tag{7}
\]

For 0<=sigma<sigma'<sigma_0, summing (7) gives

\[
\sum_{m\ge1}e^{2m\sigma}|d_m|
 \le C_x'\sum_{k\ge1}k^3e^{2k\sigma}|a_k|
 \le C_{x,\sigma'-\sigma}\|f_n\|_{\sigma'}<\infty.
\tag{8}
\]

The last constant is finite because k^3 exp(-2k(sigma'-sigma)) is bounded. This completes the polynomial-loss argument that was only sketched in the theory part report. Equation (4) converges absolutely, solves (3) by shifting the sum, and its terminal remainder tends to zero because polynomial factors are dominated by the analytic decay.

Now set c_m=d_m/(q_n^2-4m^2). At each fixed n the reciprocal denominators are bounded in m, since none vanishes and their magnitudes grow quadratically. Thus (8) gives C_n in every strip smaller than sigma_0. Termwise angular differentiation in a smaller strip verifies rho_n=-partial_y Delta chi_n. The stream chi_(n,xy) solves the same angular Poisson equation as g_n, and the irrationality assumption makes that solution unique. Hence it equals g_n. No independent stream coefficient has been introduced.

Uniqueness of the analytic potential also follows from the homogeneous equation. If partial_y Delta chi_n=0, then Delta chi_n is an even homogeneous function of x alone, hence proportional to |x|^(q_n-2). Since q_n-2 is not an integer, this cannot be smooth through x=0 unless it is zero. The remaining angular Laplacian has no kernel because q_n is not an even integer.

## Series convergence and the original equation

Choose R with A'R^(-delta)<sigma_0, and then choose a positive strip width sigma_1 such that

\[
A'R^{-\delta}<\sigma_0-\sigma_1.
\]

Bound (1) gives a strict geometric series in A'R^(-delta)/(sigma_0-sigma_1). Equations (3) of the preceding topic and (5) bound g_n and C_n by the same geometric rate, up to fixed polynomial factors and constants. The finitely many early potential orders already belong to A_(sigma_1) by (8), choosing an intermediate strip for their inputs.

Every fixed theta derivative is bounded in a smaller strip by its Fourier multiplier and the strip margin. Radial derivatives produce fixed polynomials in p_n, P_n or q_n and thus in n. Each Cartesian derivative is a finite combination of radial and angular derivatives with the corresponding power of r^(-1). The resulting weighted series remain summable. The same argument provides complex neighborhoods in z and theta, hence real analyticity in (x,y) away from the origin.

The identities linking chi, rho and psi pass to their sums. The stationary double series is absolutely summable and its coefficient of each r^(p_n) vanishes by the recurrence. The solution is nonzero because r^(-gamma)rho tends to f_1 at infinity.

## Stability in the leading profile

For fixed delta, the order-n map is obtained by composing fixed linear Poisson inverses, derivatives and products, so it is homogeneous of degree n. For any fixed n and sigma<sigma_0, insert finitely many intermediate strips between sigma and sigma_0; the derivative bounds show continuity from A_(sigma_0) to A_sigma. The map extends to a continuous complex homogeneous polynomial on the complexified S1 space.

For data of norm at most M, replace F by M in A'. The estimates then give locally uniform absolute convergence of these polynomials on every common exterior domain with a strict radius margin. Their sum is holomorphic in the complexified data, and its real restriction is real analytic. The same applies to each fixed weighted derivative. This assertion concerns a fixed strip decrease. It does not claim continuity into the original endpoint strip without derivative loss.

## Relative stability in the exponent

Fix 0<delta_-<=delta_+<1 and B_*<infinity, and restrict to

\[
D_{B_*}=\{\delta\in[\delta_-,\delta_+]:
 \delta/2\text{ irrational},\ \mathcal B(\delta/2)\le B_*\}.
\]

The constants lambda_delta, K' and A'(M) are bounded on this set. A common R can be chosen larger than one and with

\[
\sup_{\delta\in D_{B_*}}A'(M,\delta)R^{-\delta}<\sigma_0.
\]

For each fixed order n, all necessary multipliers vary continuously near any irrational delta. The finite-order coefficient map is therefore continuous into a smaller strip. For infinite Fourier inputs it is generally a convergent sum of rational multiplier expressions; it should not be described literally as a single rational function of delta.

There is also a uniform bound away from the finite-order resonances on D_(B_*). Indeed a binary tree with n leaves includes the root factor 1/d_n, and all its other factors are at least one. The tree product estimate gives

\[
d_n\ge2^{-(n-1)}e^{-2nB_*}.
\tag{9}
\]

The finitely many early potential inverses in (8) thus have uniform bounds on this parameter set. The later bound (5) is also uniform: only finitely many n can have |4-n delta|<1, and (9) controls those cases. The Weierstrass majorant then gives continuity of the weighted infinite sums and their fixed derivatives, uniformly on r>=R.

For the radial weights, write each weighted series in powers of r^(-delta). As delta varies on [delta_-,delta_+], each fixed term is uniformly continuous on r>=R: derivatives with respect to delta introduce log(r) r^(-k delta), bounded there for k>0, while the k=0 leading term is constant in r. Derivative weights add only continuous polynomial factors. This verifies the claimed uniform radial topology.

## Why the arithmetic class has full measure

This fact can be proved with the estimates already available. Fix tau>1. For each n, the set in (0,1) where dist(n delta,Z)<n^(-tau) has measure at most 2(n+1)n^(-tau-1). The sum is finite. The measure of the union from n>=N therefore tends to zero as N tends to infinity. It follows that for almost every irrational delta there is kappa>0 such that

\[
\operatorname{dist}(n\delta,\mathbb Z)\ge\kappa n^{-\tau}
\quad\text{for all }n\ge1.
\]

In particular ||n delta/2||>=kappa/(2n^tau). The convergent error bound ||q_k alpha||<1/q_(k+1) implies

\[
q_{k+1}<2\kappa^{-1}q_k^\tau.
\]

Since q_(k+2)>=2q_k, the series sum (1+log q_k)/q_k is finite. Hence Bcal(alpha)<infinity almost everywhere. The Brjuno sum is measurable: its finite partial sums are measurable functions of the continued-fraction digits, and the full sum is their increasing limit. Consequently the measure of the complement of D_(B_*) in a compact interval tends to zero as B_* tends to infinity.

This measure statement does not establish openness. Rational compatibility failures remain genuine obstructions, and no unrestricted interval of convergence is asserted.

## Dependencies and audit conclusion

The proof uses the independent recurrence, the fully audited tree theorem in `../13_lead_theory_audit/PROOF.md`, and the elementary strip estimates displayed here. It completes the early-order infinite-angular potential inverse left as a sketch in the theory part's Theorem A'. The analytic-data conclusion is confirmed with the exact smaller-strip topology stated above. There is no claim of convergence at an incompatible rational exponent, of a global canonical solution, or of summability of the rational logarithmic series.

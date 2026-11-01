# Relative parameter stability and finite-dimensional data families

## Statement

Fix an odd positive integer L, put B=L+1, and let V_L be the real vector space spanned by sin(theta), sin(3theta), ..., sin(L theta). Fix sigma>=0, a data bound F_0>0, numbers 0<delta_-<=delta_+<1, kappa>0, and tau>=1. Define the compact parameter set

\[
\mathcal D=\{\delta\in[\delta_-,\delta_+]:
 |m-n\delta|\ge\kappa n^{-\tau}\text{ for all }n\ge1,m\in\mathbb Z\}.
\]

Assume the convergence theorem of `../07_diophantine_convergence/PROOF.md`, with the notation and proof given there. Define

\[
Q=(2e)^\tau/\kappa,\qquad
\overline M=QF_0/\delta_-,
\]

\[
\overline K=
2e^\sigma(2+\delta_-^{-1})(B+1)\frac{1-\delta_-}{\delta_-},
\qquad \overline A=4\overline K\overline M.
\]

For every delta in D and f_1 in V_L with ||f_1||_sigma<=F_0, the pure recursion obeys

\[
\|f_n\|_\sigma\le\overline M\overline A^{n-1}.
\tag{1}
\]

For any fixed

\[
R>\max\{1,\overline A^{1/\delta_-}\},
\tag{2}
\]

all the exterior density, stream, potential and fixed weighted Cartesian derivative series converge uniformly over this entire parameter and data family. After factoring out their parameter-dependent leading radial powers, the sums depend continuously on (delta,f_1) in the corresponding uniform norms for r>=R. This is continuity relative to D, not a claim about an interval containing resonant rational parameters.

For a fixed admissible delta, dependence on f_1 is real analytic in each finite-dimensional space V_L. Its complexification is holomorphic on bounded complex data balls when the common exterior radius is chosen as above. In particular convergence holds for every sufficiently small V_L perturbation of any nonzero f_1; the perturbations do not need to preserve a special cancellation.

For each fixed tau>1, almost every delta in (0,1) belongs to some such Diophantine class with a positive kappa depending on delta. Thus the convergence theorem applies to every finite odd sine polynomial for almost every parameter. This measure statement does not assert convergence at every irrational parameter or generic divergence at rational parameters.

## Uniform coefficient bounds

Write c=1/(1-delta). Then c-1=delta/(1-delta). The constants in the preceding convergence theorem are

\[
M=Q\|f_1\|_\sigma/\delta,
\qquad
K_0=2e^\sigma(2+\delta^{-1})(B+1)(1-\delta)/\delta,
\qquad A=4K_0M.
\]

Each positive factor depending on delta is bounded above by its value at delta_-. Therefore M<=Mbar, K_0<=Kbar and A<=Abar, giving (1). If R satisfies (2), then for all delta in D and r>=R,

\[
\overline A r^{-\delta}\le\overline A R^{-\delta_-}=:q<1.
\tag{3}
\]

The stream bound from the conditional reconstruction theorem is uniform:

\[
\|g_n\|_\sigma\le\tfrac12e^\sigma
 (\kappa^{-1}+\delta_-^{-1}) n^\tau\|f_n\|_\sigma.
\]

For the potential, the large-order proof in that theorem applies whenever n>=8/delta_-, and its constant is bounded by 8B/(3 kappa delta_-^2). Only finitely many early matrices remain. Their entries are rational functions of delta without poles on D. Indeed D excludes every value n delta in 2Z. The finite matrix norms consequently have a finite maximum on the compact set D. Combining these early maxima with the large-order estimate gives a uniform C_* such that

\[
\|C_n\|_\sigma\le C_*n^{\tau-1}\|f_n\|_\sigma
\quad(\delta\in\mathcal D,n\ge1).
\]

Every fixed Cartesian derivative contributes only a fixed polynomial factor in n, uniformly for delta in the compact interval. Equation (3) therefore dominates each differentiated series by a summable numerical series independent of the parameters and data. This proves the stated uniform convergence and allows the same termwise potential and stationary-equation identities for the whole family.

## Continuity in the parameter and data

At every fixed order, the coefficients are polynomials in the finitely many amplitudes of f_1 and rational functions of delta. Their denominators are nonzero on D, so they are continuous there. The same holds for the reconstructed stream and potential and every finite Cartesian derivative.

For fixed integer n>=2, the map delta -> r^{-(n-1)delta} is continuous in the uniform norm on r>=R. To see this, the mean-value theorem bounds its parameter derivative by

\[
(n-1)\log r\,r^{-(n-1)\delta_-},
\]

whose supremum for r>=R is finite. For n=1 the radial factor is constant. Hence each finite sum, normalized by its corresponding leading radial power, is continuous as a uniform function of r and theta. The uniform tail bounds above transfer this continuity to the infinite sums. This proves continuity in every fixed weighted derivative norm, even though the normalizing powers themselves vary with delta.

For fixed delta, the order-n coefficient is homogeneous of degree n in the amplitudes of f_1. The norm proof also holds for complex sine amplitudes because it uses only absolute values and bilinear identities. On every bounded complex data ball the series thus converges uniformly on a common exterior region. A locally uniform sum of holomorphic polynomial maps is holomorphic. One can also see this directly by taking its Cauchy integrals on a slightly larger data ball; the same uniform bound justifies termwise integration and the derivative series. Restriction to real amplitudes gives real analyticity.

No claim is made here about arbitrary small perturbations in an infinite-dimensional smooth or analytic space without a fixed support bound. That would require a separate estimate without the finite linear-bandwidth argument.

## Why the admissible parameters have full measure after taking a union

Fix tau>1. For each n>=1, let

\[
E_n=\{\delta\in(0,1):\operatorname{dist}(n\delta,\mathbb Z)<n^{-\tau}\}.
\]

There are at most n+1 relevant integer centers m/n, each giving an interval of length at most 2n^{-(tau+1)}. Hence

\[
|E_n|\le4n^{-\tau}.
\]

The sum of these lengths is finite. The set of points lying in infinitely many E_n has measure zero: for every N it is contained in the union over n>=N, whose measure is at most the corresponding summable tail, tending to zero.

Fix an irrational delta outside this null set. There are only finitely many indices n with dist(n delta,Z)<n^{-tau}. Every one of their distances is positive. The minimum of 1 and their finitely many positive values n^tau dist(n delta,Z) is a positive number kappa. If there are no such indices, use kappa=1. By construction, dist(n delta,Z)>=kappa n^{-tau} for every n. The rational parameters form a countable null set, so the conclusion holds for almost every delta in (0,1).

On each closed interior interval, taking the union over kappa=1/j, j positive integers, contains all these parameters. At fixed kappa and tau, however, D has empty interior, because it contains no rational number and every open interval contains rationals. Uniform relative stability on D therefore must not be described as an open-interval parameter theorem. This arithmetic observation alone does not prove that every excluded parameter is obstructed.

## Dependencies and status

This is a consequence of the geometric coefficient theorem and its reconstruction proof. Its conclusion inherits the audit status of that theorem. The full-measure argument is elementary and independent of any unquoted small-divisor or measure-theoretic convergence theorem. It establishes a sufficient parameter class and continuity of the constructed exterior solutions, not a global canonical extension.

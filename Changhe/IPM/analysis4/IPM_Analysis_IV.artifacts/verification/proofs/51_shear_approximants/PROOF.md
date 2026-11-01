# Finite sine profiles that cancel the lower leading stream modes

Status: CONFIRMED after the theory part's independent04:21Z review, recorded at2026-10-31T04:25:45Z. This identifies a test family and a low-order cancellation mechanism. It does not identify a profile minimizing the infinite-series growth rate.

## Statement

Fix 0<gamma<1, c=1/gamma, delta=1-gamma and d=c-1. For K>=0 set L=2K+1, N=L+1 and

\[
 a_0=1,\qquad
 a_k=\prod_{j=1}^{k}\frac{2j-1-\gamma}{2j+1+\gamma},\qquad
 f_1^{(K)}(\theta)=\sum_{k=0}^{K}a_k\sin((2k+1)\theta).
 \tag{1}
\]

The corresponding leading stream coefficient is exactly

\[
 g_1^{(K)}(\theta)=-\frac{a_K}{2(N+\gamma+1)}\sin(N\theta).
 \tag{2}
\]

These are the unique degree-at-most-L profiles with first sine amplitude 1 for which the stream modes 2,4,...,2K all vanish. Every a_k is positive. The angular Wiener norms satisfy

\[
 \|f_1^{(K)}\|_1=\sum_{k=0}^Ka_k
 \le\frac{1+\gamma}{2\gamma},\qquad
 a_K=O_\gamma((K+1)^{-1-\gamma}).
 \tag{3}
\]

The combined Wiener norms of the leading radial and tangential velocity components equal a_K/2. The second stationary density coefficient is nonzero and satisfies

\[
 \|f_2^{(K)}\|_1
 =\frac{a_K}{2d(N+\gamma+1)}
   \sum_{k=0}^K a_k\max\{(\gamma+1)(2k+1),\gamma N\}
 \le\frac{(1+\gamma)^2}{4\gamma d}a_K.
 \tag{4}
\]

More precisely,

\[
 \lim_{K\to\infty}\frac{\|f_2^{(K)}\|_1}{a_K}
 =\frac{1+\gamma}{4d}.
 \tag{5}
\]

The leading profiles converge uniformly to a constant multiple of sign(sin(theta))|sin(theta)|^gamma. That limiting profile is not C^1 at the horizontal axis, and therefore is not an admissible smooth exterior solution in the task. Every finite K gives an analytic profile. At any Brjuno parameter covered by the confirmed convergence theorem, each such finite profile generates a convergent exterior series, with the theorem's K-dependent bound.

## 1. Exact stream cancellation

At order one the radial density degree is gamma, so topic01 gives

\[
 b_j=-\frac{a_{j-1}}{2(2j+\gamma+1)}
       +\frac{a_j}{2(2j-\gamma-1)}.
\]

For 1<=j<=K, setting b_j=0 gives exactly the ratio in (1). Its numerator and denominator are positive since gamma<1. At j=K+1 only the first term remains, giving (2); beyond this index both inputs vanish. This proves existence and uniqueness of the cancellation family.

The leading velocity components in polar coordinates are -g_1' and (gamma+1)g_1. Their combined coefficient norm is

\[
 \big(N+\gamma+1\big)\frac{a_K}{2(N+\gamma+1)}=\frac{a_K}{2}.
\]

This is a norm on the two polar components; it is not an equality asserted for every Cartesian vector norm.

## 2. Summability and the limiting profile

Put A=(1-gamma)/2 and B=(3+gamma)/2. Then a_(k+1)/a_k=(k+A)/(k+B), and

\[
 (k+B-1)a_k-(k+B)a_{k+1}=\gamma a_k.
\]

Summing yields the exact identity

\[
 \sum_{k=0}^Ka_k
 =\frac{B-1-(K+B)a_{K+1}}{\gamma}.
 \tag{6}
\]

Also

\[
 a_K=\prod_{j=1}^K\left(1-\frac{1+\gamma}{j+(1+\gamma)/2}\right)
 \le\left(\frac{(3+\gamma)/2}{K+(3+\gamma)/2}\right)^{1+\gamma}.
 \tag{7}
\]

For K=0 this is equality. For positive K, use log(1-x)<=-x and bound the decreasing harmonic sum below by its integral. Thus (K+B)a_(K+1)->0, proving both (3) and sum_(k>=0)a_k=(1+gamma)/(2gamma). The sine series converges absolutely and uniformly.

For completeness, define h(theta)=sign(sin(theta))|sin(theta)|^gamma. It is continuous, has an integrable first derivative, and satisfies gamma cos(theta)h-sin(theta)h'=0 away from the axes and distributionally across them. Integration against the even sine modes gives the same coefficient recurrence as in Section1. Its first sine amplitude is the positive number

\[
 A_\gamma=\frac2\pi\int_0^\pi\sin^{\gamma+1}(\theta)\,d\theta.
\]

It follows that the Fourier coefficients of h/A_gamma are exactly a_k. Its uniformly convergent Fourier series is therefore the limit above. Alternatively uniqueness follows from the first-order equation separately on each half-circle and the S1 parity. Near theta=0 the limit is a nonzero multiple of sign(theta)|theta|^gamma, whose derivative is unbounded since gamma<1.

The corresponding homogeneous density is A_gamma^(-1) sign(y)|y|^gamma, with zero stream and velocity. It obeys c y partial_y rho-rho=0 away from y=0 and distributionally. Its failure of C^1 regularity occurs in every exterior region. It does not contradict the analytic nontermination theorem.

## 3. Exact second-order norm

Write b=-a_K/[2(N+gamma+1)]. The order-two recurrence is

\[
 f_2=d^{-1}\big((\gamma+1)g_1f_1'-\gamma g_1'f_1\big).
\]

For each m=2k+1<N, its sine amplitudes at N+m and N-m are respectively

\[
 \frac{ba_k}{2d}\big((\gamma+1)m-\gamma N\big),\qquad
 \frac{ba_k}{2d}\big((\gamma+1)m+\gamma N\big).
\]

All these frequencies are distinct: the first group lies strictly above N and the second strictly below N. Taking absolute values therefore gives (4), using |x-y|+x+y=2 max(x,y) for nonnegative x,y. The upper bound follows from max((gamma+1)m,gamma N)<=(gamma+1)N and (3). The highest frequency N+L has amplitude ba_K(L-gamma)/(2d), which is nonzero.

Divide the exact norm by a_K and write the sum as

\[
 \frac{N}{2d(N+\gamma+1)}
 \sum_{k=0}^Ka_k\max\{(\gamma+1)(2k+1)/N,\gamma\}.
\]

For each fixed k its summand tends to gamma a_k, and every summand is bounded by (gamma+1)a_k. Summability permits dominated convergence. The limit is gamma/(2d) times (1+gamma)/(2gamma), which is (5).

## Scope for numerical experiments

The first two nontrivial ratios are a_1=delta/(4-delta) and a_2/a_1=(2+delta)/(6-delta). They are determined by exact cancellation, not by a fit to Candidate007. A small f_2 and small leading velocity do not bound the limsup growth of f_n as n grows. The bandwidth also grows with K, so the existing convergence estimates are not uniform in K. Numerical comparisons should keep a_0=1, name K and delta, and report their finite orders.

The data directory contains exact rational input lists at Candidate007's stored parameter for K=1,2,3,5,9. The independent Cartesian check verifies (2), (4), (6) and nonvanishing of f_2 for the tested parameter/bandwidth pairs. Reproduce with ../../code/shear_approximant_audit.py; results and source hashes are in verification/checks.json.

# Quantitative tails and residuals from the geometric majorant

## Statement

Assume the hypotheses of the Diophantine convergence theorem in `../07_diophantine_convergence/PROOF.md`, or of the arithmetic-integral theorem in `../11_arithmetic_integral/PROOF.md`. Use their constants M,A,Lambda_sigma,B and c, so

\[
Y_n=n\|f_n\|_\sigma/d_n\le MA^{n-1},\qquad
A=\frac{8\Lambda_\sigma(B+1)M}{c-1}.
\]

Choose R with q=A R^(-delta)<1. Let rho_N and psi_N be the first N terms of the density and stream expansions, and let u_N=(-partial_y psi_N,partial_x psi_N). Define their actual stationary residual

\[
\mathcal R_N=(cX+u_N)\cdot\nabla\rho_N-\rho_N.
\]

Then

\[
\sup_{r\ge R}\|r^{-\gamma}(\rho-\rho_N)\|_\sigma
\le\frac{M q^N}{(N+1)(1-q)},
\tag{1}
\]

and

\[
\sup_{r\ge R}\|r^{-\gamma}\mathcal R_N\|_\sigma
\le\frac{(c-1)M}{8}
 q^N\left[\frac{N}{1-q}+\frac{q}{(1-q)^2}\right].
\tag{2}
\]

For q<=1/2 this yields the simple bounds

\[
\text{density tail}\le\frac{2M}{N+1}2^{-N},\qquad
\text{residual}\le\frac{(c-1)M}{4}(N+1)2^{-N}.
\tag{3}
\]

For any fixed Cartesian multi-index alpha of order h, the corresponding weighted derivative residual is at most the right-hand side of (2) multiplied by

\[
e^{h\sigma}[2(B+1)N+2h]^h.
\tag{4}
\]

The derivative weight is r^(h-gamma). These estimates concern the velocity produced by the same truncated potential. They do not insert an independently fitted velocity.

## Density tail

Since d_n<=1, the stronger majorant gives ||f_n||_sigma<=M A^(n-1)/n. Therefore the weighted tail is bounded by

\[
M\sum_{n=N+1}^{\infty}\frac{q^{n-1}}n
\le\frac{M q^N}{(N+1)(1-q)}.
\]

This proves (1). The weaker tail constants in the original explicit examples remain valid.

## Exact cancellation and residual bound

The stream estimate gives

\[
\max\{\|g_i'\|_\sigma,|P_i|\|g_i\|_\sigma\}
\le\Lambda_\sigma Y_i.
\]

Also |p_j|<=j, deg f_j<=Bj-1 and j||f_j||_sigma=d_jY_j<=Y_j. The Wiener algebra inequality then gives

\[
\|-p_jg_i'f_j+P_ig_if_j'\|_\sigma
\le\Lambda_\sigma(B+1)Y_iY_j
\le\Lambda_\sigma(B+1)M^2A^{i+j-2}.
\tag{5}
\]

Every residual order n<=N cancels exactly by the recurrence. The remaining orders have N+1<=n<=2N, and each has at most n-1 ordered pairs. Thus

\[
\sup_{r\ge R}\|r^{-\gamma}\mathcal R_N\|_\sigma
\le\frac{\Lambda_\sigma(B+1)M^2}{A}
 \sum_{m=N}^{2N-1}m q^m.
\]

Extending the sum to infinity and differentiating the geometric series gives

\[
\sum_{m=N}^{\infty}m q^m
=q^N\left[\frac{N}{1-q}+\frac{q}{(1-q)^2}\right].
\]

The prefactor equals (c-1)M/8 by the definition of A, proving (2). Substituting q<=1/2 gives (3).

## Derivative residuals

At residual order n, the radial exponent is p_n and the angular bandwidth is at most Bn-1. One Cartesian derivative has coefficient norm at most e^sigma times the sum of the absolute radial degree and the bandwidth. After t previous derivatives, this sum is at most (B+1)n+2t, because |p_n|<=n. For n<=2N and 0<=t<h, the product of h such factors is bounded by (4). Differentiation reduces the radial degree by h, so multiplication by r^(h-gamma) leaves the same geometric factor as in (2). Summing the finitely many residual orders proves the result.

## Explicit examples

For delta=1/sqrt(5), f_1=sin(theta), sigma=(log 2)/2 and R=2^36, the previously proved inequalities M<256, c-1<1 and q<1/2 give

\[
\text{density tail}<\frac{512}{N+1}2^{-N},\qquad
\text{residual}<64(N+1)2^{-N}.
\]

For the exact extracted Candidate 007 polynomial used at the new exponent delta=1/sqrt(5), the earlier constants M<2^13 and R=2^54 give

\[
\text{density tail}<\frac{2^{14}}{N+1}2^{-N},\qquad
\text{residual}<2^{11}(N+1)2^{-N}.
\]

Both are bounds in the same weighted angular analytic norm, not grid measurements. The actual finite-order observations can be much smaller. Their rigorous status depends only on the geometric majorant proof, not on empirical root or ratio tests.

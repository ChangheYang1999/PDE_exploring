# An explicit Gevrey-one upper bound at delta = 1/sqrt(5)

## Statement

Fix

\[
\delta=1/\sqrt5,\quad c=(5+\sqrt5)/4,\quad p_n=1-n\delta.
\]

Let f_1 be a nonzero real odd sine polynomial supported in odd frequencies at most L, and put B=L+1. For sigma>=0 use the Wiener norm

\[
\|h\|_\sigma=\sum_{k\in\mathbb Z}|\widehat h(k)|e^{\sigma|k|}.
\]

For a sine polynomial this equals the sum of the absolute sine amplitudes times e^(sigma times frequency). Let F=||f_1||_sigma and define

\[
K_\sigma=\frac{e^\sigma}{2}
\left[5(B+2+\delta)+\delta^{-1}\right],\quad
H=\frac{3BK_\sigma}{c-1},\quad D=2HF.
\]

The pure formal density and stream recursion exists uniquely at every order, and

\[
\boxed{\|f_n\|_\sigma\le F D^{n-1}(n-1)!,\qquad
\|g_n\|_\sigma\le K_\sigma F D^{n-1}n!.}
\]

Each finite truncation has a pure finite potential reconstruction. The density and stream Borel transforms, obtained by dividing the coefficient of z^(n-1) by (n-1)!, converge in this Wiener space for |z|<1/D.

This is an upper Gevrey bound. It proves neither ordinary convergence nor divergence, and it does not prove Borel summability to an actual solution.

There is also an exponentially small residual for a suitable finite truncation. If R>0 and q=D R^(-delta)<=1/4, let N=floor(1/(4q)). Then the finite density and stream sums through N, with the velocity from their common potential, satisfy

\[
\boxed{\sup_{r\ge R}\|r^{-\gamma}[(cX+u_N)\cdot\nabla\rho_N-\rho_N]\|_\sigma
\le4(c-1)F N2^{-N}.}
\]

This estimates the residual of an explicit approximate solution, not the distance to an exact solution.

## Nonresonance and support

The number delta is irrational. Consequently neither n delta=2(j+1) nor n delta=2m can occur for positive integers n,j,m. The stream and finite polynomial potential inverses in `../01_recurrence/PROOF.md` are therefore well-defined at every order.

The same induction proves

\[
\deg f_n\le Bn-1,\qquad\deg g_n\le Bn.
\]

Every coefficient is a finite trigonometric polynomial, so the norm is finite for every fixed sigma.

## Small-divisor estimate

For an integer m>=1 and n>=1,

\[
|m-n\delta|=
\frac{|5m^2-n^2|}{5(m+n\delta)}\ge\frac1{5(m+n\delta)}.
\]

The numerator is a nonzero integer. The cancellation form of the Poisson inverse, with stream frequency k=2j, is

\[
b_{n,j}=-\frac{a_{n,j-1}}{2(k+2-n\delta)}
+\frac{a_{n,j}}{2(k-2+n\delta)}.
\]

Whenever an input coefficient is nonzero, the corresponding stream frequency is at most Bn. The first multiplier has absolute value at most

\[
\tfrac52(k+2+n\delta)\le\tfrac52(B+2+\delta)n.
\]

For the second, k>=2 gives

\[
\frac1{2(k-2+n\delta)}\le\frac1{2n\delta}\le\frac n{2\delta}.
\]

Each input amplitude contributes to at most one coefficient through each multiplier. A shift of its frequency by one changes the Wiener weight by at most e^sigma. Summing proves

\[
G_n:=\|g_n\|_\sigma\le K_\sigma n F_n,
\qquad F_n:=\|f_n\|_\sigma.
\]

This estimate explicitly retains a loss proportional to n. A uniform lower bound on the quadratic Poisson denominator would not remove the n-dependent numerator of the inverse.

## Quadratic majorant

The Wiener norm is submultiplicative: this follows from convolution and the triangle inequality |k+l|<=|k|+|l|. For a polynomial supported in |k|<=M, its derivative has norm at most M times its norm. Also |p_j|<=j and |p_i+1|<=2i. Therefore the angular recursion implies

\[
F_n\le\frac{3B}{(c-1)(n-1)}\sum_{i+j=n}ijG_iF_j
\le\frac H{n-1}\sum_{i+j=n}i^2jF_iF_j.
\]

For n>=2 define

\[
T_n=\frac1{(n-1)(n-1)!}
\sum_{i+j=n}i^2j(i-1)!(j-1)!.
\]

Symmetrizing in i and j gives

\[
T_n=\frac{n^2}{2(n-1)}\sum_{i=1}^{n-1}\binom ni^{-1}.
\]

For n=2 this is 1. For n>=3 the two endpoint terms contribute 2/n. Each of the n-3 interior terms is at most 2/[n(n-1)], because binomial(n,i)>=binomial(n,2) for 2<=i<=n-2. Hence

\[
T_n\le\frac{2n(n-2)}{(n-1)^2}<2.
\]

Assume inductively that F_i<=F D^(i-1)(i-1)! for i<n. Substitution into the majorant gives

\[
F_n\le2HF^2D^{n-2}(n-1)!
=F D^{n-1}(n-1)!,
\]

because D=2HF. The initial case is equality. The stream bound follows from G_n<=K_sigma n F_n. Dividing by (n-1)! gives geometric and polynomial-times-geometric bounds, proving the Borel-transform statement.

## Optimally scaled finite residual

Let S_n^(N) be the angular coefficient of u_N dot grad(rho_N) at exponent p_n, summing only 1<=i,j<=N. The density linear term and all nonlinear coefficients at orders n<=N cancel exactly. No nonlinear order exceeds 2N. Thus

\[
r^{-\gamma}[(cX+u_N)\cdot\nabla\rho_N-\rho_N]
=\sum_{n=N+1}^{2N}z^{n-1}S_n^{(N)},\quad z=r^{-\delta}.
\]

The same nonnegative majorant used above remains valid after restricting the pairs. It gives

\[
\|S_n^{(N)}\|_\sigma
\le(c-1)F D^{n-1}(n-1)(n-1)!.
\]

For r>=R, set q=D R^(-delta). With k=n-1 between N and 2N-1 and 2Nq<=1/2,

\[
k!q^k\le k^kq^k\le(2Nq)^k\le2^{-k}.
\]

Consequently the residual norm is at most

\[
(c-1)F\sum_{k=N}^{2N-1}k2^{-k}
\le4(c-1)F N2^{-N}.
\]

The chosen N satisfies 2Nq<=1/2 and is positive. This proves the claimed residual bound.

For completeness, a fixed Cartesian derivative order h has a corresponding weighted residual bound

\[
\sup_{r\ge R}\|r^{h-\gamma}\partial^\alpha R_N\|_\sigma
\le [e^\sigma(2(B+1)N+2h)]^h
\,4(c-1)F N2^{-N},\qquad |\alpha|=h.
\]

Indeed each residual term has |p_n|<=2N and angular frequency at most 2BN. A Cartesian derivative lowers the radial degree by one and increases the angular bandwidth by at most one. Its Wiener norm multiplier is at most e^sigma times the sum of the current absolute radial degree and bandwidth. After at most h derivatives this is bounded by the displayed factor. No assertion about convergence of the infinite differentiated series is used.

## Dependencies and scope

The proof uses the exact formal recurrence, the finite support induction, an elementary quadratic-irrational inequality, the Wiener algebra inequality and factorial/binomial estimates. No external existence theorem is invoked. No potential coefficient growth estimate is asserted. The finite potential reconstruction suffices for each truncated residual calculation.

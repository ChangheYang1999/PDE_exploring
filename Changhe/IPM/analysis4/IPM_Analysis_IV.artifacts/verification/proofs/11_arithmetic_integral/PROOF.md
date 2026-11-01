# A sufficient arithmetic integral beyond a polynomial Diophantine bound

## Statement

Let 0<delta<1 be irrational, c=1/(1-delta), and

\[
d_n=\operatorname{dist}(n\delta,2\mathbb Z),\qquad
q(\epsilon)=\min\{n\ge1:d_n<\epsilon\}.
\]

If the set is empty, set q(epsilon)=infinity and 1/q(epsilon)=0. Assume the explicit arithmetic condition

\[
J(\delta):=\int_0^\infty
 \min\left\{1,\frac{2}{q(2e^{-t})}\right\}\,dt<\infty.
\tag{I}
\]

For any nonzero finite odd sine polynomial f_1, let L be its highest frequency, B=L+1 and F=||f_1||_sigma in the angular Wiener norm, with sigma>=0. Put

\[
\Lambda_\sigma=e^\sigma(2+\delta^{-1}),\qquad
K_0=\frac{2\Lambda_\sigma(B+1)}{c-1},\qquad
Q=e^{J(\delta)},\quad M=QF/\delta,\quad A=4K_0M.
\]

Then the pure stationary recursion is defined at every order and satisfies the stronger estimate

\[
Y_n:=\frac{n\|f_n\|_\sigma}{d_n}\le MA^{n-1}.
\tag{1}
\]

For every R>A^(1/delta), the density, stream and potential series and all fixed weighted Cartesian derivatives converge uniformly for r>=R and solve the original exterior potential equation. No separate Diophantine estimate is needed for potential reconstruction once (1) is known.

This theorem states its own arithmetic hypothesis. It does not identify (I) with a named continued-fraction condition, and no equivalence with another arithmetic class is required for the proof.

## Reduction to scalar tree weights

The stream estimate and scalar reduction in `../07_diophantine_convergence/PROOF.md` use only irrationality and 0<d_n<=1, not the polynomial lower bound. They give

\[
Y_n\le \frac{K_0}{d_n}\sum_{i+j=n}Y_iY_j,
\qquad Y_1=F/\delta.
\]

The scalar majorant is therefore the same sum over rooted ordered full binary trees, with internal vertex weight 1/d_s when its subtree has s leaves. It remains to bound the product of these weights under (I).

## Counting small divisors in one tree

Fix a tree with N leaves, and mark an internal vertex of subtree size m whenever d_m<epsilon. Every marked subtree has at least q(epsilon)>=q(2epsilon) leaves. If marked vertices of sizes m>l are comparable by ancestry, the inequality

\[
d_{m-l}\le d_m+d_l<2\epsilon
\]

implies m-l>=q(2epsilon).

Compress the marked vertices to a forest as in the earlier proof. Let L_0 count terminal marked vertices, L_1 unary marked vertices, and L_2 marked vertices with two or more children. The forest edge count gives L_2<=L_0. Charge all leaves under each terminal marked vertex and the leaves outside the unique marked child under each unary marked vertex. These charged sets are disjoint, and each contains at least q(2epsilon) leaves. Consequently

\[
N\ge q(2\epsilon)(L_0+L_1),\qquad
L_0+L_1+L_2\le2L_0+L_1\le\frac{2N}{q(2\epsilon)}.
\]

If q(2epsilon)=infinity, there can be no marked vertex and the same statement holds with zero right-hand side. Combining this with the trivial N bound and integrating at epsilon=e^(-t) gives

\[
\log\prod_{v\text{ internal}}d_{s(v)}^{-1}
\le N\int_0^\infty\min\{1,2/q(2e^{-t})\}\,dt
=NJ(\delta).
\]

Every tree product is at most Q^N. There are at most 4^(N-1) trees. The scalar induction now proves (1), with the stated constants.

## Reconstruction directly from Y_n

The cancellation form of the Poisson inverse gives, without a Diophantine estimate,

\[
\|g_n\|_\sigma
\le\frac{e^\sigma}{2}\left(\frac1{d_n}+\frac1{n\delta}\right)\|f_n\|_\sigma
\le\frac{e^\sigma}{2}(1+\delta^{-1})\frac{Y_n}{n}.
\tag{2}
\]

For the potential, the descending density-to-Laplacian argument in `../06_conditional_convergence/PROOF.md` gives

\[
\|D_n\|_\sigma\le\frac{4B}{3\delta}\|f_n\|_\sigma
\quad(n\delta\ge8),
\]

where D_n is the angular coefficient of Delta chi_n. For each even k>=0,

\[
|(4-n\delta)^2-k^2|
=|k+4-n\delta|(k+n\delta-4)
\ge d_n\,n\delta/2.
\]

Thus

\[
\|C_n\|_\sigma
\le\frac{8B}{3\delta^2}\frac{\|f_n\|_\sigma}{nd_n}
=\frac{8B}{3\delta^2}\frac{Y_n}{n^2}
\quad(n\delta\ge8).
\tag{3}
\]

There are finitely many earlier orders, each with an invertible pure potential matrix because delta is irrational. Absorbing their finite norms into a constant gives the same exponential radius for all coefficients. Every fixed Cartesian derivative introduces only polynomial factors in n, which are dominated by the strict geometric margin A R^(-delta)<1. The argument for the exact PDE and nontriviality is then the same as in the conditional convergence theorem.

## A directly checkable dyadic sufficient condition

Define

\[
\mu(N)=\min_{1\le n\le N}d_n.
\]

The explicit dyadic condition

\[
\sum_{h=0}^{\infty}2^{-h}\log\frac{2}{\mu(2^h)}<\infty
\tag{II}
\]

implies (I). Indeed, for every positive integer q,

\[
\frac1q\le\sum_{h=0}^\infty2^{-h}\mathbf1_{q\le2^h}.
\]

Also q(2e^(-t))<=2^h exactly when mu(2^h)<2e^(-t). Integrating the resulting nonnegative series gives

\[
J(\delta)\le2\sum_{h=0}^{\infty}2^{-h}
\log\frac{2}{\mu(2^h)}.
\]

A polynomial lower bound d_n>=kappa n^(-tau) immediately makes (II) finite. More generally, a bound d_n>=kappa exp(-C n^beta) with 0<beta<1, C>0 and 0<kappa<=1 also makes (II) finite, since its h-th summand is at most

\[
2^{-h}\log(2/\kappa)+C2^{-(1-\beta)h}.
\]

These are sufficient conditions only. Failure of (I), (II), or any stated lower bound is not a divergence theorem for the nonlinear IPM recursion, whose active coefficients may contain cancellations.

## Dependencies and status

The proof uses the explicitly derived scalar recursion, finite-tree counting, and the displayed potential bounds. It is a proposed strengthening of the polynomial Diophantine theorem and awaits the same adversarial review. The dyadic criterion and the integral are supplied in full to avoid depending on an unproved identification with a named small-divisor theorem.

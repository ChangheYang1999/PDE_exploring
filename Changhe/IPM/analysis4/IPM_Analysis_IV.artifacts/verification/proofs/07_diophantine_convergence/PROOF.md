# Convergence for finite angular data at Diophantine parameters

## Theorem

Fix c>1, gamma=1/c and delta=1-gamma. Suppose that for some kappa>0 and tau>=1,

\[
|m-n\delta|\ge\kappa n^{-\tau}
\quad\text{for every }n\ge1\text{ and }m\in\mathbb Z.
\tag{D}
\]

Let f_1 be a nonzero real sine polynomial in positive odd frequencies, with highest frequency L. Set B=L+1. For sigma>=0 use the angular Wiener norm

\[
\|h\|_\sigma=\sum_{k\in\mathbb Z}|\widehat h(k)|e^{\sigma|k|},
\qquad F=\|f_1\|_\sigma.
\]

Define

\[
\Lambda_\sigma=e^\sigma(2+\delta^{-1}),\qquad
K_0=\frac{2\Lambda_\sigma(B+1)}{c-1},\qquad
Q=\frac{(2e)^\tau}{\kappa},
\]

\[
M=\frac{QF}{\delta},\qquad A=4K_0 M.
\tag{C}
\]

Then the pure stationary recursion exists uniquely at every order and satisfies

\[
\boxed{\|f_n\|_\sigma\le M A^{n-1}\quad(n\ge1).}
\tag{E}
\]

Consequently, for every R>A^(1/delta), the density, stream and pure potential series converge in their weighted angular Wiener norms on r>=R. Every fixed Cartesian derivative series converges uniformly in its corresponding radial weight. Their sums solve the original stationary potential equation on r>R and give a nonzero smooth exterior solution with S1 symmetry.

One explicit admissible choice is delta=1/sqrt(5), c=(5+sqrt(5))/4, tau=1 and

\[
\kappa=\frac1{5(1+2/\sqrt5)}.
\]

For example f_1=sin(theta) is nonzero admissible data. The result concerns the local exterior equation. It does not assert extension to a smooth whole-plane solution or equality with a prescribed canonical whole-plane inverse.

## Formal maps and finite support

Condition (D) implies irrationality of delta. Thus n delta is never an even integer. All stream and pure polynomial potential inverses are well-defined. The derivation in `../01_recurrence/PROOF.md` gives, with p_n=1-n delta and P_n=p_n+1,

\[
b_{n,j}=-\frac{a_{n,j-1}}{2(2j+P_n)}
+\frac{a_{n,j}}{2(2j-P_n)},\qquad j\ge1,
\tag{1}
\]

and

\[
f_n=\frac1{(n-1)(c-1)}\sum_{i+j=n}
[P_i g_i f_j'-p_jg_i'f_j].
\tag{2}
\]

The same finite-support induction gives deg f_n<=Bn-1 and deg g_n<=Bn. These formulas involve finite sums at every order, independently of convergence.

Put

\[
d_n=\operatorname{dist}(n\delta,2\mathbb Z).
\]

Then 0<d_n<=1, d_1=delta, and (D) implies d_n>=kappa n^(-tau). The elementary distance inequality

\[
d_{m-l}\le d_m+d_l\qquad(m>l\ge1)
\tag{3}
\]

follows by subtracting nearest even integers.

## A stream derivative estimate retaining the arithmetic divisor

Let k=2j>=2. Then

\[
|k+P_n|\ge d_n,\qquad k-P_n=k-2+n\delta\ge n\delta,
\qquad |P_n|\le2n.
\]

Each input Fourier amplitude in (1) contributes once through a frequency increase and at most once through a frequency decrease. Each such shift changes its Wiener weight by at most e^sigma. For the differentiated stream, the sum of the two multiplier bounds is

\[
\frac{k}{2|k+P_n|}+\frac{k}{2(k-P_n)}
\le1+\frac{|P_n|}{2d_n}+\frac{|P_n|}{2n\delta}
\le(2+\delta^{-1})\frac n{d_n}.
\]

Here the two occurrences of k can differ by two for a fixed input amplitude; each displayed bound holds separately, so their sum remains valid. The corresponding bound for |P_n| times the undifferentiated stream is

\[
\frac{|P_n|}{2|k+P_n|}+\frac{|P_n|}{2(k-P_n)}
\le(1+\delta^{-1})\frac n{d_n}.
\]

Therefore

\[
\max\{\|g_n'\|_\sigma,\ |P_n|\|g_n\|_\sigma\}
\le\Lambda_\sigma\frac n{d_n}\|f_n\|_\sigma.
\tag{4}
\]

The sum notation in these multiplier inequalities is a uniform upper bound on the two channels, not an assertion that both have the same output frequency.

## Reduction to a scalar tree recursion

Write F_n=||f_n||_sigma. The Wiener algebra inequality, (2), (4), |p_j|<=j and deg f_j<=Bj-1 imply

\[
F_n\le\frac{\Lambda_\sigma(B+1)}{(c-1)(n-1)}
\sum_{i+j=n}\frac{ij}{d_i}F_iF_j.
\tag{5}
\]

Define Y_n=nF_n/d_n. Since jF_j=d_jY_j and d_j<=1,

\[
Y_n\le\frac{K_0}{d_n}\sum_{i+j=n}Y_iY_j,\qquad n\ge2,
\qquad Y_1=F/\delta.
\tag{6}
\]

The factor two in K_0 uses n/(n-1)<=2. No divisor has been replaced by its pointwise polynomial bound at this step.

Let b_1=1 and

\[
b_n=\frac1{d_n}\sum_{i+j=n}b_i b_j\qquad(n\ge2).
\tag{7}
\]

Induction in (6) gives

\[
Y_n\le K_0^{n-1}Y_1^n b_n.
\tag{8}
\]

Expanding (7), b_n is a sum over rooted ordered full binary trees with n leaves. Each internal vertex v contributes a factor d_(s(v))^(-1), where s(v) is the number of leaves in its subtree. There are at most 4^(n-1) such trees. The remaining task is to bound each product uniformly by an exponential in n.

## Leaf-count packing lemma

Fix one rooted binary tree with N leaves. For 0<epsilon<=1, mark each internal vertex v for which d_(s(v))<epsilon. Let q=(kappa/epsilon)^(1/tau). Every marked vertex has at least q leaves below it, by the lower bound on d_s.

If two marked vertices are comparable by ancestry and have subtree sizes m>l, then (3) gives d_(m-l)<2epsilon. Hence

\[
m-l>(\kappa/(2\epsilon))^{1/\tau}
=q/2^{1/\tau}\ge q/2.
\tag{9}
\]

Form a forest whose vertices are the marked vertices, with an edge from a marked vertex to each nearest marked descendant. These edges may skip unmarked vertices of the original tree. Let L_0 be the number of marked vertices with no child in this forest, L_1 the number with one child, and L_2 the number with at least two children. If there are no marks, the desired estimate is immediate. Otherwise the elementary edge count of a finite forest gives L_2<=L_0.

For each of the L_0 terminal marked vertices, charge all leaves in its subtree; there are at least q. For each of the L_1 unary marked vertices, charge the leaves in its subtree outside the subtree of its unique marked child; there are at least q/2 by (9). All these charged leaf sets are pairwise disjoint. Indeed descendant charges lie inside the unique child subtree removed from any unary ancestor, and distinct descendant subtrees are disjoint. Thus

\[
N\ge qL_0+(q/2)L_1.
\]

The number of marked vertices is consequently bounded by

\[
L_0+L_1+L_2\le2L_0+L_1\le2N/q
=2N(\epsilon/\kappa)^{1/\tau}.
\tag{10}
\]

It is also at most N-1, since only internal vertices are marked.

## Product bound and convergence of the scalar majorant

Because 0<d_s<=1, a finite sum of layer-cake integrals gives

\[
\log\prod_{v\text{ internal}}d_{s(v)}^{-1}
=\int_0^\infty\#\{v:d_{s(v)}<e^{-t}\}\,dt.
\]

The endpoint convention for a strict inequality affects only finitely many integration points. Since kappa<=d_1=delta<1, the number

\[
t_0=\log(2^\tau/\kappa)
\]

is positive. Using the trivial N bound up to t_0 and (10) afterwards gives

\[
\begin{aligned}
\log\prod_vd_{s(v)}^{-1}
&\le Nt_0+2N\kappa^{-1/\tau}
\int_{t_0}^\infty e^{-t/\tau}\,dt\\
&=N(t_0+\tau)
=N\log\big((2e)^\tau/\kappa\big).
\end{aligned}
\]

Therefore every tree product is at most Q^N. The Catalan count implies

\[
b_n\le4^{n-1}Q^n.
\tag{11}
\]

Combining (8), (11) and F_n=d_nY_n/n<=Y_n proves

\[
F_n\le QY_1(4K_0QY_1)^{n-1}=MA^{n-1},
\]

which is (E). This proof controls products of small divisors along trees. Replacing each individual d_n^(-1) by kappa^(-1)n^tau before forming the tree would lose the separation property and would only give a much weaker factorial bound.

## Reconstruction, derivatives and nontriviality

The potential estimate proved in `../06_conditional_convergence/PROOF.md` gives

\[
\|C_n\|_\sigma\le C_*n^{\tau-1}F_n,
\qquad
\|g_n\|_\sigma\le K_\sigma n^\tau F_n,
\]

where the constants are finite and independent of n. For every R>A^(1/delta), multiplication by R^(-delta(n-1)) makes these bounds, and every additional fixed polynomial factor in n, summable. A Cartesian derivative adds only such polynomial factors because the radial exponents and angular bandwidths grow at most linearly in n.

Thus the termwise potential identities and stationary Cauchy products are legitimate, with all weighted derivative conclusions stated in the theorem. The weighted density tends to f_1 as r tends to infinity, so its sum is not the zero solution.

## A concrete radius and geometric tail for a nonzero example

Take f_1=sin(theta), delta=1/sqrt(5), and sigma=(log 2)/2. Put s=sqrt(5). The constants above simplify to

\[
M=10\sqrt2\,e(2+s),\qquad A=480e(11+5s).
\]

The elementary inequalities e<3 and s<9/4 give M<256 and A<32768=2^15. Also delta>4/9. Choose

\[
R=2^{36}=68719476736.
\]

Then R^delta>2^16 and A R^(-delta)<1/2. Thus this explicit nonzero example converges in the angular analytic Wiener norm with strip width (log 2)/2, and for every N>=1,

\[
\sup_{r\ge R}\left\|r^{-\gamma}\rho-
\sum_{n=1}^{N}r^{-\delta(n-1)}f_n\right\|_\sigma
\le512\,2^{-N}.
\]

This radius and tail constant are conservative. No optimization is needed for their role as an explicit existence certificate. Every fixed weighted derivative converges on the same exterior region by the polynomial-factor argument above.

## The extracted reference polynomial at the new parameter

Keep delta=1/sqrt(5), but take f_1 to be the exact density polynomial extracted from Candidate 007 in `../02_candidate007/data/leading_exact.json`. This changes the exponent while preserving the extracted leading density polynomial. Its leading potential must therefore be recomputed at the new exponent.

At sigma=(log 2)/2 its norm is sqrt(2) T, where

\[
T=\sum_{k=0}^9 2^k |a_{2k+1}|<31.
\]

Here a_(2k+1) denotes the sine amplitude indexed by its frequency. The inequality is an exact rational calculation retained in `verification/reference_constants.json` and reproducible with `../../code/reference_convergence_constants.py`.

The highest frequency is 19, so B=20. Relative to the preceding single-mode constants, M is multiplied by T and A by 7T. Hence M<2^13 and A<2^23. Taking

\[
R=2^{54}
\]

gives R^delta>2^24, so the weighted analytic-norm density tail after N terms is at most 2^14 2^(-N). The full potential and all fixed weighted derivatives converge on the same exterior region. This is a conservative explicit corollary for the extracted polynomial at the new algebraic irrational exponent. It makes no all-order claim at Candidate 007's stored rational exponent.

## Parameter example and precise limitations

For delta=1/sqrt(5), the integer identity 5m^2-n^2!=0 gives the stated value of kappa as explained in `../06_conditional_convergence/PROOF.md`. Hence the theorem applies to this explicit exponent and every finite odd sine polynomial, including f_1=sin(theta) and the exact polynomial extracted from Candidate 007 when used at this new exponent.

The theorem does not apply to Candidate 007's stored rational delta. It also does not assert an open interval of parameters: rational exact resonances occur densely. A uniform Diophantine parameter class with fixed kappa and tau, bounded away from delta=0 and delta=1, gives uniform constants for bounded families of finite-bandwidth f_1. This is the appropriate relative stability statement supplied by the proof.

No external small-divisor theorem is invoked. The scalar majorant was suggested by the theory part's notes; the reweighting, packing estimate, constants and potential/derivative conclusion are spelled out here for independent audit. The mathematical dependencies are the two earlier standalone proofs cited above and elementary finite-tree counting.

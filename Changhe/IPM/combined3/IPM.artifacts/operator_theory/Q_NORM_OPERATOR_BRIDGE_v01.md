# Frozen inverses and an exterior-barrier fixed point in the Q norm

This is an analytic bridge for the new auxiliary norm
\[
Q(g)=\|WJ^qg\|_2,\quad q=21/10,\quad W=\sqrt{1+4|X|^2}.
\]
It does not assume a uniform Q-energy estimate for every test function. An estimate valid only outside the trial radius is enough. Actual quantitative background and nonlinear estimates still must be supplied before existence is claimed.

Keep the exact Candidate 013 and c. Define A_k as in `OPERATOR_BRIDGE_v01.md`, and assume its actual signed L2 bound with rate beta2>0. The actual generator, maximal domain, core, and L2 inverse then follow from that note's Lemmas 1--2.

## 1. The two high spaces agree qualitatively

Write N(g)=||Jq(Wg)||2. The spaces N<infinity and Q<infinity agree, with equivalent Hilbert norms. Only qualitative equivalence is used in this bridge.

For a direct proof, first observe that N<infinity implies g and x_jg belong to Hq, by multiplication of Wg by the smooth bounded functions W^-1 and x_j/W. The commutator identity
\[
x_jJ^qg=J^q(x_jg)+q\partial_jJ^{q-2}g
\tag{1}
\]
then gives Q<infinity. Conversely Q<infinity gives g in Hq and x_jJqg in L2. Equation (1), in distributions, gives x_jg in Hq. Set
\[
b=(1,2x,2y)/W,\qquad H=(g,2xg,2yg).
\]
Since Wg=b dot H and every component of b is a Cb-infinity multiplier, Wg belongs to Hq. These maps are bounded by the closed graph theorem, or directly by the usual smooth multiplier bounds, proving equivalence. There is no numerical norm conversion in this argument.

The Q ball
\[
\mathcal B_Q(R,M)=\{k\text{ real S1}:\|k\|_2\le R,\ Q(k)\le M\}
\]
has the exact estimates
\[
\|J^qk\|_2\le Q(k),\qquad\||D|^qk\|_2\le Q(k).
\tag{2}
\]
It has Schwartz approximants inside the same ball. Indeed approximate Jqk by real S1 Schwartz functions in L2(W²dX), apply J^-q, and scale by the minimum of the two radius ratios if necessary. J^-q preserves Schwartz functions. The resulting k_n satisfy Q(k_n-k)->0 and ||k_n-k||Hq->0, so U[k_n] and their first derivatives converge uniformly.

## 2. A positive frozen N-matrix on the Q ball

The actual frozen N-matrix is
\[
\mathcal M_k=\mathcal M_*-q\operatorname{Sym}DU[k]
+(U[k]\cdot\nabla\log W)I.
\]
Using the inherited sharp Fourier interpolation constants Cs=B1/4 and Ca=B0/sqrt2, (2) gives
\[
\mathcal M_k\succeq
\left[\beta_*-qC_sR^{1/21}M^{20/21}
-C_aR^{11/21}M^{10/21}\right]I.
\tag{3}
\]
The second loss uses ||grad log W||infinity=1. The companion scalar certificate checks the bracket is strictly above 11/20 at the whole inherited reference rectangle
\[
R\le17/8750000,\quad M\le1/2,\quad
\beta_*=704955805507/10^{12}.
\tag{4}
\]
All smaller positive trial radii inherit this margin. Formula (3) is a matrix positivity condition for qualitative lifting; it is not the nonlinear Q-energy loss.

## 3. Individual smooth-coefficient high solvability

Fix a Schwartz k in the Q ball. Its velocity correction has bounded derivatives of every order and decays with its derivatives. The actual background structure was checked in `STRUCTURE013_PROOF.md`; therefore the variable transport field cX+u_*+U[k], and the unchanged density coefficient grad rho_*, satisfy the all-order hypotheses of the inherited weighted Garding calculation. That proof treats transport and source coefficients separately; no identity U[k]=U[rho_*]-u_* is required.

The positive matrix (3) gives an N-space Garding estimate with a finite constant depending on this k. The Schwartz weighted generator exists and identifies with the actual L2 generator by section 3 of the earlier bridge. Combining its Garding inequality with the actual L2 decay and integrating its semigroup gives
\[
z_k=-A_k^{-1}F,\qquad N(z_k)<\infty.
\tag{5}
\]
The constant in this qualitative estimate need not be uniform in k. Qualitative N/Q equivalence now proves Q(z_k)<infinity. This step supplies regularity before any exterior Q-energy inequality is applied; it does not infer high regularity from the L2 inverse alone.

For the Garding step, use the exact compact decomposition and its proved spatial compactness, with the coefficient u_*+U[k] in the transport term and rho_* in the source term. The matrix principal form has the positive margin (3). Smooth decaying U[k] changes only admissible compact terms. The constant noncompact negative multiplier remains favorable. Approximating the resulting compact operator by smooth finite rank functions gives a finite weak constant, without a numerical value. This suffices here because the next step replaces that bound by an actual uniform exterior barrier.

## 4. An exterior Q barrier is sufficient

Assume R=||F||2/beta2>0, and Q(F)<=n_Q. Suppose, for every real S1 Schwartz k in B_Q(R,M), the actual frozen energy satisfies, for every real S1 Schwartz test g with ||g||2<=R and Q(g)>=M,
\[
\operatorname{Re}\langle WJ^qA_kg,WJ^qg\rangle
\le-b\,Q(g)^2+C\|g\|_2^2,
\quad b>0,\ C\ge0.
\tag{6}
\]
The constants must be uniform over this ball, but the estimate is required only in the stated exterior region. For example b=b0-LQ(R,M), if the actual background Q estimate and the nonlinear inequality in `finite_rank/QNORM_NONLINEAR_BOUND.md` have been independently verified in precisely this scope.

If
\[
\boxed{bM^2\ge n_QM+CR^2,}
\tag{7}
\]
then the actual frozen inverse maps the whole Q ball into itself.

To prove it first fix a Schwartz k. Equation (5) gives the full high solution. If Q(z_k)>M, approximate z_k by the Schwartz core in the high generator graph norm. N/Q equivalence identifies the same high graph realization and core. Scale each approximant by min(1,R/||z_j||2), so its L2 norm is at most R; this tends to a factor one, and Q(z_j)>M for all sufficiently large j. Thus (6) passes to z_k by graph continuity, yielding
\[
bQ(z_k)^2\le n_QQ(z_k)+CR^2.
\]
The upward quadratic is strictly positive above its nonnegative root, which is at most M by (7). This contradicts Q(z_k)>M. Therefore Q(z_k)<=M. No Q-semigroup estimate uniform in k was used.

Now let k be any element of the Q ball and take the in-ball Schwartz approximants from section 1. The just-proved bound Q(z_kn)<=M gives a uniform Hq gradient bound. In distributions,
\[
A_kz_{k_n}=-F+(U[k]-U[k_n])\cdot\nabla z_{k_n}\in L^2.
\]
The actual maximal L2 domain and inverse therefore give
\[
\|z_{k_n}-z_k\|_2\le\beta_2^{-1}\|U[k_n]-U[k]\|_\infty\|\nabla z_{k_n}\|_2\to0.
\]
Weak compactness of WJq z_kn identifies its limit distributionally with WJq z_k, so Q(z_k)<=M by lower semicontinuity. This proves the uniform full frozen inverse and self-map on the rough Q ball.

If R=0 then F=0 and z=0, so the fixed-point conclusion is trivial and the scaling argument is unnecessary.

## 5. Fixed point, symmetry, and normalization

The Q ball is complete in L2: weak compactness of WJq k_j and distributional identification preserve its Q radius along an L2 limit. Its elements satisfy the direct Fourier gradient bound
\[
\|\nabla k\|_\infty\le S_1Q(k),\qquad
S_1=\frac5{\sqrt{11\pi}}<\frac67.
\tag{8}
\]
For k,l in the ball, the actual difference equation and inverse give
\[
\|T(k)-T(l)\|_2\le\frac{S_1M}{\beta_2}\|k-l\|_2.
\]
At M<=1/2 and beta2>=7/4 this ratio is strictly below 12/49. Banach's theorem supplies a unique fixed point in the ball whenever (6)--(7) and the stated structural/matrix inputs are established.

The actual source and operators preserve real S1 symmetry. At the fixed point, the origin expansion of the exact stationary equation gives
\(\ell(k)(\partial_y\rho_*(0)+\partial_yk(0))=0\). The exact structural certificate proves partial_y rho_*(0)>1, while (8) gives |partial_yk(0)|<3/7. Thus ell(k)=0, the total slope stays positive, and the fixed exponent c is preserved. No origin-jet restriction on the iterates is required.

This theorem is an explicit operator/fixed-point implication. It does not certify the background inequality (6), its missing commutators, or the scalar closure (7).

## Independent source-norm review

The operator agent independently reviewed `../SOURCE_Q_NORM_BOUND.md`. The b-map derivative bounds, both integer product estimates, the componentwise spectral interpolation, and the exact quadratic-weight Fourier identity are valid. All four rounded tensor-energy inputs were compared by exact rational arithmetic with the actual inherited `source013_moment_refinement/verification/result_v01.json` upper endpoints and passed. An independent execution of the scalar verifier is saved in `source_Q_independent_scalar_review.json`, giving Q(F)<1/125. This retains the original source/multiplier certificate scopes and is not a fresh source-field replay.

# Full frozen operators and a direct route from energy to existence

Status: new analytic proof for the `combined3` campaign. This note proves the operator and fixed-point implications below. It does **not** certify the missing background commutator constants and does **not** claim stationary IPM existence. Every invocation at Candidate 013 still requires the actual coefficient and numerical premises identified in section 8.

The fixed exponent is
\[
c=4076476460239181/2251799813685248,
\quad q=21/10,\quad W=(1+4|X|^2)^{1/2},
\quad N(f)=\|J^q(Wf)\|_2.
\]
Fourier transforms in the proofs are unitary, \(\widehat f(\xi)=(2\pi)^{-1}\int e^{-ix\cdot\xi}f(x)\,dx\). Thus \(R_j\) has symbol \(i\xi_j/|\xi|\), and
\[
U[f]=(-R_1R_2f,R_1^2f).
\]
S1 denotes real functions even in \(x\) and odd in \(y\). Write
\[
A_kf=(cX+u_*+U[k])\cdot\nabla f-f+Q_*f,
\qquad Q_*f=\nabla\rho_*\cdot U[f].
\]

## 1. The actual maximal-domain L2 generator

**Lemma 1.** Suppose \(u_*\) is globally Lipschitz and divergence free, and \(\nabla\rho_*\in L^\infty\). For every \(k\) with \(Wk\in H^q\), put \(v_k=cX+u_*+U[k]\). Then \(A_k\) generates a strongly continuous group on \(L^2\), with domain
\[
D(A_k)=\{f\in L^2:v_k\cdot\nabla f\in L^2\text{ in distributions}\}.
\tag{1}
\]
The space \(C_c^\infty\) is a core. The corresponding real S1 statements hold if the coefficients have the stated IPM parities.

**Proof.** Multiplication by \(W^{-1}\in C_b^\infty\) is bounded on \(H^q\), so \(k\in H^q\). Riesz multipliers are bounded on this unweighted space, and \(q>2\) gives \(U[k]\in C_b^1\) by Sobolev embedding. Its divergence is zero, since its Fourier symbol \((\xi_1\xi_2/|\xi|^2,-\xi_1^2/|\xi|^2)\) is perpendicular to \(\xi\). Hence \(v_k\) is globally Lipschitz, has at most linear growth, and has divergence \(2c\).

Let \(\Phi_t\) be its complete flow. The group \(P_k(t)f=f\circ\Phi_t\) satisfies
\[
\det D\Phi_t=e^{2ct},\qquad \|P_k(t)f\|_2=e^{-ct}\|f\|_2.
\tag{2}
\]
Strong continuity follows first for compactly supported continuous functions and then by density and (2). Its generator acts as \(v_k\cdot\nabla\) on \(C_c^\infty\).

Here is the domain/core argument. The distributional operator in (1) is closed. For a function in its domain, multiplication by radial cutoffs \(\chi_R\) gives graph convergence, because
\[
v_k\cdot\nabla(\chi_R f)=\chi_Rv_k\cdot\nabla f+(v_k\cdot\nabla\chi_R)f,
\]
and \(|v_k\cdot\nabla\chi_R|\le C\) on \(R\le|X|\le2R\), while the L2 mass of \(f\) on this annulus tends to zero. A compactly supported graph element can then be mollified. The commutator
\[
v_k\cdot\nabla(\eta_\epsilon*f)-\eta_\epsilon*(v_k\cdot\nabla f)
\]
is uniformly bounded on L2 by a constant times \(\|Dv_k\|_\infty\), and tends to zero in L2: prove this first for smooth compactly supported \(f\), and then use its uniform bound and density in L2. A final compact cutoff preserves the convergence. Consequently \(C_c^\infty\) is graph dense in the maximal distributional domain. The flow generator, a closed extension of the test-function operator, therefore agrees with that domain. Equivalently one may characterize distributional solutions using the same mollification and (2).

The operator \(Q_*\) is bounded on L2, since \(\|U[f]\|_{L^2(\mathbb R^2;\mathbb R^2)}\le\|f\|_2\). The bounded perturbation theorem applied to \(v_k\cdot\nabla-1\) proves the claim for \(A_k\), with the same domain and core. Reflection equivariance of \(v_k\), and invariance of \(Q_*\), give the S1 restriction. Reality is preserved throughout. ∎

**Domain caution.** The maximal domains for different \(k\) are not asserted to be equal. The difference identities used below follow from distributional equations and high regularity, which is sufficient.

## 2. Uniform L2 solvability

**Lemma 2.** In addition to Lemma 1, suppose the actual background quadratic form satisfies, for all test functions,
\[
(c+1)\|f\|_2^2-\operatorname{Re}\langle Q_*f,f\rangle
\ge\beta_2\|f\|_2^2,\qquad\beta_2>0.
\tag{3}
\]
Then for every such \(k\),
\[
\|e^{tA_k}\|_{2\to2}\le e^{-\beta_2t}\quad(t\ge0),\qquad
z=-A_k^{-1}F=\int_0^\infty e^{tA_k}F\,dt,
\quad \|z\|_2\le\|F\|_2/\beta_2.
\tag{4}
\]

**Proof.** Integration by parts on the core gives
\[
\operatorname{Re}\langle A_kf,f\rangle
=-(c+1)\|f\|_2^2+\operatorname{Re}\langle Q_*f,f\rangle,
\]
independently of \(k\). Core density extends this estimate to (1). Differentiate the norm along the group for domain data, apply Gronwall, and extend by density. The integral in (4) converges in L2. Closedness and integration up to finite \(T\) show it is in \(D(A_k)\) and has image \(-F\); exponential decay gives injectivity and the inverse bound. ∎

This supplies the uniform L2 inverse by an actual full-operator argument. A separate frozen-origin inverse is unnecessary.

## 3. Smooth weighted generators

Assume the inherited qualitative background regularity in its precise all-order form: for some \(0<\gamma<1\),
\[
|D^j\nabla\rho_*|+|D^jDu_*|\le C_j\langle X\rangle^{-\gamma-|j|}
\quad\text{for every multi-index }j.
\tag{5}
\]
For a real S1 Schwartz coefficient \(k\), the conjugated operator on \(H^q\) is
\[
W A_k W^{-1}=v_k\cdot\nabla-(1+v_k\cdot\nabla\log W)+Q_*+E_*,
\quad E_*f=\nabla\rho_*\cdot[W,U]W^{-1}f.
\tag{6}
\]
The smooth transport part has a complete flow with bounded derivatives through every finite order on bounded time intervals. Its scalar coefficient in (6) has bounded derivatives. The flow formula therefore defines a C0 group on Hq, by integer-order chain rules through order 3 and interpolation. Schwartz functions are invariant for this transport group and form a core. The pointwise vector field grows at most linearly and its flow and inverse have polynomially bounded derivatives, which justifies preservation of Schwartz functions.

The background operator \(Q_*\) is bounded on Hq by (5). The compact weighted-commutator lemma inherited as combined2 NR-2, Lemma E, proves boundedness of \(E_*\) on Hq because the weight exponent \(1<1+\gamma\). Its proof uses the actual decaying coefficient \(\nabla\rho_*\): the near-diagonal kernel has size \(C\langle x\rangle^{-\gamma-1}|x-y|^{-1}\), and the off-diagonal kernel is Hilbert--Schmidt. Differentiation through order 3 and interpolation give Hq boundedness. This use does not assert boundedness of \(WU W^{-1}\) alone at the critical weight.

Bounded perturbation now constructs the Hq generator of (6), with the same core. Under multiplication by \(W^{-1}\), its semigroup equals the L2 semigroup of Lemma 1: prove generator intertwining on the core and extend by graph closure and uniqueness of the L2 evolution. In particular its Hq-domain elements belong to the L2 maximal domain after division by W.

## 4. Quantitative energy supplies the rough-coefficient high inverse

The following bridge avoids assuming qualitative high solvability before checking the energy.

**Theorem 3.** Suppose (3), (5), and \(WF\in H^q\). Let
\[
\mathcal B(R,M)=\{k\text{ real S1}:\|k\|_2\le R,\ N(k)\le M\},\quad R,M>0.
\]
Suppose for every real S1 Schwartz \(k\in\mathcal B(R,M)\) and real S1 Schwartz \(f\), the actual full form satisfies
\[
\operatorname{Re}\langle J^q(WA_k f),J^q(Wf)\rangle
\le-b\,N(f)^2+C\|f\|_2^2,
\quad b>0,\ C\ge0,
\tag{7}
\]
with the same constants for all these \(k\). The pairing is the energy form extended from test functions; an Hq function need not yield a literal L2 first term. Then the actual L2 solution \(z=-A_k^{-1}F\), for every \(k\in\mathcal B(R,M)\), has \(N(z)<\infty\) and
\[
bN(z)^2\le N(F)N(z)+C\|F\|_2^2/\beta_2^2.
\tag{8}
\]

**Proof.** First take a Schwartz \(k\). Section 3 supplies the high generator and identification. On its core, (7) gives
\[
E'(t)\le-2bE(t)+2C\|h(t)\|_2^2,
\quad E(t)=N(h(t))^2.
\]
For any \(0<\omega<\min(b,\beta_2)\), (4) implies
\[
E(t)\le e^{-2\omega t}\left(E(0)+\frac{C}{\beta_2-\omega}\|h(0)\|_2^2\right).
\tag{9}
\]
The inequality extends by high graph density. Hence the semigroup integral (4) converges in the weighted Hq space, and testing its stationary equation gives (8).

For a general \(k\in\mathcal B(R,M)\), approximate \(Wk\) in Hq by real S1 Schwartz functions. Divide these by W and scale each by
\[
\min\{1,R/\|\widetilde k_n\|_2,M/N(\widetilde k_n)\}
\]
(omitting ratios with zero denominator). This produces Schwartz \(k_n\) in the same ball with \(N(k_n-k)\to0\). In particular \(U[k_n]\to U[k]\) uniformly. By (8), the solutions \(z_n=-A_{k_n}^{-1}F\) have a uniform N bound, namely the positive root of \(bX^2-N(F)X-C\|F\|_2^2/\beta_2^2=0\).

Consequently \(\nabla z_n\) is uniformly L2 bounded. In distributions,
\[
A_kz_n=-F+(U[k]-U[k_n])\cdot\nabla z_n\in L^2.
\]
The domain characterization (1) therefore puts \(z_n\) in \(D(A_k)\), and (4) gives
\[
\|z_n-z\|_2\le\beta_2^{-1}\|U[k_n]-U[k]\|_\infty\|\nabla z_n\|_2\longrightarrow0.
\]
Weak compactness in weighted Hq identifies its limit with z, and lower semicontinuity gives (8): equivalently every \(N(z_n)\) is at most the positive root, so \(N(z)\) is too. ∎

For the inherited route-Q proof, (7) follows from the actual base H4 inequality and the inherited HF-Q inequality with
\[
b=b_0-L_B(R,\overline K)>0,\quad C=C_0,
\tag{10}
\]
provided \(\overline K\) is the certified CE bound for \(\|D^qk\|_2\) on this same ball. The strict graph witness is one means of certifying this CE bound. It is not an additional analytic assumption needed by Theorem 3. No separate rough Hq-generator, positive reference-ball matrix, or uniform Garding theorem is required for this bridge once the uniform quantitative form (7) is established.

## 5. Fixed point by a verified L2 contraction

For any f with \(u=Wf\in H^q\), Fourier Cauchy--Schwarz gives
\[
\|u\|_\infty\le\frac{N(f)}{2\sqrt{\pi(q-1)}},\qquad
\|\nabla u\|_\infty\le\frac{N(f)}{2\sqrt{\pi(q-1)(q-2)}}.
\]
Since \(W\ge1\), \(\|\nabla\log W\|_\infty=1\),
\[
\|\nabla f\|_\infty\le C_WN(f),\quad
C_W=\frac{10+\sqrt{10}}{2\sqrt{11\pi}}<\frac{28}{25}.
\tag{11}
\]
The small certificate `verify_embedding_constants.py` checks the last rational comparison using \(\pi>157/50\) and \(\sqrt{10}<31623/10000\). It involves no unvalidated floating-point computation.

**Theorem 4.** In Theorem 3 take \(R=\|F\|_2/\beta_2\). If
\[
bM^2\ge N(F)M+CR^2,\qquad C_WM<\beta_2,
\tag{12}
\]
then there is exactly one fixed point of \(T(k)=-A_k^{-1}F\) in \(\mathcal B(R,M)\). It gives an exact stationary solution \(\rho_*+k\).

**Proof.** Equations (4), (8), and the positive-root comparison prove self-mapping. The ball is complete in the L2 metric: an L2-convergent sequence has a weakly convergent weighted-Hq subsequence, its distributional limit is the same, and lower semicontinuity preserves both radii and parities. For k,l in the ball, \(z_l=T(l)\) has bounded gradient by (11); hence \(A_kz_l=-F+U[k-l]\cdot\nabla z_l\in L^2\), so \(z_l\in D(A_k)\). Applying (4) to the difference gives
\[
\|T(k)-T(l)\|_2\le\frac{C_WM}{\beta_2}\|k-l\|_2.
\]
Banach's theorem supplies the fixed point. Its distributional equation is precisely the stationary equation. Since q>2, the correction and its velocity are C1 and the equation holds pointwise. ∎

At the inherited \(\beta_2\ge7/4\), \(M\le1/2\), the contraction ratio is strictly below \(8/25=0.32\). Thus, **after self-map closure is supplied**, this part of the existence argument has an explicit large margin. A new Schauder or weak-continuity certification is unnecessary.

## 6. Origin normalization on the full S1 ball

Let \(a_0=\partial_y\rho_*(0)>0\), and assume the actual center is normalized by \(c+\partial_y(u_*)_2(0)=1\). The parity of a C1 S1 correction gives \(k(0)=U[k](0)=0\). Its velocity derivative at zero is diagonal, with entries \((-\ell(k),\ell(k))\), where \(\ell(k)=\partial_yU_2[k](0)\).

For a fixed point, expand the stationary equation to first order along the y axis. No second derivatives are required. The coefficient of y gives
\[
\ell(k)\,(a_0+\partial_y k(0))=0.
\tag{13}
\]
Consequently \(\ell(k)=0\) whenever \(a_0>C_WM\). The latter is implied by \(a_0>1\), \(M\le1/2\), using (11). The actual Candidate 013 lower for \(a_0\) must be read from its exact input/certificate; no sampled slope is substituted here. The fixed-point ball need not impose an ell constraint during iteration. For a nonfixed input, T need not preserve that hyperplane.

The physical density slope \(a_0+\partial_yk(0)\) remains positive. This normalization fixes the vertical strain and preserves the specified exponent c; it does not assert that the density slope is exactly its numerical-center value.

## 7. Analytic near/far assumptions from coefficient structure

These lemmas give explicit analytic proofs of two qualitative obligations that combined2 retained.

**Lemma 5 (erflog near coefficient).** Suppose (5) and \(u_*\) is smooth. Set
\[
\widetilde a(X)=\frac{4u_*(X)\cdot X-c}{1+4|X|^2},\quad
\chi(r)=\frac12\operatorname{erfc}\left(\frac{\log(r/\sqrt8)}{L}\right),\quad
L=\frac{\log8}{2\sqrt\pi},\quad\chi(0)=1.
\]
Then \(a_n=\chi(|X|)\widetilde a\) is Schwartz on \(\mathbb R^2\).

**Proof.** At infinity, every radial derivative of chi is a finite sum of products of a power of \(r^{-1}\), a polynomial in \(\log r\), and \(\exp[-(\log(r/\sqrt8)/L)^2]\), or the erfc tail itself. Completing the square shows that each is bounded by \(C_{j,N}r^{-N}\) for every N. At zero the same statement holds for \(1-\chi\), with \(r^N\) in place of \(r^{-N}\); the erfc symmetry reduces it to the same Gaussian tail. Thus its extension is smooth and flat at zero. The factor \(\widetilde a\) is smooth and has polynomially bounded derivatives by (5). Leibniz proves all Schwartz seminorms finite. ∎

In particular a_n has bounded Hessian, an L1 Fourier transform, and finite fourth absolute Fourier moment, which is exactly N1 in combined2 `NEAR_CHECK_v02.md` section 3. All whole-plane Sobolev derivatives exist and Plancherel applies. The core split is an identity,
\[
a_n=-a_c+a_r,\quad a_c=c/(1+4|X|^2),\quad a_r=a_n+a_c.
\]
Here a_c and a_r belong to every Hs. **a_r is generally not Schwartz**: its tail contains a_c. This does not prevent the inherited derivative identities or Fourier-moment estimates, whose H6 assumptions hold. The noncompact support of the erflog cut is therefore handled by a global decay proof, with no uncharged truncation. This discharges the qualitative N1/core-split/decay premises once the actual coefficient structure is established. It supplies no numerical derivative upper.

**Lemma 6 (far Fourier finiteness).** Let \(0<\gamma<2\) and let a be smooth with \(|D^\alpha a(x)|\le C_\alpha\langle x\rangle^{-\gamma-|\alpha|}\) for all multi-indices. Its distributional Fourier transform is an ordinary function, with no delta mass at zero, satisfying
\[
|\widehat a(\xi)|\le C|\xi|^{\gamma-2}\quad(0<|\xi|\le1),\qquad
|\widehat a(\xi)|\le C_N|\xi|^{-N}\quad(|\xi|\ge1)
\tag{14}
\]
for every N. Every nonnegative absolute polynomial Fourier moment is finite.

**Proof.** Use a smooth dyadic partition of unity with annular radii \(2^j\). For a_j the jth piece, scaling and integration by parts give, for every K,
\[
|\widehat a_j(\xi)|\le C_K2^{(2-\gamma)j}(1+2^j|\xi|)^{-K}.
\]
Summing radii below and above \(|\xi|^{-1}\) proves the first bound; integration by parts to arbitrary order, treating the finitely many inner pieces as well, proves the second. The series converges off zero. The first bound is locally integrable because gamma>0. Dominated convergence against test functions identifies that function with the distributional transform: one can dominate the summed absolute contribution in frequency on compact sets using the displayed dyadic estimate with K>2. No point-supported distribution remains. Finally integrate (14) in polar coordinates, choosing N larger than the desired moment plus two. ∎

Under (5), \(\widetilde a\) and the far piece \(a_f=(1-\chi)\widetilde a\) meet Lemma 6 with the inherited \(\gamma=1-1/c\in(0,1)\). The compact windowed far piece is smooth and compactly supported. The remaining far tail retains the same symbol bounds. Thus the Fourier inversion, absolute moments, and Fubini premises of the inherited far forms hold qualitatively. Specific derivative envelopes and all numerical AE/CS-W/tail bounds still require their actual certificates. This lemma does not turn archived numerical summaries into a new numerical proof.

## 8. Exact status and dependencies

Newly proved here, in full stated scope:

1. The actual L2 generator, core, maximal distributional domain, and uniform inverse under the background signed form (3).
2. The high inverse and its quantitative estimate obtained directly from a uniform verified full form (7), including passage from smooth frozen coefficients to every coefficient in the Sobolev ball.
3. A complete Banach fixed-point alternative, with contraction ratio below 0.32 at the inherited radii, requiring no common full L2 domains or additional Schauder premise.
4. The normalization identity and a sufficient quantitative positive-slope condition.
5. Qualitative N1 and erflog localization from the actual background's all-order smoothness/decay; far Fourier finiteness from the same structure.

The actual application at Candidate 013 still needs the exact source/evaluator identities and their structural proofs, a certified signed L2 bound, the complete quantitative full-form estimate (7) with certified constants, source norm certificates, CE/HF-Q constants if route Q is used, positive origin slope, and the scalar self-map inequality (12). This note is not an existence certificate. In particular it does not bound any missing H4-REST contribution and does not certify an invariant ball.

Inherited primary proof sources: combined2 `THEORY_NEW_RESULTS.md`, NR-1/NR-2; `theory_agent_2/notes/T2_CEPS_v02a.md`, `T2_PS1_v01.md`, `T2_X4_v01.md`; and `theory_audit/reports/SOURCE013_CHAIN_CONDITIONS_v05.md`. The original source formulation's extra graph assumptions are replaced here only where an explicit proof above permits doing so.

External primary background checked during this work: Dong Li, *On Kato--Ponce and fractional Leibniz*, [arXiv:1609.01780](https://arxiv.org/abs/1609.01780). This note does not take any explicit commutator constant from that paper. The new quantitative inequalities above are derived directly.

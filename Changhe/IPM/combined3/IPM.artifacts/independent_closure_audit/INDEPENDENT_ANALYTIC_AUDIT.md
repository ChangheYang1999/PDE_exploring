# Independent audit of the local-Q existence argument

Status at 2026-11-05 01:58 UTC: **the complete analytic dependency chain and its actual numerical premises pass this independent audit.** The local-Q argument establishes the fixed-parameter stationary theorem stated below. The main report receives a separate publication audit. No result from the isolated residual-pairing experiment is used here.

This audit read the full campaign prompt and independently reconstructed the identities, constants, spaces, and fixed-point mechanism listed below. It also read the actual numerical consumer and its principal coefficient producers. Its scope is the new local-Q proof, rather than a declaration that the older H4-REST obligations have been verified.

Fix

\[
c=4076476460239181/2251799813685248,\quad q=21/10,
\quad\delta=1/10,\quad W^2=1+4|X|^2,
\quad Q(g)=\|WJ^qg\|_2.
\]

## 1. Exact local identity and coefficient prices

For \(f=J^\delta g\), \(h=(1-\Delta)f\), the IPM multiplier gives

\[
U[\Delta f]=(f_{xy},-f_{xx}),\qquad
b\cdot U[h]=b\cdot U[f]-K:D^2f,
\quad K=\begin{pmatrix}-b_y&b_x/2\\b_x/2&0\end{pmatrix}.
\]

The linear dilation commutator is \(cq\Delta f\). The first two background-velocity Taylor terms combine exactly to

\[
-q\operatorname{div}(S\nabla f)
+\frac{q\delta}{2}D^2u:D^3J^{\delta-2}g,
\qquad S=\operatorname{Sym}Du.
\]

Consequently the joint highest form is precisely
\(-\int W^2\Delta f\,(M:D^2f)\), with the matrix M appearing in the prompt. The identities

\[
(\operatorname{tr}H)(M:H)
=\sum_k(He_k)^TM(He_k)+(\operatorname{tr}M)\det H,
\]

\[
\int a\det D^2f
=\int a_{xy}f_xf_y-\tfrac12\int(a_{xx}f_y^2+a_{yy}f_x^2)
\]

and

\[
Q(g)^2=\|WD^2f\|_2^2+2\|W\nabla f\|_2^2+\|Wf\|_2^2
-8\|\nabla f\|_2^2-16\|f\|_2^2
\]

give exactly the signs and factors in `../operator_theory/LOCAL_Q_BACKGROUND_IDENTITY_v01.md`. In particular the v-cross term is a local quadratic form after integration by parts; it should not be charged again as an independent first-order norm product.

For the actual coefficient envelope producer I independently checked the conservative triangle bounds

\[
K_1\le 8\sqrt2(M_\infty+s)+4H_u+4\sqrt2B_0+4H_1
+2q(1+1/\sqrt2)H_1+\tfrac{1+q}{2}H_2,
\]

\[
K_0\le4\{(8-2q)c+4+B_0+(2-q/2)H_1/2\},
\quad M_\infty=1+(2-q)c,
\]

using the definitions in `../certify_local_energy_coefficients.py` and \(s=3/2\). These discard favorable negative beta corrections. The reduction \(\Delta u=(\rho_{xy},-\rho_{xx})\) is exact. The apparent fourth velocity derivatives cancel: only the displayed density and second velocity derivatives are needed.

The certificate's saved \(H_u\) on a radial leaf is its right endpoint times a uniform \(|D^2u|\) cover. Multiplying it by \(W(r_\mathrm{left})/r_\mathrm{left}\) therefore safely bounds \(W|D^2u|\) throughout that leaf. The analogous origin and exterior endpoint transformations are valid.

The implication \(d\ge c+1\) from \(\|S\|_{\infty,op}\le3/2<c\) follows by integrating \(X^TS(tX)X\) along each ray and using \(u(0)=0\). It uses no inherited numerical strain bound.

## 2. Weighted U, moments, and fractional terms

For every central-odd input the Fourier angular mean vanishes. If \(F=\widehat f\), \(m(\theta)=\cos\theta(\sin\theta,-\cos\theta)\), direct angular integration gives

\[
\int |\partial_\theta(mF)|^2d\theta
=\int\cos^2\theta(|F_\theta|^2+2|F|^2)d\theta
\le3\int|F_\theta|^2d\theta.
\]

The radial part is bounded with constant one. Angular Poincare thus proves \(\|WU[f]\|_2\le\sqrt3\|Wf\|_2\), including the critical coordinate weight. This is a joint velocity estimate, not a claim for arbitrary single Riesz transforms at that weight.

The lower source split is consequently

\[
|\langle W^2h,b\cdot U[f]\rangle|
\le B_\mathrm{near}\|f\|_2Q(g)
+\sqrt3B_\mathrm{far}\|Wf\|_2Q(g).
\]

Its far term consumes the explicit negative weighted-f allowance and costs
\(3B_\mathrm{far}^2/[4(c+1-\beta)]\). This is separate from the complete source commutator, which is fully retained.

The source and transport Taylor estimates were independently checked with the unitary Fourier normalization \((2\pi)^{-1}\) in dimension two. In particular the homogeneous Wiener inequality is

\[
M_m(v)\le\tfrac12\sqrt{\|D^mv\|_2\|D^{m+2}v\|_2}.
\]

The fractional version and its constant follow by Cauchy-Schwarz with \(1+(|\xi|/a)^4\) and optimization in a. All factors in the source estimate, including the four times \(M_{s-1}(b)\) weight-derivative contribution, are present.

The repeated third derivative of \(J^q\) has the bound
\(2q\delta/\sqrt{2-\delta}\). The resulting third-Taylor prefactor
\(q\delta/[3\sqrt{2-\delta}]<51/1000\) is valid for both the remainder and its output-frequency derivative. Differentiating the output variable at fixed input frequency does not differentiate the input U multiplier or input derivative.

The background has growth \(u\in S^{1/c}\), and \(b\in S^{-\gamma}\), \(\gamma=1-1/c>0\). The stated radial-cutoff derivative seminorms tend to zero. This validates the Fourier manipulations for growing \(u\) and \(xb\), without assuming either belongs to L2. In the velocity Taylor identity the non-divergence-free cutoff error tends uniformly to zero after applying the weight.

I also independently checked the global source norm identities

\[
\|D^2(xb)\|_2^2=\|r\nabla\Delta\rho\|_2^2+4\|\Delta\rho\|_2^2,
\]

\[
\|D^4(xb)\|_2^2=\|r\nabla\Delta^2\rho\|_2^2+16\|\Delta^2\rho\|_2^2.
\]

Their cross terms vanish because \(\int(x\cdot\nabla v)\Delta v=0\) in dimension two. The exact decay makes the omitted boundary terms vanish. These are whole-plane identities; the producer correctly bounds the actual Cartesian Laplacian combinations on the separate endpoint regions instead of applying Parseval there.

## 3. Nonlinear estimate and forcing

The symmetrized unweighted commutator kernel, after its Bessel principal term is removed, contains

\[
\frac i2\eta\cdot\widehat a(\zeta)
\{t^q-t^{-q}-q(t-t^{-1})\},\qquad t=J\xi/J\eta.
\]

The fresh scalar inequality with upper \(53/50\), the Lipschitz inequality \(|J\xi-J\eta|\le|\xi-\eta|\), divergence freeness, and the two possible minimum frequencies give the core constant \((53/100)S_1\),
\(S_1=5/\sqrt{11\pi}\). The Hilbert-Schmidt calculation includes both frequency contributions and the convolution normalization. No test parity is used.

The principal strain angular squared integral is \(\pi/8\), compared with \(2\pi\) for a scalar moment; therefore \(C_s=B_1/4\) is correct. The joint velocity angular integral is \(\pi\), giving \(C_a=B_0/\sqrt2\).

I independently reconstructed the coordinate commutator identity and the X=Y+Z estimate in `../finite_rank/QNORM_NONLINEAR_BOUND.md`. Its product interpolation powers reduce to \(1-1/q\); using \(Q(g)\ge M\) is in the correct direction. The final nonlinear coefficient \(L_Q(R,M)\) is an outside-ball bound and is not promoted to global dissipativity.

For the forcing, writing \(\nu WF=(F,2xF,2yF)\) gives the exact identity

\[
Q(F)^2=\|J^q(\nu WF)\|_2^2
-8q\|J^{q-1}F\|_2^2
-4q(q-2)\|\nabla J^{q-2}F\|_2^2.
\]

Both corrections have the claimed nonpositive sign. I checked the inverse-weight derivative constants, integer frame product estimates, and interpolation leading to the certified upper \(Q(F)<759/100000\). This uses the actual inherited source tensors, not a CE multiplier or an existence premise.

## 4. Actual generators and the fixed point

For any input in the Q ball, \(U[k]\in H^q\subset C_b^1\); hence the drift is complete and globally Lipschitz, with divergence \(2c\). The actual flow group, radial cutoffs, and mollifier commutator establish the maximal distributional L2 domain and compact smooth core. The source operator is bounded on L2. The certified direct L2 form therefore gives the actual uniform inverse, rather than just formal coercivity.

For a smooth frozen input, the transport flow acts strongly continuously on the coordinate Hq space. The exact coordinate commutator proves its equivalence with Q. The joint weighted U bound and smooth bounded source coefficients make the source bounded on Q. Its Dyson semigroup coincides with the actual L2 semigroup. Truncated resolvent flow integrals provide the asserted Q-generator core.

The forced trajectory
\(g(t)=\int_0^t e^{sA_k}F\,ds\) has the correct positive sign and solves
\(g'=A_kg+F\). Its finite-time L2 radius is strict. Thus Q-graph approximation preserves the strict constraints on every interval with \(Q(g)>M\), where the exterior energy estimate applies. A positive self-map margin prevents crossing. Weak compactness then places the actual stationary L2 inverse in the Q ball. This avoids assuming high regularity before proving it.

In-ball Schwartz approximations converge in Q and in C1 velocity. The distributional difference equation and maximal L2 domain identify the rough-input inverse; uniform Q bounds pass by lower semicontinuity. The ball is complete in L2. The contraction coefficient is exactly
\(S_1M/\beta_2\), because \(\|U[k-l]\|_2\le\|k-l\|_2\).

At a fixed point the stationary equation is continuous. Its first-order expansion on the y axis, using C1 regularity only, gives
\(\ell(k)(\rho_{*,y}(0)+k_y(0))=0\). The certified center slope exceeds one and \(S_1M<3/7\) for \(M\le1/2\), so the normalization \(\ell(k)=0\) follows. No origin-strain hyperplane was assumed during iteration.

The actual finite background formulas have the same divergence/curl and sublinear growth as the canonical symmetric-radius velocity. Their entire harmonic difference is constant and odd, hence zero. Adding the ordinary L2 correction velocity preserves this convention. A global streamfunction exists on the simply connected plane and satisfies the requested elliptic equation; a Darcy pressure follows as well. The fixed rational exponent is unchanged.

There is also a direct quantitative streamfunction construction. Define
\(\psi_k=(-\Delta)^{-1}\partial_xk\) by its Fourier multiplier. Since \(J^q\widehat k\) is central odd and belongs to frequency H1, angular Poincare gives

\[
\|J^q\psi_k\|_2\le\|xJ^qk\|_2\le M/2,
\qquad \|\nabla J^q\psi_k\|_2\le\|J^qk\|_2\le M.
\]

Thus \(\psi_k\in H^{q+1}\), with norm at most \(\sqrt5M/2\). Its ordinary multiplier satisfies \(-\Delta\psi_k=\partial_xk\) and \(U[k]=\nabla^\perp\psi_k\). Consequently

\[
\psi=\partial_{xy}\chi_{007}+\partial_x\phi+\psi_k
\]

is an explicit streamfunction for the requested full elliptic system and is locally C2,alpha for every alpha<1/10. This removes even an abstract choice of streamfunction constant from the correction: the L2 correction streamfunction is canonical.
The complete numerical-free argument is saved in `EXPLICIT_STREAMFUNCTION.md`.

## 5. Signed exterior matrix shortcut

The exact largest eigenvalue of K is

\[
\theta(b)=(|b|-b_y)/2.
\]

Therefore the uniform exterior bound is

\[
M(X)\ge\left[1+(2-q)c-\frac c{1+4r^2}
-\frac{|u|}{r}-q\|S\|_{op}-\theta(b)\right]I.
\]

The completed direct L2 certificate bounds
\(\theta(b)\le n_\theta r^p\) uniformly beyond its endpoint, where \(p=1/c-1<0\). Its normalized remainder bounds are valid on the full exterior, rather than just at the endpoint. The new far expansion terms for \(u/r\) and S each have negative powers. Thus substituting r=30000 bounds every displayed loss uniformly for all larger radii.

The independent replay `signed_matrix_far_audit.json` checks all source/code/result bindings and all five scalar rows. It verifies

\[
M(X)>0.720066108588564\,I\quad(r\ge30000).
\]

The independent `matrix_prefix_audit.json` now also verifies the complete origin calculation, all711 raw base panels and996 adaptive leaves, every nonnegative principal minor, exact radial coverage, source/code/chunk bindings, and agreement with an isolated fresh replay. The origin, prefix, and exterior overlap and exhaust the plane. Thus the actual whole-plane bound M>=7/10 is certified; the exterior shortcut alone is not substituted for that conjunction.

## 6. Completed numerical and provenance conditions

The reviewed scalar exponents are exactly

\[
e_{bg}=e_{far}+(K_1+B_{near})r^{20/21}+K_0r^{40/21}
+\tfrac{q\delta}{2}W_{u2}r^{10/21}+T_3r^{11/21}
+qH_1r^{10/21}+c_qA_2r^{20/21}+c_qA_qr.
\]

The numerical consumer and independent reconstructions establish the actual inputs and
\(b=7/10-e_{bg}-L_Q>0\), \(bM^2-nM>0\), and \(S_1M<\beta_2\), with
\(R=381377/10^{12}\), \(\beta_2=2087491/10^6\), \(n=759/100000\).
The exact L2 radius condition \(R\beta_2>7961207/10^{13}\) holds. The AM-GM tangent conversion to a global background Garding pair is correct and preserves the same scalar margin at the chosen radii.

Every required whole-plane input is now complete: direct L2 and its independent replay; actual forcing tensors/Q bound; exact structure; source envelopes and their fresh replay; raw far-source bounds; the origin/711-panel/signed-exterior matrix certificate and isolated replay; all599 local coefficient panels plus both endpoints; and all2303 source derivative/moment panels plus both endpoints. Every raw cover, code/source binding, and endpoint input used by the final scalar consumer was checked. No partial directory supplies a whole-plane premise.

My independent `verify_final_join.py` imports neither the final consumer nor the nonlinear calculator. It reassembles all2303 source energy rows and endpoint tails, reconstructs the source and velocity moments, evaluates the nonlinear formula independently, and recomputes every exterior rate. The result `final_join_audit.json` agrees with the main consumer to1e-50 and gives

\[
e_{bg}<0.157652149442256,\quad L_Q<0.227998901021981,
\]

\[
b>0.314348949535764,\quad
bM^2-nM>0.026014405458218,
\quad S_1M/\beta_2<0.122234941323522.
\]

The conventional global background pair can be coarsened to exact rationals

\[
\epsilon=3491/31250,\quad C=28427625600,\quad
b_0=7/10-\epsilon=9192/15625,\quad L_Q<57/250.
\]

Thus the frozen exterior form has b'=11259/31250 with this weak C. My separate `verify_rational_ball.py` reconstructs the tangent epsilon/C from my own rates and verifies independently

\[
R\beta_2-f_2=355107/10^{18}>0,
\]

\[
b'M^2-nM-CR^2
=\frac{8129427150678683343}{312500000000000000000}
=0.0260141668821717866976>0.
\]

The exact rational contraction upper is123/1000, using pi>157/50. The original weighted norm satisfies N2<355363/10^6<.387. These checks are recorded in `rational_ball_audit.json` and bind the main rational certificate as well.

An apparent earlier screening discrepancy was also checked: the FLOAT number16.45 was a sampled Cartesian componentwise angular-l1 majorant for H1, not a sampled value of the true Hessian norm. The certified14.83002138 uses polar Hessian components before angular enclosure and can validly be smaller. The polar/Cartesian reduction was independently checked; no contradiction or uncharged numerical estimate remains.

The inherited gradient-structured double-Riesz Hilbert-Schmidt identity is an explicit established input from combined2's reference R1. The new direct L2 certificate evaluates its norms on the actual Candidate013; it does not transfer Candidate007 numerical values. The final report should preserve that provenance.

The old compact-commutator estimates and old H4-REST route are neither proved by this audit nor silently adopted. Their independent finite-rank results remain useful deliverables, but the local-Q proof replaces their decomposition by the exact joint identity above. No TIS/TII/Cvs3/Ew price should be added again in this branch.

The residual-pairing experiment is separate and uncertified numerically. Its frequency-split improvement is not an input to this existence argument.

## Audit conclusion

No unresolved mathematical premise remains in the preferred local-Q argument. The forced-evolution bridge applies with the strict rational inequalities above, and Banach contraction gives a unique real S1 correction in

\[
\|k\|_2\le381377/10^{12},\qquad Q(k)\le3/10.
\]

The resulting actual canonical-velocity solution rho=rho*+k solves the stationary IPM system at the unchanged exact c. It has the required original weighted H^(21/10) regularity, derived origin strain ell(k)=0, and positive density slope. The explicit correction streamfunction belongs to H^(31/10), with norm at most3/10. Uniqueness is within this auxiliary Q/L2 ball; no larger-ball or global uniqueness is claimed.

This verdict concerns the precisely bound proof and certificate chain. It does not certify unrelated exploratory estimates. The final main report must reproduce this theorem and its hypotheses faithfully and preserve the qualifications below.

## Auxiliary old-decomposition and finite-rank audit

I independently reviewed `../EXACT_COMPACT_DECOMPOSITION.md`, including the displayed exact joint Fourier kernel. Its algebra is correct. In particular \(m^2+p^2=1\), with \(m=|D|J^{-1}\), gives

\[
q\langle Smv,mv\rangle
=q\langle Sv,v\rangle-q\langle Spv,pv\rangle+T_{IS}(v).
\]

Replacing the variable scalar energy by its Riesz-distributed version gives exactly the stated TII double commutator. The source remainder double-Riesz sign agrees with the direct L2 decomposition. The favorable constant term \(-qcJ^{-2}\) is genuinely noncompact on the whole plane and is correctly retained outside the compact remainder.

For qualitative compactness I read the actual inherited NR2 proof in `combined2/IPM.artifacts/THEORY_NEW_RESULTS.md`, not only the PROVED labels. K3 is explicitly restricted to the BG-reg coefficient class; the actual exact finite-profile structure satisfies it. The negative-order localized remainders for Ctr, Caw, and Cvs1 have spatially vanishing coefficient derivatives. The spatial/frequency localization argument makes them compact, including their low-frequency pieces. Lemma E supplies a direct kernel proof for EW: a removable near-diagonal weak singularity, a small remote coefficient Schur tail, and a Hilbert-Schmidt far kernel. Its weight restriction \(1<1+\gamma\) is strict here. The differentiated kernel proof and compact-cutoff interpolation cover Hq. These arguments supply the qualitative compactness statements; no new quantitative operator norm follows from them.

For `../finite_rank/ACTUAL_RANK1_OPERATOR_TAIL_PROOF.md` I checked both its mathematical derivation and actual assembler. The normalized Schwartz basis is correct. The map \(T\mapsto PTP\) is an orthogonal projection in Hilbert-Schmidt space, so

\[
\|K-PKP\|_{op}\le\sqrt{\|K\|_{HS}^2-|\langle K\phi,\phi\rangle|^2}.
\]

The actual assembler subtracts the lower endpoint of the squared absolute matrix entry, as required for an upper tail bound. Its B Gram is \(\|WJ^q\phi\|_2^2\), the correct predual norm for \(G=J^q(Wg)\). It is not the B Gram for Q. The resulting \(\epsilon<7071/10000\), \(C_N<1309/250\) certificate is a valid actual Cvs3 finite-rank approximation and remains explicitly nonclosing.

A quantitative finite-rank approximation of the entire old compact remainder Kc has not thereby been produced. Larger exploratory matrices remain numerical research where their global tails are absent. The final report should not present those auxiliary old-route obligations as certified; the preferred local-Q proof uses the different, exact full-form reduction audited above.

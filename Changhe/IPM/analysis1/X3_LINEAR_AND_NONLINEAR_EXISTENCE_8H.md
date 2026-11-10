# X3 linear invertibility and conditional nonlinear existence

Research date: 2026-11-07, America/Los_Angeles.

Recorded research interval: **2026-11-07 09:13:05–16:33:21 UTC (7 h 20 min 16 s)**. Final report finalization: **2026-11-07 18:01:56 UTC**. Total wall-clock span: **8 h 48 min 51 s**. The unlogged interval 16:33:21–17:59:37 UTC, encompassing the later repository-instruction update, is excluded from the accounted research/finalization time of **7 h 22 min 35 s**. This report does **not** claim eight active research hours.

**Result: a conditional existence framework, with the numerical inverse checks still open.** The main new result is a complete low-order inverse theorem for the full moving-tail operator. It retains a noncompact horizontal-axis Darcy operator, removes an explicitly defined compact energy defect, and tests a finite bordered matrix. The proof includes closed domains and surjectivity. Neither a positive transport coefficient nor a small finite matrix is used as a substitute for this theorem.

The higher-order inverse can then be obtained on the audited S2 anisotropic space. A later direct axis-trace argument also gives a simpler constant-2.1-order alternative, described in Section 12a. Both have conditional inverse constants and a proof of identification with the low inverse. A new low/high product estimate permits a frozen-transport contraction. Its residual thresholds are explicit functions of the finite completion, response, coefficient and product constants. **No decimal value of an upper inverse bound, and no existence theorem for the current numerical reference, has been established.**

The most useful numerical advance is an actual approximate fixed-speed response to the complete historical moving-tail column. Its independently re-evaluated residual is about **0.00123** in the natural low norm, against a right-hand-side norm about **7192.46**. The nominal scalar Schur value is about **−0.18234669**. This is strong numerical evidence, not a Schur certificate: the fixed-speed inverse has not been assumed or proved numerically.

## Inputs, conventions, and scope

The reference is the exactly joined, exactly strain-repaired modal representation associated with

`IPM_Analysis_I.artifacts/numerics/data/trial_v2_h0.008.npz`,

whose original file SHA-256 is

`a069d85d102e17340778042f85c003705716ba799c0f68873d10c1c582ea4874`.

Its parameters are

\[
k=\frac{1615536043799051}{9007199254740992},\qquad
\bar c_l=\frac1k=5.575362610641546\ldots,
\qquad \bar\rho=x^2y\bar a,\quad \bar a>0.
\]

The positivity, exact joins and strain repair are those of the [current profile audit](../case1/X3_CURRENT_PROFILE_AUDIT.md). The raw numerical profile was not substituted. The representation has 260 cofactor modes and 261 nonzero stream modes. It has finite physical regularity at the origin and \(C^6\) spline joins; unlimited physical smoothness is not assumed.

The actual Candidate 013 proof sections were read in `/mnt/d/Changhe_D/IPM_writing/sections/03-frozen.tex` through `07-analytic-appendix.tex`, along with the relevant X3 S2 proofs listed at the end. The transferable arguments are maximal transport realizations, signed nonlocal energy estimates, finite defect removal, high-order compact estimates, and contraction in a weaker norm while transport remains frozen. Candidate 013's density begins linearly at the origin; its unweighted low space, operator and numerical constants do not transfer to \(x^2y\bar a\).

The exact item titled `X3_Research_Checkpoint` was not located despite broad local filename/text searches and connected Page searches. The Page service repeatedly returned incomplete content results, and no connected document session was available. No unrelated checkpoint was substituted. The existing S2 source proofs, the profile audit, and the two earlier numerical reports supplied the mathematical inputs.

Use

\[
F_0=\bar V\cdot\nabla\bar\rho-\bar\rho,\qquad
\bar V=\bar c_l X+U[\bar\rho],\qquad
\sigma[h]=\psi[h]_{xy}(0).
\]

The Darcy multipliers are \(\xi_x\xi_y/\vert \xi\vert ^2\) and \(-\xi_x^2/\vert \xi\vert ^2\), including the local part of the second multiplier. On the low space, strain means the continuous canonical functional

\[
\sigma[h]=\frac1\pi\int_{\mathbb R^2}
 \frac{h(r,\theta)\sin(3\theta)}{r^3}\,dX.
\tag{1}
\]

It agrees with the classical trace for the regular functions used later. A pointwise derivative of an arbitrary low-space stream function is not silently presumed to exist.

All new scripts, preserved evaluators, numerical inputs and result summaries are outside this repository in

`/mnt/d/Changhe_D/X3_linear_8h_20261107/`.

Only this final Markdown report is a new repository deliverable. No reference coefficients, certificates, historical proofs or existing reports were changed. All numerical values below are ordinary floating-point evidence unless an analytic identity is expressly stated. No interval campaign or profile optimization was performed.

The conditional low gate preceded the high gate recorded at 11:40 UTC; substantive nonlinear work followed that high gate. Later work strengthened the linear theory and numerical responses, including the constant-order alternative. The gates refer to complete conditional theorems, not successful numerical verification of their hypotheses.

# Part I. Low-order linear invertibility

## 1. The Hilbert space and the actual domain

Fix

\[
s=\frac34,\quad R=100,\quad
m=(1+r^2/R^2)^{-s/2},\qquad
\|h\|_{\rm low}^2=\int m\left|\frac h{\bar\rho}\right|^2dX.
\tag{2}
\]

Thus \(g=h/\bar\rho\) is even in both coordinates and belongs to \(L^2(m\,dX)\). This nonsingular cofactor description is the definition at the axes. The physical singular weight is \(m/\bar\rho^2\).

The domain is

\[
\mathcal D_{\rm low}
=\{h=\bar\rho g:\ g\in L^2_m,
             \ \bar V\cdot\nabla g\in L^2_m\},
\tag{3}
\]

with distributional differentiation and the graph norm. No cubic point trace is imposed here: \(g(0)\) is not continuous on this Hilbert space. Cubic normalization will be a high-order coordinate followed by a spatial rescaling.

The audited field is globally Lipschitz, has complete flow, and has bounded weighted divergence. Its composition group on \(L^2_m\) is strongly continuous. Its generator has exactly the maximal domain (3), with compact smooth even cofactors as a core. The formal adjoint has the same domain, because weighted divergence is a bounded multiplication operator. The physical core is \(\bar\rho\) times these cofactors; its elements need not be physically \(C^\infty\) at the origin.

Write \(q_0=F_0/\bar\rho\). It is bounded, and

\[
\bar\rho^{-1}(\bar V\cdot\nabla-1)(\bar\rho g)
=\bar V\cdot\nabla g+q_0g.
\tag{4}
\]

The following boundedness result therefore supplies a closed realization of the complete operator, independently of any inverse assertion.

## 2. Boundedness of the full divided Darcy map

Set

\[
C_x=\frac{x\bar\rho_x}{\bar\rho},\quad
C_y=\frac{y\bar\rho_y}{\bar\rho},\quad
B_1=\frac{\bar\rho}{x}=xy\bar a,\quad
B_2=\frac{\bar\rho}{y}=x^2\bar a.
\]

All four are bounded, using divided spectral axis limits. If \(U_j\) is a Darcy multiplier, put \(D_j=x_j^{-1}[U_j,x_j]\), on the parities for which the commutator output is odd in \(x_j\). Then the exact identity is

\[
Cg:=\frac{U[\bar\rho g]\cdot\nabla\bar\rho}{\bar\rho}
=C_x(U_1+D_1)(B_1g)+C_y(U_2+D_2)(B_2g).
\tag{5}
\]

For the radial decreasing weight, the odd Hardy inequality is

\[
\|f/x_j\|_{L^2_m}\le2\|\partial_jf\|_{L^2_m}.
\tag{6}
\]

Indeed the extra integration-by-parts term has sign \(x_j\partial_jm\le0\). This avoids applying an inappropriate singular-axis \(A_2\) theorem to the physical weight.

An explicit radial conjugation estimate gives, for \(0<s<2\),

\[
E_s=2\int_0^1\frac{u^{-s/2}-1}{1-u^2}\,du,
\]
\[
\|U_1\|_m\le\tfrac12+E_s,\quad
\|D_1\|_m\le\tfrac12+2E_s,\quad
\|U_2\|_m\le1+E_s,\quad
\|D_2\|_m\le1+2E_s.
\tag{7}
\]

For completeness, conjugate by \(\sqrt m\), bound the multiplier kernels by \(1/(2\pi\vert X-Y\vert ^2)\), and use Schur's test with auxiliary function (1/r). The angular integral is \(2\pi/\vert 1-u^2\vert \); inversion identifies the two radial pieces. Apply (6) to the derivative commutators, whose unweighted norms are (1/4) and (1/2). This yields

\[
\boxed{C_D=
 \|C_x\|_\infty\|B_1\|_\infty(1+3E_s)
+\|C_y\|_\infty\|B_2\|_\infty(2+3E_s)}
\tag{8}
\]

as a valid Darcy bound when the displayed suprema are upper bounds. Dense-core extension agrees with the canonical whole-plane Green operator; no harmonic strain is added.

The strain dual norm is the square root of

\[
\frac1{\pi^2}\int
 \frac{\bar\rho^2\sin^2(3\theta)}{r^6m}\,dX.
\tag{9}
\]

It is finite at both ends for \(s<4-2k\). The complete moving-tail column belongs to (2), as shown next. Hence both nontransport parts are bounded, and the full operator and its adjoint have the same maximal transport domain (3).

## 3. The full speed and moving-tail column

Use the historical cutoff \(\chi_o\): the sum of the last ten degree-seven modal splines, continued by zero/one. Its transition is approximately \(3151.84<r<3332.44\). The actual family is

\[
\rho_c=\bar\rho+\chi_o(r)(r^{1/c}-r^k)\Theta(\theta),
\qquad
\zeta_o=\partial_c\rho_c|_{\bar c_l}
=-k^2\chi_o r^k\log r\,\Theta.
\]

Differentiating \(3c-1-\sigma[\rho_c+h]=0\) gives

\[
\delta c=\frac{\sigma[h]}{\nu_o},\qquad
\nu_o=3-\sigma[\zeta_o],
\]

and the complete linear operator is

\[
\boxed{\mathcal Lh=\mathcal L_0h+\sigma[h]M_o,\qquad
M_o=\frac{X\cdot\nabla\bar\rho+\mathcal L_0\zeta_o}{\nu_o}.}
\tag{10}
\]

Here \(\mathcal L_0=(\bar V\cdot\nabla-1)+U[\,\cdot\,]\cdot\nabla\bar\rho\). This is the full S2 column in proofs 167 and 217. A numerical `KP` column using \(\log(r/r_+)\) must be converted before comparison; it was not substituted unconverted.

The leading dilation terms cancel **before** a norm is taken:

\[
X\cdot\nabla(r^k\Theta)
+(\bar c_l r\partial_r-1)(-k^2r^k\log r\,\Theta)=0.
\]

Thus \(M_o/\bar\rho=O(r^{k-1}(1+\log r))\), which is square integrable with (2) exactly in the needed range \(s>2k\). The chart derivative \(\zeta_o/\bar\rho\sim-k^2\log r\) is **outside** this low space for \(s<2\); it remains an external tail coordinate. The strain of \(\zeta_o\) uses an analytic logarithmic exterior moment, not a pure-power exterior fit.

## 4. Exact transport identity

For a bounded even auxiliary function \(\phi\), let

\[
\|h\|_\phi^2=\int m e^{2\phi}|h/\bar\rho|^2,
\qquad J=\sqrt m e^\phi.
\]

The spaces and maximal domains are unchanged as sets. Their norm comparison costs at most \(e^{\operatorname{osc}\phi}\). Integration by parts gives

\[
-\operatorname{Re}\langle(\bar V\cdot\nabla-1)h,h\rangle_\phi
=\int\big(\kappa+\bar V\cdot\nabla\phi\big)|Jg|^2dX,
\]
\[
\boxed{\kappa=\bar c_l-\frac{F_0}{\bar\rho}
 -\frac{s}{2}\frac{\bar V\cdot X}{R^2+r^2}.}
\tag{11}
\]

The identity extends from the core to the maximal domain. The sampled natural transport minimum is \(3.369758\), consistent with the earlier delayed-weight check. Its far limit is \(\bar c_l(1-s/2)=3.484601632\ldots\). The ordinary Darcy symbol has largest eigenvalue

\[
b_+=\frac{|\nabla\bar\rho|-\bar\rho_y}{2}.
\]

Subtracting this symbol from (11) still gives negative sampled margins. This is a limitation of direct scalar energy, not evidence of noninvertibility.

## 5. The noncompact horizontal-axis term and a global signed model

The relevant horizontal-axis operator is

\[
Q=U_2+D_2=\frac1y U_2[y(\,\cdot\,)].
\]

It cannot be replaced by \(U_2\) plus a compact error. After tangential Fourier transform, \(\alpha=\vert \xi_x\vert >0\),

\[
Q_\alpha f(y)=-\frac\alpha{2y}\int_0^\infty z
 \big(e^{-\alpha|y-z|}-e^{-\alpha(y+z)}\big)f(z)\,dz.
\tag{12}
\]

All \(\alpha>0\) are related by unitary dilation. At \(\alpha=1\), its symmetric part is \(-D+R_0\), where \(0\le D\le I\) is the Dirichlet resolvent and

\[
R_0(y,z)=-\frac{(y-z)^2}{4yz}
 (e^{-|y-z|}-e^{-(y+z)}),\qquad
\|R_0\|_{\rm HS}^2=\frac1{24}.
\]

Because \(R_0\) has a nonpositive kernel, its largest positive eigenvalue is at most \(\Vert R_0\Vert _{\rm HS}/\sqrt2\). To see this, apply the positive-kernel inequality to \(-R_0\): its positive spectral maximum dominates the magnitude of its negative spectral minimum. The HS sum must contain both extrema. Consequently

\[
\boxed{-\Lambda I\le\operatorname{Re}Q\le\lambda I,
\quad\lambda=\frac1{\sqrt{48}},\quad
\Lambda=1+\frac1{\sqrt{24}}.}
\tag{13}
\]

This is an analytic bound, uniform in tangential frequency. Finite normal discretizations give a much smaller positive maximum, about \(0.00774\); that numerical value is not used in the proof.

The exact cofactor operator obeys

\[
C=\bar\rho_xU_1+\bar\rho_yQ+\text{compact}.
\tag{14}
\]

Here is the compactness mechanism. \(D_1B_1\) is compact because \(B_1\) vanishes at the vertical axis and at infinity. A coefficient vanishing on the divided axis removes its normal noncompact term; after reflection, the remaining weak kernel is a norm limit of HS kernels. For \(Q\), tangential commutators with smooth compact coefficients have high-frequency norm \(O(\vert \xi_x\vert ^{-1})\); normal cutoff commutators have the same bound. At bounded tangential frequency their localized kernels are HS, including the zero-frequency limit. Approximation extends these results to the actual continuous coefficients. This proves \([Q,B_2]\) compact and hence (14). Conjugation by \(J\) changes the operator only compactly, using the radial mapping bound to remove coefficient tails. Neither axis block has been dropped.

Choose \(\epsilon=10^{-3}\), and define

\[
a_\pm=\frac{\sqrt{\bar\rho_x^2+\epsilon^2}\pm\bar\rho_x}{2},
\qquad
b_\pm=\frac{\sqrt{\bar\rho_y^2+\epsilon^2}\pm\bar\rho_y}{2}.
\]

Let \(G\) be the self-adjoint signed square completion

\[
\begin{aligned}
G={}&\sqrt{a_+}U_1\sqrt{a_+}-\sqrt{a_-}U_1\sqrt{a_-}\\
 &+\sqrt{b_+}(\operatorname{Re}Q)\sqrt{b_+}
   -\sqrt{b_-}(\operatorname{Re}Q)\sqrt{b_-}.
\end{aligned}
\]

The horizontal signed combination preserves cofactor parity even though its separate square roots need not. Define

\[
P=\tfrac12\sqrt{\bar\rho_x^2+\epsilon^2}+\lambda b_++\Lambda b_-,
\qquad K=\operatorname{Re}(JCJ^{-1})-G.
\tag{15}
\]

Then \(K\) is a known self-adjoint compact operator and \(G\le P\). Therefore

\[
-\operatorname{Re}\langle\mathcal L_0h,h\rangle_\phi
\ge\int(\kappa+\bar V\cdot\nabla\phi-P)|Jg|^2
 -\langle KJg,Jg\rangle.
\tag{16}
\]

This global model is a new alternative to the thin-axis-strip construction. It avoids an artificial HS cost growing as the strip width decreases.

## 6. A bounded weight with a prescribed margin

Put \(a=\kappa-P\). One explicit coefficient hypothesis is

\[
\inf_xa(x,0)>1.15,\qquad\inf_ya(0,y)>1.15.
\tag{H1a}
\]

The analytic origin and far limits are about \(5.57418838\) and \(3.48342740\). The numerical whole-axis minima are approximately

\[
1.26929216\quad\text{(horizontal)},\qquad
3.36858364\quad\text{(vertical)}.
\]

They support H1a but do not verify its global inequalities.

Define \(D(u)=0\) for \(u\le-0.15\), \(D(u)=u\) for \(u\ge0.15\), and \(D(u)=(u+0.15)^2/0.6\) between. Set \(d=D(1-a)\), so \(a+d\ge1\). Under H1a, \(d\) has compact support strictly inside the open quadrants. For the actual reference flow \(\Phi_t\), define

\[
\boxed{\phi(X)=\int_0^\infty d(\Phi_{-t}X)\,dt.}
\tag{17}
\]

The accepted S2 geometry is essential here: open-quadrant orbits have the nonzero similarity source as their past limit and escape to infinity in the future. A compact support set for \(d\) has uniform entrance/exit times by finite covering and the source/far neighborhoods. Its flow tube is compact and avoids the axes. Beyond a large radial section, angular scattering has integrable cylinder derivatives \(O(r^{k-1})\). Thus (17) is bounded, even and cylinder Lipschitz, with the local regularity required by (15), and

\[
\bar V\cdot\nabla\phi=d,\qquad
\kappa+\bar V\cdot\nabla\phi-P\ge1.
\tag{H1}
\]

The exact integral defines the weight. A sampled interpolant is not its differentiated proof. Finite past-flow samples at times 4 and 8 stabilized at a largest sampled \(\phi\) about \(2.23652\), giving a sampled norm-equivalence price about \(9.36067\). These are not global upper bounds.

For a quantitative upper price one can check \(d\le C_d\bar V\cdot\nabla\Lambda\) with an explicit bounded escape \(\Lambda\); then \(\operatorname{osc}\phi\le C_d\operatorname{osc}\Lambda\). Alternatively bound the finite flow tube directly. This is a coefficient/flow calculation, independent of invertibility.

There is also a qualitative fallback: finite-time averaging makes \(a\) positive whenever its invariant-measure averages on the compactified flow are positive. The only recurrent sets are the critical points/corners. At the nonzero source, the audited boxes \(\bar c_l>5.575\), transverse rate \(\mu_P\le1.01\), and \(\bar\rho_y(P,0)\le30\), together with (13), give \(a>1.234\). The other end limits are positive. This proves a suitable bounded auxiliary weight exists and hence the Fredholm index-zero conclusion below, without requiring the stronger whole-axis H1a. For general \(2k<s<2\), choose the smoothing \(\epsilon\) small relative to \(\bar c_l(1-s/2)\); the fixed value \(10^{-3}\) is used here only at \(s=3/4\).

## 7. Finite defect removal, actual surjectivity, and the border

Let \(e_1,\ldots,e_N\) be an orthonormal finite family in unweighted even-cofactor \(L^2\), and let \(P_N\) be its projection. Define

\[
F_N=P_NKP_N,\qquad F=J^{-1}F_NJ.
\]

The required complement condition is

\[
\boxed{\|K-F_N\|\le\varepsilon_N<\delta_0,\qquad
\delta_0=\inf(\kappa+\bar V\cdot\nabla\phi-P).}
\tag{H2}
\]

Under (17), \(\delta_0\ge1\). H2 is an approximation of an explicitly known compact kernel, not an inverse assumption. Set \(\delta=\delta_0-\varepsilon_N>0\) and \(A=\mathcal L_0-F\). Equation (16) gives

\[
\operatorname{Re}\langle Ah,h\rangle_\phi\le-\delta\|h\|_\phi^2.
\]

The same inequality holds for \(A^*\) on its actual maximal domain. Closedness and the first inequality give a closed range; the adjoint inequality gives zero cokernel. Thus

\[
\boxed{A:\mathcal D_{\rm low}\longrightarrow H_\phi
\text{ is onto and one-to-one},\qquad\|A^{-1}\|\le\delta^{-1}.}
\tag{18}
\]

This proves surjectivity. An inequality only on test functions would not suffice.

Return to cofactor coordinates. Let \(U:\mathbb R^{N+1}\to H_\phi\) have columns \(J^{-1}e_i\), followed by \(M_o/\bar\rho\). Let \(V:H_\phi\to\mathbb R^{N+1}\) have as its first rows the coordinates of (Fg) in that orthonormal family, and final row \(\sigma[\bar\rho g]\). Then

\[
\mathcal L=A+UV,\qquad
Z=A^{-1}U,\qquad D_{\rm mat}=I+VZ.
\tag{19}
\]

The complete operator is bijective exactly when this \((N+1)\)-dimensional matrix is invertible. This covers a possible fixed-speed kernel and includes the full speed column. In particular, no scalar Schur complement is invoked before proving a fixed-speed inverse.

For any conforming approximate frame \(\widehat Z\), form the **full spatial** residual and finite matrix

\[
R_Z=U-A\widehat Z,\qquad \widehat D=I+V\widehat Z.
\]

A sufficient response condition is

\[
\boxed{\widehat D\text{ nonsingular},\qquad
\eta=\|\widehat D^{-1}V\|\,\|R_Z\|/\delta<1.}
\tag{H3}
\]

All residual cross terms must enter \(\Vert R_Z\Vert \); a projected residual is insufficient. Woodbury's identity and (18) give

\[
K_\phi=\frac1\delta\left[1+
\left(\|\widehat Z\|+\frac{\|R_Z\|}{\delta}\right)
\frac{\|\widehat D^{-1}\|\,\|V\|}{1-\eta}\right],
\]
\[
\boxed{\|\mathcal L^{-1}\|_{\rm low\to low}
\le K_{\rm low}:=e^{\operatorname{osc}\phi}K_\phi.}
\tag{20}
\]

H1–H3 are a complete, noncircular, quantitatively testable conditional low inverse theorem. Compactness ensures an H2 family exists; it does not prove H3. Without numerical injectivity, the unconditional structural conclusion is **Fredholm index zero**, for both \(\mathcal L_0\) and the complete \(\mathcal L\).

## 8. Making H2 a concrete kernel computation

For \(X,Y\) in the first quadrant, use the plane kernels

\[
K_1(Z)=-\frac{Z_xZ_y}{\pi|Z|^4},\qquad
K_2(Z)=\frac{Z_x^2-Z_y^2}{2\pi|Z|^4},
\]

with the local \(U_2\) delta part handled separately. Define \(K_j^P(X,Y)=\sum_{\epsilon_x,\epsilon_y=\pm1}\epsilon_yK_j(X-\epsilon Y)\). The cofactor kernel of \(JCJ^{-1}\) is

\[
\frac{J(X)}{J(Y)}\bar\rho(Y)
\left[\frac{\bar\rho_x(X)}{\bar\rho(X)}K_1^P(X,Y)
 +\frac{\bar\rho_y(X)}{\bar\rho(X)}K_2^P(X,Y)\right].
\tag{21}
\]

The \(Q\) kernel is \(Y_yK_2^P(X,Y)/X_y\). Symmetrize it for the vertical part of \(G\). For the horizontal part sum the reflected \(K_1\) kernels multiplied by

\[
\sqrt{a_+(X)a_+(\epsilon Y)}-
\sqrt{a_-(X)a_-(\epsilon Y)}.
\]

These formulas define \(K\) completely; the local delta terms cancel exactly. Joint interior symmetrization cancels first coefficient differences. Near the horizontal boundary, subtracting the **whole** \(Q\) block leaves degree (-1) in the three relative normal/tangential variables, which is square integrable. The vertical boundary has the same degree after its vanishing input factor. The origin's squared dyadic HS mass is \(O(r^4)\), comparable far annuli contribute \(O(r^{2k-2})\), and mixed ends require \(s<4-2k\). Thus this \(K\) is HS for the present parameters.

A particularly transparent sufficient H2 check is

\[
\boxed{\|K\|_{\rm HS}^2-
 \sum_{i,j\le N}|\langle Ke_j,e_i\rangle|^2<\delta_0^2.}
\tag{22}
\]

Both terms must use the same kernel and normalization. A loose triangle bound minus projected mass is not a convergent completion method. Truncated scrambled-Sobol experiments gave HS norms roughly \(27.2\)–\(27.5\) for the natural gauge and \(31.0\)–\(31.4\) for a sampled past-flow gauge. These are exploratory integrals with unresolved tails/variance and **do not check (22)**. Explicit normalized \(L^2\) cell projections captured approximate squared Frobenius mass \(107.7\) at dimension 512 and \(275.6\) at dimension 2048. Their quadrature entries and gauge errors are unresolved; they did not establish a complement bound.

A better sufficient variant pays only for the unfavorable sign. Let \(P\) be a finite projection, \(Q=I-P\), and check

\[
QKQ\le\beta I,\quad \beta<\delta_0,\qquad
\|QKP\|\le\gamma.
\]

Choose \(\eta>0\) so \(\beta+\gamma^2/\eta<\delta_0\), and use

\[
F_N=PKP+\eta P,\qquad
K-F_N\le\varepsilon I,\quad
\varepsilon=\max(0,\beta+\gamma^2/\eta)<\delta_0.
\tag{H2'}
\]

This follows by completing the square in the \(P/Q\) cross term. The proof of (18) needs only this one-sided inequality, so the entire inverse theorem and H3 apply with the modified finite rows. Large negative compact spectrum is favorable and need not be reproduced in an HS approximation. H2' is a quadratic-form bound on an explicit complement and a finite-column norm, with no inverse assumption. Neither \(\beta\) nor \(\gamma\) has been bounded numerically in this campaign.

## 9. Exact chart preconditioning and the new response

One can reduce the large speed column without changing the background. Let \(\chi_i\) transition in logarithmic radius from 10 to 30 using the regularized beta step with parameters \((7,7)\), and let \(\zeta_i,\nu_i,M_i\) be the same exact formulas with this cutoff. Define

\[
h_{\rm cut}=\frac{\zeta_o-\zeta_i}{\nu_o},\qquad
q_\nu=\frac{\nu_i}{\nu_o}.
\]

Then, exactly,

\[
M_o=\mathcal L_0h_{\rm cut}+q_\nu M_i,
\qquad
\mathcal L_i(I+h_{\rm cut}\sigma)=\mathcal L_o,
\qquad 1+\sigma[h_{\rm cut}]=q_\nu>0.
\tag{23}
\]

This is an invertible coordinate change, not a profile modification. It also respects the high space: the compact difference is \(C^6\), with scalar state regularity below \(7.5\) and image regularity below \(6.5\). The nonlinear families have the same leading tail; their differences are compact and the normalization equations transform consistently.

Rough natural-norm values are:

| Quantity | Historical cutoff | Inner cutoff |
|---|---:|---:|
| \(\sigma[\zeta]\) | −0.0180486093 | −0.5797658110 |
| \(\nu=3-\sigma[\zeta]\) | 3.0180486093 | 3.5797658110 |
| \(\Vert M\Vert _{\rm low}\), leading exterior norm included | 7192.46 | 85.05 |
| Base \(\Vert M'(\bar c_l)\Vert _{\rm low}\), leading exterior norm included | 922.49 | 27.35 |

The ratio \(q_\nu\) is about \(1.18611934\). The norm of \(h_{\rm cut}\) is about \(154.57\). Crude coordinate norm prices are \(113.67\) and \(95.99\) for the map and its inverse. These prices, and all high equivalents, must be included when transferring an inverse bound. Base derivatives in this table are not uniform bounds on a parameter interval.

The exterior column norms beyond the last radius are about \(8.74\) and \(7.37\), combined in quadrature with the represented norms. The derivative exterior norms are about \(7.70\) and \(6.21\). The table includes their analytic leading power/log continuation; remaining higher-power errors are not enclosed. In particular the inner full-column estimates are slightly larger than the earlier finite-domain values \(84.73\) and \(26.64\).

Using (23), an analytic power/log far response, and a grid in \((\log r,\log\tan\theta)\) produced the following fixed-speed response to **the historical \(M_o\)**:

| Check | Value |
|---|---:|
| Solve grid | 6368 radii × 1793 logarithmic angles |
| Canonical response stream modes / source angles | 1024 / 2048 |
| Independent check grid | 12495 radii × 1793 angles |
| Independent modes / source angles | 1536 / 3072 |
| Density-Green spatial residual | 0.00122800 |
| Differentiated-source-Green spatial residual | 0.00122883 |
| Difference of the two images | \(2.36\times10^{-5}\) |
| Excluded angular-strip residual | \(2.45\times10^{-5}\) |
| Leading inner radial-head residual | \(3.00\times10^{-6}\) |
| Leading exterior radial residual estimate | \(2.76\times10^{-6}\) |
| Represented-domain response norm | 151.5527 |
| Analytic exterior response norm | 1.9992 |
| Combined response norm, before negligible head/strip adjustment | 151.5659 |
| \(\sigma[\widehat v]\), density/source formulations | −1.1823466932 / −1.1823466961 |
| Nominal \(1+\sigma[\widehat v]\) | **−0.1823466932** |

The angular strips use affine logarithmic extensions and Gauss–Laguerre integration. The radial head uses the exact leading origin field; the far response includes analytic exterior power/log moments. Combined, the residual is approximately \(1.23\times10^{-3}\), or \(1.71\times10^{-7}\) of \(\Vert M_o\Vert _{\rm low}\). Remaining continuation and quadrature errors are not enclosed. Including the actual truncated-domain boundary flux, an independent 12735-radius/3585-angle transport-energy check agreed to \(4.8\times10^{-9}\) in unnormalized energy. The response is conforming in the low graph space; it is not claimed to be a high-order correction.

This improves substantially on the old 18-function response whose residual exceeded eight right-hand-side norms. Its values \(0.85\)–\(0.90\) should be discarded. Several unrestricted grid spectral experiments also developed angular aliasing and were discarded; they are not complement evidence.

If an independent fixed-speed inverse bound \(K_0\) were established, this response would imply

\[
\big|1+\sigma[\mathcal L_0^{-1}M_o]
 -(1+\sigma[\widehat v])\big|
\le\|\sigma\|_{\rm low^*}K_0\|M_o-\mathcal L_0\widehat v\|_{\rm low}.
\tag{24}
\]

With the floating measurements, a bound \(K_0\lesssim203\) would separate the scalar value from zero. **Such a bound has not been proved**, so (24) is not a certification. The valid general mechanism remains H2–H3.

The response can nevertheless be reused without assuming \(\mathcal L_0^{-1}\). If \(F=U_NV_N\), \(\widehat Z_N\) approximates \(A^{-1}U_N\), and \(e=M_o-\mathcal L_0\widehat v\), set

\[
\widehat Z_M=\widehat v+\widehat Z_NV_N\widehat v.
\]

Then

\[
M_o-A\widehat Z_M=e+(U_N-A\widehat Z_N)V_N\widehat v.
\tag{25}
\]

This directly supplies the speed response column in the correct full border.

Other rough natural-space constants are \(\Vert \sigma\Vert =0.72893224\), \(E_{3/4}=1.39159555\), and the crude coefficient bound (8) approximately \(494.24\). The last figure uses sampled suprema and is not a verified operator bound. No numerical \(K_{\rm low}\) is asserted.

**Stage I status:** bounded realization, axis mechanism, compact defect, Fredholm index and conditional surjectivity/inverse proof established. H1a/H1, H2 and H3 remain numerical checks. This is a Level B inverse theorem; actual invertibility of the current reference remains unverified.

# Part II. High-order linear invertibility

This stage was entered only after the complete conditional low theorem, including its mapping and surjectivity arguments, was obtained. Its role is to control the regularity of the **actual low inverse**, not just smooth test functions.

## 10. A fixed high space and its compatibility with the new low norm

The completed construction uses the S2 anisotropic space, with the audited parameter extension

\[
\delta=\frac{19}{10},\qquad s_0=\frac{21}{10},\qquad
\sigma_v=\frac{25}{4},\qquad\gamma=-\frac12.
\]

Write \(t=\log r\), \(p(\theta)=\cos^2\theta\sin\theta\), and fix

\[
A(r)=\frac{r^{1.9}}{(r^2+64)^{2.7}},\qquad B(r)=r^3A(r).
\tag{26}
\]

Let \(S\) be the smooth step \(e^{-1/u}/(e^{-1/u}+e^{-1/(1-u)})\) on \((0,1)\), extended by zero/one. Define

\[
A_\theta=S\!\left(\frac{100\sin^2\theta-4}{21}\right),\quad
A_r=S\!\left(\frac{r-9}{3}\right),\quad
s_H=s_0+(\sigma_v-s_0)(A_\theta+A_r-A_\theta A_r).
\tag{27}
\]

Thus the order is \(2.1\) near the horizontal origin corners and the nonzero sources, and \(6.25\) throughout a vertical sector and for \(r\ge12\). A globally constant order \(2.1\) in the unfactored bulk would fail the vertical origin energy. Section 12a gives a sector-based constant-order realization after deriving the new axis-row estimate it needs. Equations (26)–(41) first record the conservative anisotropic route.

Fix an even angular cutoff \(\chi_v=1\) for \(\vert \cos\theta\vert \le0.1\) and zero for \(\vert \cos\theta\vert \ge0.15\), with nested larger cutoffs inside \(\vert \cos\theta\vert <0.25\). All transitions use \(S\). For a remainder \(u\), define \(X_H\) by

\[
v=u/B\in H^{s_H(\cdot)}(\mathbb R\times\mathbb S^1),\qquad
z=\chi_vu/(Bp)\in H^{6.25},\qquad
z|_{\theta=\pi/2,3\pi/2}=0.
\tag{28}
\]

These are closed trace conditions. The bulk norm is the square sum of its variable-order Littlewood–Paley norm and ordinary Bessel \(H^{2.1}\) norm; add the Bessel \(H^{6.25}\) norm of \(z\). For a precise Fourier convention use the unitary cylinder transform, \(\varphi(\xi)=S(2-\vert \xi\vert )\), \(\Delta_0=\varphi(D)\), and \(\Delta_j=\varphi(2^{-j}D)-\varphi(2^{1-j}D)\), \(j\ge1\), with variable-order square sum \(\sum_j\Vert 2^{j s_H}\Delta_jv\Vert _2^2\). This fixes the norms before assigning constants.

Let \(\chi_0(r)=1-S(r-1)\), so it is one for \(r\le1\) and zero for \(r\ge2\). Decompose the physical density uniquely as

\[
h=E\beta+u,\qquad E\beta=x^2y\beta(t),\qquad
\beta=j\chi_0+A w,\quad w\in H^{7.25}(\mathbb R),\quad u\in X_H.
\tag{29}
\]

Use the sum norm \(\Vert h\Vert _{\rm high}=\vert j\vert +\Vert w\Vert _{H^{7.25}}+\Vert u\Vert _{X_H}\). The forcing space consists of

\[
f=E\Gamma+f_R,\quad \Gamma/A\in H^{6.25}(\mathbb R),\quad f_R\in X_H,
\quad
\|f\|_{Y_H}=\|\Gamma/A\|_{H^{6.25}}+\|f_R\|_{X_H}.
\tag{30}
\]

The scalar coordinate is the actual vertical cofactor trace. The free cubic coefficient \(j\) is necessary; setting it to zero changes the scalar index.

The new low embedding can be priced explicitly. For the remainder bulk \(v=u/B\), parity gives \(v(0)=0\), and its vertical factored extension gives \(v(\pi/2)=v'(\pi/2)=0\). One-sided Hardy and Rellich on a quadrant give

\[
\left\|\frac{v}{\sin\theta\cos^2\theta}\right\|_2
\le\frac{\pi^2}{3}\|v\|_{H^2},
\]

using \(1/(\sin^2\theta\cos^4\theta)=1/\sin^2\theta+1/\cos^2\theta+1/\cos^4\theta\). The explicitly added \(H^{2.1}\) bulk norm controls this \(H^2\) norm. The radial factor is

\[
r^2m\left(\frac A{\bar a}\right)^2.
\]

Its far power is \(r^{2\gamma-2k+2-s}\). Consequently

\[
\gamma\le k-1+s/2
\quad\Longrightarrow\quad
\|h\|_{\rm low}\le C_E\|h\|_{\rm high},\qquad
\|f\|_{\rm low}\le C_Y\|f\|_{Y_H}.
\tag{31}
\]

Here \(\gamma=-0.5< -0.44563947\ldots\); the squared far exponent is \(-0.10872106\ldots\). The residual additionally needs \(2k-1<\gamma\). The interval

\[
2k-1<\gamma\le k-1+s/2
\tag{32}
\]

is nonempty exactly when \(s>2k\), the same condition as low residual membership. This directly connects the two choices of norm.

Let \(M_*=\sup r\sqrt m A/\bar a\). The remainder price is \((\pi^2/3)M_*\), the scalar regular price is \(\sqrt{2\pi}M_*\), and the free cubic price is its explicit physical low norm. With exactly the physical cutoff \(\chi_0=1-S(r-1)\), rough coefficient-based direct-sum prices are \(C_E\approx2.53462\), \(C_Y\approx0.0812096\). Their respective component prices are \(2.53332,\ 0.0492173,\ 0.0645961\). These are sampled coefficient/quadrature estimates, not verified upper constants.

## 11. Transport, Darcy, and the scalar row

Put \(W=(q,\omega)=(\bar V_r/r,\bar V_\theta/r)\), \(\beta_B=\partial_t\log B\). The high bulk and vertical transport energy coefficients are

\[
\kappa_v=1+\bar c_l-(1+\beta_B)q,\qquad
\kappa_u=\kappa_v+2\omega\tan\theta-\omega\cot\theta.
\tag{33}
\]

The apparent tangent/cotangent singularities have regular spectral limits. Let \(H_D\) be the polar rotation of the Cartesian frequency matrix

\[
\begin{pmatrix}-\bar\rho_y&\bar\rho_x/2\\\bar\rho_x/2&0\end{pmatrix}.
\]

With the exact positive similarity zero \(P\), define

\[
\Phi=(r^2-P^2)^2+4P^2y^2,\qquad
\Lambda=\frac\Phi{P^4+\Phi}+\sin^2\theta.
\tag{34}
\]

The explicit symbol checks are

\[
W\cdot\nabla s_H\ge0,\qquad W\cdot\nabla\Lambda\ge0,
\]
\[
\boxed{(\kappa_v+N W\cdot\nabla\Lambda)I
 -s_H\operatorname{sym}DW-H_D+L W\otimes W\ge\mu I,}
\]
\[
\boxed{(\kappa_u+N W\cdot\nabla\Lambda)I
 -\sigma_v\operatorname{sym}DW-H_D+L W\otimes W\ge\mu I}
\tag{H4a}
\]

on the bulk and the larger vertical sector respectively. The order sign follows from the two coefficient checks \(\omega\ge0\) on \(r\le12, 1/25\le\sin^2\theta\le1/4\), and \(q\ge0\) on \(9\le r\le12, \sin^2\theta\le1/4\). For perturbation uniformity use strict lower bounds there.

Scans support \(N=14, L=1.3, \mu=0.25\), with completed sampled minima above \(0.310\), but these global inequalities remain unverified. The escape has a sampled normalized radial derivative margin about \(0.992\). The relevant critical margins are:

| Location/direction | Margin or mechanism |
|---|---:|
| Horizontal origin, transverse frequency | \(1+\bar c_l+(4+\delta)(2\bar c_l-1)-s_0(6\bar c_l-2)=0.41507252\ldots\) |
| Vertical origin, factored transverse frequency | \(140.37725\ldots\) |
| Far field | \(1-\bar c_l\gamma=3.78768131\ldots\) |
| Nonzero source, least direction | about \(4.475\) |

At the source, the Darcy symbol is essential: its radial contribution includes \(+\bar\rho_y(P,0)\), about \(29.75\), counteracting the large expanding radial derivative. Keeping only transport would lose this fact.

The original S2 proofs use \(\delta=1.8,s_0=2.05\). The displayed extension preserves all their strict restrictions: \(1/4<\delta<2\), \(s_0>2\), \(\sigma_v<6.5\), coefficient regularity \(H^{6.375}\), velocity \(W^{7,\infty}\), \(\gamma<\min(k,-3/8)\), and the six convergent separated-annulus exponents of proof 123. The smaller horizontal margin requires \(\mu=0.25\); the old \(0.5\) margin was not retained. Replacing exact end powers by (26) is a smooth bounded cylinder multiplier, with constants recomputed.

The full normalized coupling is

\[
C_{\rm ren}h=U[h]\cdot\nabla\bar\rho+\sigma[h]H_0,\qquad
H_0=\chi_0X\cdot\nabla\bar\rho/3.
\]

Write \(Tu=(\bar V\cdot\nabla-1)u\) for physical transport on the remainder. Let \(\Gamma_C[h]\) be the vertical cofactor trace of the normalized coupling, and \(C_Rh=C_{\rm ren}h-E\Gamma_C[h]\). The actual S2 mapping proof gives \(C_R:X_H\to X_H\) bounded and \(\Gamma_C\) compact into \(A H^{6.25}\). Its proof retains the divided nonlocal term: locally, for input \(x^2f\),

\[
U_1[x^2f]/x=xU_1[f]+2[U_1,x]f+x^{-1}[[U_1,x],x]f.
\tag{35}
\]

The last commutator gains two derivatives before one odd division. Comparable annuli use the finite-regularity multiplier calculus. Separated annuli have the six explicit powers in proof 123; in particular inner strain is canceled before summation. These facts do not assert that bare \(U\) preserves the factored space.

The local variable-order calculus uses the scalar specialization of [Krainer–Mendoza, *Elliptic systems of variable order*, Propositions 4.11, 4.12 and 5.2](https://arxiv.org/html/1301.5820v2). The global cylinder, axis factors, finite coefficient regularity and end summations are supplied by the cited S2 proofs, rather than inferred from the paper's local result.

For the scalar row, let \(d(t)=\bar V_y(0,r)/r\), \(D_0=4\bar c_l-1\), and

\[
A_{\rm axis}\beta=d\beta'+(D_0-d-2d')\beta.
\tag{36}
\]

The free-\(j\) Volterra solution is an isomorphism from the scalar domain (29) to \(A H^{6.25}\). Its differentiated kernel defines an independently calculable constant \(K_A\). With the same physical cutoff used in (29), a sampled \(L^2\) remainder Schur price is about \(0.5196\); this is not its \(H^{7.25}\) inverse price.

The complete high operator is the normalized scalar/remainder block plus \(\sigma[h](M_o-H_0)\). **The fixed-speed physical operator alone is not silently treated as an operator into (30)**: its cubic strain output is not in that forcing target. The complete canceled vector \(M_o-H_0\) is in (30), including its logarithmic far continuation.

## 12. A quantitative compact estimate and high surjectivity

Here are the independent quantities needed to compute the high constant. The order reductions \(A_v,A_u\) and penalty \(\Pi=W\cdot R\) are those of proofs 144–148; here \(R\) is the cylinder Fourier multiplier vector with symbol \(\xi/\langle\xi\rangle\). Fix \(\epsilon=1/32\) in this conservative construction. The lower norm \(X_{H,-\epsilon}\) subtracts \(\epsilon\) from both Sobolev orders and the added bulk Bessel order. Let \(H=\Vert u\Vert _{X_H}\), \(Y=\Vert u\Vert _{X_{H,-\epsilon}}\), \(F=\Vert (T+C_R)u\Vert _{X_H}\), \(w=A_v(u/B)\), \(z=A_u(\chi_vu/(Bp))\). Within (37) only, \(V\) and \(U\) denote the two unreduced channel norms, so \(H^2=V^2+U^2\). Choose upper bounds for

\[
\begin{aligned}
\mu\|w\|^2&\le C_FF\|w\|+L\|\Pi w\|^2+eH^2+C_eYH+\|J_eu\|H,\\
\mu\|z\|^2&\le C_FF\|z\|+C_\chi V\|z\|+L\|\Pi z\|^2
                  +eH^2+C_eYH+\|J_eu\|H,\\
V^2&\le C_A(\|w\|^2+Y^2),\quad
U^2\le C_A(\|z\|^2+Y^2),\\
\|\Pi w\|+\|\Pi z\|&\le C_PF+aH+C_aY.
\end{aligned}
\tag{37}
\]

These are bounded coefficient, commutator, order-reduction and mollified-penalty estimates, **not estimates of an unknown PDE inverse**. Their exact operators are fixed in proofs 144–148. In particular \(J_e\) is the compact part obtained by approximating the exact coupling/commutator coefficients; \(C_e\) is the remaining weaker-order norm. \(C_\chi\) is the overlap multiplier \((W\cdot\nabla\chi_v)/p\). Arbitrarily small \(e,a\) are available by those proofs; constants multiplying lower/compact terms may grow.

A completely specified bookkeeping choice is

\[
\begin{gathered}
B_*=\max(1,2C_\chi^2C_A/\mu^2),\quad\alpha=\mu/(4C_A),\\
e=\alpha/[16(B_*+1)],\quad a=\sqrt{\alpha/(48LB_*)},\\
A_F=(B_*+1)C_F^2/\mu+3LB_*C_P^2,\\
A_Y=\mu/2+C_\chi^2C_A/\mu+3LB_*C_a^2,\quad c_y=(B_*+1)C_e,\\
c_F=\sqrt{2A_F/\alpha},\quad
c_Y=\sqrt{2A_Y/\alpha+4c_y^2/\alpha^2},\quad
c_J=2(B_*+1)/\alpha.
\end{gathered}
\tag{38}
\]

Omit the penalty terms if \(L=0\). Triangular absorption gives \(H\le c_FF+c_YY+c_J\Vert J_eu\Vert \). The overlap price is fixed before choosing the small errors; a constant growing with the small error is never allowed to multiply the final high norm.

Use the double-factor norm \(N_0(u)=\Vert u/(B\cos^4\theta)\Vert _2\), the exact end transport margin \(c_0>0\), and the interpolation/end bounds of proof 139:

\[
Y\le\eta H+C_\eta N_0(u),\qquad
N_0(u)\le(C_H/c_0)F+(t_{\rm tail}/c_0)H+N_{\rm loc}(u).
\]

Choose \(\eta=1/(4c_Y)\) and radial ends so \(t_{\rm tail}\le c_0/(4c_YC_\eta)\). Then

\[
\|u\|_{X_H}\le C_S\|(T+C_R)u\|_{X_H}+\|K_Su\|,
\]
\[
C_S=2(c_F+c_YC_\eta C_H/c_0),\qquad
K_S=(2c_YC_\eta N_{\rm loc},\ 2c_JJ_e),
\tag{39}
\]

with the direct-sum sum norm. The localized lower-order and double-Hardy maps are compact. This removes the global weaker norm; it is not an unsupported global compact embedding.

Let \(G\beta=(TE\beta-EA_{\rm axis}\beta)+C_RE\beta\). Solving the explicit scalar row first yields

\[
\|h\|_{\rm high}\le C_{\rm full}\|\mathcal Lh\|_{Y_H}+\|K_{\rm full}h\|,
\qquad
C_{\rm full}=\max\{(1+C_S\|G\|)K_A,C_S\},
\tag{40}
\]

where the compact map is explicit as follows. Decompose \(M_o-H_0=E\Gamma_M+u_M\). In the direct-sum sum norm, take

\[
K_{\rm full}h=\big((1+C_S\|G\|)K_A[\Gamma_C[h]+\sigma[h]\Gamma_M],
                  \ C_S\sigma[h]u_M,\ K_Su\big).
\]

Each component is a known bounded kernel or coefficient map, compact on the high state independently of any inverse.

For a finite map \(S_f:H_{\rm low}\to\operatorname{target}(K_{\rm full})\), the remaining quantitative high check is

\[
\boxed{\|K_{\rm full}-S_f\iota\|_{\rm high\to target}\le\varepsilon_H<1,}
\tag{H4b}
\]

where \(\iota\) is the embedding (31). Such maps exist: compactness reduces to finitely many high dual rows, and restrictions of low dual rows are norm dense because \(\iota\) is injective between reflexive Hilbert realizations. A concrete verification uses smooth compact rows, local frequency truncation and the proved dyadic end tails. This is a compact approximation check, not the assertion that a high inverse exists.

Actual high surjectivity is proved separately. The remainder maximal domain is \(\{u\in X_H:Tu\in X_H\}\). The flow generator gives a large positive resolvent parameter at which \(T+C_R-\lambda\) is invertible. The uniform compact estimate (39) makes the path upper semi-Fredholm; continuation from that endpoint gives index zero at zero. The scalar Volterra isomorphism, compact axis row and finite-rank full tail column preserve index zero. This is the actual block argument of proof 150.

Every high-domain density and its image embed in the low space. Boundedness of the low Darcy/strain terms then places it in (3). Under H1–H3 a high null vector is zero. High index zero therefore gives high surjectivity, and low uniqueness identifies its inverse with the restriction of the low inverse. **Only after this step** may (40) be applied to the low inverse solution. H4b then gives

\[
\boxed{K_{\rm high}=
 \frac{C_{\rm full}+\|S_f\|K_{\rm low}C_Y}{1-\varepsilon_H}.}
\tag{41}
\]

No numerical values were obtained for \(K_A\) at full order, \(C_A,C_e,C_a,C_{\rm full},\Vert S_f\Vert \), or \(\varepsilon_H\). Their minimum required computations are the fixed coefficient multiplier norms, mollified transport/penalty remainders, Volterra derivatives through order \(7.25\), and the compact approximation H4b. A positive finite high matrix alone checks none of these.

**Stage II status:** a complete Level B regularity/inverse theorem, including domain preservation and actual surjectivity, conditional on H1–H3, H4a, the explicit bounded energy constants, and H4b. There is no numerical upper value of \(K_{\rm high}\). The \(N=14\) escape weight can cost as much as \(e^{28}\) in norm equivalence; it is a feasible symbolic construction, not a claim of efficient constants.

## 12a. A simpler constant-order alternative

The preceding theorem is a conservative route through the existing S2 construction. A new trace estimate permits a simpler high space with **order \(2.1\) in both sectors**, and scalar state/forcing orders \(3.1/2.1\). It retains the same radial powers (26), low space, profile and moving-tail family. This alternative was developed after the original Stage II gate; it is a further conditional high theorem, not a numerical inverse certificate.

On the first quadrant put

\[
\psi(\theta)=\frac\pi2 S\!\left(\frac{\theta-\pi/6}{\pi/6}\right),
\quad \chi_b=\cos\psi,\quad \chi_v=\sin\psi,\quad a_v=0.3,
\]

and extend by reflection. The remainder norm is the square sum of the ordinary \(H^{2.1}\) norms of

\[
v_b=\chi_bu/B,\qquad u_v=a_v\chi_vu/(Bp),
\tag{41a}
\]

with zero vertical trace of \(u_v\). The scalar state is \(j\chi_0+A H^{3.1}\), and the scalar forcing is \(A H^{2.1}\). The bulk and factored channels have the same order on their overlap; bounded sector ratios therefore suffice when flow crosses it. One cannot merely lower the order in (28) without changing the energy localization.

**Direct trace gain.** On a rescaled vertical patch write \(h=x^2f\), with \(f\in H^q(\mathbb R^2)\), \(q=2.1\), and compact normal support. Fourier transform normally in \(x\) and tangentially in \(y\), with frequencies \(\xi,\alpha\). Twice integrating by parts gives the kernel for \(\partial_xU_1[h](0,\cdot)\) as

\[
-i\alpha\,\partial_\xi^2\!\left(\frac{\xi^2}{\xi^2+\alpha^2}\right).
\]

It is homogeneous of degree \(-1\). For \(\vert \alpha\vert \ge1\), its square integral against \((1+\xi^2+\alpha^2)^{-q}\) is bounded by \(C\vert \alpha\vert ^{-2q-1}\). Hence the trace gains half a derivative: \(H^q\to H^{q+1/2}\). The \(U_2[h]\) trace gains \(3/2\). At low tangential frequency, the identity \(h(0,\cdot)=0\) removes the constant symbol term; the remaining formulas are bounded by \(O(\alpha^2)\) and \(O(\vert \alpha\vert )\), respectively, using the fixed normal support. There is no infrared singularity.

An explicit high-frequency trace price before patch multipliers is

\[
\left\{\frac{4}{2\pi}\left[
\mathrm B(1/2,q+11/2)-6\mathrm B(3/2,q+9/2)
+9\mathrm B(5/2,q+7/2)\right]\right\}^{1/2}
\approx0.550407.
\]

For support \(\vert x\vert \le4\), simple low-frequency prices are \(24.92\) and \(35.24\) for these two traces. These prices concern the flat patch operators, not the full axis coupling.

The exact cofactor row on that patch is a smooth-coefficient combination of these two traces:

\[
2\bar a\,\partial_xU_1[h](0,y)
+(\bar a+y\bar a_y)U_2[h](0,y)/y+\sigma[h]\Gamma(H_0).
\]

Thus it is locally compact into \(H^q\). Comparable annuli carry the vanishing prices \(r^2\) and \(r^{k-1}\); the six separated-annulus sums of proof 123 converge at these lower orders and have vanishing tails. At the origin the entire row must remain combined: the strain contribution of \(U[h]\) cancels \(\sigma[h]H_0\), whose axis trace alone is outside the weighted forcing space. The free cubic coordinate is finite dimensional. This proves the full compact axis row without the old strong four-derivative sector space. Formula (35) gives the factored coupling; its local commutator errors gain one derivative, and the subtracted axis row has the half-derivative gain just proved.

**The full cutoff energy.** The two transport equations have off-diagonal cutoff terms proportional to \((p/a_v)W\psi\) and \(-(a_v/p)W\psi\). Their symmetric energy is bounded by

\[
c_{\rm cut}=\frac12|W\psi|\,|p/a_v-a_v/p|
\]

times the sum of the two channel squares. Include this term in the coefficient check:

\[
(\kappa_j+NW\Lambda-c_{\rm cut})I
-2.1\,\operatorname{sym}DW-H_D+LW\otimes W\ge\mu I,
\tag{41b}
\]

on \(\theta\le\pi/3\) for bulk and \(\theta\ge\pi/6\) for cofactor. This retains all cutoff cross terms. A 6145-radius/1025-angle scan supports \(N=3.5,L=0.21,\mu=0.25\), with sampled minima \(0.41507252\) and \(0.99573273\). The factored vertical critical margin is \(9.85072522\), the horizontal one is \(0.41507252\), and the far margin remains \(3.78768131\). These global inequalities are still numerical conditions.

Use the exact order reductions \(e^{N\Lambda}\langle D\rangle^{2.1}\) in both channels. The lower elliptic comparison has \(C_A=1\), the norm-equivalence price is at most \(e^{2N}\), and no logarithmic variable-order term occurs. The cutoff cross term is already in (41b), so there is no triangular overlap price. Fixed-order commutator errors gain one derivative; the compact axis row gains one half. Thus the lower sector order can be \(1.6\), taking \(\epsilon=0.5\). This order still has the defining traces and embeds into the low space by the sector Hardy estimate. Applying \(\langle D\rangle^{-1}\) to the transported equation gives the characteristic-penalty estimate in (37); the bounded coupling and commutators then lie in that lower norm. The constants are direct norms of known coefficient/kernel maps. Bookkeeping (38)–(40) applies with the new reductions and \(C_\chi=0\). The sampled escape price \(e^7\) is substantially smaller than \(e^{28}\), although neither is an inverse bound.

**End and domain argument.** The double-factor norm \(N_0=\Vert u/(B\cos^4\theta)\Vert _2\) requires only two normal derivatives: the even vertical cofactor has zero value and zero first normal trace. Double Hardy bounds it by the \(H^{2.1}\) state. Local Rellich followed by this Hardy bound supplies the compact collars in (39). \(N_0\) controls both channel \(L^2\) norms, so frequency interpolation gives \(Y\le\eta H+C_\eta N_0\) with an explicit price \(C_\eta=C_0(2/\eta)^{3.2}\). A bound of \(N_0\) by the lower \(H^{1.6}\) norm is neither asserted nor needed.

For the end energy, do not assert an unproved \(H^1\) bound on the double quotient. If \(u,Tu\) are in the new remainder space, both their double quotients are in \(L^2\). The transformed equation holds off the axis and extends distributionally across it: an axis cutoff produces \(W_{\rm normal}\chi_\varepsilon' z\), which tends to zero because \(W_{\rm normal}=O(\text{normal distance})\) and the \(L^2\) strip mass tends to zero. Thus the double quotient is in the ordinary maximal \(L^2\) transport domain. Its energy coefficient is \(\kappa_v+4\omega\tan\theta\), with least origin limit about \(6.705\) and far limit \(3.78768\). Coupling tails tend to zero by the same double-Hardy and dyadic bounds. This proves the compact estimate (39) at the reduced order.

The smooth base flow preserves the closed sector intersection and its trace condition. Its generator equals the maximal high graph realization: solve a sufficiently large shifted generator equation, then identify any distributional maximal solution with it by uniqueness in the low transport space. This avoids assuming spatial mollifiers preserve the divided graph. The large-parameter endpoint, compact estimate, scalar Volterra isomorphism, compact axis row and canceled rank-one column give index zero exactly as in §12. The embedding (31) holds, so low injectivity gives actual high surjectivity and inverse identification. A finite compact check H4b yields formula (41) in these new norms.

For nearby frozen fields, \(2.1>2\) controls first derivatives; (35) controls the divided vertical velocity and the trace lemma controls its scalar coefficients. The fixed-order tame commutator bounds give the uniform small form errors. Equations (52)–(54) apply after recomputing their bounded coefficient constants, and the variable-order sign constraint is omitted. The low/high product (47) still holds because the vertical \(H^{2.1}\) cofactor has bounded first derivatives. Therefore the nonlinear closure (55)–(59) applies to this pair as well.

For this sector norm the reconstruction \(u/B=\chi_bv_b+(p/a_v)\chi_vu_v\) gives an explicit low remainder price \((26/3)M_*\): the bulk costs at most \(4\cdot2=8\) by horizontal Hardy, and the vertical channel costs \(1/a_v=10/3\). With the fixed cutoff, rough direct-sum embedding prices are \(C_E\approx2.53951,\ C_Y\approx0.177143\). These are still sampled coefficient prices, not numerical inverse bounds.

**Status of this simpler route:** Level B, with explicit symbol, compact-completion and response conditions; no numerical upper inverse constant. It is the simpler candidate for the next quantitative implementation. Constants and the \(H^{6.25}\) residual lower bound from the conservative norm must not be reused as constants for this different norm. Its full \(H^{2.1}\) residual is not measured. Its scalar \(L^2\) component is still about \(42.9\), which will already exceed the direct threshold cap derived below.

## 12b. A direct high/low bound for the simpler space

For the constant-order route one can replace the optional high finite completion H4b by explicit local interpolation. This does **not** remove the essential low border H2–H3.

At the base coefficients the off-principal errors gain at least half a derivative, so they are bounded by the lower \(H^{1.6}\) sector norm. The remainder compact map \(K_S\) can be chosen to consist only of fixed radial collars: lower-order localizations and the double-factor cutoff map. For every \(a>0\), ordinary frequency splitting and Hardy give a computable price \(C_K(a)\) with

\[
\|K_Su\|\le a\|u\|_X+C_K(a)\|u\|_{\rm low}.
\tag{41c}
\]

On each finite collar the low norm controls both channel \(L^2\) coordinates. The local \(H^{1.6}\) interpolation has reciprocal-error power \(3.2\). For the double quotient, first use double Hardy into \(H^2\), then interpolate with \(H^{2.1}\), giving power \(20\). Cutoff multiplier norms and the local suprema of \(\bar a/(Ar\sqrt m)\) supply the fixed coefficients. Thus (41c) has a direct finite coefficient formula, rather than requiring a new PDE estimate.

Likewise, the trace-gain lemma and the six decaying output tails give, for every \(b>0\),

\[
\|\Gamma_C[h]\|_\Gamma
\le b\|h\|_{\rm high}+C_\Gamma(b)\|h\|_{\rm low}.
\tag{41d}
\]

To compute \(C_\Gamma(b)\), choose output tails with total high price at most \(b/2\), interpolate the finitely many near-axis input patches at order \(1.6\), and add the low-dual norms of the smooth separated-input kernels. For \(J\) patches with trace price \(T_i\), high localization price \(C_i\) and low \(L^2\) price \(D_i\), take \(\tau_i=\min(1,b/(2JT_iC_i))\). A permissible coefficient expression is \(C_\Gamma(b)=D_{\rm sep}+\sum_iT_iD_i(2/\tau_i)^{3.2}\). These are the displayed rational Green kernels, trace multipliers and local coefficient suprema. The argument uses the total local cofactor of \(h\), whose \(L^2\) norm is controlled by the physical low norm; it does not assume its scalar axis trace is low-continuous.

Let \(C_B\) bound the explicit scalar lift \(E:B_H\to H_{\rm low}\), and decompose \(M_o-H_0=E\Gamma_M+u_M\). Put

\[
\begin{gathered}
C_K=C_K(1/2),\quad a_F=2C_S,\quad
a_B=2C_S\|G\|+2C_KC_B,\\
a_L=2C_SC_\sigma\|u_M\|_X+2C_K,\qquad
b=[2K_A(1+a_B)]^{-1}.
\end{gathered}
\]

First bound the remainder using (41c) and
\(\|u\|_{\rm low}\le\|h\|_{\rm low}+C_B\|\beta\|_B\).
Then solve the scalar row with (41d), choosing the displayed \(b\) to absorb half the total high norm. This gives

\[
\boxed{\|h\|_{\rm high}\le C_{\rm reg}\|\mathcal Lh\|_{Y_H}
 +C_{\rm low}\|h\|_{\rm low},}
\]
\[
\begin{aligned}
C_{\rm reg}&=2[(1+a_B)K_A+a_F],\\
C_{\rm low}&=2[(1+a_B)K_A
 (C_\Gamma(b)+C_\sigma\|\Gamma_M\|_\Gamma)+a_L].
\end{aligned}
\tag{41e}
\]

After the independent high surjectivity argument of §12a,

\[
\boxed{K_{\rm high}\le C_{\rm reg}+C_{\rm low}K_{\rm low}C_Y.}
\tag{41f}
\]

No high spectral nondegeneracy test remains in this version. The uncomputed quantities are ordinary coefficient, Volterra, cutoff, trace-kernel and interpolation prices. The fixed collars and axis row give the same estimates uniformly for the small frozen family after the explicit high-form errors are absorbed. Thus (41f), with uniform prices and \(K_L\), is an alternative to (54). Large reciprocal-error powers can make these constants expensive; no favorable numerical size is claimed.

# Part III. Nonlinear estimates and closure

The substantive nonlinear work began after the conditional low and high gates. It uses the same full operator, the same external tail coordinate, and the same norm conventions.

## 13. Exact variable-speed equation and remainder

On a compact interval \(I\) about \(\bar c_l\), for example a sufficiently small subinterval of ([5,6]), keep the exact family \(\rho_c\). Define

\[
n(c)=3c-1-\sigma[\rho_c],\qquad n(\bar c_l)=0.
\]

The accepted tail angular moment \(S_\Theta=\pi^{-1}\int\Theta(\theta)\sin(3\theta)\,d\theta\) is positive. Since the nonnegative cutoff vanishes for \(r\le1\),

\[
n'(c)=3+c^{-2}S_\Theta\int_1^\infty\chi_o(r)r^{1/c-2}\log r\,dr\ge3.
\]

This is the scalar normalization calculation in S2 proofs 35 and 59, not a consequence of cutoff nonnegativity alone. For a small correction \(h\), define \(c(h)\) by

\[
n(c(h))=\sigma[h].
\tag{42}
\]

In particular, \(\rho_{c(h)}+h\) has the required exact origin strain relation. Set

\[
\mathcal B(c)=F_c(\rho_c)-n(c)H_0,\qquad
M(c)=H_0+\frac{\mathcal B(c)-\mathcal B(\bar c_l)}{n(c)},
\tag{43}
\]

with the removable value at \(\bar c_l\). Then \(M(\bar c_l)=M_o\) from (10), and

\[
F_c(\rho_c)=F_0+n(c)M(c)
\]

is exact. This secant definition matters away from the base point; substituting a base derivative column at every speed would not give the exact nonlinear equation.

For each \(h\), define the frozen operator

\[
\begin{aligned}
\mathcal A_h f={}&[c(h)X+U[\rho_{c(h)}]+U[h]]\cdot\nabla f-f\\
 &+U[f]\cdot\nabla\rho_{c(h)}+\sigma[f]M(c(h)).
\end{aligned}
\tag{44}
\]

Then

\[
\boxed{F_{c(h)}(\rho_{c(h)}+h)=F_0+\mathcal A_hh.}
\tag{45}
\]

At \(h=0\), \(\mathcal A_0=\mathcal L\). Away from zero, (44) is the frozen factorization used for the iteration.

Let \(z_c=\rho_c-\bar\rho\) and \(\Delta c=c(h)-\bar c_l\). The exact remainder after the base full linearization is

\[
\begin{aligned}
\mathcal N(h)={}&\Delta c\,X\cdot\nabla h
 +U[z_{c(h)}]\cdot\nabla h+U[h]\cdot\nabla h\\
 &+U[h]\cdot\nabla z_{c(h)}
 +\sigma[h]\{M(c(h))-M_o\}.
\end{aligned}
\tag{46}
\]

All powers \(r^{1/c}\) and their logarithmic derivatives are retained. No external tail is treated as an ordinary low perturbation. Also

\[
3\Delta c=\sigma[h]+\sigma[z_{c(h)}].
\]

Consequently the first three terms of (46) combine as the transport of \(h\) by \(U[h]+U[z_c]+\Delta c X\), with its cubic coefficient canceled. Taking separate strong norms before this cancellation would be invalid.

## 14. A new product bound for this low space

The historical S2 low norm is substantially stronger near the vertical axis. Its product theorem cannot be imported as a theorem for (2). For the present pairing one can prove

\[
\boxed{\|U[f]\cdot\nabla h\|_{\rm low}
 \le C_{\rm prod}\|f\|_{\rm low}\|h\|_{\rm high}.}
\tag{47}
\]

The delicate horizontal patch is worth spelling out. On a unit rescaled annulus away from the vertical axis, write \(f=yF\). Then

\[
U_1[f]=yU_1[F]+[U_1,y]F,\qquad U_2[f]/y=QF.
\]

The first and last terms use the divided \(L^2\) bounds and the \(H^{2.1}\) control of the high density gradient. For the commutator term, localized \([U_1,y]\) maps \(L^2\) to \(H^1\). Its kernel is \(z_xz_y^2/(\pi\vert z\vert ^4)\); on fixed radius-four patches, Schur's test and its gradient multiplier give a price below 37 when cutoff gradients are at most 2. Meanwhile odd division gives

\[
\|h_x/y\|_{H^{0.1}}\le2\|h\|_{H^{2.1}}
\]

up to the explicitly fixed coordinate/cutoff multipliers. Use \(H^1\hookrightarrow L^{40}\), \(H^{0.1}\hookrightarrow L^{40/19}\), and Hölder. Their elementary unitary-Fourier prices are about \(1.21698\) and \(0.93868\). **No bounded cofactor gradient at the horizontal axis is assumed.**

Near the vertical axis the stronger high cofactor directly controls the divided high derivatives, and (5) handles the low velocity. Comparable annuli have price

\[
C_{\rm loc}\sup_r r^2A(r)\frac{\bar a_+(r)}{\bar a_-(r)}.
\]

Here \(\bar a_\pm\) are upper/lower bounds on a fixed enlarged annulus, and \(C_{\rm loc}\) is the sum of the preceding fixed patch multiplier, Sobolev and commutator prices. For separated annuli put

\[
\alpha_r=\frac{r\sqrt{m_r}A(r)}{\bar a_-(r)},\qquad
\beta_s=\frac{s\bar a_+(s)}{\sqrt{m_s}}.
\]

The kernel prices are \(C\alpha_r\beta_s(s/r)^4\) for inner input and \(C\alpha_r\beta_s\) for outer input. The sequence \(\beta_s\) is square summable on logarithmic annuli; \(\alpha_r\) is bounded, with far exponent \(\gamma-k+1-s/2=-0.05436053\ldots\). Thus an explicit upper expression for the remainder part of \(C_{\rm prod}\) is a fixed overlap factor times the comparable price plus

\[
C_{\rm sep}\sup_r\alpha_r\left(\sum_s\beta_s^2\right)^{1/2}.
\tag{48}
\]

Use annular upper/lower weight bounds in this expression. The separated kernel constant is obtained by differentiating the displayed rational Darcy kernels on separated unit patches. The free cubic lift is priced separately by (7) and its exactly divided derivatives. A rough price for that lift alone is \(725.11\). The full \(C_{\rm prod}\) was not numerically evaluated; (47) is a proved mapping statement with a convergent coefficient/series bound, not a measured small constant.

Define the following independent family bounds on the chosen \(I\), all in the natural low norm:

\[
\begin{aligned}
C_z&=\sup_{c\in I}\|f\mapsto U[f]\cdot\nabla\partial_c\rho_c\|_{\rm low\to low},\\
C_{\rm tail}&=\sup_{c\in I}\|h\mapsto U[\partial_c\rho_c]\cdot\nabla h\|_{\rm high\to low},\\
C_M&=\sup_{c\in I}\|M'(c)\|_{\rm low},\qquad
C_{\rm dil}=\|h\mapsto X\cdot\nabla h\|_{\rm high\to low},\\
C_\sigma&=\|\sigma\|_{\rm low^*},\qquad
\nu_* =\inf_I n'(c),\qquad L_c=C_\sigma/\nu_*.
\end{aligned}
\tag{49}
\]

The dilation/velocity bounds use at most two high derivatives, including horizontal odd division. For \(C_z\), a useful explicit two-weight proof chooses \(q_*=0.24>\sup_I1/c\), \(\beta=q_*-k\), and applies (7) in \(m_{s-2\beta,R}\). The factors \(B_j\langle r/R\rangle^\beta\) and \((x_j\partial_j\partial_c\rho_c/\bar\rho)\langle r/R\rangle^{-\beta}\) are bounded. The strict exponent gap absorbs the logarithms. Smoothness of \(M(c)\) in the low space follows from \(4q_*-2k-s<0\); its high forcing membership follows from \(q_*<1/4\).

At the base point, rough historical/inner estimates of the two-weight \(C_z\) price are \(3070.4/485.1\). Further exact-power/log family evaluations at \(c=5,5.25,5.5,5.75,6\) gave:

| Diagnostic on \(I=[5,6]\) | Historical cutoff | Inner cutoff |
|---|---:|---:|
| Largest sampled \(\Vert M'(c)\Vert_{\rm low}\), leading exterior included | 1279.14 | 48.59 |
| Sampled \(n'(c)\) range | 3.01382–3.02729 | 3.47335–3.79020 |
| Parameter-uniform triangle price for \(C_z\), extended spatial scan | 4713.70 | 1302.03 |
| Largest sampled divided tail velocity derivative | 0.20068 | 2.08852 |

The \(M'\) maxima are sampled in the parameter as well as space, with analytic leading exterior norm corrections. The \(C_z\) triangle formula is uniform in the parameter: bound all \(r^{1/c}\) factors by \(r^{1/5}\) on the cutoff support, \(c^{-2}\le1/25\), and \(|1/c-3|\le3-1/6\), before taking the spatial suprema. The scan was extended to \(\log r=80\); the inner price's far maximum is near \(\log r=24.8\). Its spatial prices are still sampled. Analytic parameter derivatives agreed with centered differences to relative error below \(2.9\times10^{-9}\). These diagnostics are not verified uniform constants. The minimum remaining computation is a continuous bound for the same suprema and the convergent sums (48).

Then

\[
\boxed{C_{\rm diff}=C_{\rm prod}
 +L_c(C_{\rm dil}+C_{\rm tail}+C_zC_E+C_\sigma C_MC_E)}
\tag{50}
\]

gives

\[
\|(\mathcal A_h-\mathcal A_g)f\|_{\rm low}
\le C_{\rm diff}\|h-g\|_{\rm low}\|f\|_{\rm high},\qquad
\|\mathcal N(h)\|_{\rm low}
\le C_{\rm diff}\|h\|_{\rm low}\|h\|_{\rm high}.
\tag{51}
\]

The unreduced high quadratic estimate loses one derivative: a fixed smooth velocity differentiating a high-frequency density already gives a counterexample to a derivative-preserving bound \(H_{\rm high}\times H_{\rm high}\to Y_H\). There is instead a finite tame bound into \(Y_H^-\), with the bulk/vertical orders reduced by one and the compatible scalar axis row at its available order. This weaker estimate follows from the same localized products and the scalar state’s extra derivative. It is not used as a false \(Y_H\) estimate. The required high control below is response-specific, with the transport derivative inside (44).

## 15. Uniform inverses are derived on the varying domains

The domains of the transports in (44) need not coincide. Norm-small bounded perturbation of a presumed common first-order graph is not used.

Retain the base low finite defect and frame from H2–H3. Require its columns to satisfy the directly checkable stronger condition \(g,xg_x,yg_y\in L^2_m\). This includes smooth compact frames and the stated logarithmic response extensions. A parity-preserving Lipschitz field has \(\vert W_j/x_j\vert \le\Vert DW\Vert _\infty\), so these columns belong to every perturbed maximal domain.

Let \(r=\Vert h\Vert _{\rm high}\), and take a coefficient price \(C_{\rm vel}\) for the Lipschitz total velocity change. In the auxiliary low norm set

\[
C_{\rm tr}=\|C_x\|_\infty+\|C_y\|_\infty+1+s/2
 +\sup r|\nabla\phi|,
\quad a_L=C_{\rm tr}C_{\rm vel}+C_zL_cC_E.
\]

Convert the bounds from (49) to that norm by bounded equivalence where needed. The shifted energy margin is at least \(\delta-a_Lr\). Let \(R_0=\Vert U-A\widehat Z\Vert \), \(a_D=\Vert \widehat D^{-1}V\Vert \), and let

\[
c_R=C_{A Z}+C_ML_cC_E,
\]

where \(C_{A Z}\) is the finite norm of the changed operator applied to the **known** frame per unit high radius. It uses the frame's divided first derivatives, not an unknown inverse. The perturbed full frame residual is at most \(R_0+c_Rr\). Set \(\eta_0=a_DR_0/\delta<1\), \(\theta=(1+\eta_0)/2\), and choose

\[
\boxed{r_L=\min\left\{\frac\delta{2a_L},
\frac{\delta(1-\eta_0)}{2a_Dc_R+(1+\eta_0)a_L}\right\}.}
\tag{52}
\]

Omit a constraint with zero denominator. For \(r\le r_L\), write \(\delta_* =\delta-a_Lr\), \(R_*=R_0+c_Rr\). The same adjoint-domain argument and finite border prove actual low surjectivity on each domain, with uniform natural bound

\[
\boxed{K_L=e^{\operatorname{osc}\phi}\delta_*^{-1}
\left[1+(\|\widehat Z\|+R_*/\delta_*)
 \frac{\|\widehat D^{-1}\|\|V\|}{1-\theta}\right].}
\tag{53}
\]

For uniform high control, proofs 155–167 give the tame coefficient/energy bounds for exactly these frozen fields. The new low inverse replaces their separate historical low hypothesis. An explicit permissible radius is obtained by requiring:

- Cylinder velocity change at most half the strict order-sign margin in H4a.
- \([(B_*+1)C_{E p}+6LB_*aC_{P p}]r+3LB_*C_{P p}^2r^2\le\alpha/16\), where the two \(C_{\cdot p}\) are the transport-energy and penalty change norms from the fixed tame commutators.
- \(C_{\rm end}r\le c_0/2\), and \(K_AC_{\rm axis}r\le1/2\), retaining the end margin and scalar Volterra inverse.
- \(C_{{\rm full},0}C_{D H}r\le1/2\), absorbing the bounded moving-tail coupling change from the base high compact estimate.

Every constant here is a coefficient, commutator, one-dimensional kernel, or explicit tail-family norm. The quadratic constraint has its ordinary positive root; all constraints give a positive radius. They contain no full-PDE inverse assumption. The source, origin and end exponents remain in their strict ranges for a sufficiently small chosen \(I\).

With these choices there is one fixed compact map \(K_0\) and an explicit coefficient constant \(C_{{\rm full},0}\), obtained from (38)–(40) with the uniform scalar/overlap bounds, such that

\[
\|f\|_{\rm high}\le2C_{{\rm full},0}\|\mathcal A_hf\|_{Y_H}
 +2\|K_0f\|.
\]

Choose one finite \(S_f\) checking \(\Vert 2K_0-S_f\iota\Vert \le\varepsilon_H<1\). Each varying high realization has index zero by the actual scalar/remainder continuation. The newly established low inverse makes it injective; hence it is onto and agrees with the low inverse. The uniform high constant is

\[
\boxed{K_H=\frac{2C_{{\rm full},0}+\|S_f\|K_LC_Y}{1-\varepsilon_H}.}
\tag{54}
\]

This uniform finite compact check is required for the finite-completion version; a base finite section is not silently promoted to uniformity. For the simpler route, §12b instead gives fixed-coupling uniform prices \(C_{{\rm reg},0},C_{{\rm low},0}\). Absorb the tail-coupling change by the explicit cap \(C_{{\rm reg},0}C_{D H}r\le1/2\), to obtain the alternative

\[
\boxed{K_H=2C_{{\rm reg},0}+2C_{{\rm low},0}K_LC_Y.}
\tag{54a}
\]

This version needs the localized coefficient/interpolation prices, with no high finite spectral check. Choose \(r_0\) no greater than \(r_L\), all coefficient radii for the selected version, 1, and

\[
\frac{\nu_*\operatorname{dist}(\bar c_l,\partial I)}{C_\sigma C_E}.
\]

If positivity is required, use the uniform high-to-cofactor bound relative to \(\rho_c\), \(c\in I\), and impose the corresponding radius. The ratio \(\rho_c/\bar\rho\) need not be uniformly bounded at infinity; that ratio is not used to justify positivity or low operator continuity.

## 16. Explicit residual thresholds and contraction

All constants in this paragraph are the **uniform** constants just constructed. Set

\[
\boxed{R_H=\min\left\{\frac{r_0}2,\frac1{4K_LC_{\rm diff}},\frac12\right\},
\qquad R_L=\frac{C_ER_H}2,}
\]
\[
\boxed{\varepsilon_{\rm low}=\frac{R_L}{K_L},\qquad
\varepsilon_{\rm high}=\frac{R_H}{K_H}.}
\tag{55}
\]

Include the positivity radius in \(R_H\) if that conclusion is desired. The explicit sufficient residual conditions are

\[
\boxed{\|F_0\|_{\rm low}<\varepsilon_{\rm low},\qquad
\|F_0\|_{Y_H}<\varepsilon_{\rm high}.}
\tag{56}
\]

These are numerical targets once the independent finite and coefficient computations above are supplied; they are not invented decimal tolerances.

On the closed ball \(\Vert h\Vert _{\rm high}\le R_H, \Vert h\Vert _{\rm low}\le R_L\), define

\[
\mathcal T(h)=-\mathcal A_h^{-1}F_0.
\]

The two uniform inverse bounds prove both self-map inequalities. Resolvent subtraction in the low maximal domains and (51) give the contraction factor

\[
q\le K_LC_{\rm diff}K_H\|F_0\|_{Y_H}\le\frac14.
\tag{57}
\]

The ball is complete in the low metric: a low-Cauchy sequence bounded in the reflexive high space has a weak high limit, and the injective low embedding identifies that limit and preserves both bounds. No low continuity of the free cubic trace is assumed. Every high state belongs to each relevant low transport domain, since a transport derivative plus horizontal odd division costs at most two derivatives, available from \(s_0>2\). Thus the difference identity is legitimate despite varying high domains.

The fixed point solves (45) and gives a classical profile with at least \(C^{1,\alpha}\) regularity for a positive small \(\alpha\), with canonical Darcy velocity. Its leading coefficient is \(1+j\), where \(\vert j\vert \le R_H\le1/2\). Normalize it to one by

\[
\lambda=\sqrt{1+j},\qquad
\rho_{\rm norm}(X)=\lambda\rho_{\rm sol}(X/\lambda).
\tag{58}
\]

This preserves speed and strain. The leading far amplitude is multiplied by \(\lambda^{1-1/c}\). That amplitude change is a real normalization coordinate; the rescaled solution is not asserted to remain in the original fixed-amplitude affine low ball.

## 17. A response-specific alternative

An inconveniently large high residual can be replaced by a small **verified correction response**, without changing the theorem. Let \(v_a\) be a conforming approximation to \(-\mathcal L^{-1}F_0\), with enough extra regularity that every \(\mathcal A_hv_a\in Y_H\). Put

\[
e_a=F_0+\mathcal Lv_a,\qquad
\|(\mathcal A_h-\mathcal L)v_a\|_{Y_H}\le D_a\|h\|_{\rm high}.
\]

Here \(D_a\) is a coefficient estimate on one known function. Then

\[
\|\mathcal T(h)\|_{\rm high}\le\eta_a+\theta_a\|h\|_{\rm high},
\quad
\eta_a=\|v_a\|_{\rm high}+K_H\|e_a\|_{Y_H},\quad
\theta_a=K_HD_a.
\tag{59}
\]

If \(\theta_a<1\), use \(R_H\ge\eta_a/(1-\theta_a)\), provided it fits the coefficient/normalization radii and \(K_LC_{\rm diff}R_H<1\). Check the low self-map with \(K_L\Vert F_0\Vert _{\rm low}\le R_L\). This replaces the direct high residual condition by an explicit response target. The response computed in Part I is to \(M_o\), **not** to \(F_0\), and cannot be substituted for \(v_a\).

## 18. What residual smallness means for this reference

For the conservative high norm (30), the exact requirements are:

| Location/property | Requirement | Present represented residual |
|---|---|---|
| Low norm | \(F_0/\bar\rho\in L^2(m\,dX)\), small as in (56) | Belongs; measured about \(0.00990995\) |
| Origin | Zero cubic coefficient, divided residual \(O(r^\alpha)\) with \(\alpha>1.9\) | Exact repaired strain kills the cubic term; divided residual is \(O(r^2)\) |
| Axes | Physical parity and factor \(x^2y\); actual vertical trace separated as (30) | Satisfied by modal spectral limits |
| High joins | Scalar/remainder orders at most \(6.25\) | \(C^6\) density joins give residual Sobolev order \(q<6.5\) |
| Infinity, low | \(F_0/\bar\rho=O(r^{k-1})\), requiring \(s>2k\) | Satisfied |
| Infinity, high | \(F_0=O(r^{2k-1})\), requiring \(2k-1<\gamma\) | \(2k-1=-0.64127894\ldots<-0.5\) |

Thus the current residual belongs to both spaces. The theorem does not require a new asymptotic cancellation merely for membership. Its leading nonzero tail makes the high norm decay slowly.

Meeting a smallness target is a stronger requirement: it must control the weighted axis derivatives and the nonzero far residual coefficient as well as the finite-radius residual. Increasing pointwise fitting accuracy alone does not imply either required norm becomes small. No such refitting was performed.

An 80-digit evaluation of the exactified modal moments gives the vertical origin coefficient

\[
\frac{F_0}{x^2y}(0,r)=C_2r^2+\cdots,
\qquad C_2\approx6.0872110521\times10^{-6}.
\]

This used the exact strain identity and analytic modal moments. The binary64 Green cache has a small origin-strain quadrature offset, about \(2.2\times10^{-10}\), which would be greatly amplified by the high origin weight. It was not interpreted as a physical cubic residual and the reference was not modified to remove it.

The scalar forcing is \(\Gamma(F_0)=\lim_{x\to0}F_0/(x^2y)\). On the compact radial interval \(0.1\le r\le10^6\), direct divided formulas give

\[
\|\Gamma(F_0)/A\|_{L^2(dt)}\approx42.9344,\qquad
\|\Gamma(F_0)/A\|_{H^1(dt)\text{, compact diagnostic}}\approx45.2639.
\tag{60}
\]

These avoid the origin quadrature offset. A naive global differentiated diagnostic near (790) was contaminated by that offset and is discarded. The full scalar/remainder norm was not measured. The analytic leading far continuation alone contributes roughly 18.1 to the scalar \(L^2\) norm beyond the outer numerical radius. These low-derivative diagnostics do not expose the much larger fifth derivative.

In fact, the existing [proof 179 certificate](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/179_high_residual_lower/PROOF.md) supplies a directed original-data jet at \(t=8\), in the old convention \(A_*=r^{1.8}/(1+r)^{5.3}\). It gives \(g_*^{(5)}(8)>447000000\), where \(g_*=\Gamma(F_0)/A_*\). Its derivatives of orders zero through four have absolute upper bounds \(0.159,0.244,2.23,2247,211000\). These are for the same exact repaired reference, not the floating Green cache.

The conversion to our norm is exact:

\[
\Gamma(F_0)/A=\mu g_*,\qquad
\mu(t)=(1+64e^{-2t})^{2.7}(1+e^{-t})^{-5.3}.
\]

At \(t=8\), \(\mu>0.99\) and \(\vert \mu^{(j)}\vert <0.1\), \(1\le j\le5\). One elementary proof uses the complex disk of radius 2: there \(\vert e^{-t}\vert <1/400\), \(\vert 64e^{-2t}\vert <1/2500\), so \(\vert \log\mu\vert <0.0144\), \(\vert \mu-1\vert <0.0146\), and Cauchy's estimate gives the derivative bounds. The real lower bound follows directly from Bernoulli's inequality. Leibniz then yields

\[
|(\mu g_*)^{(5)}(8)|>
0.99(447000000)-0.1(5(211000)+10(2247)+10(2.23)+5(0.244)+0.159)
>442422250.
\]

For unitary \(H^{25/4}(\mathbb R)\), fifth-derivative evaluation has norm

\[
C_5^2=\frac{\Gamma(11/2)\Gamma(3/4)}{2\pi\Gamma(25/4)},\qquad C_5<0.235.
\]

Consequently the accepted historical directed jet implies the new rigorous norm comparison

\[
\boxed{\|F_0\|_{Y_H}>1.88\times10^9.}
\tag{60a}
\]

A Decimal transfer of the central jet gives the stronger point lower expression about \(1.9030191\times10^9\); the conservative displayed bound uses only the coarse rational inequalities above. This is reuse of an existing certificate plus an analytic change of norm, not a new interval campaign or a full norm measurement. All saved code and evidence hashes of that certificate matched. Its current `PROOF.md` text hash differs from the old manifest; this documentary mismatch is recorded in the preserved transfer output. The directed jet is accepted here as an existing computational input, rather than claimed as a fresh independent replay.

There is a useful analytic cap on how permissive (56) could be. Far-field, slowly varying logarithmic annular tests imply every actual inverse upper constant must satisfy

\[
K_L\ge\frac1{\bar c_l(1-s/2)}\approx0.28698,\qquad
K_H\ge\frac1{1-\bar c_l\gamma}\approx0.264014.
\tag{61}
\]

For the high test take \(h=B\chi((t-T)/W)f(\theta)\), with \(f\) supported away from both axes, then \(T\to\infty\) and \(W\to\infty\). The normalized full operator tends to multiplication by \(\bar c_l\gamma-1\); the coupling and strain row tend to zero. The low test uses \(g=e^{-(1-s/2)t}\chi((t-T)/W)f\). The same state and forcing norm conventions appear on both sides, so these are necessary lower bounds, not estimated upper inverses.

Since our chosen \(R_H\le1/2\),

\[
\varepsilon_{\rm high}\le\frac{1-\bar c_l\gamma}{2}
=1.89384065\ldots.
\tag{62}
\]

The transferred high lower bound (60a) exceeds this most permissive cap by a factor **greater than \(9.92\times10^8\)**. Thus the current residual fails the conservative direct invariant-ball criterion, using the accepted historical jet. For the constant-\(2.1\) alternative, membership follows from the same origin, axis and far powers, with much weaker join requirements. The bound (60a) does not apply to that weaker norm. Its scalar \(L^2\) diagnostic alone is about **22.7 times** the same cap (62), so the current reference also fails this particular direct criterion in that space on the floating diagnostic. Actual sufficient tolerances can be smaller still. Neither comparison rules out a better reference, response-specific closure (59), or linear invertibility.

An actual decimal sufficient tolerance cannot be computed from the present data: H2, H3, the high compact completion and the uniform product/coefficient bounds have not supplied upper \(K_L,K_H,C_{\rm diff},r_0\). Equations (49)–(56) specify exactly which independent quantities would produce it. A small pointwise relative residual is not a substitute for any of them.

**Stage III status:** the exact nonlinear algebra, low/high product mapping, derivative-loss treatment, varying-domain inverse mechanism and contraction are established conditionally for either specified high pair, with constants recomputed in that pair. Assuming compatible references have uniformly verified linear/coefficient constants and residuals tending to zero in the natural low norm and the chosen high forcing norm, the thresholds eventually hold. Arbitrarily small residuals alone do not verify the missing linear finite conditions or prevent their constants from degenerating.

# Part IV. Final assessment

## 19. Status and answers

| Research objective | Status | Main bound or result | Remaining requirement |
|---|---|---|---|
| Low bounded realization and Fredholm index | **PROVED from the accepted reference hypotheses** | Divided Darcy bound (8), maximal domain (3), retained axis block (12)–(14), compact defect and index zero | No numerical inverse follows from index alone |
| Complete low inverse | **CONDITIONAL, Level B** | H1–H3 give actual bijectivity and (20); the fixed-speed inverse is not assumed | Global coefficient/flow bound, compact completion, full bordered response test |
| High inverse and regularity | **CONDITIONAL, Level B** | Conservative and constant-\(2.1\) constructions; low injectivity plus index zero gives surjectivity; (41), (41f) | Symbol/remainder bounds and either compact completion or explicit local interpolation prices |
| Uniform frozen inverses | **CONDITIONAL, Level B** | Radius (52), coefficient caps, and bounds (53)–(54) on the actual varying domains | Frame derivative and tame perturbation constants |
| Nonlinear estimates | **PROVED mappings under these background/family hypotheses** | Exact remainder (46), product (47), difference price (50); high derivative loss identified | Full numerical product/family prices |
| Nonlinear closure | **CONDITIONAL, Level B** | Low-metric contraction with factor at most \(1/4\), exact speed constraint and normalization | Linear certificates and residual/response targets |
| Residual thresholds | **Explicit conditional expressions; no sufficient decimal tolerance** | (55)–(56), or response criterion (59) | Upper \(K_L,K_H,C_{\rm diff},r_0\) |
| Current profile existence | **OPEN** | Strong direct criterion fails; weaker diagnostic also exceeds its cap; no noninvertibility conclusion | Verified linear completion and smaller residual or small conforming correction response |

1. **Can the complete operator be proved invertible in weighted \(L^2\)?** Yes conditionally, by H1–H3, with a complete surjectivity proof. Actual invertibility of the present reference has not been numerically established. The unconditional new structural result is an index-zero Fredholm realization.
2. **Can this inverse extend to sufficient high regularity?** Yes under the specified coefficient bounds. High index zero and low injectivity give surjectivity; uniqueness identifies the inverses. Sections 12a–12b give the simpler constant-\(2.1\) realization and the direct bound \(K_{\rm high}\le C_{\rm reg}+C_{\rm low}K_{\rm low}C_Y\), with no additional high spectral nondegeneracy assumption.
3. **Can nonlinear estimates close for an arbitrarily accurate reference?** Yes, provided the explicit inverse and coefficient constants remain verified and finite. Freeze transport, contract in the low metric, solve the full speed equation, and normalize the cubic coefficient. Residual smallness does not establish linear nondegeneracy by itself.
4. **Exactly how small, in which norms?** In (2) and either specified high forcing norm, require (56) with (55), or the correction-response target (59). The current low norm is about \(0.00991\). The conservative high norm exceeds \(1.88\times10^9\) using the accepted historical jet and the new norm conversion; the weaker high norm's compact scalar \(L^2\) diagnostic already exceeds \(42.9\). Both exceed the largest possible direct high threshold \(1.89384\) for the chosen radius. An actual sufficient decimal tolerance requires the missing upper constants.
5. **What is the smallest remaining obstruction?** The decisive next work is the low compact complement and the **complete bordered matrix with full spatial response errors**, H2–H3. The speed response is now useful in (25); further polishing its nominal scalar is less urgent than computing the finite defect responses and their complement. Once low nondegeneracy is quantified, high compact/error prices and a correction-response computation are the remaining quantitative tasks. No remaining analytic axis-mapping gap is being hidden behind an invertibility assumption.

The new ingredients are the low cofactor mapping bound, universal signed divided-axis estimate, global compact kernel and prescribed-margin flow weight, finite border with surjectivity, exact chart preconditioning, accurate conforming speed response, and the direct trace-gain route to constant \(2.1\) high regularity. None gives an actual numerical inverse bound until its stated finite checks are carried out.

## 20. Sources and reproducibility

The main local sources are:

- [Profile audit](../case1/X3_CURRENT_PROFILE_AUDIT.md), [initial weighted-energy audit](X3_WEIGHTED_L2_QUICK_ESTIMATE.md), and [delayed-weight/rank-one audit](X3_DELAYED_WEIGHT_RANK_ONE_CHECK.md).
- Candidate 013 actual proof sections in /mnt/d/Changhe_D/IPM_writing/sections/: 03-frozen.tex, 04-energy.tex, 05-validation.tex, 06-reconstruction.tex, and 07-analytic-appendix.tex.
- [S2 theory](../analysis3/IPM_Analysis_III.artifacts/S2_L2_THEORY.md), [global geometry 79](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/79_actual_global_zero_set/PROOF.md), [axis Volterra 114](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/114_weighted_scalar_graph/PROOF.md), and [full coupling 123](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/123_variable_order_coupling/PROOF.md).
- [Symbol inequality 142](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/142_global_symbol_inequality/PROOF.md), the actual order-reduction/coupling/penalty/domain proofs 144–148, [compact estimate 149](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/149_global_high_estimate/PROOF.md), and [high Fredholm theorem 150](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/150_actual_high_fredholm/PROOF.md).
- [Velocity coefficients 155](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/155_velocity_coefficients/PROOF.md), [uniform perturbed estimate 158](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/158_uniform_perturbed_estimate/PROOF.md), scalar/full perturbation proofs 164–165, [moving-tail uniformity 167](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/167_moving_tail_uniform/PROOF.md), [full moving-tail column 217](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/217_full_moving_tail_holder/PROOF.md), and [high residual lower bound 179](../analysis3/IPM_Analysis_III.artifacts/verification/proofs/179_high_residual_lower/PROOF.md).

The retained external directory is /mnt/d/Changhe_D/X3_linear_8h_20261107/. Its [command guide](/mnt/d/Changhe_D/X3_linear_8h_20261107/REPRODUCE.md) and [reproducibility manifest](/mnt/d/Changhe_D/X3_linear_8h_20261107/REPRODUCIBILITY_MANIFEST.json) record commands, preserved inputs and hashes. It contains:

| Deliverable | Location within that directory |
|---|---|
| Derivations and domain/kernel audits | notes/01 through notes/31 |
| Evaluator manifest and preserved inputs | INPUT_MANIFEST.json, inputs/, helpers/scan.py |
| Low coefficient, column and residual estimates | results/low_constants_stride1_nt512.json |
| Global signed-price and past-flow diagnostics | results/global_axis_price.json and past-flow summaries |
| Accurate speed response | results/logtan_response_stable5_adaptive_stride4_nz1793_nm1024.npz |
| Independent spatial response check | results/adaptive_finecheck_logtan_response_stable5_adaptive_stride4_nz1793_nm1024_stride2_nz1793_nm1536.json |
| Axis strips and origin head | results/axis_tail_logtan_response_stable5_adaptive_stride4_nz1793_nm1024.json and matching inner-head summary |
| High symbol scans | results/high_scales_scan.json and results/constant_order_sectors_symbol_scan.json |
| Fixed-cutoff Hardy embeddings and scalar kernel prices | results/high_embedding_axis_R8_fixed.json |
| Speed-interval diagnostics and exact parameter derivatives | results/parameter_family_diagnostic.json |
| Explicit compact cell projection prototypes | results/compact_cell_projection_32_16.json and results/compact_cell_projection_64_32.json |
| Exterior norm and differentiated-energy checks | results/column_tail_norms.json and results/response_boundary_identity_ref2.json |
| Historical high-jet transfer and exact coarse inequalities | scripts/transfer_high_residual_point_bound.py and results/high_residual_point_transfer.json; source jet/certificate in inputs/ |

Python 3.12.3, NumPy 1.26.4 and SciPy 1.14.1 were used. The response was checked by density-Green and differentiated-source-Green implementations; a separate Gaussian source reproduced its known strain \(1/8\) to about \(10^{-11}\). The background cache is a floating canonical quadrature, and only its 261 physical stream modes were retained. Exact origin statements use repaired modal identities and accepted certificates, rather than the cache's small strain offset.

If the original temporary evaluator disappears, put the retained helpers/ directory on PYTHONPATH; it points to inputs/ and the unchanged repository numerical source. Scripts and summaries for rejected finite sections remain identifiable, but their spurious eigenvalues and underresolved column norms are not evidence.

No report was committed or pushed. Existing untracked collaborator files were preserved. The final repository check concerns only the requested new report.

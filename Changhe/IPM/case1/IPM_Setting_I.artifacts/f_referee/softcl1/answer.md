The heuristic identifies a plausible source of weak numerical sensitivity, but it does **not presently justify an uncertainty interval for \(c_l\)**. In particular, the frozen-transport construction does not establish the coupled residual estimate, and nondegeneracy alone does not justify the proposed J-pattern estimator.

| Task | Verdict |
|---|---|
| 1. Smooth cutoff construction | **Correct for frozen transport; conditional and unproved for the coupled equation.** |
| 2. Nonclosed range | **Not established.** A bounded inverse as assumed in §13.9 excludes it in the same spaces and norms. |
| 3. J-pattern estimator | **Conditional.** Its claimed justification from nondegeneracy alone is **wrong**. |
| 4. Numerical accuracy claims | The data establish reproducibility and weak sensitivity. **Absolute uncertainty remains uncalibrated.** |

I write \(\lambda=c_l\), keeping \(\psi_{xy}(0)\) distinct. One qualification to the background: the supplied reports establish that every open-quadrant characteristic comes from \(P\) under the additional minimal-configuration hypothesis \(H_{\min}\). I accept that basin property for the characteristics considered here.

On **task 1**, the precise frozen-field calculation is straightforward. Suppose \(\rho_d\) solves the equation at \(\lambda_*+d\), with field \(W_d\), and put
\[
\widetilde\rho=\rho_d e^{-\phi},\qquad f=\widetilde\rho-\rho_d.
\]
Linearity of the canonical velocity law gives the **exact coupled identity**
\[
\boxed{\quad
\frac{F(\widetilde\rho,\lambda_*+d)}{\widetilde\rho}
=-W_d\cdot\nabla\phi
+U[f]\cdot\nabla\log\widetilde\rho .
\quad}
\]
Thus a time cutoff satisfying \(|\partial_t\phi|\lesssim s|d|/T\) controls the first term. It does not control the second.

At first order in \(\phi\), the omitted term is
\[
-U[\rho_d\phi]\cdot\nabla\log\rho_d.
\]
There is no automatic factor \(1/T\). With suitable uniform regularity estimates it might be \(O(s|d|)\); merely knowing the amplitude of \(\phi\) does not even supply that uniform estimate. The singular-integral velocity operator is not bounded from arbitrary \(L^\infty\) data to \(L^\infty\), and cutoff derivatives can grow with resolution.

A simple counterexample to discarding feedback is constant multiplication. For an exact solution \(\rho\), frozen transport also annihilates \(k\rho\), but the coupled residual is
\[
F(k\rho,\lambda)=k(k-1)U[\rho]\cdot\nabla\rho,
\]
generally nonzero. This example changes the normalization; it isolates the invalid frozen-to-coupled implication.

There is also a concrete normalization-preserving illustration with the actual canonical law. Take the smooth admissible *trials*
\[
\rho_\varepsilon=x^2y\,e^{-(1+\varepsilon)r^2}.
\]
Their cubic coefficient is one, and direct polar integration gives
\[
\psi_{xy}[\rho_\varepsilon](0)=\frac1{8(1+\varepsilon)}.
\]
At fixed \(\lambda=(1+1/8)/3\), their relative residual tends near the origin to
\[
3\lambda-\psi_{xy}[\rho_\varepsilon](0)-1
=\frac{\varepsilon}{8(1+\varepsilon)}.
\]
Yet the multiplier \(\phi=\varepsilon r^2\) has \(W\cdot\nabla\phi\to0\) there. The new origin defect comes from the nonlocal feedback. These Gaussian trials are not exact profiles; this calculation demonstrates the missing term, not nonexistence of the proposed special construction.

Several additional gaps matter:

- The hypothesized family of coupled, non-\(C^1\) solutions \(\rho_d\) has not been constructed. It does not follow from nondegeneracy in the admissible class.
- Removing a label factor in a \(C^1\) conjugacy does not establish \(C^{2,\alpha}\) regularity in physical coordinates. Section 13.8 correctly withdraws the earlier smooth-linearization assertion.
- Source regularity cannot simply be transferred to the hypothetical singular family. In the linear model,
  \[
  \partial_\xi\!\left[\eta\Phi(\xi/\eta^A)\right]
  =\eta^{1-A}\Phi'(\xi/\eta^A).
  \]
  For nonconstant \(\Phi\), this becomes unbounded. The relation \(\operatorname{curl}U=-\rho_x\) then obstructs treating its velocity as a uniformly \(C^1\) source field.
- A cutoff must preserve the center normalization, the imposed origin identity, parity, and the required growth and derivative bounds. Reimposing those constraints produces further corrections.

Can feedback be absorbed by the tangent problem? **Possibly, partly, but not automatically.** At a regular exact profile the full tangent equation is
\[
Lu+dq,\qquad
Lu=W\cdot\nabla u-u+U[u]\cdot\nabla\rho,\qquad
q=X\cdot\nabla\rho.
\]
One must solve or estimate this coupled problem with all constraints. A frozen transport correction is only one component. Conversely, the displayed feedback term does **not** prove that every possible correction leaves an \(O(|d|)\) residual. Establishing such a lower bound requires a stability or adjoint argument.

The logarithmic resolution calculation itself is correct as a local scale:
\[
T_{\rm near}\sim \frac1A\log\frac1h.
\]
With \(A=10.15272\), \(h=10^{-3}\) gives \(0.6804\), and each halving adds only \(0.06827\). It is not a guaranteed globally usable transition time.

Finally, the frozen calculation bounds \(R/\rho\). An unweighted supremum of \(R\), the fitted normalized maximum, and the discrete residual 2-norm require their own weight comparisons. Also, even a successful construction would provide an **upper bound** on the best residual at offset \(d\); calling that residual “of order \(s|d|/T\)” requires a matching lower estimate.

On **task 2**, “bad conditioning” and “nonclosed range” must be separated by specifying the spaces.

Here is a direct consequence of §13.9’s hypothesis. Suppose
\[
B(u,d)=(Lu+dq,Nu)
\]
is a bounded isomorphism between the stated Banach spaces, where \(N\) extracts the normalization coefficient. Define
\[
\ell(r)=\text{the exponent component of }B^{-1}(r,0).
\]
Then
\[
\ell(Lu)=0\quad(Nu=0),\qquad \ell(q)=1,
\]
and therefore
\[
\boxed{\quad |d|\le \|\ell\|\,\|Lu+dq\|.\quad}
\]
Moreover,
\[
\operatorname{ran}(L|_{\ker N})=\ker\ell,
\]
so the normalized shape range is a closed hyperplane.

Consequently, arbitrarily small residuals with unit exponent component are incompatible with that bounded inverse **in the same norms**. A proposed cutoff sequence must instead lose the relevant regularity bounds, use a weaker residual norm, leave the local neighborhood, or invalidate the invertibility hypothesis.

Without that hypothesis, a verified sequence
\[
Nu_n=0,\qquad Lu_n+q\longrightarrow0
\]
would show that \(-q\) lies in the closure of the shape range. If it is absent from the range itself, that range is nonclosed. If it belongs to the range, there is an infinitesimal exponent kernel; a nonlinear family still requires additional analysis.

Neither possibility follows from the reported finite-dimensional sensitivities. For example,
\[
(u,d)\longmapsto(u+d,\varepsilon d)
\]
has closed range and is invertible for every \(\varepsilon>0\), however small.

Logarithmic cutoffs can nevertheless cause genuine failure of residual control in a weak norm while the exact solution remains unique. Consider
\[
yu'(y)=0,\qquad u(0)=d,\quad u(1)=0.
\]
The only exact solution is \(u=0,d=0\). Choose smooth \(\chi\), equal to one below \(-1\) and zero above \(0\), and set
\[
u_T(y)=d\,\chi(\log y/T).
\]
These are smooth trials satisfying the boundary conditions, with
\[
\|yu_T'\|_\infty\le C|d|/T.
\]
Their \(C^1\) norms grow exponentially. Thus residual minimization can fail to identify a parameter without producing a family of exact solutions. This is a reduced transport example, not a coupled IPM construction.

The symbol computation in G38(b) is correct:
\[
\sigma_K(\zeta)
=\frac{\zeta_1\zeta_2\rho_x-\zeta_1^2\rho_y}{|\zeta|^2},
\qquad
\sigma_K(-W_2,W_1)=-\frac{W_2\rho}{|W|^2}.
\]
It explains why coupling cannot simply be discarded on characteristic labels, where the transport principal symbol vanishes. Near the weak source direction this last expression approaches \(-\rho_y(P)\). It does **not**, by itself, establish compactness, Fredholmness, or either sign of an exponent stability constant.

On **task 3**, J is a useful transport diagnostic, but its interpretation needs two qualifications before estimating anything.

First, when \(h(P)=1\), appropriate convergence holds, and \(\rho_y(P)>0\), write \(W_2=yb\). Then
\[
\rho_{\rm tr}(X)=\rho_y(P)y
 \exp\!\left[-\int_{-\infty}^0(b(\Phi_sX)-1)\,ds\right]
\]
is the transport solution for the trial’s own field, and
\[
J(X)=\log\frac{\rho(X)}{\rho_{\rm tr}(X)}.
\]
This identity follows by integrating the equation for \(\log(\rho/y)\).

If \(h(P)\ne1\), then \(R/\rho\to h(P)-1\), and the unrenormalized infinite integral diverges. One must specify a finite cutoff or a renormalization. Centering may cancel a common divergence under a common-time convention, but does not make different cutoff conventions equivalent. Also, the condition \(g=o(|X-P|)\) in §13.9 is insufficient for its transport integral: an integrand behaving as \(1/|s|\) still diverges. A positive power improvement or a suitable Dini condition is needed.

Second, invariance under residual relocation is a **fixed-field, fixed-endpoint** statement. Changing the trial changes \(U\), the paths, and \(\rho_{\rm tr}\). Moving residual beyond the observation section \(r=20\) also removes it from the measured backward integral. Therefore a transition window extending farther into the far field cannot automatically be paired with the claimed invariant J measurement at \(r=20\).

For the estimator, let \(\Pi\) denote centering with specified label weights, and define
\[
j=\Pi J,\qquad S=\Pi\,DJ(v,1),
\]
where \(v\) is the shape tangent accompanying unit exponent change. **The sensitivity must itself be centered.** Otherwise the proposed denominator is already incorrect for a pure parameter signal.

Decompose the actual error as
\[
(\rho-\rho_*,\lambda-\lambda_*)=(dv+e,d).
\]
Assuming differentiability of the chosen J diagnostic,
\[
j=dS+B_J e+\text{higher-order terms},
\]
where \(B_J e=\Pi DJ(e,0)\). Hence
\[
\boxed{\quad
\widehat d=\frac{\langle S,j\rangle}{\langle S,S\rangle}
=d+\frac{\langle S,B_J e\rangle}{\langle S,S\rangle}
+\text{higher-order terms}.
\quad}
\]
Nondegeneracy of the full equation does not eliminate the second term.

A concrete counterexample is
\[
F(a,d)=(a,d),\qquad J(a,d)=(a+d,-a-d).
\]
The full derivative is the identity, and the fixed-\(d\) least-squares shape minimizer is \(a=0\). Thus \(S=(1,-1)\). A trial \((a,d)=(\varepsilon,0)\) produces \(\widehat d=\varepsilon\), although its exponent error is zero. Everything is exactly linear.

The J estimator becomes defensible if the remaining projected shape error is shown small or orthogonal to \(S\), and the sensitivity is stable under refinement. Minimizing the **transport-row** norm does not imply orthogonality in the **J-pattern** norm.

Other failure modes include a small or resolution-dependent \(S\); omitted angular labels; source-cutoff error; interpolation error; unaccounted common-mode information; and offsets large enough to leave the linear regime. Sensitivity should be measured by recomputing the full field, moving source, characteristics, and cutoff convention at both signs of several decreasing offsets.

A full adjoint is the more principled estimator for the functional \(\lambda\). Formally, solve
\[
L^*z+\nu N^*=0,\qquad \langle z,q\rangle=1.
\]
Then for a normalized nearby trial,
\[
\lambda-\lambda_*=\langle z,R\rangle
+O(\|(\rho-\rho_*,\lambda-\lambda_*)\|^2),
\]
so the corrected value is \(\lambda-\langle z,R\rangle\). Approximate adjoints add their own error paired with \(R\). This becomes an error bound only after controlling those terms and the nonlinear remainder.

There is a useful discrete version using the existing tangent calculation. Let \(M\) contain the normalized shape columns of the **full coupled** residual Jacobian, \(b\) its exponent column, and
\[
v=\arg\min_v\|Mv+b\|_Q,\qquad s=Mv+b.
\]
The normal equations give \(M^*Qs=0\), so for any linearized residual \(r=Me+bd\),
\[
\boxed{\quad d=\frac{\langle s,r\rangle_Q}{\|s\|_Q^2}.\quad}
\]
Unlike the proposed J projection, this removes all represented shape errors because it uses the same full residual metric as the tangent minimization.

However, applying it only to the original fitted rows may return zero merely from least-squares stationarity. An accuracy assessment needs an independently evaluated residual and an enriched or otherwise checked operator/adjoint. The exported fields and integrator suffice for J diagnostics; a full adjoint additionally requires applying the canonical map \(u\mapsto U[u]\), including its tail treatment. Freezing the exported \(W\) would omit the term at issue.

On **task 4**, the numerical evidence should be classified as follows.

| Quantity | Honest interpretation |
|---|---|
| Spread of comparable fits | Empirical reproducibility and demonstrated lack of discrimination by current criteria; not an interval containing the exact exponent. |
| Tiny changes during continued LSQR or refinement | Iteration stability; weak evidence for accuracy when the soft direction is barely explored. |
| J/S projection | A conditional signed correction, once pattern alignment, nuisance error, cutoff error, and sensitivity stability are checked. |
| Fixed-\(\lambda\) residual curves | Evidence about sensitivity within the tested discretizations; bounds require additional minimization and discretization control. |
| Agreement with \(h(P)=1\) at fixed \(\rho\) | A consistency check, especially because that condition was fitted. |
| Independent solver agreement | Useful empirical accuracy evidence when both solvers actually resolve the exponent direction and their numerical errors. |

Calling the fit spread a “lower bound on uncertainty” is acceptable only informally, meaning a demonstrated range of numerically indistinguishable fitted values. It is not a mathematical lower bound on either fit’s error. If there is one exact exponent, two fits separated by \(\Delta\) imply only that at least one has error at least \(\Delta/2\).

The supplied numbers illustrate the sensitivity problem:

- The independent residual slope predicts a residual-vector change
  \[
  (3.2\times10^{-3})(3.1\times10^{-5})
  =9.92\times10^{-8},
  \]
  against a \(6\times10^{-4}\) floor.
- At a least-squares minimum with an orthogonal residual floor,
  \[
  m(\lambda_0+\delta)^2
  \simeq m_0^2+\sigma_\lambda^2\delta^2.
  \]
  For those numbers, the norm increases by only about \(8.2\times10^{-12}\). A nonzero-floor curve need not look V-shaped.
- The ratio \(6\times10^{-4}/(3.2\times10^{-3})=0.1875\) is only a local sensitivity scale. It is not an error bar or evidence that linearization remains valid over that distance.
- Dividing the two J spreads by \(0.01\) gives \(1.7\times10^{-3}\) and \(3.9\times10^{-4}\). These are **not computed exponent corrections**: a spread is not a signed projection, and the quoted sensitivity comes from another discretization with potentially different norms.

The decrease in J spread by a factor \(4.36\), while \(\lambda\) moves by only about \(10^{-7}\), is particularly informative. Conditional on a stable soft pattern, the disappearing part is predominantly representation or fitting error, rather than a fixed exponent mismatch. It does not exclude a remaining common bias.

For a residual curve, an observed optimized value is an **upper bound** on the true infimum over admissible shapes. A solver’s failure to find a good fit at some \(\lambda\) does not exclude that value. Practical numerical brackets should therefore be tested under basis enlargement, changed starts, independent residual evaluation, and improved optimization. They remain empirical brackets unless those gaps are bounded.

The fixed-\(\rho\) determination from \(h(P)=1\) is especially easy to overinterpret: its derivative near one is not the derivative along a relaxed shape direction. The supplied fits show that shape relaxation reduces that sensitivity drastically. Agreement at \(10^{-6}\) therefore does not establish \(10^{-6}\) exponent accuracy.

I would approve wording such as:

> The computed branch has a representative fitted exponent \(c_l\simeq5.57636\). Fits of comparable residual quality differ by approximately \(3.1\times10^{-5}\) and exhibit a weakly penalized exponent direction. This spread measures empirical reproducibility, not an uncertainty interval. The available diagnostics do not yet calibrate the absolute exponent error or the accuracy of the last quoted digits.

I checked the multiplier identity, linearized stability argument, symbol, J identity, estimator counterexamples, and adjoint formulas algebraically. I checked the scalar numerical comparisons with single-threaded standard-library Python; I did not rerun profile fits or characteristic integration. The arguments and calculation record are saved in [INDEX.md](INDEX.md).

Opus 5.5 collaboration was attempted through the configured Python Bedrock client, but credential retrieval failed. No Opus response or substitute-model review was obtained.
# Whole-plane coefficient certificate for the tame Q source estimate

Status: specification and proof of the running interval producer. Completion is determined by the producer's complete coverage/hash assertions and final result.json, not by this document or by partial chunks.

The executable certify_Q_source_constants.py computes actual Candidate013 bounds for
\[
 H_1=\sup W_2|D^2\rho_*|_F,\quad
 D_j=\||D|^j\nabla\rho_*\|_2\ (1\le j\le4),\quad
 X_2=\||D|^2(x\nabla\rho_*)\|_2,\quad
 X_4=\||D|^4(x\nabla\rho_*)\|_2.
\]
It then substitutes them into the Wiener moment and tame source-commutator estimate proved in Q_SOURCE_FRACTIONAL_COMMUTATOR.md. Since \(W_a\le W_2\) for \(0<a\le2\), the same \(H_1\) remains a valid upper bound for those auxiliary weights.

## Scalar radial reduction

Let \(b=\nabla\rho\). Fourier Parseval gives the whole-plane identities
\[
 D_1^2=\|\Delta\rho\|_2^2,\quad
 D_2^2=\|\nabla\Delta\rho\|_2^2,\quad
 D_3^2=\|\Delta^2\rho\|_2^2,\quad
 D_4^2=\|\nabla\Delta^2\rho\|_2^2.
\]
The weighted coordinate norms satisfy
\[
 X_2^2=\|r\nabla\Delta\rho\|_2^2+4\|\Delta\rho\|_2^2,
\]
\[
 X_4^2=\|r\nabla\Delta^2\rho\|_2^2+16\|\Delta^2\rho\|_2^2.
\]
Indeed \(\Delta(x_jb_k)=x_j\Delta b_k+2\partial_jb_k\), and
\(\Delta^2(x_jb_k)=x_j\Delta^2b_k+4\partial_j\Delta b_k\).
The cross terms vanish after summing coordinates because in dimension two
\(\int(x\cdot\nabla f)\Delta f=0\).
Candidate013's exact far decay makes the integration-by-parts boundary errors tend to zero. The density itself need not belong to L2: its derivatives of order at least2 do, and radial cutoff approximation converges in every homogeneous seminorm appearing here.

These Parseval identities are applied only after the entire plane has been covered. On the omitted origin and exterior regions the actual Laplacian sums are bounded directly by Cartesian derivatives and Minkowski; a whole-plane identity is never substituted on a restricted subregion.

For a scalar angular mode \(F(r)\sin(n\theta)\) or \(F(r)\cos(n\theta)\), let
\[
 L_nF=F''+r^{-1}F'-n^2r^{-2}F.
\]
Only the six radial fields \(L_nF,(L_nF)',nL_nF/r,L_n^2F,(L_n^2F)',nL_n^2F/r\) are required. Their squared norms use angular weights \(\pi\), or \(2\pi\) for a constant cosine mode. The final two coordinate-weighted integrals use the radial measure \(r^3dr\); all other integrals use \(rdr\).

## Certified local Taylor fields

Every panel has exact rational endpoints, centered at \(r\) with halfwidth \(h\). The inherited exact-source evaluator supplies the actual grouped scalar density Taylor series and mode majorants \(M_n\) on \(|z-r|\le r/8\). Its majorant construction bounds each exact potential atom on the disk \(r/4\), where every noninteger denominator lies in the open right half-plane, and then applies Cauchy differentiation before summing absolute contributions.

At the smaller disk \(|z-r|\le r/16\), Cauchy bounds the first five radial derivatives by
\[
 |F^{(j)}(z)|\le j!M_n(16/r)^j,\qquad |z|\ge15r/16.
\]
Inserting those bounds into the explicit radial differential expressions yields a finite majorant for every required field. In particular
\[
\begin{aligned}
L_n^2F={}&F^{(4)}+2r^{-1}F^{(3)}
-(1+2n^2)r^{-2}F''\\
&+(1+2n^2)r^{-3}F'
+n^2(n^2-4)r^{-4}F.
\end{aligned}
\]
Its derivative uses coefficients \(1,2,-(3+2n^2),3(1+2n^2),n^4-10n^2-3,-4n^2(n^2-4)\) at derivative orders5 through0, with the corresponding inverse powers of \(r\).

The producer selects a Taylor degree \(N\) for which the summed field remainder is below its explicit scale-dependent target. It computes the actual density Taylor series through degree \(N+5\), so every required field has correct Taylor coefficients through \(N\), with an assertion on the Arb series precision. If \(M_{\rm field}\) is its analytic majorant and \(z=h/(r/16)<1\), the omitted terms have the rigorous uniform bound
\[
 \varepsilon_{\rm field}\le M_{\rm field}\frac{z^{N+1}}{1-z}.
\]
No quadrature or sampling inference is involved.

For a polynomial part \(p(t)\), the integral of \((r+t)^kp(t)^2\), \(k=1\) or3, is computed by Arb polynomial multiplication followed by exact monomial integration on \([-h,h]\). If that nonnegative integral has certified upper endpoint \(I\), its true field norm on the panel is at most
\[
 \sqrt I+\varepsilon_{\rm field}
 \left(\int_{-h}^h(r+t)^kdt\right)^{1/2}.
\]
The two masses are \(2rh\) and \(2r^3h+2rh^3\). Squaring and applying the exact angular Parseval weights gives each panel's upper energy.

For the weighted Hessian supremum, its polar orthonormal components are formed before enclosure:
\[
 F'',\qquad n(F'/r-F/r^2),\qquad F'/r-n^2F/r^2.
\]
This preserves the cancellation of the linear origin mode. Polynomial interval evaluation and the same Cauchy tails bound their angular coefficients. The sum of absolute angular coefficients bounds each component; the Frobenius combination has coefficients1,2,1. Multiplication by the maximal panel weight gives \(H_1\)'s panel upper bound.

## Entire origin and exterior

The producer uses exact rational homogeneous expansions of degree20 at the origin and at infinity. The analytic expansion variable is \(r^2\) or \(r^{-2}\); differentiated Cauchy coefficient majorants enclose the full omitted series uniformly throughout the relevant region. Degree20 is large enough for the maximum Cartesian differentiation order8 of the potential: its remainder implementation requires \(N_{\rm remainder}\ge2d\).

A homogeneous term \(c r^p\) has radial L2 norm, with extra weight \(r^w\), bounded by
\[
 \sqrt{2\pi}|c|\,
 \frac{R^{p+w+1}}{\sqrt{|2p+2w+2|}},
\]
with the appropriate sign condition at zero or infinity. The same formula applies to every positive analytic-remainder monomial. Minkowski bounds the sum of all terms. The actual Cartesian Laplacian combinations, including all binomial coefficients, are then bounded by Minkowski before being squared. The producer therefore charges every omitted spatial tail.

The Hessian supremum at zero uses its exact nonnegative powers. At infinity it multiplies every Hessian monomial by \(r\) before taking the uniform endpoint bound; all shifted powers remain negative. The remaining factor \(W_2/r\) is bounded by \(\sqrt{4+R^{-2}}\). An unbounded weight is never multiplied by an unweighted uniform supremum without this power check.

## Completion and reproduction

Configuration and every saved chunk bind the exact candidate hashes, evaluator source, asymptotic source, and producer source. On resume all hashes and panel indices must match. Final assembly requires every panel index exactly covered, adds the origin/exterior energies, and only then evaluates the global identities and moment bounds. A status claiming certified constants is emitted only after those checks finish.

The completed output is `Q_source_certificate_v01/result.json`, emitted at 2026-11-05 01:53:14 UTC with status `CERTIFIED_WHOLE_PLANE_Q_SOURCE_CONSTANTS`. Its SHA256 is `b593bf4fda27af6cc8cbd8a6808fcf821dbe0d2327f32e9d7b741599e6201500`. All 2303 panels and both infinite spatial endpoint regions are included. The following convenient outward upper bounds follow from the stored Arb enclosures:

| Constant | Certified upper bound |
|---|---:|
| \(H_1\) | 14.830022 |
| \(D_1,D_2,D_3,D_4\) | 17.011863, 10.465985, 28.414492, 992.320397 |
| \(X_2,X_4\) | 57.993746, 279.211967 |
| \(A_2,A_{21/10}\) | 222.176812, 247.657246 |

The earlier exploratory value 16.453 was a Cartesian componentwise angular-l1 majorant evaluated at sampled radii. It was not a sampled value of the actual Frobenius Hessian, and need not lie below the present rigorous upper bound: the present proof combines the polar Hessian components before angular enclosure and is tighter. The exact radial reduction was independently compared with Cartesian derivatives in `Q_source_radial_reduction_audit.json`.

The strict fixed-parameter energy assembly and its independent 768-bit reconstruction consume the full unrounded enclosures, rather than the displayed rounded constants. They are separate from this coefficient certificate and are recorded in `../operator_theory/fixed_parameter_closure_v01.json` and `../ROOT_FINAL_LOCAL_Q_REPLAY.json`.

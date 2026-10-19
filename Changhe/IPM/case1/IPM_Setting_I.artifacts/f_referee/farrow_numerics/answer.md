The extrapolation geometry is correct. The claim that damping determines the band is unproved, and the verified residual remains a defect of the actual trial. The proposed continuation is useful, provided its result is described as a joint change in collocation coverage and inverse domain unless controls separate those effects.

There is also a mathematical correction: **for \(0<k<1\), there is no nonlinear angular profile equation for \(\Theta_0\) at leading order. The first correction is determined by \(\Theta_0\).**

For **question 1**, I independently loaded the stored coefficients and knots. The geometry is:

| Location | Shape radius \(u\) | \(q\) | Fraction of last knot interval |
|---|---:|---:|---:|
| Old collocation cutoff | 900 | 0.99623615 | 43.79% |
| Reported maximum, approximately | 4700 | 0.99903054 | 85.52% |
| Proposed collocation cutoff | 9000 | 0.99943116 | 91.50% |

Thus the maximum is indeed in an uncollocated portion of the same degree-seven polynomial piece.

However, “not tested by any row” needs qualification. Its coefficients also determine the polynomial on the fitted portion, and the modal inverse couples the rows through the boundary closure. In the implementation, that closure matches density and radial derivative at the finite inverse boundary; it does not directly use the limiting \(b_m(1),b_m'(1)\).

Nor does the evidence identify damping as the cause. The solver damps *scaled Gauss–Newton increments*, uses finite Krylov iteration budgets, and can freeze columns below a preconditioning threshold. Shared initialization, weak sensitivity, limited iteration, and restricted radial or angular flexibility are all possible causes of persistence. The report itself records little objective sensitivity to changing damping. A defensible diagnosis is:

> The far maximum occurs in an uncollocated spline continuation and may reflect weakly constrained exterior coefficients. Its persistence under the existing fits does not establish an intrinsic residual floor of the family.

It remains a meaningful out-of-sample defect of the candidate. It does not, by itself, reject the proposed asymptotic exponents.

The axis evidence also needs correction. [G73(h3) and G76]( VERIFY_REPORT.md) give c6g’s first-column normalized values as approximately
\[
(1.111,\ 1.096,\ 1.082,\ 1.077,\ 1.073,\ 1.073)\times10^{-6}.
\]
They are nearly flat, rather than quadratic. The quoted \(8.9\times10^{-9}\) is an **absolute residual floor**, not the normalized axis residual. The earlier entry’s notation also uses \(N_v\) for the denominator in part of its discussion, which appears to have caused the confusion. G76 additionally corrects the “every fit” claim: F1 and W1 have larger far maxima.

Write the denominator as \(D_v\), to avoid that ambiguity. If \(\delta=\pi/2-\theta\), a quadratic density zero generically gives
\[
\rho=O(\delta^2),\qquad R=O(\delta^2),\qquad D_v=O(\delta^2).
\]
Their quotient can approach a nonzero constant. The literal normalized residual on the exact axis is \(0/0\); its numerical floor is not the transverse limit. Moreover, asymptotically
\[
D_v\sim(1+k)r^k|\Theta_0|,
\]
so \(|\rho|\), rather than \(|X\cdot\nabla\rho|\), is the larger leading contribution when \(k=0.17936\).

Finite regularity is a possible numerical issue, but the proposed justification overstates what is known. [SPEC Lemma 5](SPEC.md:107) concerns a fractional contribution to the **centre trace** \(G_3(x)\). It explicitly does not prove a uniform two-dimensional expansion, much less its persistence along the far y-axis. Also, this trial already includes the fractional angular factor explicitly; the cosine series is not solely responsible for representing it.

The following tests distinguish the explanations:

- **Inverse and closure error:** freeze the physical density, including \(L\), and \(c_l\). Recompute velocities with larger inverse boundaries and separately refined radial and angular quadrature. Measure the change in the residual in the actual far annulus, including transverse axis limits. Freezing spline coefficients alone is insufficient if the code recomputes \(L\) from the inverse.
- **First-correction mismatch:** compute \(\Theta_0,\Theta_1\) from the endpoint jets and compare \(\Theta_1\) with the value required by the equation below. On sufficiently large radii, check the *signed* quantity \(r^{1-k}R/\rho\) against its predicted angular limit. Then test endpoint-derivative adjustments while holding the leading tail fixed.
- **Angular limitation:** first refine angular evaluation with the candidate frozen; then enrich the fitted angular basis while keeping rows and inverse accuracy comparable. Compare profiles at fixed \(\delta\), not just whichever column is nearest the axis. Inspect the unresolved angular part of the required first correction, including the explicitly represented fractional component.
- **Radial limitation:** after adding exterior rows, insert a few knots in the final interval by exact knot insertion, preserving the starting density. Improvement from subsequent fitting would demonstrate useful missing radial flexibility, although it would not alone prove optimality of either fit.

For **question 2**, the proposed run is a sound exploratory test, but several qualifications matter.

**First, correct the physical coverage.** The reader actually selects rows with \(u<0.9R_{\rm shape}\), as [centre_fit.py](centre_fit.py:41) confirms. With c6g’s stored \(L\),
\[
900L=6886.28,\qquad 9000L=68862.82.
\]
The numbers \(7651.42\) and \(76514.25\) are inverse-domain boundaries. Consequently:

- The old band through \(7651\) contains an uncollocated buffer.
- The proposed band through \(76514\) also contains an uncollocated buffer.
- The proposed run does cover the existing maximum near \(36000\).

Keep the historical physical bands if useful, but additionally split at the actual collocation boundary, using the new fit’s \(L\). Recompute c6g’s baseline maximum on **each identical band**. In particular, its maximum over \(r>76514\) cannot simply inherit the \(1.1\times10^{-6}\) maximum attained near \(36000\).

**Polynomial freedom is plausible, but sufficient accuracy is not established.** A degree-seven spline with simple knots is \(C^6\). If all preceding pieces are held fixed, the last piece has only one remaining degree of freedom:
\[
\delta b(q)=a(q-q_*)^7.
\]
There are not eight independent local coefficients under that constraint. Holding the polynomial exactly fixed on any open fitted subinterval would fix its entire continuation.

There can nevertheless be substantial practical freedom under approximate interior constraints. That particular perturbation is about **108 times larger at \(u=4700\) than at \(u=900\)**. Extending the rows therefore substantially increases their sensitivity to exterior changes. This supports trying the run; it does not guarantee \(10^{-7}\), especially with angular coupling and interior residual constraints.

**The proposed radial grid is slightly finer, not equally dense.** Its logarithmic steps are
\[
\Delta\log u_{\rm old}=7.87055\times10^{-4},\qquad
\Delta\log u_{\rm new}=7.49570\times10^{-4}.
\]
The new density is approximately 5% higher. Exact density matching would require about 23406 points over eight decades.

That difference is small and favorable, but count alone does not establish inverse accuracy. The implementation uses exponential-weighted cubic quadrature for modal integrals; verify it by frozen-profile radial refinement. Also refine angular quadrature independently: exponentiating a truncated angular expansion does not produce a band-limited density.

**The closure estimate is encouraging only where it was measured.** For the same frozen profile, extrapolating the measured law gives
\[
10^{-3(1-k)}=0.0034521.
\]
Thus the quoted \(2.6\times10^{-9}\) and \(1.3\times10^{-8}\) impacts would become approximately
\[
9.0\times10^{-12},\qquad 4.5\times10^{-11}.
\]
This makes closure contamination of those fixed interior diagnostics unlikely to dominate. It is not a bound in the new annulus, and it assumes the observed scaling continues. Refitting can change omitted-tail coefficients. Test the closure at the new annulus directly.

**Iteration budget and objective weighting require controls.** The most useful optimization control is an equal-budget continuation from c6g on the enlarged inverse domain and new grid, retaining the old collocation cutoff \(u<900\). Compare it with the \(u<9000\) continuation. Frozen evaluations with both inverse domains then quantify the immediate operator change.

The normalization \(\sqrt{14000/N_{\rm rows}}\) gives an average-type PDE objective. Adding a decade changes the relative mass assigned to the old region and new annulus; source and centre penalties have their own weights. Report these choices and compare both outcomes on a common validation objective. Also inspect annular RMS and maxima: a narrow axis-adjacent maximum can contribute little to the global least-squares objective.

Keeping \(c_l\) fixed is appropriate for this particular experiment. Verify residuals at that fixed value and report the strain-identity defect separately; do not silently substitute an independently recomputed \(c_l\).

Finally, your condition (a) establishes preservation of selected residual diagnostics and \(h(P)\). It does **not** establish closeness of the density or velocity to c6g. If the report claims preservation of the interior profile, also compare \(L,\rho,U\), and relevant jets in declared norms.

For **question 3**, I would use the following wording.

If the previously exterior maximum falls by at least fivefold:

> Extending collocation to \(u<9000\) reduced the independently verified \(N_v\) maximum in the specified newly covered annulus by at least a factor of five, while preserving the preregistered interior residual and \(h(P)\) controls. This supports a removable exterior-fitting defect of c6g; attribution specifically to missing rows requires the matched continuation and inverse controls, and the result proves neither existence nor accuracy outside the verified finite domain.

If it does not fall:

> At the stated basis, weights, fixed \(c_l\), and iteration budget, extending collocation did not materially reduce the far maximum, although its location was covered by residual rows. This does not distinguish insufficient optimization or weighting, radial or angular approximation error, and inverse error, and therefore does not refute the prescribed far-field expansion.

For **question 4**, distinguish the additive correction \(B\) from the relative correction \(C=\Theta_1\):
\[
\rho=r^kA(\theta)+r^{2k-1}B(\theta)+\cdots,
\qquad A=\Theta_0,\quad B=AC.
\]
Assume a termwise differentiable expansion and that the canonical velocity has leading term
\[
U=r^k(V_r e_r+V_\theta e_\theta)+o(r^k).
\]
These are hypotheses for the calculation, not consequences of the growth bound alone.

With the project’s convention \(\nabla^\perp=(-\partial_y,\partial_x)\), set
\[
\psi=r^{k+1}\Psi(\theta).
\]
Then the angular inverse is
\[
-\Psi''-(k+1)^2\Psi
 =k\cos\theta\,A-\sin\theta\,A',
\qquad
V_r=-\Psi',\quad V_\theta=(k+1)\Psi.
\]
Use periodicity and the prescribed parities. Since \(1<k+1<2\), the periodic operator has no resonant integer Fourier mode.

Now expand the transport residual:
\[
\begin{aligned}
R={}&r^k(c_lk-1)A\\
&+r^{2k-1}
\left[(1-c_l)B+kV_rA+V_\theta A'\right]
+o(r^{2k-1}).
\end{aligned}
\]
The order-\(r^k\) equation is only
\[
(c_lk-1)A=0,
\]
which is automatic for \(k=1/c_l\). The next order gives
\[
\boxed{(c_l-1)B=kV_rA+V_\theta A'.}
\]
Consequently, wherever \(A\ne0\),
\[
\boxed{\Theta_1=C
=\frac{kV_r+V_\theta A'/A}{c_l-1}.}
\]

Thus **the first correction is determined by the leading angular profile**. Its angular derivative does not enter at this order. Global matching may restrict which \(A\) occur, but this leading balance imposes no additional nonlinear equation on \(A\) alone. The equation \(kV_rA+V_\theta A'=0\) would arise if one additionally required \(B=0\).

At zeros of \(A\), use the additive equation rather than divide by \(A\). For a quadratic y-axis zero, parity and incompressibility give the finite limiting condition
\[
\Theta_1(\pi/2)
=-\frac{k+2}{c_l-1}V_r(\pi/2).
\]

This supplies a concrete diagnostic on the stored candidate. My small CPU calculation gives, in physical coordinates,
\[
\begin{aligned}
V_r(\pi/2)&\approx89.33392130,\\
\Theta_{1,\mathrm{stored}}(\pi/2)&\approx-42.55608261,\\
\Theta_{1,\mathrm{required}}(\pi/2)&\approx-42.55199833.
\end{aligned}
\]
The discrepancy is approximately \(-0.00408428\). Angular evaluations with 4096 and 8192 points agree closely, and an independent sine-coefficient summation checks the axis velocity. These are floating-point diagnostics, not interval bounds.

For a trial define
\[
F_1=(1-c_l)B+kV_rA+V_\theta A'.
\]
Then, away from angular zeros,
\[
N_v=r^{k-1}\frac{|F_1|}{(1+k)|A|}
+o(r^{k-1}).
\]
The computed axis limit is \(F_1/A\approx0.01868707\). There is therefore a concrete first-correction mismatch that endpoint-slope changes could reduce.

**It does not alone explain the finite-radius maximum.** At \(r=36000\), the first and second formal homogeneous residual contributions, divided by the leading denominator, are approximately
\[
+2.89\times10^{-6},\qquad -2.87\times10^{-6}.
\]
Furthermore, the explicit trial has a relative \(r^{-2}\) density term from its base factor, \(\chi\), and fractional radial multiplier. At the axis its coefficient is approximately \(-82.72\); drift on that term contributes approximately \(+6.03\times10^{-7}\) in the same normalization there. The omitted terms have not been bounded, so these numbers are **not** a reproduction of the measured peak. They demonstrate that cancellation and subleading radial structure matter at its location.

Adjusting \(b_m'(1)\) can therefore improve the band by correcting a mismatch, but those derivatives are not free asymptotic data once \(\Theta_0\) is fixed. A successful finite-annulus fit may also need changes to higher endpoint derivatives and their coupling to the interior.

The standalone derivation and reproducible checks are saved in [PROOF.md](PROOF.md) and [verification.json](verification.json). Only small CPU calculations were performed.

Opus 5.5 collaboration could not be completed because the configured Bedrock profile had no accessible credentials. No model was invoked or substituted.
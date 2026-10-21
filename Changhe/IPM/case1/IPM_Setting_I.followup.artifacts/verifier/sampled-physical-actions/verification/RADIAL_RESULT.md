# Sampled physical linearization: radial refinement

Date: 2026-10-20T19:41:15.561799+00:00. Status: numerical finite-span audit, no certified continuum spectral conclusion.

This supplements ANGULAR_RESULT.md using the same two pinned input fields, 58 points, 14 directions and physical domain norm. The final inverse uses 4096 angles, radial Gauss order32 and logarithmic panel width at most0.075, with outer radius10^30. Every inverse comparison uses this final inverse and the finest Cartesian gradient to fix a common base normalizer. No numerical researcher evaluator is imported.

| Grid | Columns | Smallest singular value | Cost for delta c_l=1 |
| --- | --- | --- | --- |
| n96m40S | 4 | 0.00286249143463 | 0.00302262473257 |
| n96m40S | 10 | 0.00229824450568 | 0.00245697522543 |
| n96m40S | 14 | 0.00213789304678 | 0.00236509513317 |
| n120m48_S | 4 | 0.001603162226 | 0.00161416175003 |
| n120m48_S | 10 | 0.000613758702667 | 0.00105728891806 |
| n120m48_S | 14 | 0.000529267847399 | 0.000732709738135 |

The separate order24/panel0.1 to order32/panel0.075 changes in the full14 whitened matrices have Frobenius norms1.38267318501e-7 and1.59733262543e-7. Their spectral norms are1.31893995064e-7 and1.53498994059e-7. These observed differences are6.47e-5 and3.02e-4 times the respective smallest singular values; they are sensitivities, not rigorous error bounds. At fixed order24, angular doubling changes the matrices by5.8344e-11 and5.9846e-11.

Using the final inverse, the independent analytic chain-rule gradient changes the full14 matrices by8.98487e-10 and7.84786e-10. Exact exterior-velocity bounds propagated with numerical gradients give Frobenius estimates1.83367e-9 and3.48848e-9. No complete rounding, interior quadrature or action-error enclosure has been supplied.

The n96m40S represented field has maximum sampled |R|/N_f=0.00548170121831 at point index35 of the fixed58-point set.
The n120m48_S represented field has maximum sampled |R|/N_f=0.0026269804156 at point index34 of the fixed58-point set.

Verdict: CONFIRMED as independent numerical recomputation on the stated spans and samples. Positivity on a finite span neither proves continuum isolation nor excludes an approximate kernel. The constrained costs remain upper bounds for infima over larger spaces. The residual standard for a smooth candidate is not met.

Reproduction: code/summary_all.py --radial consumes the three completed inverse action files and the separately refined Cartesian and analytic gradients. verification/summary_all_radial.json pins their SHA256 hashes and verification/summary_all_radial_matrices.npz contains the actual matrices. All asserted finite-matrix perturbation and reconstruction identities pass.

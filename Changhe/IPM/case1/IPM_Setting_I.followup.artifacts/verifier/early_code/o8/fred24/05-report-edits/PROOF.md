# Audit of the report summary

**Verdict: the central local exclusion is CONFIRMED after the norm repair. The summary is not fully correct as written.**

The proof in fred22 uses \(N_{\rm mon}\); the summary defines \(N_\phi\). Equation (N1) proves that these are different norms. The summary's attribution of the unchanged original constants to its displayed norm is therefore unsupported. The corrected origin bounds (R11), the audited remainder proof, and exact rational scalar arithmetic establish the same simple radii in \(N_\phi\), with slightly larger constants.

## Dependencies and scope

This result uses the four preceding audit proofs and the supplied report item beginning “Local exclusion with polynomial constants at the computed A.” Its historical numerical checks are treated as the supplied evidence the user expressly excluded from this arithmetic audit. Statements about fitted coefficients and sampled errors are not upgraded to interval-certified assertions here.

The exact original wording and replacements are in `REPLACEMENTS.txt`. That file changes every sentence that needs mathematical correction or a material qualification under this audit. Sentences not listed can remain, with the replacement norm conventions understood.

## Reasons for the replacements

1. **Audit status.** The opening qualification should now record that the analytic bounds have been checked, and that this required a correction when using the summary's norm.
2. **Definition of the norm.** The summary should name its \(R_\phi\) convention and specify \(\sigma\le2\), \(\theta\le1\), and the margins for the complex buffer. The original argument's algebra estimates do not state a theorem for arbitrary \(\sigma>2\).
3. **First variation and remainder claim.** The first variation applies with the compatible-polynomial decomposition, but the constants in the original norm proof use the monomial remainder. The corrected statement must distinguish these. Its reference inputs include weighted origin norms and anchored endpoint norms, not just unweighted suprema and a finite jet.
4. **Exponential claim.** The relative reconstruction avoids exponentiating a large upper bound for a reconstruction integral. It does not remove the actual exponential in the reference formula \(g_0=u^2H e^T/[A_0(1+u^2)]\). The report's literal claim that no exponential of a reference integral enters is too strong.
5. **Computed-reference constants.** In \(N_\phi\), our proved replacements are \(12519\), \(245246\), and the lower bound \(0.10269550\) for the allowable \(\delta_0\). The simple radius remains \(10^{-6}\). The derivative norm here means the trace differential \(D_wB\), not a joint differential on scalar parameters and traces.
6. **Profile statement.** Finite membership in the stated affine trace domain remains an additional condition; a source exponent exceeding \(1-\beta\) need not exceed the fixed norm exponent \(0.9\). The ball condition must be interpreted in that domain.
7. **The \(A_0=4\) comparison.** The same simple radii survive under the corrected \(N_\phi\) bounds; identify the center as \(A_0\) rather than inadvertently suggesting that \(A\) is simultaneously fixed and varied.
8. **Bare \(C^2\) counterexample.** Choose \(\gamma\) away from the possible cancellation. The argument proves divergence for the nonlinear functional on sufficiently small nonzero perturbations, which is stronger and clearer than the phrase “diverge at first order.”
9. **Dual norm and bump evidence.** The rigorous upper bound in the report's norm is now \(12519\). The quoted directional lower tests and sampled bump norms are numerical evidence. The original sampled value was about \(4.28\,10^{14}\), not a certified lower bound \(4.3\,10^{14}\).
10. **Fit distances and trial data.** The current report gives mutual distances of 15 to 56 based on sampled suprema. These are numerical estimates, not certified full-interval norms. Without additional estimates, sampled closeness cannot certify a \(10^{-6}\) trace-norm neighborhood. A version read earlier during this audit instead inferred mutual distances about \(0.5\) from the seventh-coefficient range; the current source has already removed that inference, and the replacement text below targets the current wording.

## Why the remaining scope claims are correct

For either norm, \(\|v\|\ge|c_7|\). Thus a difference of seventh coefficients gives the stated pairwise lower bound, subject to the numerical status of the coefficients. No derivative data sampled only at positive \(u\) can control the entire origin interval: choose a smooth perturbation supported below the smallest sampled \(u\), then extend it oddly near zero. It preserves all sampled data and all source constraints, while its weighted norm can be made large. This observation alone does not produce another exact PDE profile, and the corrected text does not claim it does.

The exclusion references need not be axis traces of profiles, and the positive obstruction at a rational reference does not certify the obstruction or constants of a fitted reference. The statement remains a conditional local exclusion, not a resolution of global \(P_\infty\) nonexistence.

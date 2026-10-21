# Reading-order index

The analytic argument is valid in the norm actually defined in fred22's equation (12). The report uses a different remainder in that norm. This is a real discrepancy in the attribution of the numerical constants, but it does not invalidate the advertised simple exclusion radii: the repair below proves the same radii in the report's convention.

1. [Differential](01-differential/PROOF.md). **CONFIRMED.** Normalization, affine dependence on \(e\), endpoint reconstruction, the finite-part adjoint, the three origin jets, and parameter derivatives.
2. [Remainder](02-remainder/PROOF.md). **CONFIRMED for the monomial-remainder norm in the original proof.** Every reconstruction and integral bound is checked. The transfer of those unchanged constants to the report's polynomial-remainder norm is **UNCLEAR as originally stated**. Explicit replacement constants repair it.
3. [Norms and radius](03-norm-and-radius/PROOF.md). **CONFIRMED.** The weaker endpoint norm suffices, a bare \(C^2\) tail does not, the origin threshold is sharp for the proposed supremum scale, and (32) follows. The identification of the two norm conventions is **REFUTED**. Both conventions now have certified simple radii.
4. [PDE exclusion](04-exclusion/PROOF.md). **CONFIRMED as a conditional theorem using the supplied PDE implication.** Membership in the chosen trace space is an explicit hypothesis. The source Hölder or cone condition alone does not imply membership for an arbitrarily fixed \(\theta\), such as \(0.9\).
5. [Report audit](05-report-edits/PROOF.md) and [exact replacement text](05-report-edits/REPLACEMENTS.txt). The central exclusion survives; the norm definition, constants, qualifications about reconstruction, and a few descriptions of numerical evidence need correction.

The important distinction is
\[
R_{\rm mon}=v-\sum_{j=3,5,7}c_ju^j,\qquad
R_{\phi}=v-\sum_{j=3,5,7}c_j\phi_j.
\]
The original proof and certificate use \(R_{\rm mon}\). The report and the present question use \(R_\phi\). The coefficients \(c_j\) agree, but the weighted remainder seminorms do not.

For the report's \(N_\phi\), our repaired bounds at \(A_0=10.150725,e_0=0.0135206\) are
\[
\|D_wB\|_{N_\phi^*}\le12519,\qquad C_2\le245246,\qquad
\delta_0\ge0.10269550.
\]
Equation (32) exceeds \(1.8749\,10^{-6}\), so \(10^{-6}\) remains valid. At \(A_0=4,e_0=1/16\), it exceeds \(8.0690\,10^{-8}\) with the stated parameter widths and \(1.4814\,10^{-7}\) with fixed parameters. Thus \(10^{-8}\) and \(10^{-7}\) remain valid, respectively.

These are local conditional exclusions around rational traces, not an exclusion of every \(P_\infty\) profile or a certified neighborhood of the computed branch.

## Evidence and limits

* [Exact arithmetic repair](02-remainder/verification/norm_repair.py) and [output](02-remainder/verification/norm_repair.json). Only the three origin perturbation majorants change. This deliberately reuses the original certificate's scalar arithmetic after auditing its analytic inputs; it is not a claim of an independently implemented numerical integration.
* [Execution record](verification/EXECUTION.md).
* [Source inventory](verification/sources.json).
* Each result has its own complete informal argument. No formal proof-assistant sources or formal verification are claimed.

Claude Opus 5.5 could not be consulted: the existing Python/Bedrock configuration failed during credential retrieval, before discovery or invocation. No model was invoked and no substitute was used.

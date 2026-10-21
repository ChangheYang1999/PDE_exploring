# Referee answer: fitted-reference obstruction and exclusion

Read the four results in order. Each contains its statement, hypotheses, proof, dependencies, and limits.

1. [01-obstruction/PROOF.md](01-obstruction/PROOF.md) , **CONFIRMED:** an interval Taylor certificate proves
   \(0.2830400682<B<0.2851567624\), hence \(b_0=0.28\), on the exact fitted reference. It also certifies reconstruction and parameter derivative bounds.
2. [02-radius/PROOF.md](02-radius/PROOF.md) , **CONFIRMED:** complete reference inventory and positive obstruction \(B>0.14\) on raw-remainder balls of radius \(4.5\,10^{-6}\) with the requested parameter rectangle, and \(5\,10^{-6}\) at fixed parameters. For the compatible-\(\phi_j\) remainder convention, multiply each radius by \(4/415\).
3. [03-trace-uncertainty/PROOF.md](03-trace-uncertainty/PROOF.md) , numerical pairwise distances and obstruction differences; exact separation by the Taylor coefficients alone; **REFUTED** sample-only control of the norm; a proved quantitative two-constants estimate under explicit additional analytic hypotheses. Whether an exact profile satisfies them is **UNCLEAR**.
4. [04-exclusion/PROOF.md](04-exclusion/PROOF.md) , **CONFIRMED conditional theorem:** no exact profile satisfying all the source, axis, parameter, and trace-ball hypotheses. The source endpoint theorem is a supplied analytic dependency. This is not a full \(\mathcal P_\infty\) exclusion.

The question's remainder wording can mean subtraction of compatible \(\phi_j\)'s, whereas fred22's actual estimate uses the raw Taylor remainder. Both norms, both sets of radii, and both numerical distance tables are given explicitly.

[VERIFICATION.md](VERIFICATION.md) distinguishes interval certificates from exploratory numerical values and gives reproduction commands. [INPUTS.json](INPUTS.json) records the exact input copies and their digests. The local code uses plain Python rational and interval arithmetic; no formal Lean certificate is claimed.

[collaboration/STATUS.md](collaboration/STATUS.md) records the Opus 5.5 availability limitation: the existing Bedrock profile failed to obtain credentials before model discovery. No Opus review occurred and no other model was substituted.

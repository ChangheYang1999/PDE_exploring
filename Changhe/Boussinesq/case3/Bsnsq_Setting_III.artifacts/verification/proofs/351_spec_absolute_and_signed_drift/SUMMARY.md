# Absolute and signed center drift

Updated 2026-10-22T11:42:53.969541+00:00. CONFIRMED: the uniform-tail integration lemma, positive coefficient under the stated sign hypothesis, and field-only counterexample to inferring signed divergence from absolute divergence. REFUTED: interpreting SPEC A5's unqualified never-converges as a conclusion about all signed truncations. OPEN: actual wording adoption and the general B2 endpoint.

The leading coefficient is B=[2 pi (1-1/beta)]^(-1) integral cos(theta)a(theta)dtheta. P33 gives v0(R)=B R^(1-1/beta)+o(R^(1-1/beta)). B=0 leaves convergence undecided by that leading theorem. In the nonnegative right-half-plane subclass, B>0; P18 alone supplies only the lower bound.

Own94/94 checks passed at 2026-10-22T11:41:47.689443+00:00 in 0.007202s. Proof aa4d1c95f4f3f229ad6c79e155ee8897c125626f1d33f08e83bc847929a6fb44; checker de76b9422b4f7757e11aa5006060afc795980ef23abed37d678ab29615e267ff. Initial80/81 preserved, one quadrature-tolerance failure corrected using an exact integral. All field controls are explicitly not B2 solutions. Actual model618-620 metadata records claude-opus-5-5; followups closed the scope questions. Read PROOF.md and verification/model_adjudication.md.

A precise proposed replacement is verification/approved_A5_replacement.md; it does not change the chosen observer convention.

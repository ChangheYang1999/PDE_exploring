# S11 follow-up attribution check

Written 2026-10-29 after the source-bound residual capture and resolved closure record, before the follow-up scalar calculations.

Reuse the exact-float cost analysis of V342 and the fixed two-term Taylor fit of V335. Do not refit at a step selected for a better result. Calculate the predicted crossing of the leading second-order term with the relative threshold and the registered absolute floor. Separate measured final cost/stencil rounding from the remainder that could include upstream evaluation error, omitted Taylor terms and derivative bias. The resolved closure comparison is a distinct consistency check.

For a quantitative bias bound use the inequality proved in PROOF.md. The qualitative assumption of specification3.0(b'') does not by itself supply an evaluation-error bound. Report missing hypotheses instead of assigning an unmeasured remainder wholly to rounding. No registered estimator, floor, step or decision changes.

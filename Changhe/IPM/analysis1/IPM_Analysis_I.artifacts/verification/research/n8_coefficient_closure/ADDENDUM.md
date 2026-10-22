# Source norm and acceptance-gate clarification

Topic77 PROOF.md section8 defines M_V=sup_{B_(3delta)(P)}||D^2 V||_F and M_rho=sup_{B_(3delta)(P)}||D^2 rho||_F, and proves C_V=(417/10)M_V+3M_rho. These are exactly the norms certified in topics84 and85; no equivalence constant is missing. The frozen topic77 verdict and the required canonical-sign correction in topic80 are explicit dependencies in the final scalar verdict.

The dependency checker identifies both prior verdicts by their exact already accepted hashes. The final scalar acceptance also asserts their status fields directly. Neither status labels nor a model response substitute for the whole independent numerical audits in those verdicts.

The scalar arithmetic is strict in the sense stated in PROOF.md. It closes the coefficient smallness condition only, and does not assert the remaining base-point, matrix, gradient, divergence, cutoff, domain, regularity, rank-one or global hypotheses. The original X3 profile and normalized modal_v2 are not silently identified.

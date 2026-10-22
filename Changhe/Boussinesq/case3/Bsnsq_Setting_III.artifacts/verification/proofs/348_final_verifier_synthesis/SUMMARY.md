# P348: final verifier synthesis

Recorded 2026-10-22T11:24:32.464377+00:00. Verdict **CONFIRMED** for the finite synthesis and exact identities in PROOF.md. General B2 remains **OPEN**. This is not another full-plane inverse run and not a complete YES programme.

The final independent checker passed **29740/29740** controls, running from 2026-10-22T11:20:22.938671Z to 11:20:23.075641Z (0.136976 s). It froze 15 inputs and re-reduced all 5904 rows of the 123-entry table. The 121 forced entries have self-velocity divided regional maxima in [0.693002737995303,1] for F and [0.4121134257571939,0.9937668129755434] for G. The six selected equal-budget rows are preserved in verification/selected_rows.json. These are finite sampled measurements, not continuum error bounds or exact rejection of every represented state.

The first run passed 29616/29740. All 124 failures came from my incorrect assumption that the CSV's last region label was 300-inf: one schema check and 123 key-set checks. Its actual label is 300-1e8. The original evaluator JSON selects the last band with a [300,infinity) mask, but the sample grid stops at radius 1e8. No numerical residual value failed. I preserved the first proof, source and output; the repaired label and scope passed. Later proof revisions made the kernel sign, zero-normalizer convention, physical reconstruction and observer transformation explicit. The last revision narrowed the forced-velocity interpretation. Earlier check outputs are retained.

The control source hash is 11c6781913d99d2d000023dd4c032a247e6afd5fa792aa245083184925ae6311. The checked proof hash is 75b1abbfca7462c6895eca977b643f6292f5045b56315f012b86d3098380f8ea. The source checks establish finite import properties, not historical authorship. Prior packets provide the actual independently implemented inverse computations and their precise coverage.

Actual Claude Opus 5.5 requests 610, 611 and 612 reviewed the mathematical identities and scope. Request 610 was truncated; follow-ups resolved its unsupported observer objection. I independently caught the plus-sign curl error in 611, and 612 confirmed the minus sign and closed the scoped review. The model did not execute the numerical checker or certify these numbers. See verification/model_adjudication.md.

Dependencies and limitations are stated in PROOF.md. Final report writing, archive readback and actual T_end remain future actions at this timestamp. The root FINAL_VERIFIER_SUMMARY.md is an interim reading guide, not a new theorem.

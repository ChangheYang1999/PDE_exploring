# Corrections to the main application review

Written 2026-10-22T11:43:39.277996+00:00, after the complete main actual response and after literal coefficient replay.

Main request fe48686a-07c4-486f-97a7-f8685fa40557 reported direct agreement of all 6264 density coefficients. The old executable compared hashes of the reconstructed coefficients and exact Q values. COEFFICIENT_COMPARISON_CORRECTION.md is mandatory for both the old preparation and this application. The new direct_coefficients.py source was recorded before execution. Its result now directly compares 6264 density, 6264 B and 6264 C exact rational coefficients and recomputes all three Q values by distinct square-integral methods. All passed at 2026-10-22T11:42:11.333340+00:00. The old acceptance history is retained, with this precise correction; it is not retroactively a literal comparison.

The main review also says the linkage check files are absent from review_request.json and not bound by auth. They are both present in the expanded request and actual metadata. The complete request was reconstructed against current file bytes by protocol.auth and its hash matched the actual metadata. The packet extension was saved before the actual request, without modifying the frozen mathematical source or numerical output. These files were created after the original source freeze, so they are supplemental checks rather than original frozen sources.

The denominator has 1970 core verdict pins; the separate external sha256sum check covered 2007 distinct paths, including supplementary files. These are distinct counts. Review authentication establishes local request, response and declared-model consistency, not a cryptographic provider signature.

The complete NONZERO_IMAGE.md is supplied for the follow-up; its result was already inherited. The quotient argument would remain valid by contradiction if the image were zero. None of this asserts invertibility.

research/scaling_selected_application/code/linkage_check.py: 25c7851b7c9851f941363ce8e6eb9d1d727f10f2a130137e313d9ff675287772

research/scaling_selected_application/evidence/linkage_check.json: 357c154e1dc5785d66f54fab3503a21b09a7ee4eb63c3c9a299c56fcb44c5cb4

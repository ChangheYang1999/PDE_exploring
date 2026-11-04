# Final report assumption-table consistency audit

## Statement and scope

The frozen assembly cdeab6615b7e16a52a98c808de2e3888bb5c1ff85f24e3bf3cda8ca57ec3308c has a scope defect in Section 3.1. Its table says it lists exactly what each theorem of Section 1 uses, but its Theorem 3 row omits the additional premises of parts (o) and (p), and its Theorem 8 row describes only (a)-(c) without saying that (d)-(p) are outside that row. The newly added Theorem AP has no row. The detailed theorem statements themselves retain their correct hypotheses. This is a report-consistency repair, not a refutation of any theorem and not a new mathematical direction.

## Complete comparison

In report lines 324-337, Theorem 3(o) explicitly assumes finite limsup G_a(R)/log R for its strict source surplus and angular bounds. Whether velocity decay gives this finiteness is explicitly open. In lines 339-344, Theorem 3(p) instead assumes that the logarithmic critical moment of the pointwise negative part of q has liminf zero; nonnegative spherical mean is expressly not a substitute. The table's Theorem 3 extra-hypothesis cell lists only U nonzero, part (i)'s annular vorticity bound and part (f)'s smoothness/nonzero-core-vorticity alternative. Thus its advertised list is incomplete. Finite gradient budget belongs to (o); the negative-source premise belongs to (p). These premises must not be interchanged.

The Theorem 8 row gives only the c ranges and extra assumptions of parts (a)-(c), even though the label names all of Theorem 8 and the derivative column says none. But part (m), lines 1018-1020, states a nonexistence criterion under DU=o(r^(-1/c)); its unconditional gradient lower bound is a different conclusion. Parts (n) and (p) explicitly retain finite logarithmic-gradient budgets for their respective quantitative conclusions. Part (p)'s stronger gap from vanishing negative source has that separate source premise. The report's own lines 1343-1345 correctly preserve these distinctions. The table should either label its existing row 8(a)-(c) and point separately to (d)-(p), or expand the row to include their stated premises. No assertion that every part requires every one of these premises is intended.

Theorem AP, lines 207-245, assumes pressure axisymmetry on a ball that absorbs every backward carrier orbit, in addition to C1 regularity, uniform sublinearity, 0<c<1/2 and the whole-space equation. The pressure symmetry is not derived from velocity decay. A separate row would make the table cover this theorem too. It would be equally accurate to qualify the table as a selected summary and explicitly direct readers to Theorem AP and 8(d)-(p), provided that the named Theorem 3 row itself is corrected.

## Required repair and approval consequences

Add the (o) and (p) assumptions to the Theorem 3 row. Clarify that the existing Theorem 8 row covers only (a)-(c), with an explicit account or cross-reference for the assumptions in (d)-(p). Add Theorem AP or qualify the promised coverage of the table. Preserve every hypothesis already in Section 1. No mathematical statement, proof or open question needs changing.

A3229 remains a correct status-and-notation comparison of the two pinned assemblies. This fresh check identifies a pre-existing table defect outside that small delta. Final approval of the assembled main report is pending this repair; it must not be represented as refutation of A3223-A3224 or of the smooth coverage/helicity-sign results. The original arbitrary-rotation conjecture remains open.

## Dependencies and evidence limits

The bounded source excerpts are retained in the team records. The exact relevant statements and table were read, then compared directly. The larger combined search display was truncated and is not counted as a complete reading. No numerical calculation, external theorem, formal build or new model call is a premise of this textual comparison. Existing configured model coordinator/A/C collaboration continues through working files; provider-side execution is independently unattested.

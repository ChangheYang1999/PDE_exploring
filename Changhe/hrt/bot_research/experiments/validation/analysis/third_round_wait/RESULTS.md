# Third-round waiting on H and S

Checked 2026-10-31T22:13:57.794346+00:00.

Audit completion: COMPLETE. H1 CONFIRMED; H2 CONFIRMED; H3 CONFIRMED; H4 CONFIRMED.

| Opponent | T seat | WDL | HP, T first | Rounds | Verified |
| --- | ---: | --- | --- | ---: | --- |
| H | 0 | W | [800, 656] | 50 | True |
| H | 1 | W | [800, 656] | 50 | True |
| S | 0 | D | [740, 740] | 50 | True |
| S | 1 | D | [740, 740] | 50 | True |

H1 requires nonnegative T WDL in all four new games. H2 requires the exact round-four opening, private-state and selection checks. H3 compares both T/S streams to the original G/S stream in the same physical G seat. H4 compares the complete two-seat histories for each opponent.

Ordinary fresh external decisions verified: 400. Additional successful entrypoint calls: {"actual_T": 200, "reference_G": 106, "reference_L4": 106}. Nested successful component/model calls: {"internal_G": 106, "internal_H_model": 106, "internal_L4": 106, "reference_H_model": 106}. Nested calls are subsets of those entrypoint calls and are not added to the ordinary external-call count. Two original G/S controls are reused with zero new control-policy calls.

The component audit records each attempted call before invocation, completed/failed calls immediately, and completed rounds in individual checkpoints. An interrupted call can remain pending. The existing ordinary fresh checker buffers detailed calls until completion; interrupted ordinary fresh runs retain child output and existing match artifacts but may lack detailed per-call receipts. This limitation does not apply retroactively to the separate durable component journal.

Forecasted H actions are compared with actual opponent actions only as a diagnostic. Full private-state agreement compares fresh references on the actual T observations, including the discarded L4 proposal in round three; it does not assert standalone L4 history transfer. Earlier selection branches in rounds two and three are source-reviewed and are not additionally exercised on other histories.

All four cases remain in the fixed grid. Failures, missing evidence, early termination, opening violations and first complete-history divergences are preserved in verification/full_games.json and referenced receipts. H1/H3/H4 use authenticated game histories; H2 additionally uses the first-four component audit. Overall audit completion also requires the complete component audit to pass. A counterexample and an audit failure are different findings.

Later planning deadlines and shared caches prevent unconditional cross-execution history equivalence. Logical-state snapshots omit module globals, clocks and alias identity. These four selected development games establish neither unrestricted dominance nor a complete finite matrix or global game value.

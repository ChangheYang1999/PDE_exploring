# Remaining coverage gap in the v2 finite-section assembler

## Claims under audit

The numerics note24 of2026-10-28 12:38Z says the repaired fsec_assemble.py uses disjoint block cell sets whose union equals the run's cells. The snapshot in this topic selects final parts in preference to retained checkpoints, so it repairs the concrete never-resumed S1 and S1M3 double-counting defect. Its general coverage statement is stronger than the implemented check.

For blocks carrying IDs, the program tests pairwise disjointness and equality between each block's ID count and its diagnostic count. It compares only the total number of IDs with an expected cardinality NEXP. A mismatch prints a warning and execution continues. It never compares the union with the expected set of IDs. Consequently both an incomplete cover and a wrong cover of the same cardinality can produce a result file.

## Exact counterexamples

Use a two-column fixture with positive definite input and image matrices equal to the identity, zero strain row, one worker and expected cell set{0,1}. Give its single final part either:

 1. done={1,2}, diagnostic cell count2;
 2. done={0}, diagnostic cell count1.

The first has the expected cardinality but omits cell0 and includes an unintended cell2. The second is incomplete. In each case the matrices are innocuous; the sole issue is coverage. The v2 checker accepts the first as two disjoint cells and continues after a warning for the second. It writes a generalized-singular-value result for both. A check of counts cannot distinguish the first cover from the correct one. The program must compare with an explicit expected ID set if it claims that equality of sets has been verified.

These fixtures execute only the immutable assembler snapshot, with output directories inside the verifier team. They do not start a worker, recompute a profile, change the numerics team or use a server.

## Required distinction and repair

Partial-domain matrices can be useful diagnostics when deliberately requested, but their output must remain explicitly partial. For a complete section or a complete-domain norm claim, the required condition is that every expected cell appears exactly once and no other cell appears. A strict comparison of disjoint unions with a recorded expected set enforces that condition. The expected set may be a custom cell list; it must be recorded when the run is created rather than inferred from its cardinality afterward.

Legacy parts without IDs need the additional assignment reconstruction used for the actual S1 and S1M3 audits. Their diagnostic counts alone cannot prove disjointness or their identity with a particular expected set. The old robustness script also still uses parts-only preference and omits base blocks in a completed resumed run; that separate proof 176 defect is not repaired by changing the default assembler.

## Scope

This does not invalidate the independently reconstructed complete coverage of the actual S1 or S1M3 final parts. It refutes the generic claim that the v2 implementation enforces union equality. The corrected selection of parts over checkpoints is confirmed for those actual never-resumed runs. Their numerical quadrature, division and conditioning limitations remain those of proof 183.

Dependencies: proof 176 for the original accounting issue; proof 183 for actual S1M3 coverage; immutable v2 assembler and note24 snapshots in evidence. Fixture outcomes are recorded in evidence/check.json.

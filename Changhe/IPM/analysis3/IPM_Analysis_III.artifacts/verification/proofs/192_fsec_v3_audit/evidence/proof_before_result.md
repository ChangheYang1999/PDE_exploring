# Expected-cell equality in the third finite-section assembler

## Claims and scope

The numerics team's note26, dated2026-10-28 13:00Z, reports two repairs after topics183 to185: the assembler now requires the union of recorded cell IDs to equal the expected set, and new runs use the exact integer angular input quotients. This topic checks those two claims on immutable source snapshots and finite fixtures. It does not certify the matrix entries, output division, numerical integration or the infinite-dimensional operator.

An accumulator block consists of two matrix sums G,B, a set D of processed cell IDs and a diagnostic cell count. If every ID in a fixed expected set E is processed exactly once, the sets D must be pairwise disjoint, each block's count must equal its set cardinality, and their union must be E. Assuming the block matrices are exactly the sums declared by their IDs, these checks suffice for correct accounting: finite addition is associative, and every cell contribution then occurs exactly once. They do not prove the accuracy of the contributions themselves or their mathematical provenance.

The required negative fixtures are: an equal-cardinality wrong ID set, a missing cell, an extra cell, overlapping blocks and a duplicated ID within one block. The correct set is the positive control. Explicitly partial output must be labelled partial and must require the documented environment switch. A legacy block without IDs can be accepted only through the documented deterministic assignment reconstruction and matching counts; that reconstruction is conditional on the recorded never-resumed launch history, as separately checked for the real S1/S1M3 runs.

## Source audit

The current assembler reads cells_expected from the run metadata or its sidecar. It selects final parts over retained checkpoints for the same worker and includes disjoint base blocks. It rejects intersections between block ID sets, rejects disagreement with the block count, rejects IDs outside the expected set and exits on missing IDs unless FSEC_PARTIAL=1 is explicitly supplied. Its output records the number of missing cells and the partial flag. Thus the old cardinality-only weakness of proof 184 is repaired for recorded ID sets.

For legacy final parts, the code reconstructs worker w's assignment as sorted(E)[w::nworkers], and checks the corresponding count. This is consistent with the actual full sorted launches audited in proof 183. It must not be reinterpreted as verification of arbitrary legacy data without their launch history. New runs write the explicit expected IDs and their own actual done arrays.

The new VM[m] array sets its first m entries to2(-1)^(m-1-j)(2m-2j-1) and every later entry to zero. Proof 185 proves exactly that quotient. The actual small integer coefficients used in the planned runs are exactly representable in binary64. The old pseudoinverse is still evaluated for comparison, but the stored VM uses the integer template. Output-image division remains a floating pseudoinverse and is not covered by this repair.

The already completed S1 and S1M3 runs, and the S1M4P run started before the repair, used the older input division. Repairing the current source does not retroactively change their stored input Gram matrices. The numerics team now states that explicitly and labels its accumulation sensitivity model as incomplete.

## Verification protocol

Copy the assembler and producer into this topic's evidence. Run only the copied assembler on two-dimensional identity-matrix fixtures, all under this team directory and with a single computation at a time. Record exits, logs and whether an output is written. The fixtures establish the visible accounting checks without loading the actual large IPM trial or running a worker. The current actual S1/S1M3 partition remains covered by topics176 and183. Numerical acceptance of this code repair requires every expected fixture outcome to pass.

Dependencies: topics176,183,184 for the real accounting history and previous exact counterexamples; proof 185 for the input quotient identity. Status is PENDING until the fixture record is written.

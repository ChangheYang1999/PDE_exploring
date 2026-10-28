# Finite-section checkpoint accounting

## Claim being tested

For a fixed finite basis, suppose radial cell i contributes positive semidefinite Gram matrices G_i and B_i for the input and image norms. A correct assembly is

 G = sum_i G_i, B = sum_i B_i,

with every required cell counted once. Generalized singular values are square roots of the eigenvalues of B x = lambda G x, when G is positive definite. This statement concerns the chosen discretization. Its quadrature and arithmetic must separately be certified before it represents the continuous operator.

The tested implementation is the snapshot of numerics team/work/fsec.py, fsec_assemble.py and s1_robust.py in evidence. These files were read only. Their worker writes a cumulative checkpoint for the cells completed by that worker, and later a final part containing all that worker's contributions. The checkpoint is retained after writing the final part.

## Duplicate counting in the default assembler

The assembler sums every part_*.npz, base_*.npz and ckpt_*.npz. In a completed run without a restart, a checkpoint is a strict prefix of its corresponding final part. Therefore the assembled matrices are

 G_bad = G + sum_(i in checkpoint prefixes) G_i,
 B_bad = B + sum_(i in checkpoint prefixes) B_i.

These matrices do not represent the intended cellwise quadrature. Positive semidefiniteness does not fix the error: numerator and denominator are changed in different proportions.

An exact one-dimensional counterexample has two cells with

 (G_1,B_1)=(1,1), (G_2,B_2)=(1,9).

The correct squared singular value is 10/2=5. A final part for both cells plus a retained checkpoint for cell 1 gives 11/3, not 5. Thus duplicate counting need not preserve even a single singular value.

The saved completed S1 directory exhibits precisely this overlap: four final parts account for 1569 cells and their four retained checkpoints account for 1502 cells from those same worker partitions. There are no base files. The worker dispatch assigns cell i to worker i modulo four in this run. The independent checker verifies each checkpoint's recorded cell set is a prefix-subset of that partition. The final-part diagnostics give all four partition cardinalities.

Consequently the default fsec_assemble output for that directory has an accounting error. This conclusion does not invalidate results recomputed from final parts alone, and makes no assertion about the size or direction of any particular singular-value change.

## Resume and partial-completion cases

The robustness script uses final parts alone whenever any part exists. For a completed run without a restart this avoids the preceding double count. In a resumed run, however, the final parts hold only the cells processed after the latest restart, while the earlier contributions are in base files. Dropping the bases then omits cells. In the two-cell example, retaining only the second cell gives squared singular value 9 rather than 5.

The resume code collects the done sets in checkpoint files, moves those contributions into a new base file, and excludes only that collected done set from the next work list. It does not include done sets already stored in older base files. On a second restart, cells represented only in an older base can be recomputed. For example, base A stores cell 1, a later checkpoint stores cell 2, and the second restart excludes only cell 2. It schedules cell 1 again, which duplicates base A if all bases and final parts are subsequently summed.

If some workers have completed and others have not, selecting all final parts and no checkpoints omits unfinished workers' valid prefixes. Selecting all parts and all checkpoints duplicates completed workers' prefixes. Hence the choice must be made per worker and generation, with explicit cell coverage, rather than by whether any part exists.

## Correct accounting invariant

Every accumulated file should identify its exact set of cells and its generation. Files chosen for an assembly must have pairwise disjoint cell sets, whose union is the required set. A final part supersedes that generation's checkpoint for the same worker. Earlier disjoint bases remain necessary after a restart. A restart must exclude the union of all already accepted cell sets, including bases and completed parts. If the current file format cannot establish these sets, the missing provenance must be reconstructed from the known worker schedule or the computation must be repeated under a corrected manifest.

For the completed S1 run in the snapshot, parts alone have the complete known partition and no bases exist. The independently reported robustness calculation used precisely this selection. It remains a floating calculation, with quadrature and rounding errors outside this accounting audit. The current S1M3 run had no base or final part at the initial inspection, so the same parts-only rule applies if it completes without a restart.

## Evidence and verdict

The snapshot records real UTC time, file hashes, per-file cell counts and diagnostic traces. The checker uses exact rational arithmetic for the counterexamples and directly reads the recorded checkpoint cell sets for the actual run. Trace values are floating diagnostics, not certified norm values.

The claim that the default assembler counts each required cell exactly once is REFUTED. Its completed, never-resumed parts-only counterpart has CONFIRMED cell coverage. The correctness of an infinite-dimensional inverse, complement estimate, off-basis bound or nonlinear smallness test does not follow from either assembly.

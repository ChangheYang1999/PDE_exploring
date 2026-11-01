# Accuracy of the floating high-order tuning responses

Status: CONFIRMED for the finite assertions below (V541). No all-order growth theorem is claimed.

## Exact quantities and question

Fix Q in {7,8}, the exact algebraic root b_i of253 or256, and an integer k>=2. The response sigma_k is the coefficient of the free harmonic at order kQ in the next forbidden density coefficient. The affine-response proof130 shows that sigma_k depends only on f_1 through f_Q and g_1 through g_(Q-1). Therefore it can be evaluated without the long high-order continuation used by the floating program.

For each saved floating tuning row, evaluate this response independently with directed768-bit arithmetic at both b_i and the exact binary64 coefficient used by the producer. The second value separates the discrepancy caused by initial-root rounding from the discrepancy arising during floating arithmetic. This comparison does not certify any later density coefficient.

## Complete finite method

Refine each exact algebraic root within its certified isolating interval. Independently reconstruct the low prefix and Q-step linear response. For k>=2Q+1 use the compact identity149 at t=1/(2k-2), and compare full and compact evaluations at the first available tail index and last printed index. Before that threshold use the full formula. Check overlap with the already independently replayed prefix responses wherever both exist.

The producer first parses its displayed third-harmonic coefficient into binary64, including in long-double mode. Convert that binary64 number to its exact dyadic rational and repeat the low-prefix response calculation there. The displayed response is normalized to unit leading amplitude. Compute its relative discrepancy from the exact-root response and from the binary-input response, and the relative effect of changing the exact root to that binary input. Every reference response must be separated from zero before division.

Preserve the exact producer snapshots, directed values and all code hashes. A large discrepancy refutes high relative accuracy of that saved response. A small discrepancy at finitely many indices does not imply the accuracy of the full high-order coefficient array or the existence of a limiting growth constant. The source file's completion flag and observed index range define the scope.

Dependencies:130,149,253,256,261. The exact-root response formula and compact identity have already been proved and independently replayed.

## Completed verification

The 24 frozen outputs contain 915 responses. All are separated from zero in both directed reference calculations. Every relative discrepancy from the exact algebraic-root value is strictly less than 6.1e-12, and the effect of rounding the root to the producer's binary64 input is strictly less than 1.34e-12. A separate collection pass reconstructs these strict inequalities from the retained directed enclosures. There are 168 overlaps with the independently replayed prefixes and 96 full/compact cross-checks. The arithmetic took 250.47073 seconds. RESPONSE_TABLE.md records each file's finite range and completion flag.

The largest exact-root discrepancies occur in the third-root outputs: about 6.06479e-12 at Q7 in binary64 and 3.90813e-12 at Q8. Their extended-precision counterparts have maxima about 4.81169e-13 and 9.87707e-13. The Q8 root-rounding effect reaches 1.33237e-12. The producer prints thirteen significant digits for each response; differences at that scale do not measure the full internal arithmetic error. These finite observations give no error bound on the later high-order density or stream norms.

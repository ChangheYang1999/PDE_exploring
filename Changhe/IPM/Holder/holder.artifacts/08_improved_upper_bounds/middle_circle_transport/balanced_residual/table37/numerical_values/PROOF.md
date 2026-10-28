# Further certified middle-arc residual bounds

## Statement

Let C_alpha be the norm of T_xx on the real homogeneous Euclidean Holder seminorm, initially on smooth compactly supported functions on R^2. Use the kernels, circular principal values and homogeneous extension modulo constants of 01_setup/PROOF.md. By the rotation identity these bounds also hold for T_xy. The following exact decimals are upper bounds:

| alpha | C_alpha upper |
|---|---:|
| 1/1000 | 637.0404694256 |
| 1/100 | 64.0882119580 |
| 1/20 | 13.1840592665 |
| 1/10 | 6.8514311158 |
| 1/5 | 3.7431835793 |
| 99/100 | 42.2180350354 |

The first value is weaker than the accepted small-alpha bound and is not selected in the best-bound table. None of these numbers is claimed to be an exact operator norm.

## Proof

Apply the finite residual replacement proved in ../PROOF.md to the accepted V131 direct certificates after their V161 local radial refinement. The upper-half middle arc has diameter 2sin^2(t), while its antipodal displacement is 2sin(t). With residual variation bounded by tau and absolute signed residual mass bounded by h<=tau, the two-half residual costs at most (tau-h)(2sin^2(t))^alpha+h(2sin(t))^alpha. Each original radial bin is divided into eight intervals, on which h is bounded by the exact signed-mass formula and both distances by their right-endpoint values.

The source extraction uses 512 radial bins, 512 angular cells per half, 17 phases and integer mass unit2^44 at160-bit precision. Its bin_data syntax tree and complete cell-measure helper file are identical to the independently replayed V168 extraction. Plan selection changes with alpha, but neither the extracted masses nor their residual variation changes. The independent audit checks this equivalence, all source hashes and exact row coverage, and compares every old residual interval against the recomputed interval.

At each phase the new residual upper endpoint replaces a lower endpoint of the same residual in the V161 phase bound. Any nonpositive gain is discarded. The phase maximum, factor sec(pi/64), and unchanged small-disk term give the claimed complete operator bounds. The second acceptance program checks the entire input chain, resums all 512 rows with exact rational arithmetic, verifies every phase gain and maximum, and re-evaluates the final formula at384 bits. The displayed decimals are rounded upward. The accepted numerical evidence is in ../verification/accepted.json.

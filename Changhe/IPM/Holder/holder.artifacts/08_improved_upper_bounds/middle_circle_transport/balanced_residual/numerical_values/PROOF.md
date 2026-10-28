# Certified middle-arc residual refinement

## Statement

For real-valued smooth compactly supported functions on R^2, with Euclidean homogeneous Holder seminorm [f]_a, let C_a be the norm of T_xx (equally T_xy) and D_a the norm of R_1^2=T_xx-I/2. The kernels, circular principal values and extension to homogeneous Holder functions modulo constants are those of 01_setup/PROOF.md. The following are upper bounds, with all decimals exact:

| a | C_a upper | D_a upper |
|---|---:|---:|
| 3/10 | 2.7729133174 | 3.2175043762 |
| 1/2 | 2.1934924293 | 2.6460060556 |
| 3/4 | 2.6387739538 | 3.0984107266 |
| 9/10 | 5.0071216363 | 5.4698599222 |

They also hold on the homogeneous spaces modulo constants. No claim of exact optimality is made.

## Proof and certificate contract

The parent PROOF.md bounds the residual signed measure on each middle arc and its negative central reflection. Its exact signed-mass formula was independently cross-read in 05_team_audit/lead_note36/NOTE.md. The earlier extracted transport plans remain admissible because the original 160-bit mass rule, 512 angular cells per half-circle, 512 radial rows, 17 phases and integer mass unit 2^44 are replayed unchanged. Eight equal subintervals per radial row are used only to bound the new residual cost. Every completed row records the extracted integer masses, original residual interval, new upper endpoint and all source hashes.

The replay in code/replay_middle_balanced_residuals.py and the exact recombination in code/combine_middle_balanced_residuals.py verify complete row coverage. For each phase and exponent, the summed original residual enclosure intersects the accepted original residual enclosure. The sharper upper bound replaces a lower endpoint of that original residual in the earlier total upper bound. More precisely, if U is a previously accepted phase upper bound, L a lower bound for its old residual cost, and H an upper bound for its replacement, then U-max(0,L-H) is valid. This uses the same residual term in the two expressions, rather than subtracting an upper endpoint.

Both the original C and D certificates use data/middle_circle_certificate_n512.json. The C certificate first incorporates the accepted radial local-disk improvement V161; the D certificate retains its accepted near-pole term. The local, middle and exterior region partition is unchanged. Taking the maximum over the 17 phases and multiplying by sec(pi/64) uses the accepted phase interpolation inequality. The phase-independent small-disk or near-pole term is then added. Exact rational endpoint comparisons round the resulting upper endpoint upward to the displayed decimal.

The independent acceptance file ../verification/accepted.json binds this proof, the analytic proof, the frozen cross-read, all 512 row files, the original inputs, the prior acceptance chain and both programs. The selected worst phases are respectively (14,11), (12,11), (11,11), (11,11) for (C,D). These are complete operator upper bounds conditional only on the already accepted parent certificates, whose hashes are retained in the acceptance chain.

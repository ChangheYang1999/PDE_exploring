# Effective pool-C diversity

Checked 2026-10-31T16:28:51.033096+00:00.

CONFIRMED for the recorded games: each candidate has 33 distinct complete normalized trajectories across its 72 nominal games. There are 36 opponent/start pairs, but three pairs duplicate another pair within the same start. The predeclared W/D/L totals remain unchanged.

| Candidate | Start | Nominal games | Distinct complete trajectories |
|---|---|---:|---:|
| best-v9e | standard | 24 | 12 |
| best-v9e | mirror_7493_3 | 24 | 11 |
| best-v9e | asym_8669_2 | 24 | 10 |
| p5tnubm | standard | 24 | 12 |
| p5tnubm | mirror_7493_3 | 24 | 11 |
| p5tnubm | asym_8669_2 | 24 | 10 |

Duplicate groups beyond the ordinary two-seat controls:

- best-v9e, mirror_7493_3: `mirror_7493_3-10-side0`, `mirror_7493_3-10-side1`, `mirror_7493_3-11-side0`, `mirror_7493_3-11-side1`.
- best-v9e, asym_8669_2: `asym_8669_2-08-side0`, `asym_8669_2-08-side1`, `asym_8669_2-09-side0`, `asym_8669_2-09-side1`.
- best-v9e, asym_8669_2: `asym_8669_2-10-side0`, `asym_8669_2-10-side1`, `asym_8669_2-11-side0`, `asym_8669_2-11-side1`.
- p5tnubm, mirror_7493_3: `mirror_7493_3-10-side0`, `mirror_7493_3-10-side1`, `mirror_7493_3-11-side0`, `mirror_7493_3-11-side1`.
- p5tnubm, asym_8669_2: `asym_8669_2-08-side0`, `asym_8669_2-08-side1`, `asym_8669_2-09-side0`, `asym_8669_2-09-side1`.
- p5tnubm, asym_8669_2: `asym_8669_2-10-side0`, `asym_8669_2-10-side1`, `asym_8669_2-11-side0`, `asym_8669_2-11-side1`.

The guard variants are C-10 and C-11 (zero-based job indices 10 and 11). Their only differing actions occur at round one, which both continuation starts replace with scripted actions while skipping the policies. Both then call the same fresh economy17 delegate. The proof states the precise conditional policy equivalence. C-08 and C-09 are different budget-timing settings; their equality on the asymmetric start is an observed full-history equality, not a claim that their policies always agree.

Between the two declared candidates, the counts of equal matched complete histories are asym_8669_2: 24/24; mirror_7493_3: 24/24; standard: 6/24. Across all 144 logs there are 42 distinct normalized histories. In particular, the two continuation sets do not provide independent evidence for each candidate: both candidates use the same economy20 foreign-map delegate and every matched continuation history agrees.

The checker rereads every complete replay, verifies the raw bytes against the strict audit and result, independently implements the declared normalization, and checks its digest against the earlier audit. It also compares the normalized JSON objects within hash groups. Match IDs, player names, physical seat labels and the global action-order metadata are removed; actions, their within-player order, events, states, round numbers and results remain.

These are equality classes of observed trajectories, not independent statistical observations. No historical behavioral-novelty claim follows from the exact parameter-separation audit. The eight unresolved historical rows in the separation audit remain unresolved. Reproduce with `python -B -m bot_research.experiments.validation.audit_effective_pool_c` under the documented local environment and assigned affinity, using a fresh output location if the receipt already exists.

# First-leak defense witnesses

Checked 2026-10-31T19:37:15.060867+00:00.

Existential defense claim: CONFIRMED.

| Selected attack | Round | Available gold | Original damage | Planner | Legal | Construction cost | Alternative damage | Seconds |
|---|---:|---:|---:|---|---|---:|---:|---:|
| r3_tier2 | 7 | 1045 | 280 | free30 | True | 880 | 0 | 0.207356 |
| r3_tier2 | 7 | 1045 | 280 | fortress38 | True | 970 | 0 | 0.639830 |
| r3_tier3 | 7 | 1240 | 280 | free30 | True | 880 | 0 | 0.151565 |
| r3_tier3 | 7 | 1240 | 280 | fortress38 | True | 1004 | 0 | 0.337000 |
| r4_tier3 | 7 | 965 | 280 | free30 | True | 880 | 0 | 0.152274 |
| r4_tier3 | 7 | 965 | 280 | fortress38 | True | 964 | 0 | 0.300863 |

Every original prefix and selected round reproduces exactly in the unchanged Engine. Every recorded private H prediction matches the actual opponent action list, and its positive residual-damage prediction equals the original received damage. The table tests the construction projection of each proposal from the same public state. All full proposals, action acceptance records, observations and alternative round records are retained.

A zero-damage row is a legal one-round feasibility witness, not a winning complete policy. If no row succeeds for a state, the existential claim remains open because these searches are not exhaustive. No new full strength game was run. The original wall-signal losses and delayed-grid results are unchanged. These selected failure states do not estimate an average repair rate or a general advantage of one planner.

Reproduce with python -B -m bot_research.experiments.validation.check_wall_signal_defense after restoring the pinned sources and original replays. The exclusive result paths must first be archived or a separate reproduction directory used.

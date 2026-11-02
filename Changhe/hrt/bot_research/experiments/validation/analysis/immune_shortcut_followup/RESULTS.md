# Boundary checks and shortcut-only timing

Completed 2026-10-31T21:03:09.538723+00:00.

H1 **CONFIRMED**: all74 input streams have exactly2(r+1) ordered records, no earlier terminal result and identical non-null final results agreeing with their summaries. Together with protocol151's initial and per-round Engine checks, this closes its complete-stream claim.

H2 **CONFIRMED**: all100 shortcut-only calls match the retained actions, with legal actions, unchanged observations and two complete original-engine replays. There were0 parent policy calls and0 external eligibility preflights.

H3 **CONFIRMED**: maximum shortcut process CPU 0.207627s (seat0, round8); maximum wall time 0.207646s. Each50-call history used a fresh process, with caches naturally warming across rounds.

Protocol150's separate parent measurements reached 6.716633s CPU and 6.770995s wall. These were measured at a different time, so the comparison is descriptive. The151 paired measurements additionally included an untimed eligibility preflight before both calls; they are not cold-call benchmarks.

H4 **CONFIRMED**: the unprofiled seat0 round50 _worst_leak returned 0 in 6.347995s CPU and 6.363192s wall. Its sampled rosters contain 1372720 type slots; construction was outside this timed interval.

The separate profiler call returned 0 and took 22.952603s CPU. Profiler overhead is included in the following function times and must not be added to or substituted for the unprofiled measurement.

| Function | Calls | Own profiled s | Cumulative profiled s |
| --- | ---: | ---: | ---: |
| bot_research/experiments/lead/frozen/best_v9e.py:188 _worst_leak | 1 | 0.000013 | 22.989980 |
| ~:0 <built-in method builtins.max> | 16225 | 0.003863 | 22.989945 |
| bot_research/experiments/lead/frozen/best_v9e.py:192 <genexpr> | 9 | 0.007744 | 22.989927 |
| bot_research/harness/gamekit.py:128 simulate_defense | 8 | 14.880716 | 22.982183 |
| ~:0 <method 'append' of 'list' objects> | 49475369 | 8.067585 | 8.067585 |
| ~:0 <method 'get' of 'dict' objects> | 91882 | 0.017700 | 0.017700 |
| bot_research/harness/gamekit.py:73 splash_profile | 8 | 0.000622 | 0.013557 |
| ~:0 <built-in method builtins.sum> | 624 | 0.000348 | 0.012802 |
| bot_research/harness/gamekit.py:83 <genexpr> | 1864 | 0.005680 | 0.012454 |
| ~:0 <built-in method builtins.abs> | 32448 | 0.002929 | 0.002929 |
| ~:0 <built-in method builtins.len> | 6080 | 0.001716 | 0.001716 |
| bot_research/harness/gamekit.py:91 gun_coverage | 8 | 0.000984 | 0.001054 |

No new strength games, no final-candidate change and no terminal-pool use. Native transition equivalence retains the exact hypotheses of protocol151; foreign histories remain empirical checks. Neither runtime measurement is a portable upper bound. PROOF.md gives the complete argument and method.

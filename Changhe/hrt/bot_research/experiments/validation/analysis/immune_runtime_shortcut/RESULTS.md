# Immune shortcut: finite action and state check

Completed 2026-10-31T21:00:49.482299+00:00.

H1 **CONFIRMED**: 74/74 retained histories completed; 0 differences and 0 failed attempts. There were 1204 fresh calls per implementation (2408 total), with 120 prescribed prefix turns skipped per implementation.

H2 **CONFIRMED**: 364 calls used the shortcut. 508 calls per implementation entered the unchanged foreign path.

H3 **CONFIRMED**: both high-factory histories completed and the shortcut maximum process CPU time was below3 seconds.

| Implementation | High-factory max wall s | High-factory max CPU s | All-call wall total s | All-call CPU total s |
| --- | ---: | ---: | ---: | ---: |
| Unchanged parent | 6.700285 | 6.583384 | 319.855188 | 315.039874 |
| Research shortcut | 0.299015 | 0.298869 | 95.009256 | 93.626205 |

Every completed case replays the complete retained history through the original Engine. Fresh actions are checked against each other and the recorded candidate actions, with legal application and no observation mutation. Persistent instance fields and foreign function closure values are compared after each actual call.

These are existing development histories, not new strength games. The implementations share module caches within each per-history process; call order alternates by round. Measured times describe these executions and are not portable bounds. The native transition proof is in PROOF.md; foreign-history agreement is empirical because the unchanged fallback has a finite clock cutoff.

The installed best_v9e and reserved terminal validation remain unchanged. This worker-owned research variant is a possible performance improvement, not a newly validated final candidate.

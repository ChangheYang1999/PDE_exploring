# Exact wall-cost verification results

Completed 2026-10-31T20:23:15.081477+00:00. H1: **CONFIRMED**. Minimum wall cost: **5**.

The complete scan contains 14901218 distinct wall sets of cardinality0 through4. Strict ordering, disjoint shard membership and binomial counts check coverage. The independent audit checked 11097 routes through original Python shortest_path, and six maximum/five-wall witnesses through the unchanged Engine. No policy calls or strength games were run.

| Wall count | Sets | Invalid paths | Maximum splash damage per copy |
| --- | --- | --- | --- |
| 0 | 1 | 0 | 100 |
| 1 | 138 | 3 | 100 |
| 2 | 9453 | 410 | 100 |
| 3 | 428536 | 27813 | 100 |
| 4 | 14463090 | 1248613 | 150 |

The existing five-wall witness gives190 splash damage per copy and800:774 round6HP. The smallest feasible count under the exact stated restrictions is 5. See PROOF.md for the reduction, source correspondence argument and scope. This is a finite computational verification, with no proof-assistant or verified-compiler claim. Every wall-set score is retained in the compact binary records and decoded by the independent checker.

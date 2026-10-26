# g3_bench_policy.json

Created 2026-10-24T13:21Z on the lead's ruling (c4-lead NOTES 13:19Z item 4). Identical to outputs/g2_policy_v3.json except
max_seconds 10800 -> 36000. Reason: bench860 requires exactly N_ASSESS = 3 full assessments of the seed in one step JSON
(configurations G3_BENCH_WORKERS="4 8 12", pairs (4,4), (8,4), (12,4)), so the bench cannot be split across guard runs; the
10 h value is a guard safety ceiling for the single bench run, not a target. Every other limit is unchanged (family RSS 160 GiB,
PSI 60, min_available 16 GiB and 10%, disk 10 GiB, swap, pageout, load). g2_policy_v3.json (manifest-independent but used by
T4) is not edited. The guard rejects unknown keys, so this note lives beside the policy file.

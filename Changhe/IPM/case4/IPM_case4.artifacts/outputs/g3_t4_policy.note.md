# g3_t4_policy.json

Created 2026-10-24T13:25Z on the lead's advance ruling (message 13:2xZ, reply to the numerics 3 h caveat). Identical to outputs/g2_policy_v3.json
except max_seconds 10800 -> 28800 (8 h guard safety ceiling for one T4 run, not a target). Use: ONLY if the guard stops the running T4
(run 20261024T125001Z, session s1, policy v3) on exactly 'per-run wall-time budget exhausted' and nothing else; then the same step is rerun on the
same g3_v1 bytes in a NEW session s3 under this policy, nice 15, with no code change, and the stopped run is recorded as a budget stop (no T4 verdict
from it; not a scientific FAIL). Any other failure: no rerun, report to the lead. Every other limit is unchanged. The guard rejects unknown keys, so this
note lives beside the policy file.

# G3 ledger completeness (generated 2026-10-25T03:59Z)

Ledger status/ledger.jsonl: 1503 records; kinds: correction 1, job_done 135, job_end 207, job_error 23, job_failed 5, job_retry 27, launch 214, note 6, reevaluation 67, resume 59, start_result 759

start_result rows: 759 (405 before 2026-10-24T19:39Z, 354 after).

| period | field | rows missing | note | examples |
|---|---|---|---|---|
| before 19:39Z | holdout present but half-offset family missing (pre-7.3a row; reevaluate_holdout.py fills it) | 41 |  |  |
| before 19:39Z | missing holdout vector and no failure reason | 364 | missing (pre-19:39Z, field did not exist in the ledger schema; marked explicitly, not blank) | pilot_L6/0, s1a_L6_cl0.41_om+3.0/0, s1a_L6_cl0.41_om-3.0/0 |
| before 19:39Z | missing rng_seed | 405 | missing (pre-19:39Z, field did not exist in the ledger schema; marked explicitly, not blank) | pilot_L6/0, s1a_L6_cl0.41_om+3.0/0, s1a_L6_cl0.41_om-3.0/0 |
| before 19:39Z | missing solver_version | 391 | missing (pre-19:39Z, field did not exist in the ledger schema; marked explicitly, not blank) | pilot_L6/0, s1a_L6_cl0.41_om+3.0/0, s1a_L6_cl0.41_om-3.0/0 |
| after 19:39Z | holdout present but half-offset family missing (pre-7.3a row; reevaluate_holdout.py fills it) | 129 |  |  |
| after 19:39Z | missing holdout vector and no failure reason | 1 |  | wtest_free/0 |
| after 19:39Z | missing rng_seed | 20 |  | s1c_vortnlw_L6_cl0.49_om+1.0/2, s1c_vortnlw_L6_cl0.47_om+3.0/5, s1c_vortnlw_L6_cl0.41_om+10.0/4 |
| after 19:39Z | missing solver_version | 4 |  | s1c_vortnlw_L6_cl0.47_om+3.0/5, s1c_vortnlw_L6_cl0.41_om+10.0/4, s1c_vortnlw_L6_cl0.47_om+10.0/5 |

Rules: every start_result after 19:39Z carries rng_seed and solver_version (worker.py); a start without holdout diagnostics carries a 'failure' string
(collapse, gauge defect, NaN) with no ratios and no tier; disposable test jobs (smoke_*, resume_test) are excluded from leaderboards by name.
Pre-19:39Z rows belong to the s1a/s1b sweeps (weak axisymmetric collapse states and the first reweighted momentum starts); they are kept for the record.
Post-19:39Z rows missing rng_seed/solver_version come from worker processes launched before 19:39Z (s1c jobs; the worker code is loaded at launch) and from
the disposable job wtest_free; they are marked here explicitly. Half-offset-family columns are filled for shortlisted states by reevaluate_holdout.py (ledger kind 'reevaluation').

# NEXT_STEPS

Final state at the end of the run (2026-10-23 08:24 UTC): training stopped gracefully at 07:47 UTC; the
campaign ledger (64 records) is closed; the 96-hour active minimum was NOT met (credited non-overlapping training
union 0.999 to 1.180 h). The primary class 0.4 < c_l < 0.5 is excluded for exact decaying C^2 profiles by Theorem L2
(THEORY_NOTES.md section 7), so the continuation below addresses only the open secondary questions. Before
resuming, set the GPU indices in runner_config.json to devices that exist on the new machine. The section that
follows is the numerics plan as written when training stopped.

## Numerics plan (numerics), updated 2026-10-23T08:10Z

Campaign state: STOPPED on the lead's instruction of 2026-10-23 07:38Z (PROMPT section 13: a rigorous obstruction covering the
whole explicitly specified primary search class, Theorem L2 of the lead's THEORY_NOTES.md, independently proved by the verifier
and audited by referees, supersedes further blind numerical work). All queue entries were kept; every worker checkpointed and
exited. Measured active numerical time: see STATE.json (credited elapsed intervals, far below 96 h).

Queue state: the primary-interval entries (c_l = 0.41 ... 0.49, 25 files: 10 stopped with checkpoints, 15 never started) were moved to
queue/archived_primary/ at 2026-10-23T08:10Z so that a resume runs only the secondary questions; queue/stopped holds v1_M1_cl050, v2_M1_cl050
(checkpoints), queue/pending holds v2_M3_cl050, v2_Z0_cl050, v2b_BL_cl050. To re-add an archived entry: mv it to queue/pending.
Entry point to restore work after any interruption (resumes every entry in queue/stopped and queue/pending from its last atomic checkpoint):
    bin/resume.sh        (run from the root of this artifacts folder)
Status: bin/status.sh ; bin/watch.sh ; python3 ledger.py --state ; graceful stop: bin/stop.sh

Continuation queue for the OPEN secondary questions (not the primary target, which L2 excludes), in priority order,
to be used only if the team reopens numerical work:
1. c_l = 1/2 calibration (not excluded by L2): finish v2_M1_cl050 (stage 1 and 2 Adam, then the L-BFGS stage), then the
   refinement series `python3 make_configs.py refine v2_M1_cl050 0.5 r1` (warm start, 2x points, R_max 3e4, L-BFGS 600)
   and a fresh n_tail = 3 run (adds potential degree 3d-1, pressure 4d-2; see notes/TAIL_EXPANSION.md). Compare n_tail 2 vs 3.
2. c_l > 1/2 (outside the prompt's primary interval, not excluded): edit configs with cl in {0.55, 0.6} (envelope degrees follow
   d = 1 - 1/c_l automatically; T_lambda schedule unchanged).
3. Other seed families at c_l = 1/2: v2_Z0_cl050 (zero axis vorticity seed), v2_M3_cl050, v2b_BL_cl050 (off-axis Q-paired blobs).
4. Free-exponent refit as a diagnostic only (`python3 make_configs.py clfree v2_M1_cl050`, bounds [0.40, 0.50] or wider): L2 says
   nothing about optimizer behavior on approximate states; a drift of c_l is not evidence about existence.
5. L-BFGS stage and refinement series for any branch kept; report the residual floor versus width, points and R_max.
6. Negative-result archive: the held v1 runs and the stopped v2 runs at c_l < 1/2 remain as records of what the approximate
   optimization does in the excluded class (eps_m rising while absolute residuals fall, vorticity concentrating off-axis).
Every c_l above is a fixed input unless the run id contains 'clfree'; trainer holdout metrics are internal diagnostics, not
evidence; independent evaluation is in verification/CHECKPOINT_TABLE.tsv.

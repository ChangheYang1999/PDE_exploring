# RUNBOOK (all commands from this directory; python = .venv/bin/python)

## Tests (SPEC 7.9 T01-T12 coverage noted in NUMERICAL_METHODS.md)
    .venv/bin/python tests/test_solid_harmonics.py
    .venv/bin/python tests/test_residuals.py            # curl identity, exact spiral tail + sign flips, dilation, rotation, two-fold
    .venv/bin/python tests/test_pressure.py             # Green solver, m = 0 manufactured
    .venv/bin/python tests/test_pressure_twisted.py     # twisted manufactured sources, grad P(0)
    .venv/bin/python tests/test_lm.py                   # AD Jacobian vs FD (4 step sizes, c_l and omega), LM recovery
    .venv/bin/python tests/test_channels.py             # SPEC 4.4 radial channels
    .venv/bin/python tests/test_spec_T06_T07.py         # reflection omega -> -omega, random tails
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python tests/test_pressure_ray.py    # independent ray-integral pressure cross-check (GPU)
    .venv/bin/python tests/test_fields.py even          # whole-field sympy comparison (6 min)

## Benchmark one GPU
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/benchmark.py cuda:0   -> status/benchmark.json

## Pilot (one job, directly, no supervisor)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/worker.py runs/pilot_L6/job.json runs/pilot_L6

## Campaign
    scripts/start_supervisor.sh                 # detached supervisor (setsid nohup); config configs/supervisor.json
    .venv/bin/python scripts/enqueue_stage1.py --tag <tag> --L 6 --Nk 16 --formulation mom --nlw [--efrac 0.5] [--free] [--channels 6,6,6] [--m_parity all]
    .venv/bin/python scripts/status.py [N]      # status + leaderboard (top N)
    .venv/bin/python scripts/leaderboard.py     # reports/PARAMETER_SWEEP.csv, reports/CANDIDATE_LEADERBOARD.csv
    .venv/bin/python scripts/daily_report.py    # reports/DAILY_REPORT_<date>.md
    scripts/stop_supervisor.sh                  # workers checkpoint and exit; jobs stay queued

## Recovery (single command): restart the supervisor; orphaned running jobs go back to pending and resume from checkpoint.pt
    scripts/start_supervisor.sh

## Interruption test (disposable job, kill -9 then resume; SPEC T11)
    scripts/resume_test.sh 5                    # GPU index argument; result in logs/resume_test.log, status/RESUME_TEST.md

## Validate a saved start without retraining (training grid, 1.5x refined grid, holdout points; --full adds holdout SPEC diagnostics, critical points, strength, X5, orbit averages)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/validate_candidate.py runs/<job>/starts/start_000.pt --json out.json

## Export a state in the SPEC 10 exchange format (for the verifier)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/export_candidate.py runs/<job>/starts/start_000.pt <candidate_id>

## Supervisor restarts (jobs resume from SIGTERM checkpoints)
    scripts/restart_supervisor.sh                 # plain stop + start (new supervisor code; jobs keep their in-progress starts)
    scripts/restart_supervisor_fixflags.sh        # stop, normalize pending job flags (exclusive for L>=10, retries, Sigma_Z ramp), start
    scripts/restart_supervisor_fresh_starts.sh    # stop, drop in-progress starts (fresh seeds with new code), start

## Continuation / refinement of a saved state (exact embedding into a larger basis)
    .venv/bin/python scripts/enqueue_continuation.py --src runs/<job>/starts/start_000.pt --tag c2x2 --L 10 --Nk 24 --sigmaZ 1 --channels 6,6,6 [--free]
    .venv/bin/python scripts/resolution_table.py  # reports/RESOLUTION_LADDER.md (best holdout rho_u per L, fixed/free, solver version)

## Re-evaluate saved states with the current diagnostics code (both shell families, single spheres, rho_lin/rho_sp; writes 'reevaluation' ledger rows)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/reevaluate_holdout.py --device cuda:0 [--top 10] [start files]

## Channel angular degrees (SPEC 4.4 closure) and the G[F] closure report
    .venv/bin/python scripts/enqueue_continuation.py --src <start.pt> --tag d6w --L 6 --Nk 16 --channels 4,4,4 --chdeg 15,14,6 --nl_den all5far --priority 13 [--R1 3.33] [--free]
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/g_closure.py <start.pt>          # ||G[F]||, dist(G[F], carried span)/||G[F]|| (own, degree-L, SPEC-degree spans)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/bench_extended.py 6 16 15 14 4     # memory and Jacobian time of an extended model (L Nk LB LD NkB)

## Transfer fits of the verifier's exports (N1/R3) and their fit spectrum
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/eval_transfer.py <export_dir> transfer_eval/<name>.json --device cuda:0 --levels 6:16:48,8:20:60 --tail_constraints --source_rho_u <value>
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/fit_spectrum.py <export_dir> 6 16 48 [--no-tc]

## Nested ladder (lead 23:06Z item 2): promote the best starts of a cheap sweep to the next level
    .venv/bin/python scripts/promote_nest.py --tag nest2 --to_tag nest4 --L 4 --Nk 12 --n_promote 5 [--dry]

## Parameter scan / odd-m / split-weighting arms from a saved state
    .venv/bin/python scripts/enqueue_continuation.py --src <start.pt> --tag d6scan --L 6 --Nk 16 --nl_den all5 --c_l 0.47
    .venv/bin/python scripts/enqueue_continuation.py --src <start.pt> --tag d6odd --L 6 --Nk 16 --nl_den all5 --m_parity all --perturb_m 1 --perturb_m_rel 0.01 --suffix _m1e-2
    .venv/bin/python scripts/enqueue_continuation.py --src <start.pt> --tag d6split --L 6 --Nk 16 --channels 4,4,4 --nl_den split

## Where things are
    logs/supervisor.log, runs/<job>/worker.log, status/heartbeat_<job>.json, status/STATUS.json, status/ledger.jsonl

## Far-field coefficients (SPEC v1.24 7.8; shift 4)
    CUDA_VISIBLE_DEVICES=4 .venv/bin/python scripts/far_coefficients.py --device cuda:0 [--only <export id>]   # K_E / K_H ratios, vector defect split for every export
    # writes candidates/<id>/meta_supplement_v124.json (meta.json and SHA256.json stay as exported) and reports/FAR_COEFFICIENTS.md (built from every supplement);
    # L >= 8 exports are evaluated on the CPU automatically. tests/test_far_helicity.py checks the identity closure, the two carried forms and the verifier's rows.
## Stage II arm flags of enqueue_continuation.py (all registered by the lead before data; exact lines in reports/STAGE2_QUEUE_PREP.md)
    --closure_lambda <w>          # S11: full-vector closure rows G_carried - G_required on the sphere grid (1e-3 default in the nest rungs; 1 enforces the closure at once)
    --formulation both --both_weight <w> --chunk 128    # S10: momentum + vorticity rows (chunk <= 128 at L6-ext; chunk 512 OOMs)
    --radial_lambda_w <w>         # S12: sphere rows on the radial-lambda part of the momentum residual (d93); the RADIAL LAMBDA line reports the share
    --balance_lambda <l> --nonaxi_pin auto   # S9b (scalar balance rows with the non-axisymmetry guards; lambda = 1 destroys L6-ext starts, see FAILURE_ANALYSIS 30-31)
## Memory rules (one A100 80 GB; the supervisor places by slot bookkeeping, not GPU memory)
    # L >= 8 and SPEC-degree-channel (chdeg) jobs are exclusive; an L6-ext worker job peaks at 70-73 GB in its end-of-start battery; Nk 32 at L6-ext and the both
    # formulation need --chunk 128; a 40 GB re-evaluation of an L6/L8-ext state runs only on a held GPU (scripts/hold_and_reevaluate.sh <gpu> <job to wait for>,
    # which parks the exclusive pending jobs in queue/hold and releases them; scripts/release_hold.sh if it dies); never enqueue a smoke job while a GPU is held.
    # Heartbeats: the supervisor kills a running job whose heartbeat is older than heartbeat_stale_s = 1500 s (configs/supervisor.json). Since 14:20Z the worker runs
    # a 60 s watchdog thread through the whole end-of-start battery (new jobs), and scripts/heartbeat_guard.sh (detached: setsid nohup bash scripts/heartbeat_guard.sh &)
    # refreshes the epoch of any live running job older than 900 s every 60 s (logs/adhoc/heartbeat_guard.log); check it is alive at every shift start (pgrep -f heartbeat_guard).
    # Shift 5 (2026-10-25T16:35Z): (1) lm_solve releases the stored Jacobian right after J^T J, J^T r and the scaling are formed; before this fix every dense job held
    # TWO Jacobians at its peak (the previous J stayed bound into the next build), which is what OOMed L10 with SPEC-degree channels (J 43.3 GiB) at the second
    # iteration. (2) Split-column J^T J accumulation: --jtj_blocks k (enqueue_continuation.py; cfg jtj_blocks) stores at most N/k columns at once (time (k+1)/2
    # Jacobian builds; identical normal equations; validated at L8: steps equal to 4.6e-11, costs to 2e-15); use k = 2 for L10 with SPEC channels (peak about 57 GB
    # at chunk 64); not combinable with free parameters (fd columns). (3) Operator cancel of a queued/retrying job: touch queue/cancel/<job_id>; the next launch
    # of that job exits at once (ledger job_cancelled), the supervisor files it under queue/done, move the file to queue/cancelled by hand and remove the marker.
    # (4) Solver validation without the battery: --lm_only (worker saves z, z_lm_raw and the cost history to starts/start_000.pt; ledger kind lm_only_result with
    # the peak GPU memory; never a ranked state); compare two such runs with scripts/compare_lm_only.py <A.pt> <B.pt> <parent.pt>. (5) Every worker logs the sha256
    # of lm.py, worker.py, problem.py and fields.py it imported (CODE VERSIONS line; ledger job_code_versions; start_result.code_versions): a code edit never
    # changes a running job, only launches after the edit.
    # Shift 6 (2026-10-25T21:58Z-23:20Z): (6) the battery's heaviest item was the ray-integral pressure check (gradP_ray evaluates 491 520 scattered points per target
    # point in chunks; the per-chunk solid-harmonic and radial arrays scale with chunk x Nq_union): spec_diagnostics.RAY_CHUNK = 25000 (env E3_RAY_CHUNK; 200000 before)
    # cuts that item about 8x with per-point values unchanged (1303 stored scalars bitwise identical at L4 on the CPU; the GPU 1e-12 comparison is due on the first
    # L8/L10 battery launched with the new code: scripts/compare_ray_chunk.py <start> --device cuda:0 on a held GPU); d['extras_memory'] in the holdout spec_diag records
    # the cumulative allocated peak after the shells, origin Taylor, fine-grid Z/I and ray check. (7) Every start file carries the LM history (cost, rms, lam, accepted,
    # t_jac, z_sha256_12 per iteration); cfg save_iterates stores the iterates themselves (disposable T11 tests only). (8) code_versions hashes spec_diagnostics.py and
    # ray_integral.py as well. (9) Kill/resume is reproducible to 1e-14 over ten iterates, not bitwise (FAILURE_ANALYSIS 38); scripts/t11_literal_cpu.sh repeats the test.
    # (10) scripts/arm_reading.py <job_id> [--json] prints the standing lines of a finished job against its start; scripts/stage_coverage.py --boundary <ts> --label <l>
    # writes the per-stage coverage snapshot; export_candidate.py --extra_src_factor 6 stores a second pressure at 6 Nk source nodes (Stage II exports).

## Supervisor code version (added 2026-10-26T18:44Z, lead d128 IH)
The supervisor is a long-lived process: it runs the code loaded at its start, not the current scripts/supervisor.py. The live supervisor (pid 3548537, started 2026-10-24T23:02:39Z)
predates the 2026-10-26T03:56:48Z edit that added gpus_allowed to the dispatch loop, so job JSON fields added after a supervisor start (gpus_allowed) are NOT enforced until a restart
(scripts/restart_supervisor.sh at a quiet point: no running job that a restart would orphan; record the time, the live code sha and the treatment of running jobs in WORKLOG and a dated
line to the lead). Workers, by contrast, import the current scripts/worker.py at each job launch (CODE VERSIONS line in every stdout.log). Placement is therefore by queue order and priority
only; the job JSON stage field is bookkeeping and may be stale. Whole-job caps are not enforced by the supervisor (time_limit_per_start bounds the LM only): use scripts/cap_watcher.py
(a separate detached process bound to one job id and its owned PID; SIGTERM then SIGKILL at the whole-job cap or absolute end; no retry; records occupied seconds) or stop by hand.

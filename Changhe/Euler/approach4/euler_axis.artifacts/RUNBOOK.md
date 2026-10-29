# RUNBOOK.md (primary numerical search)

All commands run from numerical_code/ (the numerical project root) with the Python environment of numerical_code/env/
(pip_freeze_shared_interpreter.txt: Python 3.12.13; numpy, scipy, torch and mpmath versions also in hardware/HARDWARE_INVENTORY.md).
Every command below was run during the campaign; paths are relative to numerical_code/. The published code folders are src/, tests/,
supervisor/, scripts/, configs/, env/, hardware/ and candidates/; queue/, runs/ and logs/ are created at run time by the supervisor,
the worker and the test scripts. Commands marked [archive] read existing campaign run directories: they require the full run archive
(runs/, checkpoints/), not published. Log files named in the recorded outcomes (logs/...) belong to the run records (not published).

    PY="${PYTHON:-python3}" ; export OMP_NUM_THREADS=1      # always; mkdir -p logs before the first detached launch

## Tests (operator identities, Jacobians, pressure)
    $PY tests/test_ops.py            # 68 checks: chain rules, Delta_5, manufactured fields, Cartesian vs cylindrical momentum,
                                     # dilation covariance, axis limits, basis exactness, dtype (6 s). Record: 68 PASS, 0 failures in the three Stage III
                                     # runs (logs/tests/stage3_test_ops_*.log) and from a fresh copy of the artifacts (2026-10-29T12:41:07Z). History: the two retained
                                     # 2026-10-28 logs (19:16:48Z, 19:19:25Z) show 64 PASS and 1 FAIL of the 65-check suite of that time (exterior basis
                                     # exactness at tolerance 1e-9, errors 6.3e-5 and 2.8e-5 in the two logs, failing after the 18:29Z change to log-spaced exterior nodes; repaired at
                                     # 19:2xZ by the node count, run records); no log of the repaired 65-check pass is retained; the suite grew to 68 checks
                                     # with the Jacobi radial option (20:28Z). Each check has its own stated tolerance; not all are at round-off.
    CUDA_VISIBLE_DEVICES=0 $PY tests/test_jacobian.py cuda   # JVP vs finite differences (plain, free c_l, S1 rows, q0 pin) + timing
    $PY tests/test_pressure.py       # manufactured -Delta P = f (Gaussian, algebraic tail, monopole): P and grad P to 1e-11

## Supervisor (detached; survives the end of the launching session)
    mkdir -p logs
    CUDA_VISIBLE_DEVICES=0,1,2,3,4 setsid nohup $PY supervisor/supervisor.py --poll 15 > logs/supervisor.out 2>&1 &
    cat supervisor/heartbeat.json      # running jobs, counts, gpus, limits (updated every 30 s)
    tail -f logs/supervisor.log
    echo "0,1,2,3,4" > supervisor/gpus.txt            # change the usable GPUs without restarting
    echo '{"max_workers": 6, "per_gpu": 2, "stale_heartbeat_s": 900}' > supervisor/limits.json
    touch supervisor/STOP              # launch nothing new (running jobs continue); rm to resume launching
    touch supervisor/STOP_ALL          # also SIGTERM all workers (they checkpoint and exit 3; requeued, resumable)

## Jobs
    $PY scripts/make_sweep.py pilot1          # write the Stage I pilot sweep into queue/pending (idempotent)
    $PY scripts/make_sweep.py critical1       # c_l = 1/2 experiment
    $PY scripts/make_sweep.py s1pin1          # S1 branch with q(0, z0) pinned and c_l free
    $PY supervisor/worker.py runs/<job_id>/job.json --run-dir runs/<job_id>     # run or RESUME one job in the foreground
                                              # (the supervisor creates runs/<job_id> from queue/; [archive] for the campaign's own jobs)
    # resume test (SIGTERM after 20 s, relaunch, check "resumed from checkpoint" in the log); the script writes a unique disposable
    # run directory runs/zz_test_resume_<UTC>, whose name it records in logs/tests/resume_test.log.rundir:
    bash scripts/test_resume.sh ; cat logs/tests/resume_test.log ; grep -E "interrupted|resumed" "$(cut -d' ' -f3 logs/tests/resume_test.log.rundir)/log.txt"

## Monitoring and ranking
    for f in runs/*/heartbeat.json; do echo "$f $(cat $f)"; done
    $PY scripts/leaderboard.py --top 40       # -> CANDIDATE_LEADERBOARD.csv, PARAMETER_SWEEP.csv (ranked by the holdout rho_max of the pre-registered
                                              # specification when present) [archive to reproduce the published tables]
    $PY scripts/validate_candidate.py runs/<job_id>      # section 6.1 shell metrics of the pre-registered specification, with full-space
                                                         # pressure -> validation.json [archive for the campaign runs]

## Candidate export (exchange format of section 10 of the pre-registered specification) and independent value check
    $PY scripts/export_candidate.py runs/<job_id> <branch> <level> --note "..."     # [archive]
    cd candidates/<branch>/<level> && $PY field_eval.py      # numpy-only evaluator vs samples.npz (runs from the published candidates/)

## Added 2026-10-28T20:3xZ
    $PY scripts/make_sweep.py pilot2          # Jacobi ball basis + emax 4 (campaign default after the conditioning finding)
    $PY scripts/make_sweep.py critical2       # same at c_l = 1/2
    $PY scripts/make_refine.py continue|refine|freecl --top K   # continuation / refinement jobs from the best finished runs [archive]
    CUDA_VISIBLE_DEVICES=0 $PY tests/test_optimizer_manufactured.py   # forced manufactured solution: LM must recover it
    # Jacobian conditioning and null-direction support: computed by a scratch script (scratch/nullspace.py), not published
    mv queue/pending/<pattern> queue/held/    # park jobs without deleting them (queue/held is ignored by the supervisor)
    $PY scripts/make_figures.py [run_dir...]  # figures/ (cost, residual vs radius, spectral decay, fields, axis profiles, sweep) [archive]
    $PY scripts/summary_table.py              # branch-wise summary for the primary search's report (not published; summarized in the
                                              # accompanying report); reads PARAMETER_SWEEP.csv in the project root: cp ../PARAMETER_SWEEP.csv . first
Optimizer stage "homotopy" (worker): continuation in the forcing from the seed; see lm.homotopy_solve (test: configs/test_homotopy_job.json).
    $PY scripts/failure_map.py                # failure map of section 9.1 of the pre-registered specification -> FAILURE_MAP.md, FAILURE_MAP.csv [archive]
    $PY scripts/make_sweep.py t2a             # T2 odd-swirl ring-source branch (c_l 0.60/0.68, K 1/2, free c_l)
    $PY scripts/jacobian_svals.py <run_dir>   # section 9.1 Jacobian diagnostics: smallest singular values of the gauged Jacobian [archive for the campaign runs]
    $PY tests/test_farfield.py                # algebraic first far-field correction: scaled residuals decay like R^-(1/c) with it
    $PY scripts/make_refine.py continue --top 6 --prefix s1pin2_ --set slave_correction=true --tag slv1 --iters 2000   # T1 rerun with slaved exterior correction [archive]
    $PY scripts/t2_diagnostics.py runs/t2a_*  ;  $PY scripts/t3_diagnostics.py runs/t3a_*    # branch-specific diagnostics [archive]

## CPU-only operation since the GPU revocation (2026-10-29T00:57:59Z; all commands below were run on CPU)
    export CUDA_VISIBLE_DEVICES=            # mandatory for every command and job: a guard kills any of our processes that opens a GPU
    echo "cpu0,cpu1,cpu2,cpu3,cpu4" > supervisor/gpus.txt          # five CPU slots (one core each); the sixth core serves drivers and analysis
    echo '{"max_workers": 5, "per_gpu": 1, "stale_heartbeat_s": 900, "omp_threads": 1}' > supervisor/limits.json
    CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 setsid nohup nice -n 19 $PY supervisor/supervisor.py > logs/supervisor.out 2>&1 &
    # the supervisor reconciles queue/running against live pids and resumes interrupted jobs from their checkpoints (done for real at 01:06:41Z: requeue of the six interrupted jobs, checkpoint reloads at 01:06:44Z for five and 01:21:59Z for fmAL0_cl0p74
    # after the GPU kill: six jobs resumed at their checkpoint iterations); workers get --device cpu and OMP_NUM_THREADS = omp_threads
    # CPU timing (scratch/cpu_bench.py on a D24, a D36 and a D48 run; scratch script not published, runs [archive]):
    # one LM iteration: 0.31 s (D24), 1.3 s (D36), 4.4 s (D48) per core
## Small-step c_l chains for the failure map (scripts/chain_driver.py; detached pollers that write one queue job at a time) [archive: --start reads a run directory]
    CUDA_VISIBLE_DEVICES= setsid nohup nice -n 19 $PY scripts/chain_driver.py --start runs/<state> --tag fmA \
        --cls 0.73,0.72,0.70,0.65,0.60,0.55 --levels-at 0.70,0.60,0.55 --rm20-at 0.70 --priority 6 --iters 1000 --iters-level 1000 > logs/chain_driver_fmA.out 2>&1 &
    # --q0s 5.5,6.0,7.0 (aligned with --cls) raises the q0 pin per step; logs/chain_driver_<tag>.{log,json}; rerun the same
    # command to resume (finished steps are skipped). Level jobs: D24/n12/K16 (down-projection) and D48/n32/K32 (refinement) from the D36 step state.
## Frozen-phi swirl diagnostics (all require the full run archive (runs/, checkpoints/), not published)
    CUDA_VISIBLE_DEVICES= $PY scripts/q_eigen_floor.py runs/<state>            # PDE-q-rows-only least squares with the hard pin (NO interface rows:
                                                                               # q* = 0 outside the ball; superseded, kept for the record)
    CUDA_VISIBLE_DEVICES= $PY scripts/q_eigen_nullspace.py runs/<state>        # singular values, TSVD, source jets of that q*
    CUDA_VISIBLE_DEVICES= $PY scripts/q_eigen_values.py runs/<state> --inner full   # continuous q* (PDE + q interface + Tikhonov + q-slave rows):
                                                                               # values per shell, eta-row cost, singular directions, B(mu), source-adaptive points
    CUDA_VISIBLE_DEVICES= $PY scripts/homotopy_q_test.py runs/<state> --iters 1000 --validate   # q_t path and phi-only refits
## Stage II tables and figures (all require the full run archive (runs/, checkpoints/), not published)
    CUDA_VISIBLE_DEVICES= $PY scripts/failure_map.py          # FAILURE_MAP.csv/.md incl. the Stage II table (approach-test columns requested by the report author)
    CUDA_VISIBLE_DEVICES= $PY scripts/branch_table.py t1lad2_cl0p740 lad2 lad3 lad4 chain fmap fmA fmB fmC refl > LADDER_BRANCH_TABLE.md
    CUDA_VISIBLE_DEVICES= $PY scripts/stage2_figures.py       # figures/stage2_{rho_vs_level,rho_vs_cl,farfield_convergence,axis_origin}.png
## Reflection-class run: cfg parity_phi "odd", parity_q "even", z0_fixed true, z0_init 0.0, merge_tol 0.002 (examples: the runs/refl_* job files of the full run archive, not published)
## Additions of 2026-10-29T06:5xZ
    CUDA_VISIBLE_DEVICES= $PY scripts/make_stage2_sensitivity.py [--dry]   # sensitivity/robustness jobs of the 0.74 direct-seed state: outer interface R 5/20,
                                                                           # 1.5x quadrature, w_int 1000, scale_power_shift 0, perturbed restarts (written to a scratch folder),
                                                                           # L-BFGS then LM, q0 2.0/3.0 seeds (idempotent; writes queue/pending) [archive]
    $PY scripts/class_counts.py ../FAILURE_MAP.csv                         # per-class counts for FINAL_REPORT 4.6 (stdout and a Markdown table of the
                                                                           # run records); runs from the published FAILURE_MAP.csv
    $PY scripts/export_candidate.py runs/t1seedC_cl0p74_q2p5 T1_seed_cl0p74 L1 --note "..."   # exports of 06:47Z to 06:55Z (L1, L2, L2a); then chmod -R a-w [archive]
    CUDA_VISIBLE_DEVICES= $PY scripts/make_relative_perturbations.py   # per-coefficient relative perturbation restarts of the 0.74 state (RPert1-3) [archive]
    CUDA_VISIBLE_DEVICES= $PY scripts/make_stage2_extra.py             # second continuation, D48 of the variant with scale power shift s = 0, free c_l with bound 0.80 [archive]
    CUDA_VISIBLE_DEVICES= $PY scripts/make_critical_levels.py          # c_l = 1/2: D32 refinement and 2000-iteration continuation of the two best swirl-retaining states [archive]
    CUDA_VISIBLE_DEVICES= $PY scripts/make_stage2_late.py              # unrelated initializations at 0.74 with the direct-seed rows, fresh D24/D48 seeds, 0.68 sensitivity suite [archive]
    # one-command refresh of the failure map, class counts, leaderboard, F1/F5, stage2 figures, branch table, resource totals and the internal
    # artifact bundle (3 min, CPU; tested 07:07Z and 08:35Z): a packaging script of the internal bundle, not published
    CUDA_VISIBLE_DEVICES= $PY scripts/chain_driver.py --start runs/t1seedC_cl0p74_q2p5 --tag fmE --cls 0.735,0.73,0.725,0.72,0.71,0.70 --priority 6 --iters 1000   # 0.005-step chain (detached) [archive]
    bash scripts/stage3_tests.sh 0        # Stage III protected reproduction: tests/test_ops.py and scripts/test_resume.sh from a clean process with UTC
                                          # start/end, wall time and outcome -> logs/tests/stage3_tests_<UTC>.log (run after 11:59:44Z, before 14:00Z)
                                          # Record to cite (run records, not published): logs/tests/stage3_tests_20261029T122152Z.log (whole suite 12:21:52Z to 12:26:55Z, 303 s: test_ops wrapper
                                          # 8.9 s, 12:21:52Z to 12:22:01Z, 68 PASS, 0 failures; then test_resume wrapper 293.8 s, 12:22:01Z to 12:26:55Z: SIGTERM, measured exit 3 at 12:22:22Z after the checkpoint at iteration 405, clean-process relaunch,
                                          # 'resumed from checkpoint: stage 0 it 405' at 12:22:24Z, exit 0 at 12:26:55Z, wrapper wall 293.8 s; disposable run
                                          # runs/zz_test_resume_20261029T122201Z on GPU 0). The 12:03:08Z run (stage3_tests_20261029T120308Z.log) stands with
                                          # an unmeasured first exit status. n_iter of resumed runs double counts the checkpoint prefix (qualification table in the run records, not published).
    CUDA_VISIBLE_DEVICES=0 $PY scripts/jacobian_svals.py runs/t1seedC_cl0p74_q2p5   # section 9.1 Jacobian conditioning -> runs/<job>/jacobian_svals.json [archive]
    CUDA_VISIBLE_DEVICES= $PY scripts/make_stage2_final.py                          # the six final question jobs of 08:37Z (NoS1, Sep, freeclmid, seeds near 0.74) [archive]

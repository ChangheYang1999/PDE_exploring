# START HERE (numerics lane, rotating_euler_96h)

Purpose: numerical search for smooth decaying rotating backward self-similar profiles of 3D Euler
(2/5 < c_l < 1/2, omega != 0), primary spectral route of a three-lane campaign (lead: <lead directory>, verifier: <independent-route directory>).
Binding conventions: docs/ACCEPTANCE_SPEC.md. This directory: solver, campaign supervisor, queue, ledger, checkpoints, reports.

Read in this order:
1. reports/CONVENTIONS.md        exact representation, gauges, weights, residuals, pressure treatment of this code
2. NUMERICAL_METHODS.md          methods, tests, benchmarks, known limitations
3. RUNBOOK.md                    exact commands: tests, pilot, campaign, status, resume, validation
4. status/STATUS.json            machine-readable campaign status (written every minute by the supervisor)
5. status/ledger.jsonl           append-only run ledger (every start, job, retry, resume)
6. reports/CANDIDATE_LEADERBOARD.csv, reports/PARAMETER_SWEEP.csv (scripts/leaderboard.py regenerates them)
7. reports/DAILY_REPORT_*.md, FAILURE_ANALYSIS.md
8. ../NUM_REPORT.md (lane summary), ../WORKLOG.md (dated log), ../RUN_STATUS.md (resume pointer for the operator shifts)

Layout: src/{bases,equations,far_field,pressure,optimization,validation,campaign}, tests/, scripts/, configs/, queue/,
runs/<job_id>/ (worker.log, checkpoint.pt, starts/start_xxx.pt, results.jsonl), checkpoints/accepted/ (immutable), status/.
Environment: .venv (python 3.9, torch 2.8 CUDA 12.8, numpy, scipy, sympy, psutil); status/environment_lock.txt;
status/HARDWARE_INVENTORY.md.

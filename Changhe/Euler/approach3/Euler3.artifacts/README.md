# Euler3.artifacts: the accompanying artifacts of the rotating self-similar Euler campaign

This folder holds the records of a 96-hour numerical search for smooth, decaying, rotating backward self-similar profiles of the 3D incompressible Euler equations (2/5 < c_l < 1/2, omega != 0). It contains the solver code, the configurations, the supervisor and queue scripts and the queue state at the close, the complete run ledger, the status summaries, the coverage snapshots, the daily reports, the failure maps, the spectral coefficients of the exported candidate states, the test records of the reproducibility tests, the transfer evaluation of the independent route's exports, and copies of the independent verifier's final records.

Campaign facts:
- The campaign ran 96.00 h, from T0 2026-10-24T17:09:12Z (the supervisor's logged start, status/CAMPAIGN_START_UTC, is 17:09:14Z) to the supervisor exit at 2026-10-28T17:09:25Z, which the supervisor triggered itself when its 96 h budget was reached. No job was pending or running at the close.
- No state met the discovery tier. The best saved state (nest10, c_l 0.45, omega 1, omega/c_l 20/9, R_0 = 0.3; degree 10, Nk 24, Nr 72, even azimuthal modes) has a holdout rho_u^max of 0.04195 and 0.04145 on the two shell families, 4.2 times the Tier S bound 1e-2 (primary-reported); it is not a candidate.
- Every candidate file is a numerical approximation on a finite basis, not an exact profile.
- The ledger status/ledger.jsonl has 2405 records (994 start results).

## Directory map

- README.md: this file. MANIFEST.sha256: sha256 of every other file in this folder (relative paths, sha256sum format).
- code/src/: the solver (bases, equations, far_field, pressure, optimization, validation, campaign).
- code/scripts/: the supervisor (supervisor.py, start_supervisor.sh, stop_supervisor.sh, restart_*.sh), the worker (worker.py), queue scripts (enqueue_stage1.py, enqueue_continuation.py, hold_exclusive.sh, release_hold.sh, release_lowprio.sh), the validator (validate_candidate.py), report generators (status.py, leaderboard.py, resolution_table.py, daily_report.py, stage_coverage.py, make_plots.py, failure_map_rows*.py, shortlist*.py) and the reading and comparison helpers. Superseded versions are kept under versioned names (for example cap_watcher_v2.py to v4_1.py, make_artifacts_v2.sh to v7.sh).
- code/tests/: the test suite (tests T01 to T12; scripts/run_tests.sh runs it).
- configs/supervisor.json: the supervisor configuration (GPUs 0, 1, 4, 5, two slots per GPU, campaign start and length). The configuration of each experiment is the "config" block of its job file in queue/.
- queue/: the job files at the close: done/ (270), failed/ (30), hold/ (8, each with its hold_reason), hold_lowprio/ (64), cancelled/ (6). pending/ and running/ were empty at the close and are not present.
- status/: ledger.jsonl (the complete append-only run ledger), STATUS.json (the final machine-readable status summary, 2026-10-28T17:09:25Z), supervisor_heartbeat.json (the last heartbeat), CAMPAIGN_START_UTC, environment_lock.txt, HARDWARE_INVENTORY.md, RESUME_TEST.md.
- reports/: the daily reports (DAILY_REPORT_2026-10-24.md to DAILY_REPORT_2026-10-28.md; the script-generated T0+24h, T0+48h, T0+72h and T0+96h tables; DAILY_STATUS_*.json machine-readable summaries; DAILY_REPORT_2026-10-28.md is the final assembled report of the last day), the coverage snapshots (COVERAGE_stage1_20261025T230912Z, COVERAGE_stage2_20261027T170912Z, COVERAGE_stage3_20261028T170912Z (hour 96), and a test preview; .md and .json each), CANDIDATE_LEADERBOARD.csv and PARAMETER_SWEEP.csv (hour-96 versions), RESOLUTION_LADDER.md, the failure maps (FAILURE_MAP*.md), CONVENTIONS.md, the registrations (STAGE*_REGISTRATION*.md, S14/S15 records), the shortlists, the per-state readings (arm_reading_*.json, T09_*), the Stage III readings R1 to R3 (stage3_readings/), the external GPU process sightings (stage3_external_processes_*.md), drafts that were cited as drafts (GATE_I4_RESPONSE_DRAFT.md, STAGE2_FEASIBILITY_DRAFT.md, NUM_FINAL_SUMMARY_DRAFT.md), and reports/figures/ (the plots of the campaign prompt's section 8 with their CSV data, regenerated at hour 96).
- candidates/<id>/: coeffs.npz (spectral coefficients), meta.json (export metadata and diagnostics), meta_supplement_v124.json where present (SPEC v1.24 far coefficients computed after the export; meta.json stays as exported), BASIS.md (coefficient layout and conventions), SHA256.json (hashes, including the samples.npz file that is not included).
- section8/: the records of the three reproducibility tests: validation/ (single-command validation of the saved nest10 state), resume_test/ (interruption and resume), recovery/ (single-command stop and restart of the supervisor); COPY_CHECK.sha256 gives each copied record's sha256 against its source (original bytes, before path editing).
- transfer_eval/: cross-code evaluations of the independent route's exported states (REPORT.md and the fit JSON files).
- docs/: START_HERE.md, RUNBOOK.md (the exact commands of the campaign), NUMERICAL_METHODS.md, FAILURE_ANALYSIS.md (final version, items 1 to 55), NUM_REPORT.md (the primary route's dated report, final version), CPU_LIMIT.md (the operator's CPU limit of 2026-10-28 01:50 UTC), MATHEMATICAL_FORMULATION.md, FAR_FIELD_AND_ORIGIN_AUDIT.md, ACCEPTANCE_SPEC.md (the campaign lead's SPEC.md: the pre-registered acceptance norms), MANIFEST_frozen_20261028T034504Z.sha256 (the manifest of the package as frozen at 2026-10-28T03:45:04Z, before path scrubbing; unchanged bytes), EDITED_FILES.txt (the files whose text was edited in assembly, see below). The independent validation document is independent_validation/INDEPENDENT_VALIDATION.md.
- figures/: the campaign lead's figures (velocity profiles, balance profiles, spectral decay) with their CSV data and README.md.
- independent_validation/: copies of the independent verifier's records: INDEPENDENT_VALIDATION.md (the verifier's VERIFY_REPORT.md), FINAL_DISPOSITION.md and FINAL_REQUIREMENT_COVERAGE.md (the final disposition of 2026-10-28), REVIEW_fr19h.md, LABEL_C_VALIDATION_fr19h.md and ALL36_FINAL.md (the final review of the report installation), pressure_validation_nest10_registration/ (REGISTRATION.json, sha256 5a37faf9..., and FREEZE.json, sha256 d3bcd800..., of the verifier's registered pressure validation of the degree-10 rung at c_l = 0.45, omega = 1, R_0 = 0.3; byte-identical copies), stage2_gate_audits/ (four audit reviews of the Stage II gate II.4 and its failure map, and the audited gate text, revision r2; file names prefixed by the review directory name).

## Status of the records

- Every daily report and status summary is a primary-route record unless the report says otherwise. The independent verifier audited the final report and the hour-96 chain records, but the assembled daily report of 2026-10-28 (reports/DAILY_REPORT_2026-10-28.md) and the final primary summary were not given their own independent review before the run ended; they are primary-route records.
- The files in independent_validation/ are copies of the independent verifier's records. Links inside them to files that are not included here will not resolve. The 3 OPEN rows of the final audit remain open: resource closure, candidate validation beyond the text, and the canonical primary daily report and final summary not separately reviewed.
- section8/validation/: the single-command validation of the saved nest10 state (c_l 0.45, omega 1, omega/c_l 20/9, R_0 = 0.3) ran once on GPU 0 with unchanged code and no training, 2026-10-27 16:45:11Z to 18:42:07Z (7016 s), exit 0. The campaign lead accepted it (2026-10-27T19:17:17Z) as a reproduction of the saved nest10 diagnostics from a clean process: of the 89 compared rows, 81 agree within 1e-6 relative (57 identical, 21 to rounding, 3 close; they include the holdout rho_u^max 0.04195 and 0.04145), 7 differ (rho_u_bal on both grids by about 5 per cent, cause open and not cited; three Gram shell lists with 21 against 23 shells; two rounding-floor closure quantities) and 1 is definitional. The validation's new sections are unreviewed numbers and are not cited. This is not new evidence about the state. RECORD_CORRECTIONS_20261027.md lists the lead's corrections VC1 to VC13 to RECORD.md.
- section8/resume_test/: the interruption-and-resume test of the deployed worker (v2.4) on a disposable job (degree 4, Nk 10, two starts, SIGKILL after 120 s, resume at iteration 230, both starts done), accepted by the lead as a software resume test only.
- section8/recovery/: the single-command recovery test (scripts/stop_supervisor.sh, then scripts/start_supervisor.sh, each from a new login shell, with no job pending or running; 2026-10-28 02:49:03Z to 02:55:48Z; the queue counts unchanged and the 2405-row ledger byte-identical before and after), accepted by the lead (2026-10-28T03:04:31Z) as a software test of the supervisor's stop and restart. Its one open item (the STATUS.json best_rms figure changed with an identical ledger) was closed by the lead's reading (the old process held an older src/campaign/ledger.py 'latest' rule in memory); RECORD_ADDENDUM1_20261028.md carries that closure and one wording correction (the saved status files hold three leaderboard rows each, not ten).
- reports/stage3_readings/: the Stage III replication and perturbation readings R1 to R3 at c_l 0.45, omega 1, omega/c_l 20/9 (reader outputs and chain logs as written by the CPU readers, and the hashes files of R2 and R3; R1 has no hashes file). The two stage3_r1 logs named FAILED_SHELL are a tooling relaunch, not a retry: each holds three shell redirection errors and no reader output, no comparison ran, and their rc 0 lines certify nothing; the R1 distances come from the relaunched compare chains (the logs without FAILED_SHELL). Every value is primary-reported; none is a gate entry and none makes any state a candidate. The R4 reading is cited in reports/DAILY_REPORT_2026-10-28.md as a lead-accepted late result, but its files are not included.
- INDEPENDENT_VALIDATION.md did not exist in the campaign directory or in the frozen package; the independent validation document provided here is the verifier's VERIFY_REPORT.md, copied as independent_validation/INDEPENDENT_VALIDATION.md.

## Changes against the frozen package and the campaign directory

- Added after the freeze of 2026-10-28T03:45:04Z (closing records): status/STATUS.json (final), status/supervisor_heartbeat.json, reports/COVERAGE_stage3_20261028T170912Z.md and .json, reports/DAILY_REPORT_2026-10-28.md, reports/DAILY_REPORT_2026-10-28_T0+96h.md, reports/DAILY_STATUS_2026-10-28_T0+96h.json, the hour-96 versions of reports/CANDIDATE_LEADERBOARD.csv, reports/PARAMETER_SWEEP.csv, reports/RESOLUTION_LADDER.md and reports/figures/, the final reports/stage3_external_processes_20261028.md, docs/FAILURE_ANALYSIS.md and docs/NUM_REPORT.md, queue/, and the docs, figures/ and independent_validation/ files listed above. status/ledger.jsonl holds the same 2405 records as the campaign's final ledger (no row was written after the freeze); only its paths were edited.
- Renamed: the campaign files "DAILY_REPORT_2026-10-28_T0 + 96 h.md" and "DAILY_STATUS_2026-10-28_T0 + 96 h.json" (names with spaces) are reports/DAILY_REPORT_2026-10-28_T0+96h.md and reports/DAILY_STATUS_2026-10-28_T0+96h.json; references to them in the markdown files use the new names.
- Removed: the primary route's work log (docs/WORKLOG.md of the frozen package), operator hand-over notes, superseded daily report drafts of days that have a final report, test-output scratch, backup copies (*.bak_*), and plot logs.
- Edited: absolute local paths were replaced by paths relative to the campaign root or by neutral placeholders (<independent-route directory>, <lead directory>, <shared volume>, <python site-packages>, <home>, <other project>), and internal directory names in prose were replaced by "the primary route", "the independent route" and "the campaign lead". No CSV or JSON value was changed except for paths. docs/EDITED_FILES.txt lists the edited files; their sha256 values quoted inside records, and their entries in docs/MANIFEST_frozen_20261028T034504Z.sha256, refer to the unedited originals.

## Environment

- Python 3.9.25, torch 2.8.0+cu128 (CUDA 12.8, cuDNN 91002), numpy 2.0.2, scipy 1.13.1, sympy 1.14.0, mpmath 1.3.0, numba 0.60.0, psutil 7.2.2, matplotlib 3.9.4; float64 throughout. The full package list is status/environment_lock.txt.
- Hardware: one node with eight NVIDIA A100-SXM4-80GB GPUs (driver 580.167.08), Intel Xeon Platinum 8275CL (96 logical CPUs), about 1.1 TB of RAM (status/HARDWARE_INVENTORY.md). This route used four of the GPUs (0, 1, 4 and 5). From 2026-10-28 01:46Z the operator limited this route to CPUs 0 and 2, at most two worker processes, OMP_NUM_THREADS=1 (docs/CPU_LIMIT.md).

## Not included (size)

Checkpoints (runs/<job>/checkpoint.pt, checkpoints/accepted/), the run directories (runs/<job>/, including the start files runs/<job>/starts/start_xxx.pt), the logs (logs/, runs/_logs/), the exchange samples (candidates/<id>/samples.npz, 32 MB to 40 MB each; their sha256 is in candidates/<id>/SHA256.json) and the R4 reading files are not included. A resume from this folder therefore cannot continue any interrupted job: it starts from the saved candidate files, candidates/<id>/coeffs.npz with meta.json and BASIS.md (the best state is candidates/nest10_L10_cl0.45_om1.0_p0/). The start file of the best state, runs/nest10_L10_cl0.45_om+1.0_fixed_p0/starts/start_000.pt (118348 bytes, sha256 b2c111728a215c985bc0aaa9c96bcb3df77afd912f02de0dfa132adab4c7ee64), is not included as such: two string fields of its pickled contents (config/init_from and meta/source, the path of its parent start file) hold an absolute local path of the campaign machine. In its place, candidates/nest10_L10_cl0.45_om1.0_p0/start_000_relpath.pt (sha256 d4e5e444b6f23c5f9383d9bca52d93dc0d8f3af26aafe8760380dcd8d09dbbb2) is the same file loaded with torch.load and saved again with torch.save after only those two fields were made relative to the campaign root (runs/nest8_L8_cl0.45_om+1.0_fixed_p0_cont150/starts/start_000.pt); on reloading, every tensor, array and other entry is equal to the original (exact comparison, done at the close of the run). The validator does not read either field. Its bytes, and so its sha256, differ from the original file named above. To rebuild a state from coeffs.npz: Model(L, Nk, m_parity, R0, channels=json.loads(channels)) of code/src/equations/fields.py with z = pack(A, C, extra=dict(B=B, D=D, E=E)) (coefficient layout and conventions in candidates/<id>/BASIS.md).

## Exact commands

Every script finds the campaign root as the parent of its own directory (bash: ROOT=$(cd "$(dirname "$0")/.." && pwd); python: os.path.join(os.path.dirname(__file__), "..")) and expects src/, scripts/, tests/, configs/, status/, queue/, reports/, candidates/, logs/, runs/ and .venv/ side by side under that root. In this folder src/, scripts/ and tests/ are under code/, so first recreate the campaign-root layout in a working copy (run from the directory that contains Euler3.artifacts/; the published folder stays untouched):

    mkdir campaign
    cp -a Euler3.artifacts/code/src Euler3.artifacts/code/scripts Euler3.artifacts/code/tests campaign/
    cp -a Euler3.artifacts/configs Euler3.artifacts/status Euler3.artifacts/queue Euler3.artifacts/reports Euler3.artifacts/candidates Euler3.artifacts/transfer_eval campaign/
    mkdir -p campaign/logs campaign/runs campaign/checkpoints campaign/queue/pending campaign/queue/running campaign/queue/cancel
    python3.9 -m venv campaign/.venv
    campaign/.venv/bin/pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cu128
    campaign/.venv/bin/pip install numpy==2.0.2 scipy==1.13.1 sympy==1.14.0 mpmath==1.3.0 numba==0.60.0 psutil==7.2.2 matplotlib==3.9.4
    cd campaign
    scripts/run_tests.sh                                   # the test suite; GPU tests on CUDA device 0; log in logs/test_suite_<time>.log

All later commands run inside campaign/.

(a) Validate the saved best state with the single-command validator (no training; training grid, 1.5x refined grid, holdout points; --full adds the holdout SPEC diagnostics, critical points, strength, off-grid vorticity residual maxima and orbit averages). The start file is put at the path the recorded run used:

    mkdir -p runs/nest10_L10_cl0.45_om+1.0_fixed_p0/starts
    cp candidates/nest10_L10_cl0.45_om1.0_p0/start_000_relpath.pt runs/nest10_L10_cl0.45_om+1.0_fixed_p0/starts/start_000.pt
    sha256sum runs/nest10_L10_cl0.45_om+1.0_fixed_p0/starts/start_000.pt   # prints d4e5e444b6f23c5f9383d9bca52d93dc0d8f3af26aafe8760380dcd8d09dbbb2 (the original file of the campaign machine: b2c111728a215c985bc0aaa9c96bcb3df77afd912f02de0dfa132adab4c7ee64)
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/validate_candidate.py runs/nest10_L10_cl0.45_om+1.0_fixed_p0/starts/start_000.pt --full --json validate_full_nest10.json

The reference output of this command is section8/validation/validate_full_nest10.json with stdout.log (7016 s on one A100).

(b) Start, stop and resume the supervisor. The supervisor stops by its own rule once campaign_hours (96) have passed since campaign_start in configs/supervisor.json (2026-10-24T17:09:14Z), so with the published configuration it stops again at once. Before a new run set campaign_start to the current time, and set "gpus" to the devices you have:

    .venv/bin/python -c "import json,time; p='configs/supervisor.json'; c=json.load(open(p)); c['campaign_start']=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()); json.dump(c, open(p, 'w'), indent=1)"
    scripts/start_supervisor.sh          # detached (setsid nohup); log logs/supervisor.log; refuses if the pid in status/supervisor_heartbeat.json is a live supervisor.py
    .venv/bin/python scripts/status.py 10   # status and the top 10 leaderboard rows
    scripts/stop_supervisor.sh           # creates status/STOP_SUPERVISOR; the supervisor sends SIGTERM to its workers (they checkpoint) and exits; jobs stay in the queue
    scripts/start_supervisor.sh          # resume: removes STOP_SUPERVISOR, moves job files left in queue/running/ back to queue/pending/, and each worker resumes from runs/<job_id>/checkpoint.pt

The queue is filled by writing job files into queue/pending/; the supervisor launches them by priority, then creation time:

    .venv/bin/python scripts/enqueue_stage1.py --tag <tag> --L 6 --Nk 16 --formulation mom --nlw [--efrac 0.5] [--free] [--channels 6,6,6] [--m_parity all]
    .venv/bin/python scripts/enqueue_continuation.py --src runs/<job>/starts/start_000.pt --tag <tag> --L 10 --Nk 24 --sigmaZ 1 --channels 6,6,6 [--free]   # needs a start file
    scripts/release_hold.sh              # moves every job of queue/hold/ (each carries its hold_reason) to queue/pending/

Workers write runs/<job_id>/checkpoint.pt at most every 15 minutes and after every start; a job that is stopped (stop_supervisor.sh, SIGTERM) or killed resumes from it when it is launched again with the same run directory (status/RESUME_TEST.md, section8/resume_test/RECORD.md). In this folder no checkpoint is included and queue/pending/ and queue/running/ are empty, so nothing is left to resume: new work starts from the saved candidate files described above.

(c) Re-run one queue job (one experiment configuration) directly, without the supervisor. The example is a Stage I multistart job (degree 2, Nk 8, 60 starts, no warm start); jobs whose config has init_from need that start file under runs/:

    CUDA_VISIBLE_DEVICES=0 OMP_NUM_THREADS=1 .venv/bin/python scripts/worker.py queue/done/nest2_L2_cl0.45_om+1.0.json runs/rerun_nest2_L2_cl0.45_om+1.0

Running the same command again after an interruption resumes from runs/rerun_nest2_L2_cl0.45_om+1.0/checkpoint.pt. To run it through the supervisor instead, copy the job file into the queue (cp queue/done/nest2_L2_cl0.45_om+1.0.json queue/pending/) with the supervisor running. The worker appends its records to status/ledger.jsonl of the working copy.

(d) Regenerate a coverage snapshot, the tables and a daily report from the ledger (these overwrite the copies in campaign/reports/):

    .venv/bin/python scripts/stage_coverage.py --boundary 2026-10-28T17:09:12Z --label stage3 --no_bins   # reports/COVERAGE_stage3_20261028T170912Z.md and .json
    .venv/bin/python scripts/leaderboard.py          # reports/PARAMETER_SWEEP.csv, reports/CANDIDATE_LEADERBOARD.csv
    .venv/bin/python scripts/resolution_table.py     # reports/RESOLUTION_LADDER.md
    .venv/bin/python scripts/daily_report.py T0+96h  # reports/DAILY_REPORT_<today>_T0+96h.md and reports/DAILY_STATUS_<today>_T0+96h.json

--no_bins skips the descriptor bins, which read the run start files (not included), so a regenerated snapshot lacks that section. daily_report.py dates its output and its elapsed time by the clock at the time it runs. make_plots.py (reports/figures/) reads run start files and cannot be re-run from this folder.

## Publication review additions

The report's state identifiers are mapped below to the original run and export names. These are record identifiers, not paths guaranteed to be present: the omissions described above still apply. The scientific state descriptions, parameters, degrees and leaderboard ranks are unchanged.

| Report state | Original run and export record |
|---|---|
| St1 | primary nest8nk8_L8_cl0.45_om+1.0_fixed (not on the LB); independent nest8nk8_L8_cl0.45_om1.0_p0 |
| St2 | LB rank 1, nest8_L8_cl0.45_om+1.0_fixed_p0_cont150; independent nest8_L8_cl0.45_om1.0_p0_cont150 |
| St3 | LB rank 3, nest8_L8_cl0.45_om+1.0_fixed_p0; independent nest8_L8_cl0.45_om1.0_p0 |
| St4 | LB rank 7, nest6_L6_cl0.45_om+1.0_fixed_p0_om+1.0s43s0; independent nest6_L6_cl0.45_om1.0_p0 |
| St5a | LB rank 30, nest4_L4_cl0.45_om+1.0_fixed_p1_om+1.0s43; not exported, no independent copy |
| St5b | LB rank 31, nest4_L4_cl0.45_om+1.0_fixed_p0_om+1.0s31; independent nest4_L4_cl0.45_om1.0_p0 |
| St6 | LB rank 45, s9b_L4_cl0.45_om+1.0_fixed_bal10_naxpin_from_bal1; independent s9b_L4_cl0.45_om1.0_bal10 |
| St7a | LB rank 35, nest8_L8_cl0.45_om+0.3_fixed_p0; independent nest8_L8_cl0.45_om0.3_p0 |
| St7b | LB rank 32, nest8_L8_cl0.45_om+0.3_fixed_p0_cont150; independent nest8_L8_cl0.45_om0.3_p0_cont150 |
| St8a | LB rank 44, nest6_L6_cl0.45_om+0.3_fixed_p0_om+0.3s55s0; independent nest6_L6_cl0.45_om0.3_p0 |
| St8b | LB rank 43, nest6_L6_cl0.45_om+0.3_fixed_p1_om+0.3s16s0; independent nest6_L6_cl0.45_om0.3_p1 |
| St9a | LB rank 38, nest8_L8_cl0.42_om+0.3_fixed_p0; independent nest8_L8_cl0.42_om0.3_p0 |
| St9b | primary nest8_L8_cl0.42_om+0.3_fixed_p0_cont150 (not on the LB); independent nest8_L8_cl0.42_om0.3_p0_cont150 |
| St10 | LB rank 4, d6w_L8_cl0.45_om+0.3_fixed; independent d6w_L8_cl0.45_om0.3 |
| St11a | LB rank 23, d6t_L6_cl0.45_om+0.3_fixed; independent d6t_L6_cl0.45_om0.3 |
| St11b | LB rank 6, d6t_L8_cl0.45_om+0.3_fixed; independent d6t_L8_cl0.45_om0.3 |
| St12 | independent D6GN400 (run stage1_original_d6_gn); no primary copy |

Other identifiers removed from the report's prose:

| Report description | Identifier in the records |
|---|---|
| First R3 source attempt | source_R3_001 |
| Second R3 source attempt | source_R3_002 |
| First, second and third Group B controls | mixed101, fullcall129, precision249 (in that order) |
| Local block of 32 pressure targets | local32 |
| Pressure registration and freeze | independent_validation/pressure_validation_nest10_registration/REGISTRATION.json (5a37faf9...) and FREEZE.json (d3bcd800...) |
| Deployed worker v2.4 | code/scripts/worker.py (historical hash 2edbd00c...) |

Two retained evidence files exceed 1 MB. status/ledger.jsonl is the complete input needed by the coverage, leaderboard, resolution and daily-report commands above. independent_validation/INDEPENDENT_VALIDATION.md contains the detailed mathematical and numerical audit history, including failed checks, corrections and their scope; the short final audit summaries do not reproduce these individual checks. Both support the report and are retained as evidence, not disposable scratch output. No other file exceeds 1 MB.

To verify the published files before creating a working copy, run this from the directory containing Euler3.artifacts/:

    (cd Euler3.artifacts && sha256sum -c MANIFEST.sha256)

The publication review changed this README to preserve the identifiers removed from the report and explain the retained large evidence files. MANIFEST.sha256 was refreshed for the published bytes; the historical frozen manifest remains unchanged.

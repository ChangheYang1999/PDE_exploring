#!/bin/bash
# Publishable subset (run instructions): code, configs, tests, run ledger, status summaries, reports, README with exact commands,
# the best candidate coefficients (small files only; samples.npz excluded), integrity manifest with sha256. Target < 50 MB, relative paths.
set -e
ROOT=$(cd "$(dirname "$0")/.." && pwd); A=$ROOT/../artifacts; TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
mkdir -p $A; rm -rf $A/code $A/configs $A/status $A/reports $A/candidates $A/transfer_eval $A/docs
mkdir -p $A/code $A/configs $A/status $A/reports $A/candidates $A/transfer_eval $A/docs
cp -r $ROOT/src $ROOT/scripts $ROOT/tests $A/code/; find $A/code -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
cp $ROOT/configs/*.json $A/configs/ 2>/dev/null || true
cp $ROOT/status/ledger.jsonl $ROOT/status/STATUS.json $ROOT/status/benchmark.json $A/status/ 2>/dev/null || true
cp $ROOT/status/HARDWARE_INVENTORY.md $ROOT/status/environment_lock.txt $ROOT/status/CAMPAIGN_START_UTC $ROOT/status/RESUME_TEST.md $A/status/ 2>/dev/null || true
cp $ROOT/reports/*.md $ROOT/reports/*.csv $ROOT/reports/*.json $A/reports/ 2>/dev/null || true
mkdir -p $A/reports/figures; cp $ROOT/reports/figures/* $A/reports/figures/ 2>/dev/null || true
cp $ROOT/transfer_eval/*.json $ROOT/transfer_eval/REPORT.md $A/transfer_eval/ 2>/dev/null || true
for d in $ROOT/candidates/*/; do c=$(basename $d); mkdir -p $A/candidates/$c; cp $d/coeffs.npz $d/meta.json $d/meta_supplement_v124.json $d/BASIS.md $d/SHA256.json $A/candidates/$c/ 2>/dev/null || true; done
cp $ROOT/START_HERE.md $ROOT/RUNBOOK.md $ROOT/NUMERICAL_METHODS.md $ROOT/FAILURE_ANALYSIS.md $A/docs/ 2>/dev/null || true
cp $ROOT/../NUM_REPORT.md $ROOT/../WORKLOG.md $A/docs/ 2>/dev/null || true
cp $ROOT/requirements*.txt $ROOT/environment*.txt $ROOT/pip_freeze*.txt $A/ 2>/dev/null || true
[ -f $ROOT/.venv/bin/pip ] && $ROOT/.venv/bin/pip freeze > $A/pip_freeze.txt 2>/dev/null || true
cat > $A/README.md <<EOR
# Artifacts of the numerics lane (rotating backward self-similar Euler profiles, 2/5 < c_l < 1/2, omega != 0)

Generated $TS by scripts/make_artifacts.sh from the campaign directory rotating_euler_96h/ (all paths relative to this directory).
Everything is an approximate numerical state; no exact profile was found (see docs/NUM_REPORT.md and reports/).

Contents
- code/src, code/scripts, code/tests: the solver, campaign supervisor, diagnostics and tests (python 3.9, torch 2.8 CUDA 12.8, float64).
- configs/: supervisor configuration. status/ledger.jsonl: the complete run ledger (every start, job event, re-evaluation, note).
- status/STATUS.json: machine-readable status summary; status/benchmark.json: one-GPU benchmark.
- reports/: CANDIDATE_LEADERBOARD.csv, PARAMETER_SWEEP.csv, RESOLUTION_LADDER.md, STAGE1_SHORTLIST.md, DAILY_REPORT_*.md, CONVENTIONS.md, G1_TESTS.md,
  STAGE2_FEASIBILITY_DRAFT.md, GATE_I4_RESPONSE_DRAFT.md, S8_PROTOTYPE.md, s2s3_*.json (prototype readings); reports/figures/: the PROMPT section 8 plots with CSV data.
- candidates/<id>/coeffs.npz + meta.json (+ meta_supplement_v124.json: SPEC v1.24 far coefficients, computed after the export; meta.json and its manifest stay as exported) + BASIS.md: spectral coefficients of exported states (the exchange samples.npz files, 32 MB each,
  stay in the campaign directory candidates/<id>/samples.npz; their sha256 is in SHA256.json).
- transfer_eval/: cross-code evaluations of the independent route's exported states.
- docs/: START_HERE, RUNBOOK (exact commands), NUMERICAL_METHODS, FAILURE_ANALYSIS, NUM_REPORT, WORKLOG.
- MANIFEST.sha256: integrity manifest of every file here.

Exact commands (from a copy of the campaign directory with its .venv; see docs/RUNBOOK.md)
    scripts/run_tests.sh                                                   # tests T01-T12
    CUDA_VISIBLE_DEVICES=0 .venv/bin/python scripts/validate_candidate.py runs/<job>/starts/start_000.pt --full   # validation without retraining
    scripts/start_supervisor.sh                                            # recovery from the last accepted campaign state (queue + checkpoints)
    .venv/bin/python scripts/status.py 10                                  # status
    .venv/bin/python scripts/leaderboard.py; .venv/bin/python scripts/resolution_table.py; .venv/bin/python scripts/daily_report.py
To rebuild a state from coeffs.npz: Model(L, Nk, m_parity, R0, channels=json.loads(channels)) of code/src/equations/fields.py with
z = pack(A, C, extra=dict(B=B, D=D, E=E)) (coefficient layout and conventions in candidates/<id>/BASIS.md).
EOR
(cd $A && find . -type f ! -name MANIFEST.sha256 -print0 | sort -z | xargs -0 sha256sum > MANIFEST.sha256)
du -sh $A | cut -f1; echo "artifacts written $TS"

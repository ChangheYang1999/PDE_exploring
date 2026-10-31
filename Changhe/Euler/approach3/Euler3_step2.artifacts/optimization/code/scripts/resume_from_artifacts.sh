#!/bin/bash
# Publication path correction: also resolve starting-state paths relabeled RUN_ROOT/ in the published job files.
# Campaign version history: resume_from_artifacts.sh v2.1 (2026-10-30T13:3xZ: comment wording per V750; the executed lines are those of v2 fb35ce8e3bf2a03d). v2 (2026-10-30T13:1xZ; lead 11:43:30Z, 13:01:25Z item 3; verifier V739): one-command resume of a published final state from the ARTIFACTS layout, relative paths.
# Run from the artifacts folder (the one that holds code/, final_states/, starts/, runs/):
#   bash code/scripts/resume_from_artifacts.sh <ROLE__JOB.pt in final_states/> <GPU index or cpu> [extra requested iterations, default 1] [scratch dir, default ./resume_scratch] [LM allowance in seconds, default 1800]
# What it does (a reader's procedure; no published or recorded file is modified): (1) creates a FRESH scratch ROOT (it refuses an existing directory) and copies the published code
# (code/src, code/scripts, code/configs) and the lineage root starts (starts/) into it, failing at once if a required copy fails; (2) places the final state (the worker's segment-end
# checkpoint: coefficients, parameters, optimizer state, counters) as runs/<JOB>/checkpoint.pt; (3) writes runs/<JOB>/job.json from the published job file runs/<JOB>/job.json with
# init_from made relative to the scratch ROOT, max_iter = (checkpoint iteration + extra), time_limit_per_start = the LM allowance, the cheap end battery (holdout diagnostics only) and the
# label SMOKE; (4) PATCHES THE SCRATCH COPY of scripts/worker_d6.py in one documented line: the frozen worker carries the campaign clock guard
# TEAM_STOP_EPOCH = T0_EPOCH + 47.0 * 3600.0 (2026-10-30T19:30:31Z) and caps every LM segment at max(60 s, time to the team stop minus 25 min), so after the campaign it would cap the LM at
# 60 s whatever the job file asks; no job-file key overrides it; the scratch copy gets TEAM_STOP_EPOCH = time.time() + 365 days (the original and patched sha256 are written to
# runs/<JOB>/WORKER_PATCH_RECORD.txt); (5) runs the worker: python scripts/worker_d6.py runs/<JOB>/job.json runs/<JOB>. The worker resumes from the checkpoint by its production resume
# path (iteration > 0, counters present, same gradient spacing), logs "LM initial cost" = the raw saved-iterate objective of the final state (not a normalized end-diagnostic value),
# then requests `extra` more outer LM iterations: max_iter requests outer iterations and does not guarantee accepted increments (damping, counter, stall and stale-Jacobian retry
# behaviour are the worker's own); the LM allowance excludes the initial objective and the end battery and is checked between iterations. The patch replaces the worker's fixed
# campaign stop by a one-year relative stop only; the min/max budget expression and its 25-min battery reserve are unchanged (campaign v2.1 wording, V750; the publication correction affects starting-state path resolution only).
# The cheap battery writes runs/<JOB>/results.jsonl. The label SMOKE marks the run as a software test, not a scientific result.
set -eu
A=$(pwd); FS=$1; GPU=${2:-0}; EXTRA=${3:-1}; S=${4:-$A/resume_scratch}; ALLOW=${5:-1800}
[ -f "$A/final_states/$FS" ] || { echo "final state $FS not found in $A/final_states/"; exit 2; }
JOB=${FS#*__}; JOB=${JOB%.pt}; [ -f "$A/runs/$JOB/job.json" ] || { echo "published job file runs/$JOB/job.json not found"; exit 2; }
[ -e "$S" ] && { echo "scratch directory $S exists: refusing to reuse it (give a fresh directory)"; exit 3; }
PY=${PYTHON:-python}
mkdir -p "$S/runs/$JOB" "$S/status" "$S/queue/cancel" "$S/starts"
cp -r "$A/code/src" "$S/src"; cp -r "$A/code/scripts" "$S/scripts"; cp -r "$A/code/configs" "$S/configs"
cp "$A/starts/"*.pt "$S/starts/"
cp "$A/final_states/$FS" "$S/runs/$JOB/checkpoint.pt"
# (4) the documented one-line patch of the SCRATCH worker copy (the published code/scripts/worker_d6.py is untouched)
W="$S/scripts/worker_d6.py"; ORIG_LINE='TEAM_STOP_EPOCH = T0_EPOCH + 47.0 * 3600.0'
grep -qF "$ORIG_LINE" "$W" || { echo "the scratch worker copy does not contain the expected clock-guard line; refusing to patch"; exit 4; }
SHA0=$(sha256sum "$W" | cut -c1-64)
$PY - "$W" "$ORIG_LINE" <<'PYEOF'
import sys
p, orig = sys.argv[1], sys.argv[2]; s = open(p).read()
new = "TEAM_STOP_EPOCH = time.time() + 365.0 * 86400.0   # resume_from_artifacts.sh v2: the campaign clock guard (team stop 2026-10-30T19:30:31Z) is removed in this SCRATCH copy only; the LM allowance is the job file's time_limit_per_start"
assert s.count(orig) == 1; open(p, "w").write(s.replace(orig, new, 1))
PYEOF
SHA1=$(sha256sum "$W" | cut -c1-64)
printf 'scripts/worker_d6.py in this scratch copy: original sha256 %s (the published file), patched sha256 %s; patched line: "%s" -> "TEAM_STOP_EPOCH = time.time() + 365.0 * 86400.0"; reason: the frozen worker caps each LM segment at max(60 s, time to 2026-10-30T19:30:31Z minus 25 min); no job-file key overrides it.\n' "$SHA0" "$SHA1" "$ORIG_LINE" > "$S/runs/$JOB/WORKER_PATCH_RECORD.txt"
$PY - "$A/runs/$JOB/job.json" "$S/runs/$JOB/job.json" "$S/runs/$JOB/checkpoint.pt" "$EXTRA" "$ALLOW" <<'PYEOF'
import json, sys, os
src, dst, ck, extra, allow = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), float(sys.argv[5])
j = json.load(open(src)); cfg = j.get("config", j)
v = cfg.get("init_from")
if isinstance(v, str) and (os.path.isabs(v) or v.startswith("RUN_ROOT/")):
    cfg["init_from"] = os.path.join("starts", os.path.basename(v))        # relative to the scratch ROOT; the file comes from the published starts/
    if not os.path.exists(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(dst))), cfg["init_from"])):
        print("ERROR: the lineage root start", cfg["init_from"], "is not among the published starts"); sys.exit(5)
import torch
cur = torch.load(ck, map_location="cpu", weights_only=False).get("current") or {}
it = int(cur.get("it", 0))
if it <= 0:
    print("ERROR: the final state has no resumable current iterate (iteration 0)"); sys.exit(6)
cfg["max_iter"] = it + extra; cfg["time_limit_per_start"] = allow; cfg["battery"] = "cheap"; cfg.pop("continue_from_run", None)
j["label"] = "SMOKE"; j["note"] = (j.get("note") or "")[:200] + " | RESUME SMOKE from the published artifacts (resume_from_artifacts.sh v2): checkpoint iteration %d, max_iter %d (a request for %d more iterations, not a guarantee of accepted increments), LM allowance %.0f s, cheap battery; not a scientific result" % (it, cfg["max_iter"], extra, allow)
json.dump(j, open(dst, "w"), indent=1); print("job file written: checkpoint iteration", it, "max_iter", cfg["max_iter"], "time_limit_per_start", allow, "init_from", cfg.get("init_from"))
PYEOF
cd "$S"
if [ "$GPU" = "cpu" ]; then export CUDA_VISIBLE_DEVICES=; else export CUDA_VISIBLE_DEVICES=$GPU; fi
export OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1
echo "running: (cd $S && CUDA_VISIBLE_DEVICES=$GPU OMP_NUM_THREADS=1 $PY scripts/worker_d6.py runs/$JOB/job.json runs/$JOB)"
$PY scripts/worker_d6.py "runs/$JOB/job.json" "runs/$JOB"
echo "done; see $S/runs/$JOB/worker.log, results.jsonl (label SMOKE) and WORKER_PATCH_RECORD.txt"

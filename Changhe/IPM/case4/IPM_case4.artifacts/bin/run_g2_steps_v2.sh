#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G2 step runner, version 2 (for runs after the current chain): per-step manifest verification; the step verdict is taken from the
# guard run's result.json (success, returncode, stop_reasons), never from the log; stops on a guard stop/hold or a failed step.
# Usage: run_g2_steps_v2.sh <tag> <session-suffix> <workers> <policy.json> step1 [step2 ...]
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=$LANE/work/research/hardware/guard.py
TAG=$1; SUF=$2; W=$3; POLICY=$4; shift 4; OUT=$LANE/outputs/g2/$TAG; mkdir -p $OUT; cd $LANE/work/research860
M=$LANE/outputs/manifests/code_manifest_$TAG.json; [ -f $M ] || { echo "no manifest $M"; exit 1; }
SESS=$LANE/outputs/g2/session_${TAG}_$SUF
[ -d $SESS ] || $PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $POLICY >> $OUT/run.log 2>&1 || exit 1
verify() { $PY - "$M" <<'PYEOF'
import json, hashlib, sys
m = json.load(open(sys.argv[1])); bad = []
for row in m['files']+m['frozen_181_closure']:
    p = (__import__("os").environ["IPM_ARTIFACT_ROOT"] + "/")+row['path']
    try: h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    except FileNotFoundError: h = None
    if h != row['sha256']: bad.append(row['path'])
print(json.dumps({'manifest_verified': not bad, 'mismatched': bad})); sys.exit(0 if not bad else 3)
PYEOF
}
SEEDCHECK=$OUT/seed_check; SEEDARG="--seed-dir=$SEEDCHECK"
for step in "$@"; do
  case $step in t0t1) S=g2_t0_t1.py; EXTRA="$SEEDARG";; t2) S=g2_t2.py; EXTRA="";; t3) S=g2_t3.py; EXTRA="$W $SEEDARG";; t26) S=g2_t26.py; EXTRA="$W";; t27h) S=g2_t27h.py; EXTRA="$W";; t27hx) S=g2_t27hx.py; EXTRA="$W";; supplement) S=g2_supplement.py; EXTRA="$W";; *) echo "unknown step $step"; exit 1;; esac
  V=$(verify 2>/dev/null | tail -1); VRC=$?
  echo "[$(date -u +%FT%TZ)] verify manifest before $step: $V" | tee -a $OUT/run.log
  echo "$V" | grep -q '"manifest_verified": true' || { echo "[$(date -u +%FT%TZ)] MANIFEST MISMATCH; stopping" | tee -a $OUT/run.log; exit 3; }
  echo "[$(date -u +%FT%TZ)] start $step (session $SUF)" | tee -a $OUT/run.log
  $PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label g2_$step -- $PY -B tests/$S $OUT/$step.json $M $EXTRA >> $OUT/run.log 2>&1
  GRC=$?
  R=$(ls -td $SESS/runs/*_g2_$step 2>/dev/null | head -1)
  VERDICT=$($PY -c "import json,sys; d=json.load(open('$R/result.json')); print(json.dumps({'success': d.get('success'), 'returncode': d.get('returncode'), 'stop_reasons': d.get('stop_reasons'), 'wall_s': round(d.get('wall_seconds',0))}))" 2>/dev/null || echo '{"success": null}')
  echo "[$(date -u +%FT%TZ)] end $step guard_exit=$GRC result=$VERDICT" | tee -a $OUT/run.log
  echo "$VERDICT" | grep -q '"success": true' || { echo "[$(date -u +%FT%TZ)] STEP $step DID NOT SUCCEED; chain stopped (no later step started)" | tee -a $OUT/run.log; exit 4; }
done
echo "[$(date -u +%FT%TZ)] STEPS DONE ($*)" | tee -a $OUT/run.log

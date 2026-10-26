#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G2 step runner, version 6 (new file; v5 kept frozen in g2_v6): adds step t27hfloor -> tests/g2_t27h_floor.py (lead 08:30Z). Version 5 text:
# G2 step runner, version 5 (new file; v4 kept frozen in g2_v5): adds step t27hx2 -> tests/g2_t27hx2.py (SPEC v9.9) and the SPEC v9.10 strict step verdict:
# the step JSON parses to an object, top-level passed is True (identity), checks is a nonempty list, every record is a dict with a unique string check name
# and passed is True (identity). Self-test: bin/runner_selftest_v5.py (the verifier's 31 fixtures). Version 4 text:
# G2 step runner, version 4 (new file; v3 kept frozen in g2_v4). Changes from v3 (SPEC v9.6 item 4): the step verdict additionally requires the step JSON's
# 'passed' field to be true and every record in its 'checks' list to have passed=true; new step t0t1v2 -> tests/g2_t0_t1_v2.py (v9.6 supplement).
# Version 3 text (fail closed; lead ruling 07:0xZ after c4-ver reviews/g2_runner_stale_result_20261024T0701.md):
# Usage: run_g2_steps_v3.sh <tag> <session-suffix> <workers> <policy.json> step1 [step2 ...]
# Rules: (1) any nonzero guard exit stops the chain; (2) exactly one new run directory with label g2_<step> must appear and its result.json
# command must equal the launched command; (3) a pre-existing step JSON is moved aside before the call and the new one must exist with an
# mtime inside [started_time, finished_time] of that run, exact interval, no slack (sha256 logged beside the run dir); (4) the session suffix must be new;
# (5) the manifest verification is gated on the verifier's own exit status. Verdicts come from result.json (success, returncode 0) only.
# Environment overrides exist only for the self-test (bin/runner_selftest.sh) and are logged: G2_GUARD (guard script), G2_OUTROOT (output root),
# G2_TESTDIR (directory holding the step scripts). A production launch sets none of them.
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; GUARD=${G2_GUARD:-$LANE/work/research/hardware/guard.py}
OUTROOT=${G2_OUTROOT:-$LANE/outputs/g2}; TESTDIR=${G2_TESTDIR:-$LANE/work/research860}
TAG=$1; SUF=$2; W=$3; POLICY=$4; shift 4; OUT=$OUTROOT/$TAG; mkdir -p $OUT; cd $TESTDIR || exit 1
M=$LANE/outputs/manifests/code_manifest_$TAG.json; [ -f $M ] || { echo "no manifest $M"; exit 1; }
SESS=$OUTROOT/session_${TAG}_$SUF
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a $OUT/run.log; }
[ -d $SESS ] && { log "session $SESS exists; a new suffix is required per launch (rule 4); stopping"; exit 2; }
log "runner v6 start tag=$TAG suffix=$SUF workers=$W policy=$POLICY steps=$* overrides: G2_GUARD=${G2_GUARD:-none} G2_OUTROOT=${G2_OUTROOT:-none} G2_TESTDIR=${G2_TESTDIR:-none}"
log "runner v6 cpu affinity: $(taskset -cp $$ 2>/dev/null | sed "s/.*: //") nproc_allowed=$(nproc)"
$PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $POLICY >> $OUT/run.log 2>&1 || { log "guard init failed"; exit 1; }
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
  case $step in t0t1) S=g2_t0_t1.py; EXTRA="$SEEDARG";; t2) S=g2_t2.py; EXTRA="";; t3) S=g2_t3.py; EXTRA="$W $SEEDARG";; t26) S=g2_t26.py; EXTRA="$W";; t27h) S=g2_t27h.py; EXTRA="$W";; t27hx) S=g2_t27hx.py; EXTRA="$W";; supplement) S=g2_supplement.py; EXTRA="$W";; t0t1v2) S=g2_t0_t1_v2.py; EXTRA="$SEEDARG";; t27hx2) S=g2_t27hx2.py; EXTRA="$W";; t27hfloor) S=g2_t27h_floor.py; EXTRA="$W";; selftest) S=selftest_step.py; EXTRA="";; *) log "unknown step $step"; exit 1;; esac
  V=$(verify > $OUT/.verify.$$ 2>&1; echo "rc=$?"); VRC=${V#rc=}; VOUT=$(tail -1 $OUT/.verify.$$); rm -f $OUT/.verify.$$
  log "verify manifest before $step: $VOUT (verify_exit=$VRC)"
  [ "$VRC" = 0 ] || { log "MANIFEST MISMATCH (verify exit $VRC); stopping"; exit 3; }
  if [ -e $OUT/$step.json ]; then STALE=$OUT/$step.json.stale_$(date +%s%N); mv $OUT/$step.json $STALE; log "pre-existing $step.json moved aside to $STALE (rule 3)"; fi
  BEFORE=$(ls -d $SESS/runs/*_g2_$step 2>/dev/null | sort | tr '\n' ' ')
  CMD=("$PY" -B tests/$S $OUT/$step.json $M $EXTRA)
  log "start $step (session $SUF): ${CMD[*]}"
  $PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label g2_$step -- "${CMD[@]}" >> $OUT/run.log 2>&1
  GRC=$?
  [ $GRC -eq 0 ] || { log "STEP $step: guard exit $GRC (nonzero); chain stopped (rule 1)"; exit 4; }
  AFTER=$(ls -d $SESS/runs/*_g2_$step 2>/dev/null | sort | tr '\n' ' ')
  NEW=$(comm -13 <(echo $BEFORE | tr ' ' '\n' | sed '/^$/d' | sort) <(echo $AFTER | tr ' ' '\n' | sed '/^$/d' | sort))
  NNEW=$(echo "$NEW" | sed '/^$/d' | wc -l)
  [ "$NNEW" = 1 ] || { log "STEP $step: expected exactly one new run dir, found $NNEW ($NEW); chain stopped (rule 2)"; exit 5; }
  R=$NEW
  VERDICT=$($PY - "$R" "$OUT/$step.json" "${CMD[@]}" <<'PYEOF'
import json, sys, os, hashlib
run, stepjson = sys.argv[1], sys.argv[2]; cmd = sys.argv[3:]
try: d = json.load(open(os.path.join(run, 'result.json')))
except Exception as e: print(json.dumps({'ok': False, 'why': 'no result.json: %s' % e})); sys.exit(0)
why = []
if d.get('success') is not True: why.append('success is not true')
if d.get('returncode') != 0: why.append('returncode %r' % d.get('returncode'))
if list(d.get('command') or []) != cmd: why.append('command differs: %r' % (d.get('command'),))
if d.get('stop_reasons'): why.append('stop_reasons %r' % d.get('stop_reasons'))
if not os.path.exists(stepjson): why.append('step json missing')
else:
    mt = os.path.getmtime(stepjson); st, ft = d.get('started_time'), d.get('finished_time')
    if not (st is not None and ft is not None and st <= mt <= ft): why.append('step json mtime %r outside [%r, %r]' % (mt, st, ft))   # exact interval (verifier 07:16Z): the guard records started_time before Popen and finished_time after the child exits
sha = hashlib.sha256(open(stepjson, 'rb').read()).hexdigest() if os.path.exists(stepjson) else None
passed = None; failing = []
if os.path.exists(stepjson):                                  # SPEC v9.10 strict step verdict
    try:
        sj = json.load(open(stepjson))
        if not isinstance(sj, dict): why.append('step json is not an object')
        else:
            passed = sj.get('passed')
            if passed is not True: why.append('step json passed is %r (identity True required)' % (passed,))
            checks = sj.get('checks')
            if not isinstance(checks, list) or not checks: why.append('step json checks is not a nonempty list')
            else:
                names = []
                for i, c in enumerate(checks):
                    if not isinstance(c, dict): why.append('check %d is not a dict' % i); continue
                    name = c.get('check')
                    if not isinstance(name, str) or not name: why.append('check %d has no string name' % i)
                    names.append(name)
                    if c.get('passed') is not True: failing.append(name if isinstance(name, str) else '#%d' % i)
                dup = sorted({str(n) for n in names if names.count(n) > 1})
                if dup: why.append('duplicate check names: %s' % dup)
                if failing: why.append('failing checks: %s' % failing)
    except Exception as e: why.append('step json unreadable: %s' % e)
sha = hashlib.sha256(open(stepjson, 'rb').read()).hexdigest() if os.path.exists(stepjson) else None
passed = None; failing = []
if os.path.exists(stepjson):
    try:
        sj = json.load(open(stepjson)); passed = sj.get('passed'); failing = [c.get('check') for c in sj.get('checks', []) if not c.get('passed')]
        if passed is not True: why.append('step json passed is %r' % (passed,))
        if failing: why.append('failing checks: %s' % failing)
        if 'checks' in sj and not sj['checks']: why.append('step json has an empty checks list')
    except Exception as e: why.append('step json unreadable: %s' % e)
rec = {'ok': not why, 'why': why, 'run_id': d.get('run_id'), 'wall_s': round(d.get('wall_seconds') or 0), 'step_json_sha256': sha, 'returncode': d.get('returncode'), 'success': d.get('success'), 'step_json_passed': passed, 'failing_checks': failing}
open(os.path.join(run, 'step_json_sha256.txt'), 'w').write('%s  %s\n' % (sha, stepjson))
print(json.dumps(rec))
PYEOF
)
  log "end $step guard_exit=$GRC run=$R verdict=$VERDICT"
  echo "$VERDICT" | grep -q '"ok": true' || { log "STEP $step DID NOT SUCCEED (fail closed); chain stopped"; exit 6; }
done
log "STEPS DONE ($*)"

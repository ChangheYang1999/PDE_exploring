#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# G3 step runner (new file, SPEC v9.10 item 3; lead pre-audit 10:07Z: the legacy verdict block that followed the strict block is removed; selftest/selftest2 are fixture-only steps): the fail-closed rules and strict step verdict of run_g2_steps_v5.sh with the G3 dispatch table:
# t4 -> tests/g3_t4.py <out> <manifest> <workers>; kappa -> tests/g2_kappa_v97.py <out> <manifest> <workers>; bench -> bench860.py <out> <manifest> <workers list from G3_BENCH_WORKERS, default '1 4 8 12'>.
# Output root outputs/g3/<tag>; sessions outputs/g3/session_<tag>_<suffix>. Inherited text of runner v5:
# the step JSON parses to an object, top-level passed is True (identity), checks is a nonempty list, every record is a dict with a unique string check name
# and passed is True (identity). Self-test: bin/runner_selftest_v5.py (the verifier's 31 fixtures plus 6 typed guard-record negatives, 37 cases). Version 4 text:
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
OUTROOT=${G2_OUTROOT:-$LANE/outputs/g3}; TESTDIR=${G2_TESTDIR:-$LANE/work/research860}
TAG=$1; SUF=$2; W=$3; POLICY=$4; shift 4; OUT=$OUTROOT/$TAG; mkdir -p $OUT; cd $TESTDIR || exit 1
M=$LANE/outputs/manifests/code_manifest_$TAG.json; [ -f $M ] || { echo "no manifest $M"; exit 1; }
SESS=$OUTROOT/session_${TAG}_$SUF
log() { echo "[$(date -u +%FT%TZ)] $*" | tee -a $OUT/run.log; }
[ -d $SESS ] && { log "session $SESS exists; a new suffix is required per launch (rule 4); stopping"; exit 2; }
log "G3 runner start tag=$TAG suffix=$SUF workers=$W policy=$POLICY steps=$* overrides: G2_GUARD=${G2_GUARD:-none} G2_OUTROOT=${G2_OUTROOT:-none} G2_TESTDIR=${G2_TESTDIR:-none}"
log "G3 runner cpu affinity: $(taskset -cp $$ 2>/dev/null | sed "s/.*: //") nproc_allowed=$(nproc)"
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
  case $step in t4) S=tests/g3_t4.py; EXTRA="$W";; kappa) S=tests/g2_kappa_v97.py; EXTRA="$W";; bench) S=bench860.py; EXTRA="${G3_BENCH_WORKERS:-1 4 8 12}";; selftest|selftest2) S=tests/selftest_step.py; EXTRA="";; *) log "unknown step $step"; exit 1;; esac
  V=$(verify > $OUT/.verify.$$ 2>&1; echo "rc=$?"); VRC=${V#rc=}; VOUT=$(tail -1 $OUT/.verify.$$); rm -f $OUT/.verify.$$
  log "verify manifest before $step: $VOUT (verify_exit=$VRC)"
  [ "$VRC" = 0 ] || { log "MANIFEST MISMATCH (verify exit $VRC); stopping"; exit 3; }
  if [ -e $OUT/$step.json ]; then STALE=$OUT/$step.json.stale_$(date +%s%N); mv $OUT/$step.json $STALE; log "pre-existing $step.json moved aside to $STALE (rule 3)"; fi
  BEFORE=$(ls -d $SESS/runs/*_g3_$step 2>/dev/null | sort | tr '\n' ' ')
  CMD=("$PY" -B $S $OUT/$step.json $M $EXTRA)
  log "start $step (session $SUF): ${CMD[*]}"
  $PY -B $GUARD run --session-dir $SESS --cwd $PWD --lock-file $SESS.lock --label g3_$step -- "${CMD[@]}" >> $OUT/run.log 2>&1
  GRC=$?
  [ $GRC -eq 0 ] || { log "STEP $step: guard exit $GRC (nonzero); chain stopped (rule 1)"; exit 4; }
  AFTER=$(ls -d $SESS/runs/*_g3_$step 2>/dev/null | sort | tr '\n' ' ')
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
rcv = d.get('returncode')
if not (isinstance(rcv, int) and not isinstance(rcv, bool) and rcv == 0): why.append('returncode %r is not the int 0' % (rcv,))          # ruling 9: typed
if list(d.get('command') or []) != cmd: why.append('command differs: %r' % (d.get('command'),))
if not isinstance(d.get('stop_reasons'), list) or d.get('stop_reasons'): why.append('stop_reasons %r is not an empty list' % (d.get('stop_reasons'),))
import math as _m
st_, ft_, ws_ = d.get('started_time'), d.get('finished_time'), d.get('wall_seconds')
if not all(isinstance(v, (int, float)) and not isinstance(v, bool) and _m.isfinite(float(v)) for v in (st_, ft_, ws_)) or not (st_ <= ft_) or ws_ < 0: why.append('timing fields not finite typed numbers with start <= finish and wall >= 0: %r %r %r' % (st_, ft_, ws_))
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
rec = {'ok': not why, 'why': why, 'run_id': d.get('run_id'), 'wall_s': round(d.get('wall_seconds') or 0), 'step_json_sha256': sha, 'returncode': d.get('returncode'), 'success': d.get('success'), 'step_json_passed': passed, 'failing_checks': failing}
open(os.path.join(run, 'step_json_sha256.txt'), 'w').write('%s  %s\n' % (sha, stepjson))
print(json.dumps(rec))
PYEOF
)
  log "end $step guard_exit=$GRC run=$R verdict=$VERDICT"
  echo "$VERDICT" | grep -q '"ok": true' || { log "STEP $step DID NOT SUCCEED (fail closed); chain stopped"; exit 6; }
done
log "STEPS DONE ($*)"

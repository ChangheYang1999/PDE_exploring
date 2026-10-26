#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Self-test of bin/run_g2_steps_v3.sh with a stub guard (lead rule 5). Scenarios: A) a real new success passes; B) a stale success in the
# session plus a guard refusal (exit 73, no new run dir) stops with nonzero exit; C) a pre-existing step JSON is moved aside. Writes under outputs/g2/runner_selftest.
set -u
LANE=$IPM_ARTIFACT_ROOT; ST=$LANE/outputs/g2/runner_selftest; rm -rf $ST/out; mkdir -p $ST/out
export G2_GUARD=$ST/stub_guard.py G2_OUTROOT=$ST/out G2_TESTDIR=$ST     # the runner does cd $G2_TESTDIR and runs tests/<script>: TESTDIR is the parent of tests/ (verifier 07:16Z)
TAG=selftest; echo '{"tag": "selftest", "files": [], "frozen_181_closure": [], "note": "empty manifest for bin/runner_selftest.sh only; verifies trivially"}' > $LANE/outputs/manifests/code_manifest_selftest.json
LOG=$ST/selftest.log; : > $LOG
echo "scenario A: new success" >> $LOG; bash $LANE/bin/run_g2_steps_v3.sh $TAG sA 1 none selftest >> $LOG 2>&1; A=$?; echo "A exit=$A (expect 0)" >> $LOG
echo "scenario B: stale success + refusal" >> $LOG; echo refuse > $ST/out/session_${TAG}_sA/MODE
# reuse the same session dir by copying it to a new suffix (the runner refuses an existing suffix, rule 4), so the stale run dir is present
cp -r $ST/out/session_${TAG}_sA $ST/out/session_${TAG}_sB_pre; mv $ST/out/session_${TAG}_sB_pre $ST/out/session_${TAG}_sB
bash $LANE/bin/run_g2_steps_v3.sh $TAG sB 1 none selftest >> $LOG 2>&1; B=$?; echo "B exit=$B (expect nonzero: existing session refused by rule 4)" >> $LOG
# B2: force the stale situation past rule 4: a fresh suffix whose session is created by init, then MODE=refuse and a stale run dir copied in
echo "scenario B2: fresh session, stale run dir injected, refusal" >> $LOG
python3 - "$ST" "$TAG" <<'PYEOF'
import os, shutil, sys, glob
st, tag = sys.argv[1], sys.argv[2]; src = glob.glob(os.path.join(st, 'out', 'session_%s_sA' % tag, 'runs', '*_g2_selftest'))[0]
dst_sess = os.path.join(st, 'out', 'session_%s_sC' % tag); os.makedirs(os.path.join(dst_sess, 'runs')); shutil.copytree(src, os.path.join(dst_sess, 'runs', os.path.basename(src))); open(os.path.join(dst_sess, 'MODE'), 'w').write('refuse')
PYEOF
# the runner refuses an existing session dir (rule 4), so the stale run dir cannot even be reached; record that outcome
bash $LANE/bin/run_g2_steps_v3.sh $TAG sC 1 none selftest >> $LOG 2>&1; C=$?; echo "C exit=$C (expect nonzero: rule 4 stops before any step)" >> $LOG
# B3: refusal inside a fresh session with a stale step JSON present: exercise rules 1 and 3 directly
echo "scenario D: fresh session, stale step json present, guard refuses" >> $LOG
mkdir -p $ST/out/$TAG; echo '{"stale": true}' > $ST/out/$TAG/selftest.json
cat > $ST/stub_guard_refuse_after_init.py <<'PYEOF2'
import sys, os, runpy
args = sys.argv[1:]
if args[0] == 'init': sys.argv = sys.argv; runpy.run_path(os.path.join(os.path.dirname(__file__), 'stub_guard.py'), run_name='__main__')
else: print('stub guard: refusing (hold)'); sys.exit(73)
PYEOF2
G2_GUARD=$ST/stub_guard_refuse_after_init.py bash $LANE/bin/run_g2_steps_v3.sh $TAG sD 1 none selftest >> $LOG 2>&1; D=$?; echo "D exit=$D (expect 4: nonzero guard exit stops; stale json moved aside)" >> $LOG
ls $ST/out/$TAG/ >> $LOG
echo "scenario E: stale step json present, real success (json replaced, sha logged)" >> $LOG
echo '{"stale": true}' > $ST/out/$TAG/selftest.json; bash $LANE/bin/run_g2_steps_v3.sh $TAG sE 1 none selftest >> $LOG 2>&1; E=$?; echo "E exit=$E (expect 0)" >> $LOG
# F: a pathological guard that exits 0 without creating a run dir (rule 2 must stop the chain, exit 5)
echo "scenario F: guard exits 0 but creates no run dir" >> $LOG
cat > $ST/stub_guard_silent_after_init.py <<'PYEOF3'
import sys, os, runpy
args = sys.argv[1:]
if args[0] == 'init': runpy.run_path(os.path.join(os.path.dirname(__file__), 'stub_guard.py'), run_name='__main__')
else: print('stub guard: silent exit 0 without a run dir'); sys.exit(0)
PYEOF3
G2_GUARD=$ST/stub_guard_silent_after_init.py bash $LANE/bin/run_g2_steps_v3.sh $TAG sF 1 none selftest >> $LOG 2>&1; F=$?; echo "F exit=$F (expect 5: no new run dir)" >> $LOG
# G: the verifier's scenario in one launch: init plants a stale successful run dir with the step label, then the guard refuses (exit 73): rule 1 stops (exit 4) and the stale success is never read
echo "scenario G: stale success planted at init, guard refuses at run" >> $LOG
cat > $ST/stub_guard_stale_then_refuse.py <<'PYEOF4'
import sys, os, runpy, glob, shutil, json, time
args = sys.argv[1:]; sess = args[args.index('--session-dir')+1]
if args[0] == 'init':
    runpy.run_path(os.path.join(os.path.dirname(__file__), 'stub_guard.py'), run_name='__main__')
    src = sorted(glob.glob(os.path.join(os.path.dirname(sess), 'session_selftest_sA', 'runs', '*_g2_selftest')))[0]
    shutil.copytree(src, os.path.join(sess, 'runs', os.path.basename(src)))
else: print('stub guard: refusing (hold) with a stale success present'); sys.exit(73)
PYEOF4
G2_GUARD=$ST/stub_guard_stale_then_refuse.py bash $LANE/bin/run_g2_steps_v3.sh $TAG sG 1 none selftest >> $LOG 2>&1; G=$?; echo "G exit=$G (expect 4: refusal stops although a stale success exists)" >> $LOG
grep -c "STEPS DONE" $ST/out/$TAG/run.log >> $LOG
echo "RESULT A=$A B=$B C=$C D=$D E=$E F=$F G=$G" >> $LOG; cat $LOG | grep -E "exit=|RESULT|moved aside|chain stopped|STEPS DONE"
if [ $A = 0 ] && [ $B != 0 ] && [ $C != 0 ] && [ $D = 4 ] && [ $E = 0 ] && [ $F = 5 ] && [ $G = 4 ]; then echo "SELFTEST PASS" | tee -a $LOG; exit 0; else echo "SELFTEST FAIL" | tee -a $LOG; exit 1; fi

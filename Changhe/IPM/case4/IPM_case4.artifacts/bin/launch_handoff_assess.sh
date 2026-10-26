#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# E3 option (A), lead decision 2026-10-25T15:40:37Z with the exact handoff-state rule of the lead note 2026-10-25T16:00:25Z and the corrections of the
# verifier's launcher audit (c4-ver/reviews/handoff_launcher_20261025T1604Z/AUDIT.md 703299de): ONE guarded standalone full assessment of the handoff state,
# launched no earlier than 2026-10-26T04:00:00Z and no later than 04:45:00Z.
# Handoff state: among the trial events with trial.accepted true, those with post_state.last_epoch < CUT AND event file mtime < CUT; the one with the greatest
# trial.event_sequence; its candidate is post_state.candidate_path (sha256 must equal post_state.candidate_sha256) with arrays post_state.arrays_path (sha256 must
# equal post_state.arrays_sha256). An event with one time before and one after the cut is excluded and the previous accepted event is used (both-times rule).
# Command exactly as E3_STANDALONE_ASSESSMENT_FEASIBILITY.md section 6: frozen assess860.py of manifest g4_v2 (full sha256 checked), 8 workers, cores 78-89,
# nice 19, setsid nohup, own guard session with outputs/dev_policy_assess8_psi60.json (lead 16:49:16Z: PSI full ceiling 60.0, all else as dev_policy_assess8), own lock (never
# $ROOT/worker.lock), output outside the run root, python -B. An event without post_state.last_epoch is not a candidate (no fallback to the file time).
# Once only: an exclusive mkdir of outputs/handoff_assess/LAUNCH_CLAIM is the atomic claim; the window (04:00:00.000Z <= now < 04:45:00.000Z, exact sub-second
# comparison) is checked first and re-checked immediately before the exec; the guard session must be fresh (refusal if it or its lock exists), is always
# initialized with the approved policy, and the stored policy.json is compared with the requested policy by dictionary equality after Policy normalization,
# with session.json policy_sha256 compared to the digest of the stored policy.json (lead 17:00:06Z (a), (b)).
# Usage: launch_handoff_assess.sh                       real mode: fixed cut and window, no overrides accepted
#        launch_handoff_assess.sh --dry-run [--cut-epoch E] [--window-start E --window-end E]   prints the selection and the command; creates and launches nothing
set -u
LANE=$IPM_ARTIFACT_ROOT; PY=$LANE/env/bin/python; ROOT=$LANE/outputs/campaign860/pilot_g4_v2
MANIFEST=$LANE/outputs/manifests/code_manifest_g4_v2.json; MANIFEST_SHA=dacb203633d450ac9af62393244f88aa8aba7a8cc9416afbd1c2e84efb723037
GUARD=$LANE/work/research/hardware/guard.py; ASSESS=$LANE/work/research860/assess860.py
POLICY=$LANE/outputs/dev_policy_assess8_psi60.json; POLICY_SHA=9ba18a6f4e88da4fcfd490c642c48a36aad592766da7e3da2796554c0338801e   # lead 16:49:16Z item 3: copy of dev_policy_assess8.json with only max_memory_psi_full_avg10 5.0 -> 60.0
CUT=1792987200; WSTART=1792987200; WEND=1792989900          # 2026-10-26T04:00:00.000Z <= now < 04:45:00.000Z (lead 17:00:06Z (b)); LAST_CHECK holds the precise time of the last window check
LAST_CHECK=""
CLAIM=$LANE/outputs/handoff_assess/LAUNCH_CLAIM
DRY=0; OVERRIDE=0
while [ $# -gt 0 ]; do case "$1" in --dry-run) DRY=1;; --cut-epoch) CUT=$2; OVERRIDE=1; shift;; --window-start) WSTART=$2; OVERRIDE=1; shift;; --window-end) WEND=$2; OVERRIDE=1; shift;; *) echo "unknown argument $1"; exit 2;; esac; shift; done
[ $DRY = 0 ] && [ $OVERRIDE = 1 ] && { echo "REFUSED: window or cut overrides are accepted only with --dry-run"; exit 2; }
in_window() { LAST_CHECK=$(date -u +%s.%N); $PY -c "from fractions import Fraction as F; import sys; n=F(sys.argv[1]); sys.exit(0 if F(sys.argv[2]) <= n < F(sys.argv[3]) else 1)" "$LAST_CHECK" "$WSTART" "$WEND"; }   # exact: WSTART <= now < WEND, sub-second
if [ $DRY = 0 ]; then
  in_window || { echo "REFUSED: now $LAST_CHECK ($(date -u +%FT%TZ)) is outside the window [$(date -u -d @$WSTART +%FT%TZ), $(date -u -d @$WEND +%FT%TZ)); do not launch (option C wording if after the window)"; exit 3; }
  FIRST_CHECK=$LAST_CHECK
  [ -e $CLAIM ] && { echo "REFUSED: $CLAIM exists (once only; a launch was already claimed)"; exit 3; }
  ls $LANE/outputs/handoff_assess/*/LAUNCH.md >/dev/null 2>&1 && { echo "REFUSED: a LAUNCH.md already exists under outputs/handoff_assess (once only)"; exit 3; }
fi
ACTUAL_MANIFEST_SHA=$(sha256sum $MANIFEST | cut -d' ' -f1)
[ "$ACTUAL_MANIFEST_SHA" = "$MANIFEST_SHA" ] || { echo "REFUSED: manifest sha256 $ACTUAL_MANIFEST_SHA differs from $MANIFEST_SHA"; exit 3; }
[ -f $ASSESS ] && [ -f $POLICY ] && [ -f $GUARD ] || { echo "REFUSED: assess860.py, policy or guard missing"; exit 3; }
[ "$(sha256sum $POLICY | cut -d' ' -f1)" = "$POLICY_SHA" ] || { echo "REFUSED: policy sha256 differs from $POLICY_SHA"; exit 3; }
# candidate selection (lead rule 16:00:25Z); prints: event_file event_sequence trial accepted last_epoch mtime candidate_path candidate_sha arrays_path arrays_sha
SEL=$($PY -B - "$ROOT" "$CUT" <<'PYEOF'
import json, os, sys, glob
root, cut = sys.argv[1], float(sys.argv[2]); best = None
for p in sorted(glob.glob(os.path.join(root, 'commits', 'event_*.json'))):
    mt = os.path.getmtime(p); e = json.load(open(p)); t = e.get('trial') or {}; ps = e.get('post_state') or {}
    if t.get('kind') is not None or not t.get('accepted') or 'accepted_after' not in t: continue
    le = ps.get('last_epoch')
    if le is None: continue
    if le < cut and mt < cut and (best is None or t['event_sequence'] > best[1]):
        best = (os.path.basename(p), t['event_sequence'], t['trial'], ps.get('accepted', t['accepted_after']), le, mt, ps.get('candidate_path'), ps.get('candidate_sha256'), ps.get('arrays_path'), ps.get('arrays_sha256'))
print(*best) if best else print('none')
PYEOF
)
[ "$SEL" = none ] && { echo "REFUSED: no accepted commit with both times before the cut"; exit 4; }
read EVF EVSEQ TRIAL IDX LE MT CJ CSHA CN NSHA <<< "$SEL"
[ -f "$CJ" ] && [ -f "$CN" ] || { echo "REFUSED: candidate files missing: $CJ $CN"; exit 4; }
SJ=$(sha256sum $CJ | cut -d' ' -f1); SN=$(sha256sum $CN | cut -d' ' -f1)
[ "$SJ" = "$CSHA" ] || { echo "REFUSED: candidate json sha256 $SJ differs from post_state.candidate_sha256 $CSHA"; exit 4; }
[ "$SN" = "$NSHA" ] || { echo "REFUSED: arrays sha256 $SN differs from post_state.arrays_sha256 $NSHA"; exit 4; }
case "$CJ" in $ROOT/snapshots/accepted_*.json) ;; *) echo "REFUSED: candidate path $CJ is not a snapshot of the root"; exit 4;; esac
UTC=$(date -u +%Y%m%dT%H%M%SZ); OUT=$LANE/outputs/handoff_assess/${UTC}_state$IDX; SESS=$LANE/outputs/dev_sessions/$(date -u +%Y%m%d)_handoff_assess
CMD="cd $LANE/work/research860 && taskset -c 78-89 nice -n 19 setsid nohup $PY -B $GUARD run --session-dir $SESS --cwd $LANE/work/research860 --lock-file $SESS.lock --label handoff_assess_state$IDX -- $PY -B $ASSESS $OUT/assessment_state$IDX.json $MANIFEST $CJ 8 > $OUT/launch.log 2>&1 < /dev/null &"
echo "handoff state: event file $EVF, event_sequence $EVSEQ, trial $TRIAL, accepted index $IDX; post_state.last_epoch $LE ($(date -u -d @${LE%.*} +%FT%TZ)); event file mtime $MT ($(date -u -d @${MT%.*} +%FT%TZ)); cut $CUT ($(date -u -d @$CUT +%FT%TZ)); both times before the cut"
echo "candidate $CJ sha256 $SJ (= post_state.candidate_sha256)"; echo "arrays    $CN sha256 $SN (= post_state.arrays_sha256)"; echo "manifest $MANIFEST sha256 $ACTUAL_MANIFEST_SHA"
echo "output dir $OUT"; echo "command: $CMD"
[ $DRY = 1 ] && { echo "DRY RUN: nothing created, nothing launched"; exit 0; }
mkdir -p $LANE/outputs/handoff_assess
mkdir $CLAIM 2>/dev/null || { echo "REFUSED: could not claim $CLAIM (already exists): once only"; exit 3; }    # atomic once-only claim
echo "claimed $(date -u +%FT%T.%NZ) by pid $$ for state $IDX" > $CLAIM/claim.txt
mkdir $OUT || { echo "REFUSED: output dir exists"; exit 3; }
touch $OUT/BEFORE; BT=$(date -u +%FT%T.%NZ)
[ -e $SESS ] || [ -e $SESS.lock ] && { echo "REFUSED: guard session $SESS or its lock already exists; a fresh session is required (lead 17:00:06Z (a)); nothing launched"; exit 3; }
$PY -B $GUARD init --session-dir $SESS --disk-path $LANE/outputs --policy $POLICY > $OUT/guard_init.log 2>&1 || { echo "guard init failed (see $OUT/guard_init.log); nothing launched"; exit 5; }
POLCHECK=$($PY -B - "$LANE" "$SESS" "$POLICY" <<'PYEOF'
import sys, json, hashlib
from pathlib import Path
lane, sess, pol = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, lane + '/work/research/hardware')
from policy import Policy
requested = Policy.from_dict(json.loads(pol.read_text())).to_dict()
stored = json.loads((sess / 'policy.json').read_text())
stored_digest = hashlib.sha256((sess / 'policy.json').read_bytes()).hexdigest()
session = json.loads((sess / 'session.json').read_text())
equal = (requested == stored); digest_ok = (session.get('policy_sha256') == stored_digest)
print('%s %s %s %s %s' % ('OK' if (equal and digest_ok) else 'MISMATCH', hashlib.sha256(pol.read_bytes()).hexdigest(), stored_digest, session.get('policy_sha256'), 'dict_equal=%s session_digest_equal=%s' % (equal, digest_ok)))
PYEOF
)
read POLVERDICT POLREQ_SHA POLSTORED_SHA POLSESSION_SHA POLDETAIL <<< "$POLCHECK"
[ "$POLVERDICT" = OK ] || { echo "REFUSED: stored session policy differs from the requested policy ($POLCHECK); nothing launched"; echo "policy_check: $POLCHECK" >> $OUT/LAUNCH.md 2>/dev/null; exit 3; }
{
echo "# LAUNCH.md: standalone full assessment of the handoff state (E3 option A; lead decisions 2026-10-25T15:40:37Z and 16:00:25Z)"
echo "written_utc: $(date -u +%FT%TZ)"; echo "data_cut_epoch: $CUT ($(date -u -d @$CUT +%FT%TZ)); window: $(date -u -d @$WSTART +%FT%TZ) to $(date -u -d @$WEND +%FT%TZ)"
echo "handoff_rule: accepted trial events with post_state.last_epoch < cut AND event file mtime < cut; greatest trial.event_sequence; candidate = post_state.candidate_path, arrays = post_state.arrays_path, hashes recomputed and compared"
echo "event_file: $EVF"; echo "event_sequence: $EVSEQ"; echo "trial: $TRIAL"; echo "accepted_index: $IDX"
echo "post_state.last_epoch: $LE ($(date -u -d @${LE%.*} +%FT%TZ))"; echo "event_file_mtime: $MT ($(date -u -d @${MT%.*} +%FT%TZ))"
echo "candidate_json: $CJ"; echo "candidate_json_sha256: $SJ (equals post_state.candidate_sha256)"; echo "candidate_npz: $CN"; echo "candidate_npz_sha256: $SN (equals post_state.arrays_sha256)"
echo "manifest: $MANIFEST sha256 $ACTUAL_MANIFEST_SHA"; echo "assess860_sha256: $(sha256sum $ASSESS | cut -d' ' -f1)"; echo "guard_sha256: $(sha256sum $GUARD | cut -d' ' -f1)"
echo "policy: $POLICY sha256 $(sha256sum $POLICY | cut -d' ' -f1) (expected $POLICY_SHA; max_memory_psi_full_avg10 60.0, lead 16:49:16Z)"; echo "BEFORE_marker: $OUT/BEFORE created $BT"; echo "claim: $CLAIM/claim.txt ($(cat $CLAIM/claim.txt))"
echo "guard_session: $SESS (lock $SESS.lock), freshly initialized"; echo "policy_check: $POLVERDICT requested_file_sha256 $POLREQ_SHA stored_policy_json_sha256 $POLSTORED_SHA session_policy_sha256 $POLSESSION_SHA $POLDETAIL"; echo "first_window_check: $FIRST_CHECK (epoch, exact comparison $WSTART <= now < $WEND)"; echo "command: $CMD"
} > $OUT/LAUNCH.md
BEFORE_RUNS=$(ls -d $SESS/runs/*_handoff_assess_state$IDX 2>/dev/null | tr '\n' ' ')
in_window || { echo "REFUSED at the last check: now $LAST_CHECK ($(date -u +%FT%TZ)) is outside the window; nothing launched" | tee -a $OUT/LAUNCH.md; exit 3; }   # window re-check immediately before the exec (exact, sub-second)
echo "last_window_check: $LAST_CHECK ($(date -u -d @${LAST_CHECK%.*} +%FT%TZ) plus the fraction)" >> $OUT/LAUNCH.md
echo "exec_utc: $(date -u +%FT%T.%NZ) (epoch $(date -u +%s.%N))" >> $OUT/LAUNCH.md
eval "$CMD"; GPID=$!
sleep 25
RUNDIR=$(comm -13 <(echo $BEFORE_RUNS | tr ' ' '\n' | sed '/^$/d' | sort) <(ls -d $SESS/runs/*_handoff_assess_state$IDX 2>/dev/null | sort) | tail -1)
APID=$(pgrep -f "assess860.py $OUT/assessment_state$IDX.json" | head -1)
{ echo "guard_pid: $GPID (ps: $(ps -o pid=,ppid=,pgid=,sid=,ni=,args= -p $GPID 2>/dev/null | cut -c1-160))"; echo "assess860_pid: ${APID:-not yet} ; children: $(pgrep -P ${APID:-0} | tr '\n' ' ')"; echo "guard_run_dir: ${RUNDIR:-not yet}"; echo "affinity: $(taskset -cp ${APID:-$GPID} 2>/dev/null | cut -d: -f2)"; } >> $OUT/LAUNCH.md
cat $OUT/LAUNCH.md

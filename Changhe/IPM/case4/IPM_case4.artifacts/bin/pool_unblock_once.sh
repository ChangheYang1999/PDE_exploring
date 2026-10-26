#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# One targeted unblock of the campaign driver's fork-pool exit deadlock, under the lead's ruling 2026-10-25T00:53:32Z (option A, standing authority):
# verifies the four conditions, and only if ALL hold sends SIGKILL to the idle pool child ONLY; writes a numbered intervention record under
# outputs/diag/interventions/. Never signals the worker, the guard or the supervisor. Usage: bin/pool_unblock_once.sh <worker-pid> [root]
set -u
W=$1; ROOT=${2:-$IPM_ARTIFACT_ROOT/outputs/campaign860/pilot_g4_v1}; LANE=$IPM_ARTIFACT_ROOT
PYSPY=$HOME/.local/bin/py-spy; DIR=$LANE/outputs/diag/interventions; mkdir -p $DIR
N=$(printf %04d $(( $(ls $DIR/intervention_*.json 2>/dev/null | wc -l) + 1 ))); T0=$(date -u +%FT%TZ)
[ -d /proc/$W ] || { echo "worker $W not found"; exit 2; }
WCHW=$(cat /proc/$W/wchan); PS=$(timeout 60 $PYSPY dump --pid $W 2>&1); printf "%s\n" "$PS" > $DIR/intervention_${N}_parent_stack.txt; c1=$(echo "$PS" | grep -c "_terminate_pool (multiprocessing/pool.py"); c1b=$(echo "$PS" | grep -c "join (multiprocessing/process.py")
K=""; nonz=0; SIBS=""; for q in $(pgrep -P $W); do st=$(awk '{print $3}' /proc/$q/stat 2>/dev/null); SIBS="$SIBS $q:$st"; if [ "$st" != "Z" ]; then if [ -z "$K" ]; then K=$q; else nonz=$((nonz+1)); fi; fi; done
[ -z "$K" ] && { echo "no live pool child; nothing to do (siblings:$SIBS)"; exit 3; }
KS=$(timeout 60 $PYSPY dump --pid $K 2>&1); printf "%s\n" "$KS" > $DIR/intervention_${N}_child_stack.txt; c2=$(echo "$KS" | grep -c "__enter__ (multiprocessing/synchronize.py"); c2b=$(echo "$KS" | grep -c "worker (multiprocessing/pool.py"); PPIDK=$(ps -o ppid= -p $K | tr -d ' '); WCHK=$(cat /proc/$K/wchan)
# identity-bound window and signal (lead condition 2026-10-25 about 01:05Z, verifier 01:00:29Z/01:03:23Z): one Python process opens a pidfd on the
# target at first observation, records the child's starttime (field 22) and PPID and the parent's starttime, waits 6 s for the zero-CPU test,
# re-reads all three identity fields, and sends SIGKILL ONLY through the pidfd (a reused PID can never be hit); any identity change = no signal.
IDENT=$(python3 - "$W" "$K" "$c1" "$c1b" "$WCHW" "$c2" "$c2b" "$nonz" <<'PY'
import os, sys, time, json, signal
W, K = int(sys.argv[1]), int(sys.argv[2]); c1, c1b, WCHW, c2, c2b, nonz = sys.argv[3:9]
def stat(pid):
    with open('/proc/%d/stat' % pid) as f: t = f.read()
    rest = t[t.rindex(')')+2:].split(); return {'ppid': int(rest[1]), 'starttime': int(rest[19]), 'ticks': int(rest[11])+int(rest[12])}
out = {'pidfd_opened': False, 'signal_sent': False, 'reason': None}
try:
    fd = os.pidfd_open(K); out['pidfd_opened'] = True
    k0 = stat(K); w0 = stat(W); out.update(child_ppid_first=k0['ppid'], child_starttime_first=k0['starttime'], parent_starttime_first=w0['starttime'], ticks_before=k0['ticks'])
    time.sleep(6)
    k1 = stat(K); w1 = stat(W); out.update(child_ppid_last=k1['ppid'], child_starttime_last=k1['starttime'], parent_starttime_last=w1['starttime'], ticks_after=k1['ticks'])
    ident = k0['ppid'] == W == k1['ppid'] and k0['starttime'] == k1['starttime'] and w0['starttime'] == w1['starttime']
    stacks = int(c1) >= 1 and int(c1b) >= 1 and WCHW == 'do_wait' and int(c2) >= 1 and int(c2b) >= 1
    zero_cpu = k0['ticks'] == k1['ticks']; others = int(nonz) == 0
    out.update(identity_unchanged=ident, stack_conditions=stacks, zero_cpu_6s=zero_cpu, every_other_worker_exited=others)
    if ident and stacks and zero_cpu and others:
        signal.pidfd_send_signal(fd, signal.SIGKILL); out['signal_sent'] = True; out['signal_sent_utc'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime()) + '.%03dZ' % int((time.time() % 1)*1000)
    else: out['reason'] = 'conditions not all met: identity %s stacks %s zero_cpu %s others_exited %s' % (ident, stacks, zero_cpu, others)
except Exception as exc: out['reason'] = 'exception %s: %s' % (type(exc).__name__, exc)
print(json.dumps(out))
PY
)
echo "identity/signal record: $IDENT"
a=$(echo "$IDENT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('ticks_before',''))"); b=$(echo "$IDENT" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('ticks_after',''))")
if echo "$IDENT" | grep -q '"signal_sent": true'; then ok=1; TK=$(echo "$IDENT" | python3 -c "import json,sys; print(json.load(sys.stdin)['signal_sent_utc'])"); RC=0; echo "intervention $N pre $T0: (i) terminate_pool=$c1 join=$c1b wchan=$WCHW; (ii) child $K ppid=$PPIDK semlock=$c2 worker=$c2b wchan=$WCHK; (iii) ticks $a->$b over 6 s; (iv) siblings$SIBS others_nonzombie=$nonz => all_hold=1; SIGKILL via pidfd at $TK"; else ok=0; TK=none; RC=-1; echo "intervention $N pre $T0: NO SIGNAL ($IDENT)"; fi
printf "%s\n" "$IDENT" > $DIR/intervention_${N}_identity.json
sleep 4; POSTW=$(cat /proc/$W/wchan 2>/dev/null); POSTK=$([ -d /proc/$K ] && echo alive || echo gone)
python3 - "$DIR/intervention_${N}_$(echo $T0 | tr -d ':-').json" "$N" "$W" "$K" "$T0" "$TK" "$RC" "$c1" "$c1b" "$WCHW" "$PPIDK" "$c2" "$c2b" "$WCHK" "$a" "$b" "$SIBS" "$nonz" "$ok" "$POSTW" "$POSTK" "$ROOT" <<'PY'
import json, sys, time, os  # stacks are in files, never embedded (lead 00:59Z (b))
(p,N,W,K,T0,TK,RC,c1,c1b,WCHW,PPIDK,c2,c2b,WCHK,a,b,SIBS,nonz,ok,POSTW,POSTK,ROOT) = sys.argv[1:23]
hb = None
try: hb = json.load(open(os.path.join(ROOT, 'HEARTBEAT.json')))
except Exception: pass
rec = {'intervention': int(N), 'ruling': 'lead 2026-10-25T00:53:32Z option A, standing authority (c4-lead/NOTES_FOR_TEAM.md)', 'root': ROOT, 'worker_pid': int(W), 'target_pool_child_pid': int(K), 'pre_snapshot_utc': T0,
       'conditions': {'i_parent_in_terminate_pool_join': {'py_spy_terminate_pool_frames': int(c1), 'py_spy_join_frames': int(c1b), 'wchan': WCHW},
                      'ii_target_is_pool_child_blocked_in_semlock': {'ppid': int(PPIDK), 'py_spy_semlock_enter_frames': int(c2), 'py_spy_pool_worker_frames': int(c2b), 'wchan': WCHK},
                      'iii_zero_cpu_over_6s': {'ticks_before': int(a), 'ticks_after': int(b)}, 'iv_every_other_pool_worker_exited': {'children_states': SIBS.split(), 'non_zombie_others': int(nonz)}, 'all_hold': ok == '1'},
       'signal': 'SIGKILL to the idle pool child only' if ok == '1' else 'NONE (conditions not all met)', 'signal_sent_utc': TK, 'kill_rc': int(RC), 'post': {'utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'worker_wchan': POSTW, 'target': POSTK, 'heartbeat': hb},
       'not_signalled': ['the worker', 'the guard', 'the supervisor'], 'tool': 'bin/pool_unblock_once.sh'}
rec['stack_files'] = [p.replace('.json', '')[:p.replace('.json','').rfind('_')] + '_parent_stack.txt', p.replace('.json', '')[:p.replace('.json','').rfind('_')] + '_child_stack.txt']
json.dump(rec, open(p, 'w'), indent=1); json.load(open(p)); print('record', p)
PY
RCW=$?; [ "$RCW" = "0" ] && echo "record write ok (rc 0)" || echo "RECORD WRITE FAILED rc $RCW"

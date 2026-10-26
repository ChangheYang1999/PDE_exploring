#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# Restart test helper for the G4 pilot (lead checklist B8; SPEC 16), version 2 (2026-10-25T03:3xZ, after the lead's HOLD 03:23Z).
# Sends ONE signal to the campaign860 WORKER of a campaign root and records the facts the lead's reader cannot see, then polls until the
# supervisor has restarted the worker and records the first commits after the restart. No STOP file is written. Record under
# outputs/campaign860/pilot_signal_tests/ (never inside the campaign root).
# Worker selection (v2): the worker is the process whose argv[2] (after python -B) ends with research860/campaign860.py, whose argv contains
# "--root <ROOT>", whose PPID is the live guard of the current slice (argv[2] ends with hardware/guard.py, argv[3] == run, argv contains
# "--session-dir <ROOT>/guard_session"), and whose PID equals the pid in <ROOT>/HEARTBEAT.json. Forked pool children (same argv, PPID = worker)
# and the guard (argv contains the worker command after "--") are therefore excluded. If the three do not agree, NOTHING is sent (exit 3).
# Usage: bin/pilot_signal_test.sh <campaign-root> TERM|KILL [wait-for-phase-regex] [max-wait-s]      (DRYRUN=1 prints the selection and exits)
set -u
ROOT=$1; SIG=$2; PHASE_RE=${3:-}; MAXW=${4:-900}
LANE=$IPM_ARTIFACT_ROOT; OUT=$LANE/outputs/campaign860/pilot_signal_tests; mkdir -p $OUT
stamp() { date -u +%FT%T.%3NZ; }
REC=$OUT/signal_${SIG}_$(date -u +%Y%m%dT%H%M%SZ).json
# select: prints "guard_pid guard_ppid worker_pid worker_ppid heartbeat_pid agree" (agree = 1 only if exactly one guard, exactly one worker, worker ppid == guard pid, worker pid == heartbeat pid)
select_family() { python3 - "$ROOT" <<'PY'
import os, sys, json
root = sys.argv[1]; guards = []; workers = []
for p in os.listdir('/proc'):
    if not p.isdigit(): continue
    try:
        argv = open('/proc/%s/cmdline' % p, 'rb').read().split(b'\0')[:-1]; argv = [a.decode(errors='replace') for a in argv]
        ppid = int(open('/proc/%s/stat' % p).read().rsplit(')', 1)[1].split()[1])
    except Exception: continue
    if len(argv) < 4: continue
    if argv[2].endswith('hardware/guard.py') and argv[3] == 'run' and '--session-dir' in argv and argv[argv.index('--session-dir')+1] == root + '/guard_session': guards.append((int(p), ppid))
    if argv[2].endswith('research860/campaign860.py') and '--root' in argv and argv[argv.index('--root')+1] == root: workers.append((int(p), ppid))
gp = guards[0][0] if len(guards) == 1 else None
w = [x for x in workers if gp is not None and x[1] == gp]
try: hb = json.load(open(root + '/HEARTBEAT.json')).get('pid')
except Exception: hb = None
agree = 1 if (len(guards) == 1 and len(w) == 1 and w[0][0] == hb) else 0
print(guards[0][0] if len(guards) == 1 else -1, guards[0][1] if len(guards) == 1 else -1, w[0][0] if len(w) == 1 else -1, w[0][1] if len(w) == 1 else -1, hb if hb is not None else -1, agree, len(guards), len(workers))
PY
}
family_listing() { python3 - "$ROOT" <<'PY'
import os, sys
root = sys.argv[1]; rows = []
for p in os.listdir('/proc'):
    if not p.isdigit(): continue
    try:
        argv = open('/proc/%s/cmdline' % p, 'rb').read().replace(b'\0', b' ').decode(errors='replace')
        st = open('/proc/%s/stat' % p).read().rsplit(')', 1)[1].split(); ppid = int(st[1]); state = st[0]
    except Exception: continue
    if root in argv and 'shell-snapshots' not in argv and 'pilot_signal_test' not in argv: rows.append({'pid': int(p), 'ppid': ppid, 'state': state, 'argv': argv[:140]})
print(__import__('json').dumps(rows))
PY
}
last_event() { ls $ROOT/commits/event_*.json 2>/dev/null | sort | tail -1 | xargs -r basename; }
t_start=$(stamp)
read GPID GPPID PID WPPID HBPID AGREE NG NW <<< "$(select_family)"
echo "$(stamp) selection: guard $GPID (ppid $GPPID) worker $PID (ppid $WPPID) heartbeat pid $HBPID agree=$AGREE guards=$NG campaign-argv-matches=$NW"
if [ -n "${DRYRUN:-}" ]; then echo "DRYRUN: no signal sent"; exit 0; fi
if [ -n "$PHASE_RE" ]; then
  echo "$(stamp) waiting for heartbeat phase matching '$PHASE_RE' (max ${MAXW}s)"; w=0
  while [ $w -lt $MAXW ]; do ph=$(python3 -c "import json; print(json.load(open('$ROOT/HEARTBEAT.json')).get('phase',''))" 2>/dev/null); [[ "$ph" =~ $PHASE_RE ]] && break; sleep 3; w=$((w+3)); done
  [[ "$ph" =~ $PHASE_RE ]] || { echo "$(stamp) phase '$ph' never matched '$PHASE_RE' within ${MAXW}s; NO signal sent"; exit 4; }
fi
# re-select immediately before sending; refuse on any disagreement or change
read GPID2 GPPID2 PID2 WPPID2 HBPID2 AGREE2 NG2 NW2 <<< "$(select_family)"
if [ "$AGREE2" != "1" ] || [ "$PID2" != "$PID" ] || [ "$GPID2" != "$GPID" ]; then echo "$(stamp) REFUSE: selection changed or disagrees (guard $GPID2 worker $PID2 heartbeat $HBPID2 agree $AGREE2); NO signal sent"; exit 3; fi
HB_BEFORE=$(cat $ROOT/HEARTBEAT.json 2>/dev/null | tr -d '\n'); EV_BEFORE=$(last_event); GUARD_RUNS_BEFORE=$(ls -d $ROOT/guard_session*/runs/* 2>/dev/null | wc -l)
PS_BEFORE=$(ps -o pid,ppid,etimes,args -p $PID --no-headers | cut -c1-200); FAM_BEFORE=$(family_listing)
kill -$SIG $PID; RC=$?; T_SEND=$(stamp); T_SEND_EPOCH=$(date +%s.%N)
echo "$T_SEND sent SIG$SIG to worker $PID (kill rc $RC); guard $GPID untouched; last event before: $EV_BEFORE"
# wait for the worker to be gone, record the family at that moment (orphans), then wait for a NEW guard+worker pair (supervisor restart with backoff)
w=0; while kill -0 $PID 2>/dev/null && [ $w -lt 900 ]; do sleep 2; w=$((w+2)); done; T_GONE=$(stamp); sleep 3; FAM_AFTER_GONE=$(family_listing)
w=0; NEWPID=""; NEWG=""; while [ $w -lt $MAXW ]; do read ng ngp nw nwp nhb na x y <<< "$(select_family)"; if [ "$na" = "1" ] && [ "$nw" != "$PID" ]; then NEWPID=$nw; NEWG=$ng; break; fi; sleep 5; w=$((w+5)); done; T_NEW=$(stamp)
sleep 20; EV_AFTER=$(last_event); GUARD_RUNS_AFTER=$(ls -d $ROOT/guard_session*/runs/* 2>/dev/null | wc -l); FAM_FINAL=$(family_listing)
NEW_EVENTS=$(ls $ROOT/commits/event_*.json 2>/dev/null | sort | awk -v b="$ROOT/commits/$EV_BEFORE" '$0 > b' | xargs -r -n1 basename | tr '\n' ' ')
python3 - "$REC" <<PY
import json, sys, os
rec = {'schema': 'pilot_signal_test_v2', 'root': '$ROOT', 'signal': 'SIG$SIG', 'phase_wait_regex': '$PHASE_RE', 'started_utc': '$t_start',
       'selection': {'guard_pid': $GPID, 'guard_ppid': $GPPID, 'worker_pid': $PID, 'worker_ppid': $WPPID, 'heartbeat_pid': $HBPID, 'agree': $AGREE2, 'rule': 'worker argv[2] endswith research860/campaign860.py with --root ROOT, PPID == the single live guard (argv guard.py run --session-dir ROOT/guard_session), PID == HEARTBEAT.json pid; re-checked immediately before the signal'},
       'ps_before': '''$PS_BEFORE''', 'heartbeat_before': json.loads('''$HB_BEFORE''' or 'null'), 'family_before': json.loads('''$FAM_BEFORE'''),
       'last_event_before': '$EV_BEFORE', 'guard_runs_before': $GUARD_RUNS_BEFORE, 'sent_utc': '$T_SEND', 'sent_epoch': $T_SEND_EPOCH, 'kill_rc': $RC,
       'worker_gone_utc': '$T_GONE', 'family_after_worker_gone': json.loads('''$FAM_AFTER_GONE'''),
       'new_worker_pid': int('$NEWPID') if '$NEWPID' else None, 'new_guard_pid': int('$NEWG') if '$NEWG' else None, 'new_worker_seen_utc': '$T_NEW',
       'last_event_after_20s': '$EV_AFTER', 'guard_runs_after': $GUARD_RUNS_AFTER, 'new_events': '$NEW_EVENTS'.split(), 'family_final': json.loads('''$FAM_FINAL'''),
       'supervisor_log_tail': open('$ROOT/supervisor.log').read().splitlines()[-10:] if os.path.exists('$ROOT/supervisor.log') else None,
       'note': 'B8 restart test record v2 (numerics); the lead reader checks replay, orphan and intent from the commits; no STOP file was written; family listings are every process whose argv contains the root (tool shells excluded) with PPID and state'}
json.dump(rec, open(sys.argv[1], 'w'), indent=1); print('record', sys.argv[1]); print(json.dumps({k: rec[k] for k in ('selection', 'sent_utc', 'worker_gone_utc', 'new_worker_pid', 'new_guard_pid', 'new_worker_seen_utc', 'last_event_before', 'new_events')}))
print('orphans after worker gone (pid, ppid, state):', [(r['pid'], r['ppid'], r['state']) for r in rec['family_after_worker_gone']])
PY

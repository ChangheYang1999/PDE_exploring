#!/bin/bash
# Resolve the working layout relative to this script, without a campaign-host path.
IPM_ARTIFACT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)"
while [ ! -d "$IPM_ARTIFACT_ROOT/work/research860" ] || [ ! -d "$IPM_ARTIFACT_ROOT/outputs" ]; do
    [ "$IPM_ARTIFACT_ROOT" != / ] || { echo "artifact root not found" >&2; exit 1; }
    IPM_ARTIFACT_ROOT="${IPM_ARTIFACT_ROOT%/*}"
    [ -n "$IPM_ARTIFACT_ROOT" ] || IPM_ARTIFACT_ROOT=/
done
export IPM_ARTIFACT_ROOT
# B8 (b) SIGKILL-inside-a-trial helper, version 3.1 (final bytes with K1 hashes; lead NOTES 2026-10-25T03:29:50Z item 3 and 03:41:11Z (a)-(f)). Separate from v2 (TERM).
# Sequence: (i) select the worker (argv[2] endswith research860/campaign860.py with --root ROOT; PPID == the single live guard whose argv is
# hardware/guard.py run --session-dir ROOT/guard_session; PID == HEARTBEAT.json pid; PGID(worker) == worker PID; PGID(guard) != worker PID),
# re-selected right before acting; (ii) SIGSTOP the worker and continue only if rc 0 and its state is T, else SIGCONT and exit 6; (iii) while frozen,
# the in-trial check: the newest trial_intents trial n must exceed the trial of the last committed trial event and have no commit, else SIGCONT and
# exit 5; (iv) list every process with PGID == worker; if any member other than the worker has a parent other than the worker, SIGCONT and exit 7;
# (v) SIGKILL every child with PPID == worker and PGID == worker (pid, state, pgid, rc, time recorded); (vi) wait <= 60 s until each is zombie or
# gone; (vii) SIGKILL the worker (also on timeout, recorded); then wait for the worker to be gone (<= 900 s), list the family, wait for the new
# guard+worker pair (same selector, <= max-wait) and record the first commits. Every step is timed. No STOP file. The record is written by a
# Python block that reads the facts from exported environment variables (no shell token is interpolated into Python source).
# Usage: bin/pilot_signal_test_v3.sh <campaign-root> KILL [wait-for-phase-regex] [max-wait-s]      DRYRUN=1: selection, group, children, plan; no signal
set -u
ROOT=$1; SIG=$2; PHASE_RE=${3:-}; MAXW=${4:-900}
[ "$SIG" = "KILL" ] || { echo "v3.1 is for KILL only (bin/pilot_signal_test.sh is for TERM)"; exit 2; }
LANE=$IPM_ARTIFACT_ROOT; OUT=${B8_OUT_DIR:-$LANE/outputs/campaign860/pilot_signal_tests}; mkdir -p $OUT
stamp() { date -u +%FT%T.%3NZ; }
REC=$OUT/signal_KILL_v31_$(date -u +%Y%m%dT%H%M%SZ).json
pstate() { awk '{print $3}' /proc/$1/stat 2>/dev/null || echo gone; }
select_family() { python3 - "$ROOT" <<'PY'
import os, sys, json
root = sys.argv[1]; guards = []; workers = []
def stat(p):
    rest = open('/proc/%s/stat' % p).read().rsplit(')', 1)[1].split(); return rest[0], int(rest[1]), int(rest[2])
for p in os.listdir('/proc'):
    if not p.isdigit(): continue
    try:
        argv = [a.decode(errors='replace') for a in open('/proc/%s/cmdline' % p, 'rb').read().split(b'\0')[:-1]]; st, ppid, pgid = stat(p)
    except Exception: continue
    if len(argv) < 4: continue
    if argv[2].endswith('hardware/guard.py') and argv[3] == 'run' and '--session-dir' in argv and argv[argv.index('--session-dir')+1] == root + '/guard_session': guards.append((int(p), ppid, pgid))
    if argv[2].endswith('research860/campaign860.py') and '--root' in argv and argv[argv.index('--root')+1] == root: workers.append((int(p), ppid, pgid))
g = guards[0] if len(guards) == 1 else (-1, -1, -1)
w = [x for x in workers if g[0] > 0 and x[1] == g[0]]; w = w[0] if len(w) == 1 else (-1, -1, -1)
try: hb = json.load(open(root + '/HEARTBEAT.json')).get('pid')
except Exception: hb = None
hb = hb if hb is not None else -1
agree = 1 if (len(guards) == 1 and w[0] > 0 and w[0] == hb and w[2] == w[0] and g[2] != w[0]) else 0
print(g[0], g[1], g[2], w[0], w[1], w[2], hb, agree, len(guards), len(workers))
PY
}
group_members() { python3 - "$1" <<'PY'
import os, sys, json
w = int(sys.argv[1]); rows = []
for p in os.listdir('/proc'):
    if not p.isdigit(): continue
    try: rest = open('/proc/%s/stat' % p).read().rsplit(')', 1)[1].split()
    except Exception: continue
    if int(rest[2]) == w: rows.append({'pid': int(p), 'ppid': int(rest[1]), 'pgid': int(rest[2]), 'state': rest[0]})
print(json.dumps(sorted(rows, key=lambda r: r['pid'])))
PY
}
children_lines() { python3 - "$1" <<'PY'
import os, sys
w = int(sys.argv[1])
for p in sorted(int(x) for x in os.listdir('/proc') if x.isdigit()):
    try: rest = open('/proc/%d/stat' % p).read().rsplit(')', 1)[1].split()
    except Exception: continue
    if int(rest[1]) == w and int(rest[2]) == w: print(p, rest[0], rest[2])
PY
}
family_listing() { python3 - "$ROOT" <<'PY'
import os, sys, json
root = sys.argv[1]; rows = []
for p in os.listdir('/proc'):
    if not p.isdigit(): continue
    try:
        argv = open('/proc/%s/cmdline' % p, 'rb').read().replace(b'\0', b' ').decode(errors='replace'); rest = open('/proc/%s/stat' % p).read().rsplit(')', 1)[1].split()
    except Exception: continue
    if int(p) == os.getpid() or argv.startswith('python3 - '): continue      # this helper's own subprocesses
    if root in argv and 'shell-snapshots' not in argv and 'pilot_signal_test' not in argv: rows.append({'pid': int(p), 'ppid': int(rest[1]), 'pgid': int(rest[2]), 'state': rest[0], 'argv': argv[:140]})
print(json.dumps(sorted(rows, key=lambda r: r['pid'])))
PY
}
intrial_check() { python3 - "$ROOT" <<'PY'
import os, sys, json, glob, re
root = sys.argv[1]
intents = sorted(glob.glob(root + '/trial_intents/trial_*.json')); newest = None
if intents:
    m = re.match(r'trial_(\d+)_', os.path.basename(intents[-1])); newest = int(m.group(1)) if m else None
last = 0; commit_for_newest = False
for p in sorted(glob.glob(root + '/commits/event_*.json')):
    try: t = json.load(open(p)).get('trial', {})
    except Exception: continue
    n = t.get('trial') if isinstance(t, dict) else None
    if isinstance(n, int) and 'accepted' in t and 'kind' not in t: last = max(last, n); commit_for_newest = commit_for_newest or (newest is not None and n == newest)
ok = newest is not None and newest > last and not commit_for_newest
print(json.dumps({'newest_intent_trial': newest, 'newest_intent_file': os.path.basename(intents[-1]) if intents else None, 'last_committed_trial': last, 'commit_for_newest_exists': commit_for_newest, 'ok': ok}))
PY
}
last_event() { ls $ROOT/commits/event_*.json 2>/dev/null | sort | tail -1 | xargs -r basename; }
export T_START=$(stamp); export HELPER_PATH=$(readlink -f "$0"); export HELPER_SHA=$(sha256sum "$HELPER_PATH" | cut -c1-64)
read GPID GPPID GPGID PID WPPID WPGID HBPID AGREE NG NW <<< "$(select_family)"
echo "$(stamp) selection: guard $GPID (ppid $GPPID pgid $GPGID) worker $PID (ppid $WPPID pgid $WPGID) heartbeat pid $HBPID agree=$AGREE guards=$NG argv-matches=$NW"
echo "process group $PID members (pid ppid pgid state): $(group_members $PID)"
echo "children with PPID=$PID and PGID=$PID (pid state pgid):"; children_lines $PID | sed 's/^/  /'
echo "in-trial check now: $(intrial_check)"
echo "planned order: SIGSTOP $PID (continue only if rc 0 and state T) -> in-trial check -> group parent check -> SIGKILL each child PPID=$PID PGID=$PID -> wait <= 60 s zombie/gone -> SIGKILL $PID -> wait gone -> family listing -> wait new guard+worker pair (<= ${MAXW}s)"
if [ -n "${DRYRUN:-}" ]; then echo "DRYRUN: no signal sent"; exit 0; fi
[ "$AGREE" = "1" ] || { echo "$(stamp) REFUSE: selection does not agree; NO signal sent"; exit 3; }
if [ -n "$PHASE_RE" ]; then
  echo "$(stamp) waiting for heartbeat phase matching '$PHASE_RE' (max ${MAXW}s)"; w=0; ph=""
  while [ $w -lt $MAXW ]; do ph=$(python3 -c "import json; print(json.load(open('$ROOT/HEARTBEAT.json')).get('phase',''))" 2>/dev/null); [[ "$ph" =~ $PHASE_RE ]] && break; sleep 3; w=$((w+3)); done
  [[ "$ph" =~ $PHASE_RE ]] || { echo "$(stamp) phase '$ph' never matched '$PHASE_RE' within ${MAXW}s; NO signal sent"; exit 4; }
fi
read GPID2 GPPID2 GPGID2 PID2 WPPID2 WPGID2 HBPID2 AGREE2 NG2 NW2 <<< "$(select_family)"
if [ "$AGREE2" != "1" ] || [ "$PID2" != "$PID" ] || [ "$GPID2" != "$GPID" ]; then echo "$(stamp) REFUSE: selection changed or disagrees (guard $GPID2 worker $PID2 heartbeat $HBPID2 agree $AGREE2); NO signal sent"; exit 3; fi
export ROOT SIG PHASE_RE GPID GPPID GPGID PID WPPID WPGID HBPID AGREE2 REC
export GUARD_PY=$(tr "\0" "\n" < /proc/$GPID/cmdline | sed -n 3p); export GUARD_PY_SHA=$(sha256sum "$GUARD_PY" 2>/dev/null | cut -c1-64); echo "$(stamp) helper $HELPER_PATH sha256 $HELPER_SHA; guard script $GUARD_PY sha256 $GUARD_PY_SHA"
export HB_BEFORE=$(cat $ROOT/HEARTBEAT.json 2>/dev/null | tr -d '\n'); export EV_BEFORE=$(last_event); export GUARD_RUNS_BEFORE=$(ls -d $ROOT/guard_session*/runs/* 2>/dev/null | wc -l); export FAM_BEFORE=$(family_listing)
export INTENTS_BEFORE=$(ls $ROOT/trial_intents 2>/dev/null | wc -l); export PROPOSALS_BEFORE=$(ls $ROOT/trial_proposals 2>/dev/null | wc -l)
# (ii) SIGSTOP
kill -STOP $PID; export RC_STOP=$?; export T_STOP=$(stamp); sleep 0.5; export WSTATE=$(pstate $PID)
if [ "$RC_STOP" != "0" ] || [ "$WSTATE" != "T" ]; then echo "$T_STOP SIGSTOP rc $RC_STOP state '$WSTATE' not T: SIGCONT and exit 6"; kill -CONT $PID 2>/dev/null; exit 6; fi
echo "$T_STOP SIGSTOP worker $PID rc 0, state T"
# (iii) in-trial check while frozen
export INTRIAL=$(intrial_check); echo "$(stamp) in-trial check: $INTRIAL"
if [ "$(python3 -c "import json,os; print(json.loads(os.environ['INTRIAL'])['ok'])")" != "True" ]; then echo "$(stamp) not inside a trial: SIGCONT and exit 5"; kill -CONT $PID; exit 5; fi
# (iv) group members: every PGID == worker member other than the worker must have PPID == worker
export GROUP_BEFORE=$(group_members $PID); echo "$(stamp) group members: $GROUP_BEFORE"
if [ "$(python3 -c "import json,os; g=json.loads(os.environ['GROUP_BEFORE']); w=int(os.environ['PID']); print(all(r['pid']==w or r['ppid']==w for r in g))")" != "True" ]; then echo "$(stamp) a group member has a parent other than the worker: SIGCONT and exit 7"; kill -CONT $PID; exit 7; fi
# (v) SIGKILL children
CH=$(children_lines $PID); export T_KILL_CH=$(stamp)
export CHILD_RECORDS=$(python3 - "$PID" "$CH" <<'PY'
import os, signal, json, time, sys
rows = []
for line in sys.argv[2].strip().splitlines():
    if not line.strip(): continue
    pid, st, pg = line.split(); pid = int(pid)
    try: os.kill(pid, signal.SIGKILL); rc = 0
    except ProcessLookupError: rc = 'ESRCH'
    rows.append({'pid': pid, 'state_before': st, 'pgid': int(pg), 'sigkill_rc': rc, 'utc': time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime()) + 'Z'})
print(json.dumps(rows))
PY
); echo "$T_KILL_CH SIGKILL children: $CHILD_RECORDS"
# (vi) wait <= 60 s until each child is zombie or gone
w=0; LIVE=1; while [ $w -lt 60 ]; do LIVE=$(children_lines $PID | awk '$2!="Z"' | wc -l); [ "$LIVE" = "0" ] && break; sleep 1; w=$((w+1)); done
export T_CH_DONE=$(stamp); export CH_AFTER=$(children_lines $PID | tr '\n' ';'); export CH_WAIT_S=$w; export CH_TIMED_OUT=$([ "$LIVE" = "0" ] && echo no || echo yes)
echo "$T_CH_DONE children after ${w}s: ${CH_AFTER:-none}; timed_out=$CH_TIMED_OUT"
# (vii) SIGKILL the worker
kill -KILL $PID; export RC=$?; export T_SEND=$(stamp); export T_SEND_EPOCH=$(date +%s.%N); echo "$T_SEND SIGKILL worker $PID rc $RC; guard $GPID untouched; last event before: $EV_BEFORE"
w=0; while kill -0 $PID 2>/dev/null && [ $w -lt 900 ]; do sleep 1; w=$((w+1)); done; export T_GONE=$(stamp); export GONE_TIMED_OUT=$(kill -0 $PID 2>/dev/null && echo yes || echo no); sleep 3; export FAM_AFTER_GONE=$(family_listing)
echo "$T_GONE worker gone (wait ${w}s, timed_out=$GONE_TIMED_OUT); family now: $FAM_AFTER_GONE"
w=0; export NEWPID=""; export NEWG=""; while [ $w -lt $MAXW ]; do read ng a b nw c d nhb na x y <<< "$(select_family)"; if [ "$na" = "1" ] && [ "$nw" != "$PID" ]; then export NEWPID=$nw; export NEWG=$ng; break; fi; sleep 5; w=$((w+5)); done; export T_NEW=$(stamp); export NEW_TIMED_OUT=$([ -n "$NEWPID" ] && echo no || echo yes)
echo "$T_NEW new pair: guard ${NEWG:-none} worker ${NEWPID:-none} (wait ${w}s, timed_out=$NEW_TIMED_OUT)"
sleep 20; export EV_AFTER=$(last_event); export GUARD_RUNS_AFTER=$(ls -d $ROOT/guard_session*/runs/* 2>/dev/null | wc -l); export FAM_FINAL=$(family_listing)
export NEW_EVENTS=$(ls $ROOT/commits/event_*.json 2>/dev/null | sort | awk -v b="$ROOT/commits/$EV_BEFORE" '$0 > b' | xargs -r -n1 basename | tr '\n' ' ')
python3 - <<'PY'
import json, os
E = os.environ; j = lambda k: json.loads(E[k]) if E.get(k) else None; i = lambda k: int(E[k]) if E.get(k) not in (None, '') else None
rec = {'schema': 'pilot_signal_test_v3.1_KILL', 'helper_path': E['HELPER_PATH'], 'helper_sha256': E['HELPER_SHA'], 'guard_py_path': E['GUARD_PY'], 'guard_py_sha256': E['GUARD_PY_SHA'], 'root': E['ROOT'], 'signal': 'SIGSTOP worker; SIGKILL pool children; wait; SIGKILL worker', 'phase_wait_regex': E['PHASE_RE'], 'started_utc': E['T_START'],
       'selection': {'guard_pid': i('GPID'), 'guard_ppid': i('GPPID'), 'guard_pgid': i('GPGID'), 'worker_pid': i('PID'), 'worker_ppid': i('WPPID'), 'worker_pgid': i('WPGID'), 'heartbeat_pid': i('HBPID'), 'agree': i('AGREE2')},
       'heartbeat_before': j('HB_BEFORE'), 'family_before': j('FAM_BEFORE'), 'last_event_before': E['EV_BEFORE'], 'guard_runs_before': i('GUARD_RUNS_BEFORE'), 'intents_before': i('INTENTS_BEFORE'), 'proposals_before': i('PROPOSALS_BEFORE'),
       'sigstop_worker': {'utc': E['T_STOP'], 'rc': i('RC_STOP'), 'worker_state_after': E['WSTATE']}, 'sigstop_state_ok': E['RC_STOP'] == '0' and E['WSTATE'] == 'T',
       'inside_trial_check': j('INTRIAL'), 'group_members_before': j('GROUP_BEFORE'),
       'sigkill_children': j('CHILD_RECORDS'), 'children_wait': {'done_utc': E['T_CH_DONE'], 'seconds': i('CH_WAIT_S'), 'children_after': E['CH_AFTER'], 'timed_out': E['CH_TIMED_OUT'] == 'yes'},
       'sigkill_worker': {'utc': E['T_SEND'], 'epoch': float(E['T_SEND_EPOCH']), 'rc': i('RC')},
       'worker_gone': {'utc': E['T_GONE'], 'worker_gone_wait_timed_out': E['GONE_TIMED_OUT'] == 'yes'}, 'family_after_worker_gone': j('FAM_AFTER_GONE'),
       'new_pair_found': bool(E.get('NEWPID')), 'new_pair_wait_timed_out': E['NEW_TIMED_OUT'] == 'yes', 'new_worker_pid': i('NEWPID'), 'new_guard_pid': i('NEWG'), 'new_pair_seen_utc': E['T_NEW'],
       'last_event_after_20s': E['EV_AFTER'], 'guard_runs_after': i('GUARD_RUNS_AFTER'), 'new_events': E['NEW_EVENTS'].split(), 'family_final': j('FAM_FINAL'),
       'supervisor_log_tail': open(E['ROOT'] + '/supervisor.log').read().splitlines()[-12:] if os.path.exists(E['ROOT'] + '/supervisor.log') else None,
       'note': 'B8 (b) record v3.1 (numerics); no STOP file written; family listings = every process whose argv contains the root (tool shells and this helper excluded) with pid, ppid, pgid, state'}
json.dump(rec, open(E['REC'], 'w'), indent=1); print('record', E['REC'])
print(json.dumps({k: rec[k] for k in ('helper_sha256', 'guard_py_sha256', 'selection', 'sigstop_state_ok', 'inside_trial_check', 'group_members_before', 'sigkill_children', 'children_wait', 'sigkill_worker', 'worker_gone', 'new_pair_found', 'new_pair_wait_timed_out', 'new_worker_pid', 'new_guard_pid', 'new_events')}))
print('family after worker gone (pid, ppid, pgid, state):', [(r['pid'], r['ppid'], r['pgid'], r['state']) for r in rec['family_after_worker_gone']])
PY

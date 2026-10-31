#!/bin/bash
# Stop the supervisor, normalize job flags on the pending files (exclusive for L>=10, retry budget, Sigma_Z ramp), start again.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
echo "$(date -u +%FT%TZ) requesting stop"; touch status/STOP_SUPERVISOR
pid=$(python3 -c "import json;print(json.load(open('status/supervisor_heartbeat.json'))['pid'])")
for i in $(seq 1 100); do kill -0 $pid 2>/dev/null || break; sleep 6; done
kill -0 $pid 2>/dev/null && { echo "supervisor still alive; aborting"; exit 1; }
sleep 15; echo "$(date -u +%FT%TZ) supervisor exited; workers left: $(pgrep -f scripts/worker.py | wc -l)"
python3 - <<'PY'
import json, glob
n=0
for f in glob.glob('queue/pending/*.json'):
    j=json.load(open(f)); c=j['config']; ch=False
    if c.get('L',0) >= 8 and not j.get('exclusive'): j['exclusive']=True; ch=True
    if j['job_id'].startswith('c2x2') and j.get('max_retries',2) < 6: j['max_retries']=6; j['retries']=min(j.get('retries',0), 2); ch=True
    if c.get('sigmaZ') is not None and not c.get('sigmaZ_ramp_iters'): c['sigmaZ_ramp_iters']=60; ch=True
    if ch: json.dump(j, open(f,'w'), indent=1); n+=1
print('normalized', n, 'pending job files')
PY
rm -f status/STOP_SUPERVISOR; scripts/start_supervisor.sh; echo "$(date -u +%FT%TZ) done"

#!/bin/bash
# Stop the supervisor (workers checkpoint and exit), drop the in-progress start of every checkpoint so it restarts
# from a fresh seed with the current code (completed starts are kept), then restart the supervisor.
ROOT=$(cd "$(dirname "$0")/.." && pwd); cd $ROOT
echo "$(date -u +%FT%TZ) requesting stop"; touch status/STOP_SUPERVISOR
pid=$(python3 -c "import json;print(json.load(open('status/supervisor_heartbeat.json'))['pid'])")
for i in $(seq 1 100); do kill -0 $pid 2>/dev/null || break; sleep 6; done
if kill -0 $pid 2>/dev/null; then echo "$(date -u +%FT%TZ) supervisor still alive after 10 min; aborting"; exit 1; fi
echo "$(date -u +%FT%TZ) supervisor exited; running workers left: $(pgrep -f scripts/worker.py | wc -l)"
sleep 5
.venv/bin/python - <<'PY'
import torch, glob, os
n=0
for f in glob.glob('queue/pending/*.json'):
    import json; j=json.load(open(f)); ck=os.path.join('runs', j['job_id'], 'checkpoint.pt')
    if os.path.exists(ck):
        s=torch.load(ck, map_location='cpu', weights_only=False)
        if s.get('current') is not None:
            s['current']=None; s['note']='in-progress start dropped 2026-10-24T19:1xZ (weight-normalization fix); completed starts kept'
            tmp=ck+'.tmp'; torch.save(s, tmp); os.replace(tmp, ck); n+=1
print('checkpoints reset:', n)
PY
rm -f status/STOP_SUPERVISOR
scripts/start_supervisor.sh
echo "$(date -u +%FT%TZ) done"

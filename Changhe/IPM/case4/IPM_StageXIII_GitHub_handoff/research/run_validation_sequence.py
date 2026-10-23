"""Explicit sequential validation jobs. Never selects or runs an optimizer."""
import argparse,json,os
from pathlib import Path
import subprocess,time
ROOT=Path(__file__).resolve().parent


def atomic(p,v):
    t=p.with_name(p.name+'.partial')
    with t.open('w') as f:json.dump(v,f,indent=2);f.write('\n');f.flush();os.fsync(f.fileno())
    t.replace(p)


def main(a):
    state_path=a.jobs.with_suffix('.state.json')
    state=json.loads(state_path.read_text()) if state_path.exists() else {'completed':[],'failed':[],'active':None,'history':[]}
    if state['active'] or state['failed']:raise ValueError('Interrupted or failed sequence requires explicit review; no automatic reset')
    for job in json.loads(a.jobs.read_text())['jobs']:
        if job['label'] in state['completed']:continue
        cmd=['/usr/bin/python3','-B',str(ROOT/'launch.py'),'--label',job['label'],job['worker']]+job.get('arguments',[])
        state['active']={'label':job['label'],'command':cmd,'started_epoch':time.time()};atomic(state_path,state)
        print(json.dumps({'starting_validation':job['label']}),flush=True)
        rc=subprocess.call(cmd,cwd=ROOT,env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1'))
        state['active'].update(returncode=rc,finished_epoch=time.time());state['history'].append(state['active']);state['active']=None
        state['failed' if rc else 'completed'].append(job['label']);atomic(state_path,state)
        if rc:raise SystemExit('Validation stopped for review: '+job['label'])
    print('Explicit validation sequence completed; no optimization performed.',flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--jobs',type=Path,required=True);main(p.parse_args())

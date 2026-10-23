"""Bounded, resumable checkpoint validation supervisor. No network or listeners."""
from __future__ import annotations
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
NUM=Path('.')
STOP=ROOT/'VALIDATOR_STOP'
DRAIN=ROOT/'VALIDATOR_DRAIN'


def utc():return datetime.datetime.now(datetime.timezone.utc).isoformat()

def atomic(path,data):
    temp=path.with_suffix(path.suffix+f'.{os.getpid()}.tmp')
    temp.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n');os.replace(temp,path)

def read_json(path,default):
    try:return json.loads(path.read_text())
    except (FileNotFoundError,json.JSONDecodeError):return default

def digest(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()

def ledger_state():
    records=[]
    p=ROOT/'VALIDATION_LEDGER.jsonl'
    if p.exists():
        for line in p.read_text().splitlines():
            try:records.append(json.loads(line))
            except json.JSONDecodeError:pass
    starts={r['interval_id']:r for r in records if r.get('event')=='start'}
    stops={r['interval_id']:r for r in records if r.get('event')=='stop'}
    intervals=[]
    for key,r in stops.items():
        if key not in starts:continue
        start=datetime.datetime.fromisoformat(starts[key]['start_utc']).timestamp()
        end=datetime.datetime.fromisoformat(r['end_utc']).timestamp()
        if end>=start:intervals.append((start,end))
    merged=[]
    for start,end in sorted(intervals):
        if merged and start<=merged[-1][1]:merged[-1]=(merged[-1][0],max(merged[-1][1],end))
        else:merged.append((start,end))
    seconds=sum(b-a for a,b in merged)
    return dict(active_seconds=seconds,active_hours=seconds/3600,closed_intervals=len(intervals),
                unmatched_start_ids=sorted(set(starts)-set(stops)),
                counting='union of closed validation-task UTC wall intervals, only this lane; unmatched starts and watcher idle time excluded; not CPU time or certified against unlogged suspension',
                union_intervals=[dict(start_utc=datetime.datetime.fromtimestamp(a,datetime.timezone.utc).isoformat(),
                                      end_utc=datetime.datetime.fromtimestamp(b,datetime.timezone.utc).isoformat()) for a,b in merged])

def publish(state,write_worklog=False):
    state.update(updated_utc=utc(),pid=os.getpid(),lane_ledger=ledger_state())
    atomic(ROOT/'VALIDATOR_STATUS.json',state)
    atomic(ROOT/'STATE.json',dict(updated_utc=utc(),role='independent verifier',status=state['status'],
                                 active_time=state['lane_ledger'],last_checkpoint=state.get('last_checkpoint'),
                                 campaign_target_hours=96,campaign_target_reached=False,
                                 campaign_time_scope='Numerics owns the shared campaign ledger. Union, never sum, concurrent lane intervals.',
                                 resume_command=f'cd {ROOT} && ./resume.sh',supervisor_pid=os.getpid()))
    text=f'''# Verifier status\n\nUpdated: {state['updated_utc']}.\n\nRESUME_HERE: Read PROMPT.md in full and the lead/numerics reports, then read FINALIZATION.md, NEXT_STEPS.md, NOTES_FOR_TEAM.md, THEORY_V3_AUDIT.md, HOSTILE_THEORY_AUDIT.md, SCOPE_AUDIT.md, REPORT_AUDIT.md, RUNTIME_REPAIR_AUDIT.md, VERIFY_REPORT.md and VALIDATOR_STATUS.json. Audit any published EQUATIONS.md against research/*/PROOF.md. Confirm the checkpoint radial feature formula and extend the independent decoder only from saved architecture metadata. Start or resume checkpoint validation with `./resume.sh`; inspect with `./status.sh`; stop gracefully with `./stop.sh`.\n\nSupervisor status: {state['status']}. PID {state['pid']}. Current checkpoint: {state.get('current_checkpoint')}. Last checkpoint: {state.get('last_checkpoint')}. Last error: {state.get('last_error')}.\n\nThis lane has {state['lane_ledger']['active_seconds']:.6f} seconds in the union of validation-task wall intervals ({state['lane_ledger']['active_hours']:.9f} hours). Idle watcher time is excluded; these are not CPU seconds or a certificate against unlogged suspension. Unmatched intervals: {len(state['lane_ledger']['unmatched_start_ids'])}. The shared 96-hour campaign is NOT claimed complete; numerics owns its ledger.\n\nL2 is independently CONFIRMED: every exact C2 sublinear profile for 0<c_l<1/2 has constant U, hence U=0 under decay. The c_l=1/2 calibration and larger-exponent secondary search remain outside this obstruction. Final REPORT approval requires a separate exact-version audit. No nonzero exact profile was constructed, and no stability or blowup theorem is established.\n\nIndependent evaluator: NumPy forward and explicit potential tangents, followed by physical fourth/sixth-order finite differences. It does not import numerics residual code. The 32 calibration tests, nine synthetic decoder configurations, and whole-space manufactured quadratures passed. The prompt seed fails momentum and tail checks. The sqrt(R2+1e-300) origin defect was repaired with a smooth log1p radial feature in the audited pilot. The dir_log saturation restriction and v2 bounded-feature cancellation condition are proved in research/radial-feature-tails/PROOF.md and research/bounded-tail-expansion/PROOF.md. Both old and v2 state layouts are decoded. Matched pilot500 residual metrics agree with saved trainer values to 3e-13 relative; the overlapping-weight defect remains a separate finding. The repaired regional norm, C denominator and fresh-batch L-BFGS reset passed review. Stage-transition resume and eligible activity accounting still have demonstrated defects; see RUNTIME_REPAIR_AUDIT.md. Actual trainer eligible time cannot be recovered exactly from the ledger.\n\nResources: one checkpoint worker with one BLAS/OMP thread at nice 19; bounded manual audits may run alongside it, always below four total CPU workers. GPU 4 is reserved but has not been needed. No JavaScript/TypeScript, servers, RLScience access, remote compute, Lean/lake, commits, or writes outside this lane.\n\nCollaboration: lead launch log confirms us.anthropic.claude-opus-5-5; numerics log specifies us.anthropic.claude-fable-5-1. Exchange mathematical findings through local files and verify replies.\n'''
    (ROOT/'RUN_STATUS.md').write_text(text)
    try:
        import importlib,report
        importlib.reload(report).build_report(state)
    except Exception as error:
        print(utc(),'REPORT_ERROR',repr(error),flush=True)
    if write_worklog:
        with (ROOT/'WORKLOG.md').open('a') as f:f.write(f"\n- {state['updated_utc']}: Supervisor {state['status']}; closed validation-task wall union {state['lane_ledger']['active_seconds']:.6f} seconds. Last checkpoint {state.get('last_checkpoint')}; current {state.get('current_checkpoint')}. Idle time excluded.\n")

def jobs():
    cfg=read_json(ROOT/'VALIDATION_QUEUE.json',dict(jobs=[],auto_discover=True))
    work=list(cfg.get('jobs',[]))
    if cfg.get('auto_discover',True):
        for pattern in ['artifacts/candidates/*/*.pt','exports/*.npz','validation_exports/*.npz','runs/*/best.pt','runs/*/latest.pt','checkpoints/*/best.pt','checkpoints/*/latest.pt','checkpoints/best.pt','checkpoints/latest.pt','runs/*/ckpt_best.pt','runs/*/ckpt_last.pt','runs_test/*/ckpt_best.pt','runs_test/*/ckpt_last.pt']:
            for path in sorted(NUM.glob(pattern)):
                work.append(dict(checkpoint=str(path),n=256,radial_kind=cfg.get('auto_radial_kind')))
    unique={}
    for job in work:
        path=Path(job['checkpoint'])
        if path.is_file():
            unique[str(path)]=job
    return list(unique.values())

def safe_snapshot(path,key):
    if path.stat().st_size>512*1024*1024:
        raise RuntimeError('Checkpoint exceeds 512 MiB snapshot budget')
    dest=ROOT/'snapshots'/(key+path.suffix)
    if dest.exists():return dest
    temp=dest.with_suffix(dest.suffix+'.tmp')
    shutil.copyfile(path,temp)
    if digest(temp)!=key:
        temp.unlink(missing_ok=True)
        raise RuntimeError('Source checkpoint changed during snapshot; retry next cycle')
    os.replace(temp,dest)
    return dest

def freeze_code():
    names=['checkpoint.py','core.py','evaluate.py','models.py']
    contents={name:(ROOT/'validation'/name).read_bytes() for name in names}
    hashes={name:hashlib.sha256(content).hexdigest() for name,content in contents.items()}
    key=hashlib.sha256(json.dumps(hashes,sort_keys=True).encode()).hexdigest()
    destination=ROOT/'snapshots'/('validator-code-'+key[:16])/'validation'
    destination.mkdir(parents=True,exist_ok=True)
    for name,content in contents.items():
        target=destination/name
        if target.exists():
            if target.read_bytes()!=content:raise RuntimeError('Frozen code digest collision')
        else:target.write_bytes(content)
    manifest=destination.parent/'MANIFEST.json'
    if not manifest.exists():atomic(manifest,dict(created_utc=utc(),sha256=key,files=hashes,scope='Exact immutable Python source loaded by checkpoint workers'))
    return key,destination

def run_job(job,state,done):
    source=Path(job['checkpoint'])
    if time.time()-source.stat().st_mtime<10:return
    key=digest(source)
    decoder_hash,code_dir=freeze_code()
    science_config={k:job.get(k,v) for k,v in [('n',256),('holdout_seed',736291),('radial_kind',None)]}
    config_key=hashlib.sha256(json.dumps(science_config,sort_keys=True).encode()).hexdigest()[:12]
    job_id=key+'-'+decoder_hash[:12]+'-'+config_key
    if job_id in done:return
    free=shutil.disk_usage(ROOT).free
    if free<10*1024**3:
        state.update(status='suspended_disk_headroom',last_error='Less than 10 GiB free; no new snapshots')
        return
    snapshot=safe_snapshot(source,key)
    output=ROOT/'evidence'/('checkpoint-'+key[:16]+'-'+decoder_hash[:10]+'-'+config_key[:8]+'.json')
    log=ROOT/'logs'/('checkpoint-'+key[:16]+'-'+decoder_hash[:10]+'-'+config_key[:8]+'.log')
    command=[sys.executable,str(code_dir/'checkpoint.py'),str(snapshot),'--n',str(job.get('n',256)),
             '--holdout-seed',str(job.get('holdout_seed',736291)),'--output',str(output)]
    if job.get('radial_kind'):command+=['--radial-kind',job['radial_kind']]
    state.update(status='validating',current_checkpoint=str(source),last_error=None)
    publish(state,True)
    print(utc(),'START',source,key,flush=True)
    started=utc()
    with log.open('w') as stream:
        child_env=os.environ.copy();child_env['E1_VER_ROOT']=str(ROOT)
        proc=subprocess.Popen(command,stdout=stream,stderr=subprocess.STDOUT,env=child_env,cwd=ROOT)
        state['child_pid']=proc.pid
        publish(state)
        deadline=time.monotonic()+540
        while proc.poll() is None:
            if STOP.exists() or time.monotonic()>deadline:
                proc.terminate()
                try:proc.wait(timeout=10)
                except subprocess.TimeoutExpired:proc.kill();proc.wait(timeout=10)
                state['last_error']='Validation interrupted by STOP or 540-second per-checkpoint limit; open interval is not counted.'
                break
            time.sleep(2)
        code=proc.returncode
    done[job_id]=dict(source=str(source),snapshot=str(snapshot),sha256=key,output=str(output),log=str(log),
                      start_utc=started,end_utc=utc(),returncode=code,code_snapshot=str(code_dir),code_sha256=decoder_hash,science_config=science_config)
    atomic(ROOT/'VALIDATION_COMPLETED.json',done)
    state.update(status='watching',current_checkpoint=None,child_pid=None,last_checkpoint=str(source))
    if code!=0:state['last_error']=state.get('last_error') or f'Validation exited {code}; see {log.name}'
    else:
        result=read_json(output,{})
        state['last_assessment']=result.get('assessment')
    publish(state,True)
    print(utc(),'END',source,'returncode',code,flush=True)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--once',action='store_true')
    parser.add_argument('--interval',type=float,default=120.)
    parser.add_argument('--max-hours',type=float,default=128.)
    args=parser.parse_args()
    if os.getpriority(os.PRIO_PROCESS,0)<19:os.nice(19-os.getpriority(os.PRIO_PROCESS,0))
    lock=(ROOT/'VALIDATOR.lock').open('a')
    try:fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    except BlockingIOError:
        print('Validator already running',flush=True);return
    (ROOT/'VALIDATOR.pid').write_text(str(os.getpid())+'\n')
    state=dict(status='watching',started_utc=utc(),current_checkpoint=None,last_checkpoint=None,last_error=None)
    done=read_json(ROOT/'VALIDATION_COMPLETED.json',{})
    start=time.monotonic();last_log=0.
    def handle(signum,frame):STOP.touch()
    signal.signal(signal.SIGTERM,handle);signal.signal(signal.SIGINT,handle)
    try:
        while not STOP.exists() and not DRAIN.exists() and time.monotonic()-start<args.max_hours*3600:
            try:
                for job in jobs():
                    if STOP.exists() or DRAIN.exists():break
                    run_job(job,state,done)
                if not state.get('current_checkpoint') and state['status']!='suspended_disk_headroom':state['status']='watching'
                publish(state,time.monotonic()-last_log>=3600)
                if time.monotonic()-last_log>=3600:last_log=time.monotonic()
            except Exception as error:
                state.update(status='watching_after_error',last_error=repr(error))
                publish(state,True)
                print(utc(),'ERROR',repr(error),flush=True)
            if args.once:break
            until=time.monotonic()+args.interval
            while not STOP.exists() and not DRAIN.exists() and time.monotonic()<until:time.sleep(min(5,until-time.monotonic()))
    finally:
        state['status']='stopped';publish(state,True)
        print(utc(),'STOPPED',flush=True)
        (ROOT/'VALIDATOR.pid').unlink(missing_ok=True)

if __name__=='__main__':main()

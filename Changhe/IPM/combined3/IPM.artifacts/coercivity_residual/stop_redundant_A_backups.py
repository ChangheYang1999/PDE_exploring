"""Stop only the superseded A producers after their next valid checkpoint.

Authorized by the parent after complete independently reviewed A>2.08. The
actual completed certificate is L2_signed_far_v05/result.json. This watcher
does not stop any main-campaign, operator, source or matrix-cover process.
"""
import json,os,signal,time
from datetime import datetime,timezone
from hashlib import sha256
from pathlib import Path

HERE=Path(__file__).resolve().parent


def processes(script):
    result={}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit():continue
        try:
            argv=(path/'cmdline').read_bytes().split(b'\0')
            if not any(Path(a.decode()).name==script for a in argv if a):continue
            status=(path/'status').read_text()
            ppid=int(next(row.split()[1]for row in status.splitlines()if row.startswith('PPid:')))
            result[int(path.name)]=ppid
        except(FileNotFoundError,ProcessLookupError,PermissionError):continue
    return result


def stop(script):
    jobs=processes(script);parents=[pid for pid,ppid in jobs.items()if ppid not in jobs]
    assert len(parents)<=1,(script,jobs)
    if not parents:return {'status':'ALREADY_EXITED','pids':[]}
    parent=parents[0]
    try:os.kill(parent,signal.SIGSTOP)
    except ProcessLookupError:return {'status':'ALREADY_EXITED','pids':list(jobs)}
    current=processes(script)
    for pid in current:
        if pid!=parent:
            try:os.kill(pid,signal.SIGTERM)
            except ProcessLookupError:pass
    try:
        os.kill(parent,signal.SIGTERM);os.kill(parent,signal.SIGCONT)
    except ProcessLookupError:pass
    return {'status':'STOPPED_AFTER_VALID_CHECKPOINT','pids':sorted(current)}


def main():
    result=json.loads((HERE/'L2_signed_far_v05/result.json').read_text())
    assert result['status']=='CERTIFIED_DIRECT_L2'
    from flint import arb,ctx
    ctx.prec=384;assert arb(result['beta_L2_lower'])>arb('2.08')
    audit=json.loads((HERE/'A_final_finiteness_audit_v01.json').read_text());assert audit['status']=='FINITE_SCALARS_CONFIRMED'
    targets=[('certify_L2_013.py',HERE/'L2_cert_v04/chunk_02176_02207.json'),
             ('assemble_L2_signed_far_v04.py',HERE/'L2_signed_far_v04/far_norm_rho_1_1.cache.json')]
    receipt={'status':'WATCHING_FOR_NEXT_VALID_CHECKPOINT','authorized_condition':'Completed independently reviewed whole-plane betaL2>2.08',
             'certificate_sha256':sha256((HERE/'L2_signed_far_v05/result.json').read_bytes()).hexdigest(),
             'jobs':{},'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    path=HERE/'A_backup_stop_receipt.json';start=time.monotonic()
    while len(receipt['jobs'])<len(targets)and time.monotonic()-start<1200:
        for script,target in targets:
            if script in receipt['jobs']:continue
            try:record=json.loads(target.read_text())
            except(FileNotFoundError,json.JSONDecodeError):continue
            if script=='certify_L2_013.py':assert [row['index']for row in record['rows']]==list(range(2176,2208))
            receipt['jobs'][script]={**stop(script),'checkpoint':str(target),'checkpoint_sha256':sha256(target.read_bytes()).hexdigest(),
                'finished_utc':datetime.now(timezone.utc).isoformat()}
            print(json.dumps(receipt['jobs'][script]),flush=True)
        if len(receipt['jobs'])==len(targets):receipt['status']='SUPERSEDED_A_BACKUPS_STOPPED'
        receipt['updated_utc']=datetime.now(timezone.utc).isoformat()
        temporary=path.with_suffix('.tmp');temporary.write_text(json.dumps(receipt,indent=2)+'\n');temporary.replace(path)
        if receipt['status']=='SUPERSEDED_A_BACKUPS_STOPPED':break
        time.sleep(1)
    print(json.dumps(receipt,indent=2),flush=True)

if __name__=='__main__':main()

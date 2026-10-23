"""Coverage and immutable final snapshot; no experiment or process is changed."""
from __future__ import annotations
import argparse,csv,datetime,hashlib,json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
NUM=Path('.')
LEAD=Path('analysis')

def sha(data):return hashlib.sha256(data).hexdigest()
def read_json(p,default):
    try:return json.loads(p.read_text())
    except (FileNotFoundError,json.JSONDecodeError):return default

def active_pid(pid):
    try:
        state=Path(f'/proc/{int(pid)}/stat').read_text().split(') ',1)[1].split()[0]
        if state=='Z':return False
        return True
    except (FileNotFoundError,ValueError,PermissionError):return False

def inspect():
    completed=read_json(ROOT/'VALIDATION_COMPLETED.json',{})
    good={}
    for job,entry in completed.items():
        if entry.get('returncode')!=0:continue
        out=read_json(Path(entry['output']),{})
        if out.get('checkpoint_sha256')!=entry['sha256'] or 'assessment' not in out:continue
        good[entry['sha256']]=dict(evidence=entry['output'],evidence_sha256=sha(Path(entry['output']).read_bytes()),job_id=job,code_sha256=entry.get('code_sha256'),science_config=entry.get('science_config'),snapshot=entry['snapshot'])
    paths=set()
    for pattern in ('runs/*/ckpt_best.pt','runs/*/ckpt_last.pt','artifacts/candidates/*/*.pt'):
        paths.update(NUM.glob(pattern))
    covered=[];missing=[]
    for p in sorted(paths):
        b=p.read_bytes();h=sha(b);r=dict(source=str(p),sha256=h,bytes=len(b),mtime_utc=datetime.datetime.fromtimestamp(p.stat().st_mtime,datetime.timezone.utc).isoformat())
        if h in good:r.update(good[h]);covered.append(r)
        else:missing.append(r)
    own=read_json(ROOT/'VALIDATOR_STATUS.json',{})
    pids=[own.get('pid'),own.get('child_pid')]
    running_own=[int(p) for p in pids if p is not None and active_pid(p)]
    nstate=read_json(NUM/'runner_status.json',{})
    npids=[nstate.get('pid')]+[r.get('pid') for r in (nstate.get('running') or [])]
    rp=NUM/'runner.pid'
    if rp.exists():
        try:npids.append(int(rp.read_text().strip()))
        except ValueError:pass
    previous=read_json(ROOT/'FINAL_COVERAGE.json',{})
    npids.extend(previous.get('recorded_numerics_pids',previous.get('active_recorded_numerics_pids',[])))
    known_num=sorted({int(p) for p in npids if p is not None})
    running_num=[pid for pid in known_num if active_pid(pid)]
    return dict(date_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),source_checkpoint_files=len(paths),unique_source_checkpoint_hashes=len({r['sha256'] for r in covered+missing}),covered=covered,missing=missing,active_verifier_pids=running_own,active_recorded_numerics_pids=running_num,recorded_numerics_pids=known_num,scope='Coverage of present native best/last and published candidate PT files. Historical evaluated hashes remain in CHECKPOINT_TABLE.tsv. PID checks retain previously recorded runner/worker identities after the runner clears its list; unrelated jobs are not inspected. A recycled PID requires manual identity review before freezing.')

def main():
    p=argparse.ArgumentParser();p.add_argument('--freeze',action='store_true');p.add_argument('--expected-training-sha');a=p.parse_args();r=inspect()
    (ROOT/'FINAL_COVERAGE.json').write_text(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:v for k,v in r.items() if k!='covered'},indent=2))
    if not a.freeze:return
    if not a.expected_training_sha:raise SystemExit('--expected-training-sha required to freeze')
    if r['missing'] or r['active_verifier_pids'] or r['active_recorded_numerics_pids']:raise SystemExit('Freeze refused: uncovered checkpoints or recorded workers remain')
    training=NUM/'CAMPAIGN_LEDGER.jsonl';content=training.read_bytes()
    if sha(content)!=a.expected_training_sha:raise SystemExit('Training ledger differs from announced final hash')
    # Rebuild only the report, which does not append numerical activity.
    import report
    report.build_report(read_json(ROOT/'VALIDATOR_STATUS.json',{}))
    sources={'CAMPAIGN_LEDGER.jsonl':training,'VALIDATION_LEDGER.jsonl':ROOT/'VALIDATION_LEDGER.jsonl','CHECKPOINT_TABLE.tsv':ROOT/'CHECKPOINT_TABLE.tsv','VERIFY_REPORT.md':ROOT/'VERIFY_REPORT.md','VERIFICATION_CHECKS.json':ROOT/'VERIFICATION_CHECKS.json','FINAL_COVERAGE.json':ROOT/'FINAL_COVERAGE.json','NUMERICS_RUN_STATUS.md':NUM.parent/'RUN_STATUS.md','NUMERICS_STATE.json':NUM/'STATE.json','NUMERICS_REPORT.md':NUM.parent/'NUM_REPORT.md','NUMERICS_NEXT_STEPS.md':NUM/'NEXT_STEPS.md','VALIDATOR_STATUS.json':ROOT/'VALIDATOR_STATUS.json','THEORY_NOTES.md':LEAD/'THEORY_NOTES.md','EQUATIONS.md':LEAD/'EQUATIONS.md'}
    token=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ');dest=ROOT/'final_snapshot'/token;dest.mkdir(parents=True,exist_ok=False)
    manifest=dict(created_utc=r['date_utc'],checkpoint_coverage=r,files={},scope='Immutable final evidence snapshot. Credited elapsed time is not certified eligible numerical activity; 96-hour campaign not completed.')
    for name,source in sources.items():
        b=source.read_bytes();(dest/name).write_bytes(b);manifest['files'][name]=dict(source=str(source),snapshot=str((dest/name).relative_to(ROOT)),sha256=sha(b),bytes=len(b))
        if source.read_bytes()!=b:raise RuntimeError('Source changed while freezing: '+str(source))
    if sha(training.read_bytes())!=a.expected_training_sha:raise RuntimeError('Training ledger changed during snapshot')
    from report_snapshot_audit import snapshot_audit
    audited=snapshot_audit(dest/'CHECKPOINT_TABLE.tsv',dest/'CAMPAIGN_LEDGER.jsonl',dest/'VALIDATION_LEDGER.jsonl');(dest/'NUMERIC_AUDIT.json').write_text(json.dumps(audited,indent=2)+'\n')
    (dest/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
    (ROOT/'FINAL_SNAPSHOT.json').write_text(json.dumps(dict(path=str(dest.relative_to(ROOT)),manifest_sha256=sha((dest/'MANIFEST.json').read_bytes()),date_utc=r['date_utc'],files=manifest['files'],checkpoint_count=audited['checkpoint_count'],training_bounds=audited['ledger']['credited_elapsed_union_bounds'],combined_bounds=audited['ledger']['combined_with_validation']),indent=2)+'\n')
    print('FINAL SNAPSHOT',dest)

if __name__=='__main__':main()

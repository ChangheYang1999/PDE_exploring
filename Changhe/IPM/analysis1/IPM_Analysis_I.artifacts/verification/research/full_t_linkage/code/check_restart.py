"""Fault tests on the actual resume/output paths, retaining each input and log."""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
os.environ['PYTHONDONTWRITEBYTECODE']='1'
import hashlib,json,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
B=Path(__file__).resolve().parents[3];D=B/'research/full_t_linkage';E=D/'evidence'
assert not sys.flags.optimize

def utc():return datetime.now(timezone.utc).isoformat()
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def run(tag,kind='resume'):
 command=['python3',str(D/'code/check_coefficients.py'),'--tag',tag,'--spans','0','--resume'] if kind=='resume' else ['python3',str(D/'code/audit_coefficients.py'),'--tag',tag,'--allow-partial']
 with (E/(tag+'_test.log')).open('w') as f:result=subprocess.run(command,cwd=B,stdout=f,stderr=subprocess.STDOUT,timeout=80)
 return result.returncode

def output(tag,data):
 p=E/(tag+'_spans.jsonl');assert not p.exists();p.write_bytes(data)
 return p

started=utc();lines=(E/'smoke_spans.jsonl').read_bytes().splitlines(keepends=True)
assert len(lines)==3 and all(x.endswith(b'\n') for x in lines)
header,row,footer=map(json.loads,lines)
assert row['counts']['deboor_cox_equalities']==64
prefix=lines[0]+lines[1]
p=output('restart_ok',prefix+b'{"type":"span","unfinished":')
assert run('restart_ok')==0
newlines=p.read_bytes().splitlines(keepends=True)
assert len(newlines)==3 and b''.join(newlines[:2])==prefix and json.loads(newlines[-1])['type']=='complete'
summary=json.loads((E/'restart_ok_summary.json').read_text());assert summary['resumed_spans']==1 and summary['status']=='OPEN_PARTIAL_DIAGNOSTIC'
events=[json.loads(s) for s in (E/'restart_ok_resume_events.jsonl').read_text().splitlines()]
assert len(events)==1 and events[0]['last_saved_span']==0 and events[0]['next_span'] is None
assert run('restart_ok','audit')==0
assert json.loads((E/'restart_ok_output_audit.json').read_text())['replay_required_spans']==[0]
results={'truncated_tail_repair_preserves_complete_bytes':True,'resume_auditor_accepts_and_requires_span0_replay':True}
changed=dict(header);changed['arb_bits']=641
bad=output('restart_header_fault',(json.dumps(changed)+'\n').encode()+lines[1])
before=sha(bad);assert run('restart_header_fault')!=0 and sha(bad)==before
results['changed_header_rejected_without_write']=True
changed=json.loads(lines[1]);changed['counts']['deboor_cox_equalities']=512
bad=output('restart_count_fault',lines[0]+(json.dumps(changed)+'\n').encode())
before=sha(bad);assert run('restart_count_fault')!=0 and sha(bad)==before
results['changed_count_rejected_without_write']=True
bad=output('restart_duplicate_fault',prefix+lines[1]);before=sha(bad)
assert run('restart_duplicate_fault')!=0 and sha(bad)==before
results['duplicate_span_rejected_without_write']=True
bad=output('restart_missing_footer',prefix)
(E/'restart_missing_footer_summary.json').write_bytes((E/'smoke_summary.json').read_bytes())
assert run('restart_missing_footer','audit')!=0
results['missing_footer_auditor_rejected']=True
out={'start_utc':started,'end_utc':utc(),'status':'PASS_DIAGNOSTIC_RESTART_FAULTS','checks':results,'producer_sha256':sha(D/'code/check_coefficients.py'),'auditor_sha256':sha(D/'code/audit_coefficients.py'),'source_sha256':sha(Path(__file__)),'scope':'Diagnostic one-span stream and malformed copies only. No full coefficient membership claim.'}
(E/'restart_checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

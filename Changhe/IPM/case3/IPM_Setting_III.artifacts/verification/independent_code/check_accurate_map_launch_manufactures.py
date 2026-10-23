"""Read-only admission fixtures, no worker starts."""
from pathlib import Path
from datetime import datetime,timezone
import sys,json,subprocess,os
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
import launch_accurate_map_audit as w
V=Path('research/accurate_map_final_audit/verification');D=V/'launch_manufactures'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');D.mkdir(parents=True);P=D/'previous';P.mkdir();Q=D/'current';Q.mkdir();checks=[]
def ck(name,b):
 checks.append(dict(name=name,passed=bool(b)))
 if not b:raise AssertionError(name)
def reject(name,fun):
 try:fun()
 except (ValueError,FileNotFoundError):ck(name,True)
 else:raise AssertionError('accepted '+name)
def gate(p,status):w.put(p,dict(status=status,count=1,checks=[dict(passed=True)],bindings={}))
for name in ['JOB.json','MP_JOB.json']:w.put(P/name,dict(pid=999999999))
for folder,status in [('candidate','COMPLETE_FINITE_LARGER_NODES_REQUIRES_MP_AND_FINAL_REVIEW'),('mp','COMPLETE_LARGER_NODE_MP_REQUIRES_INDEPENDENT_FINAL_AUDIT')]:
 (P/folder).mkdir();gate(P/folder/'COMPLETE.json',status)
for name,status in [('DESIGN_ACCEPTANCE.json','ACCEPTED_FOR_FINITE_AUXILIARY_COMPUTATION'),('FINAL_DESIGN_ACCEPTANCE.json','ACCEPTED_CANDIDATE_FREE_FINAL_CHECKER_DESIGN')]:w.put(Q/name,dict(status=status,bindings={}))
for name,status in [('MANUFACTURES.json','PASS_ACCURATE_MAP_MANUFACTURES'),('RECORD_CHECKS.json','PASS_FROZEN_ACCURATE_MAP_RECORD_CONSISTENCY'),('FINAL_MANUFACTURES.json','PASS_INDEPENDENT_ACCURATE_MAP_FINAL_MANUFACTURES'),('LAUNCH_MANUFACTURES.json','PASS_ACCURATE_MAP_LAUNCH_ADMISSION'),('PROVENANCE_MANUFACTURES.json','PASS_ACCURATE_MAP_PROVENANCE_MANUFACTURES')]:gate(Q/name,status)
ck('valid synthetic read-only admission',w.admission(Q,P));(Q/'candidate').mkdir();w.put(Q/'candidate/COMPLETE.json',{});reject('already complete refused',lambda:w.admission(Q,P));(Q/'candidate/COMPLETE.json').unlink()
p=Q/'RECORD_CHECKS.json';old=p.read_bytes();d=json.loads(old);d['checks'][0]['passed']=False;w.put(p,d);reject('failed record gate refused',lambda:w.admission(Q,P));p.write_bytes(old)
d=json.loads(old);d['count']=2;w.put(p,d);reject('wrong check count refused',lambda:w.admission(Q,P));p.write_bytes(old)
t=D/'bound.txt';t.write_text('original');d=json.loads(old);d['bindings']={str(t):w.sha(t)};w.put(p,d);t.write_text('changed');reject('changed file refused',lambda:w.admission(Q,P));p.write_bytes(old)
proc=subprocess.Popen([sys.executable,'-c','import time; time.sleep(3)','run_larger_node_audit.py'])
try:
 w.put(P/'JOB.json',dict(pid=proc.pid));reject('active previous job refused',lambda:w.admission(Q,P))
finally:proc.terminate();proc.wait(timeout=5);w.put(P/'JOB.json',dict(pid=999999999))
p=P/'mp/COMPLETE.json';old=p.read_bytes();p.unlink();reject('missing MP completion refused',lambda:w.admission(Q,P));p.write_bytes(old)
for name in ['check_accurate_map_final.py','launch_accurate_map_audit.py','run_accurate_map_audit.py']:
 z=subprocess.run([sys.executable,'-O',str(Path('independent_code')/name)],capture_output=True,text=True,timeout=10);ck('optimized refusal '+name,z.returncode!=0 and 'optimized Python prohibited'in z.stderr)
bindings={str(p):w.sha(p)for p in [Path(__file__),Path(w.__file__),Path('independent_code/check_accurate_map_final.py'),Path('independent_code/run_accurate_map_audit.py'),Path('research/accurate_map_final_audit/FINAL_COVERAGE_AND_LAUNCH_PROOF.md')]}
w.put(V/'LAUNCH_MANUFACTURES.json',dict(status='PASS_ACCURATE_MAP_LAUNCH_ADMISSION',utc=w.now(),count=len(checks),checks=checks,bindings=bindings,fixture=str(D),scope='Read-only admission fixtures and optimized-Python refusals; no numerical worker started.'));print('PASS_ACCURATE_MAP_LAUNCH_ADMISSION',len(checks))

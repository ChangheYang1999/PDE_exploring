"""Short local record_attempt tests; no numerical worker, network or listener."""
from pathlib import Path
from datetime import datetime,timezone
import os,sys,json,subprocess,hashlib,copy,fcntl
if sys.flags.optimize:raise SystemExit('optimized Python prohibited')
for k in ['OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:os.environ[k]='1'
import check_accurate_map_final as f
import launch_accurate_map_audit as w
V=f.BASE;D=V/'provenance_manufactures'/datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ');D.mkdir(parents=True);checks=[]
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e))
 if not b:raise AssertionError((n,e))
def fail(n,fn):
 try:fn()
 except(AssertionError,ValueError,KeyError,FileNotFoundError)as e:ck(n,True,str(e)[:220])
 else:raise AssertionError('not refused '+n)
runner="import sys;sys.path.insert(0,'independent_code');import launch_accurate_map_audit as w;from pathlib import Path;w.record_attempt(Path(sys.argv[1]),[sys.executable,'-c',sys.argv[2]],timeout_seconds=int(sys.argv[3]))"
def attempt(p,code='pass',timeout=10800):return subprocess.run([sys.executable,'-c',runner,str(p),code,str(timeout)],capture_output=True,text=True,timeout=10)
def inputs(p):
 b=p/'input.txt';b.write_text('finite synthetic input')
 for name in ['INPUTS.json','INPUTS_SUPPLEMENT.json','INPUTS_ADDITIONAL.json']:w.put(p/name,dict(files=[dict(frozen=str(b),sha256=w.sha(b))]if name=='INPUTS.json'else[]))
 return b
P=D/'valid';P.mkdir();z=attempt(P);ck('wrapper same recorded pass child',z.returncode==0,z.stderr);b=inputs(P);a=f.Audit(P,True);ck('production provenance positive',a.provenance(P)=={b.name:str(b)})
job=json.loads((P/'JOB.json').read_text());ap=Path(job['admission_path']);pp=P/'PROCESS_POLICY.json';rp=P/'EXECUTION_RESULT.json';paths=[P/'JOB.json',ap,pp,rp,P/'INPUTS.json',b];original={p:p.read_bytes()for p in paths}
def restore():
 for p,s in original.items():p.write_bytes(s)
def setfield(p,k,value):d=json.loads(p.read_text());d[k]=value;w.put(p,d)
def rechain():
 ad=json.loads(ap.read_text());ad['policy_sha256']=w.sha(pp);w.put(ap,ad);j=json.loads((P/'JOB.json').read_text());j['admission_sha256']=w.sha(ap);w.put(P/'JOB.json',j);r=json.loads(rp.read_text());r['admission_sha256']=w.sha(ap);w.put(rp,r)
def mutation(name,fun):
 try:fun();fail(name,lambda:f.Audit(P,True).provenance(P))
 finally:restore()
for code in [7,124]:mutation('returncode refused '+str(code),lambda code=code:setfield(rp,'returncode',code))
mutation('admission digest refused',lambda:setfield(P/'JOB.json','admission_sha256','0'*64))
for field,value in [('nice',0),('memory_limit_bytes',16*1024**3),('timeout_seconds',999),('schema','other')]:
 def change(field=field,value=value):setfield(pp,field,value);rechain()
 mutation('policy field refused '+field,change)
mutation('driver hash refused',lambda:setfield(rp,'driver_sha256','0'*64))
mutation('start time refused',lambda:setfield(rp,'started_utc','2026-10-20T00:00:00+00:00'))
mutation('missing execution result refused',lambda:rp.unlink())
mutation('input changed refused',lambda:b.write_text('changed'))
for field,value in [('nice',0),('memory_limit_bytes',1),('lock_held',False),('wrapper_pid',999999999)]:
 def change(field=field,value=value):setfield(ap,field,value);rechain()
 mutation('attempt field refused '+field,change)
proc=subprocess.Popen([sys.executable,'-c','import time;time.sleep(3)','accurate_map'])
try:mutation('actual live accurate_map PID refused',lambda:setfield(P/'JOB.json','pid',proc.pid))
finally:proc.terminate();proc.wait(timeout=5)
setfield(pp,'nice',0);z=attempt(P);ck('wrapper changed stable policy refused',z.returncode!=0 and'changed stable process policy'in z.stderr);restore()
lock=(P/'execution.lock').open('a+b');fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
try:z=attempt(P);ck('wrapper actual held lock refused',z.returncode!=0 and'BlockingIOError'in z.stderr)
finally:lock.close()
for name,code,timeout,expected in [('failed','raise SystemExit(7)',10800,7),('timeout','import time;time.sleep(2)',1,124)]:
 p=D/name;p.mkdir();z=attempt(p,code,timeout);inputs(p);r=json.loads((p/'EXECUTION_RESULT.json').read_text());ck('wrapper actual '+name+' result',r['returncode']==expected);fail('production rejects actual '+name,lambda:f.Audit(p,True).provenance(p))
# Reuse the positive path after every refusal; altered record bytes were restored.
ck('positive provenance after restored mutations',f.Audit(P,True).provenance(P)=={b.name:str(b)})
# Exercise the exact production chronology with both timestamp constructors.
from datetime import timedelta
import accurate_map_stage as stage
t0=w.now();t1=stage.now();t2=stage.now();t3=w.now();ad={'started_utc':t0};res={'finished_utc':t3};cand={'started_utc':t1,'finished_utc':t2}
a=f.Audit(P,True);a.chronology(ad,res,cand);ck('production mixed constructors chronology accepted',a.checks[-1]['passed'])
early=dict(cand,started_utc=(datetime.fromisoformat(t0)-timedelta(seconds=1)).isoformat());late=dict(cand,finished_utc=(datetime.fromisoformat(t3)+timedelta(seconds=1)).isoformat())
fail('worker before admission refused',lambda:f.Audit(P,True).chronology(ad,res,early))
fail('worker finish beyond wrapper refused',lambda:f.Audit(P,True).chronology(ad,res,late))
bindings={str(p):w.sha(p)for p in [Path(__file__),Path(f.__file__),Path(w.__file__),Path('independent_code/run_accurate_map_audit.py'),f.ROOT/'FINAL_PROVENANCE_AND_COVERAGE_PROOF.md',f.ROOT/'CHRONOLOGY_MANUFACTURE_PROOF.md']}
w.put(V/'PROVENANCE_MANUFACTURES.json',dict(status='PASS_ACCURATE_MAP_PROVENANCE_MANUFACTURES',utc=w.now(),count=len(checks),checks=checks,bindings=bindings,fixture=str(D),scope='Same production record_attempt and provenance functions on short harmless Python children. No numerical worker or server. Process records are not OS attestation.'));print('PASS_ACCURATE_MAP_PROVENANCE_MANUFACTURES',len(checks))

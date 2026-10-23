"""Replayable failure preservation checks in a temporary directory inside this lane."""
from pathlib import Path
from datetime import datetime,timezone
from tempfile import TemporaryDirectory
import hashlib,json,math
import check_residual_fraction_arithmetic as m
R=Path('research/hydrostatic_common_residual_audit');V=R/'verification';checks=[]
def ck(n,b):
 checks.append(dict(name=n,passed=bool(b)))
 if not b:raise AssertionError(n)
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
started=datetime.now(timezone.utc).isoformat()
with TemporaryDirectory(dir=V,prefix='fraction_io_')as root:
 root=Path(root);p=root/'gate.json';one={'status':'PASS','value':1};bad={'status':'FAIL','value':math.inf};two={'status':'PASS','value':2}
 m.write_gate(p,one);old=p.read_bytes();m.write_gate(p,bad)
 fails=list(root.glob('gate.failed.*.json'));archive=root/('gate.previous.'+hashlib.sha256(old).hexdigest()+'.json')
 ck('exclusive failure record',len(fails)==1);ck('previous bytes unchanged',archive.read_bytes()==old);ck('nonfinite diagnostic retained',json.loads(fails[0].read_text())['value']=='inf');ck('canonical means latest attempt',json.loads(p.read_text())['status']=='FAIL')
 failed=p.read_bytes();m.write_gate(p,two)
 ck('failed snapshot preserved',fails[0].read_bytes()==failed);ck('canonical recovered PASS',json.loads(p.read_text())==two)
 ck('failure also archived', (root/('gate.previous.'+hashlib.sha256(failed).hexdigest()+'.json')).read_bytes()==failed)
 m.write_gate(p,one);m.write_gate(p,two);ck('identical previous archive reused',archive.read_bytes()==old)
 ck('no staging files remain',not list(root.glob('*.staging.*')))
 # A deliberately damaged existing archive must not replace the current gate.
 current=p.read_bytes();a=root/('gate.previous.'+hashlib.sha256(current).hexdigest()+'.json');a.write_text('damaged test archive')
 try:m.write_gate(p,bad);rejected=False
 except OSError:rejected=True
 ck('corrupt archive rejected',rejected);ck('corruption leaves canonical intact',p.read_bytes()==current)
# Context must identify only an ongoing point evaluation.
nb=math.sqrt(2249/512)+5/16
stored=dict(W=[13/8,1/4],parts=[13/32,5/16],Rh=13/32,Nf=33/32,Nv=43/32,Nbound=nb,Rf=13/33,Rv=13/43,Rbound=(13/32)/nb)
record=(17,.5,.25,3,[5/16,1/4,5/4,0],[1/8,-1/2],stored)
m.audit_group('context_success',[record],1);ck('successful group clears point context',m.current_context=={})
try:m.audit_group('wrong_count',[record],2);rejected=False
except AssertionError:rejected=True
ck('nonpoint count failure has empty context',rejected and m.current_context=={})
bad=dict(stored);bad['Rh']=1;record=record[:-1]+(bad,)
try:m.audit_group('context_failure',[record],1);rejected=False
except AssertionError:rejected=True
ck('point failure retains actual point',rejected and m.current_context==dict(group='context_failure',index=17,x=.5,y=.25))
out=dict(started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),status='PASS',count=len(checks),checks=checks,bindings={p:sha(p)for p in [__file__,'independent_code/check_residual_fraction_arithmetic.py','independent_code/rational_residual_arithmetic.py',str(R/'FRACTION_CONTEXT_CLOSURE_PROOF.md')]})
m.write_gate(V/'FRACTION_IO_MANUFACTURES.json',out);print('PASS',len(checks),out['finished_utc'])

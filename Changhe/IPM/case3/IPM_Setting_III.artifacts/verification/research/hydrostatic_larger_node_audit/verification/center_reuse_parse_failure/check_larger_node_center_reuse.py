from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib
R=Path('research/hydrostatic_larger_node_audit');V=R/'verification';checks=[];bindings={};sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ck(n,b,e=None):
 checks.append(dict(name=n,passed=bool(b),evidence=e));assert b,(n,e)
def bind(p,h=None):
 p=str(p);v=sha(p);ck('binding '+p,(h is None or h==v)and(p not in bindings or bindings[p]==v));bindings[p]=v;return Path(p)
for p in [__file__,R/'CENTER_REUSE_PROOF.md']:bind(p)
i=json.loads(bind(V/'INPUTS.json').read_text());out=[]
for N,root in [(224,'hydrostatic_c2_resolved_224_audit'),(192,'hydrostatic_n192_polynomial_application')]:
 v=Path('research')/root/'verification';a=json.loads(bind(v/'FINAL_BINDINGS.json').read_text())
 if N==224:
  ck('224 prior complete finite verdict',a['status']=='PASS_SCOPED_N224_AUXILIARY_AUDIT'and a['count']==len(a['checks'])and all(z['passed']for z in a['checks']))
  for p,h in a['bindings'].items():bind(p,h)
 else:
  ck('192 prior final binding status',a['status']=='PASS')
  for z in a['files']:bind(z['path'],z['sha256'])
  c=json.loads(bind(v/'CHECKS.json').read_text());ck('192 application456',c['status']=='PASS'and c['count']==456 and all(z['passed']for z in c['checks']))
  for z in json.loads(bind(v/'SOURCE_BINDINGS.json').read_text())['files']:bind(z['frozen'],z['sha256'])
 p=v/f'hsG_c2.0_N{N}_log.json';d=json.loads(bind(p).read_text());state=next(s for s in i['states']if s['N']==N);bind(state['path'],state['sha256']);ck('same exact defining state '+str(N),d['source_sha256']==state['sha256']and d['status']=='DONE')
 aa,cH,D=[F(d['exact'][k])for k in ['a','cH','delta']];ck('nonzero a and exact center defect '+str(N),aa!=0 and 1+cH==D and D!=0);limit=abs(D)/(abs(1+D)+1);printed=F('3.279e-5'if N==224 else'3.228e-5');ck('printed core maximum differs from exact limit '+str(N),abs(printed-limit)>F(5,10**9))
 out.append(dict(N=N,state_sha256=state['sha256'],exact_a=str(aa),exact_cH=str(cH),exact_delta=str(D),exact_core_axis_limit=str(limit),a=float(aa),cH=float(cH),delta=float(D),core_axis_limit=float(limit),producer_printed_core_maximum=float(printed),producer_core_to_limit=float(printed/limit)))
for p,h in bindings.items():ck('stable '+p,sha(p)==h)
a=dict(status='PASS_EXACT_CENTER_REUSE',utc=datetime.now(timezone.utc).isoformat(),count=len(checks),checks=checks,bindings=bindings,results=out,scope='Exact center data for the same finite auxiliary states. No continuum sequence or full-plane endpoint.')
(V/'CENTER_REUSE_CHECKS.json').write_text(json.dumps(a,indent=2)+'\n');print(a['status'],len(checks));print(json.dumps([{k:v for k,v in z.items()if not k.startswith('exact_')}for z in out],indent=2))

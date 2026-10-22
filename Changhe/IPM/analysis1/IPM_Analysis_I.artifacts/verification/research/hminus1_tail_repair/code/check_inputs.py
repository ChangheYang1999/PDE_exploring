"""Join two exact audits, verify frozen dependencies and every original row entry.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import audit_from_json as A,audit_from_npz as N
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/hminus1_tail_repair';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
start=time.monotonic();files={};dependencies={}
for topic,expected in [('normalized_tail_repair','CONFIRMED_EXACT_NORMALIZED_TAIL_REPAIR_WITH_L2_RESIDUAL'),('outer_majorant','CONFIRMED')]:
 p=B/'research'/topic/'evidence/verdict.json';v=load(p);assert v['status']==expected,(topic,v['status']);files[str(p.relative_to(B))]=sha(p)
 for f,h in v['files'].items():assert sha(B/f)==h,f;files[f]=h
 dependencies[topic]={'status':v['status'],'verdict_sha256':sha(p),'pins_checked':len(v['files'])}
a=A.evaluate();n=N.evaluate();assert a['exact']==n['exact'];raw=load(B/'data_exact/modal_v2.json')
assert all(x==A.dec(h) for x,h in zip(n.pop('outer_exact'),raw['arrays']['Aout']['hex'],strict=True))
assert all(x==A.dec(h) for x,h in zip(n.pop('knots_exact'),raw['arrays']['knots']['hex'],strict=True))
public={'k':['0.17936052','0.17936054'],'a1':['-0.641279','-0.641278'],'a2':['-1.461919','-1.461918'],'d':['-1.820640','-1.820639'],'a3':['-2.282558','-2.282557']}
for key,(lo,hi) in public.items():assert F(lo)<F(a['exact'][key])<F(hi),(key,a['exact'][key])
# Avoid duplicating an exact coefficient table; expose a hash of the fully
# checked product table and 8 representative entries, with replayable sources.
table=n.pop('product_table');n['product_table_sha256']=hashlib.sha256(json.dumps(table,sort_keys=True).encode()).hexdigest();n['product_witnesses']=[table[i] for i in (0,1,2,10,11,12,98,99)]
pf=load(E/'proof_first.json');assert pf['sha256']==sha(D/'PROOF.md')
for p in [D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json']+list((D/'code').glob('*.py'))+list((D/'source').glob('*.json')):files[str(p.relative_to(B))]=sha(p)
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'PASS_TWO_EXACT_INPUT_EXPONENT_AND_ANGULAR_IDENTITY_AUDITS','outputs':{'exact_json':a,'exact_npz':n},'strict_public_exponent_intervals':public,'dependencies':dependencies,'files':dict(sorted(files.items())),'seconds':time.monotonic()-start,'scope':'Exact original data and all finite exponent/resonance/angular-derivative conditions. No new angular convolution or numerical C2,Cd,residual-norm ceiling. Analytic theorem requires proof plus actualreview.'}
(E/'inputs.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'utc':out['utc'],'status':out['status'],'counts':{'json':a['counts'],'npz':n['counts']},'dependencies':dependencies,'seconds':out['seconds']}))

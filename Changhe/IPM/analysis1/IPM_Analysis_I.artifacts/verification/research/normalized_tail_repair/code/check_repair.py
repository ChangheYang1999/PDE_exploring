"""Two independent finite quotient norms, all coefficient comparisons and exact pins.
No JS/TS, servers/listeners/tunnels, RLScience or Lean/Lake.
"""
import os
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
import sys,json,hashlib,time
from pathlib import Path
from fractions import Fraction as F
from datetime import datetime,timezone
import engine_arb as A,engine_iv as I
assert not sys.flags.optimize
B=Path(__file__).resolve().parents[3];D=B/'research/normalized_tail_repair';E=D/'evidence'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):return json.loads(p.read_text())
def ends(b):lo,hi=F(b['lower_exact']),F(b['upper_exact']);assert lo<=hi;return lo,hi
start=time.monotonic();v=load(B/'research/outer_leading_cancellation/evidence/verdict.json');assert v['status']=='CONFIRMED';files={}
for p,h in v['files'].items():assert sha(B/p)==h,p;files[p]=h
vp=B/'research/outer_leading_cancellation/evidence/verdict.json';files[str(vp.relative_to(B))]=sha(vp)
Aout,aq=A.evaluate();Iout,iq=I.evaluate();assert Aout['scalars']==Iout['scalars'];checks=0
for j,(ab,ib) in enumerate(zip(aq,iq,strict=True)):
 al,ah=ends(A.box(ab));il,ih=ends(I.box(ib));assert max(al,il)<=min(ah,ih),('quotient',j);checks+=1
scalarchecks=0
for key in Iout['values']:
 al,ah=ends(Aout['values'][key]);il,ih=ends(Iout['values'][key]);assert max(al,il)<=min(ah,ih),('scalar',key);scalarchecks+=1
for source in (Aout,Iout):assert files[source['source']['path']]==source['source']['sha256']
for p in list((D/'code').glob('*.py'))+list((D/'source').glob('*.json'))+[D/'PROOF.md',D/'ADDENDUM.md',E/'proof_first.json']:files[str(p.relative_to(B))]=sha(p)
pf=load(E/'proof_first.json');assert pf['sha256']==sha(D/'PROOF.md')
Clo,Chi=ends(Aout['values']['C']);C_integer=Chi.numerator//Chi.denominator+1
out={'utc':datetime.now(timezone.utc).isoformat(),'status':'COMPUTED_TWO_METHOD_NORMS_REQUIRES_EXACT_OUTPUT_AUDIT','outputs':{'arb512':Aout,'iv180':Iout},'counts':{'all_quotient_interval_overlaps_diagnostic':checks,'scalar_interval_overlaps_diagnostic':scalarchecks},'suggested_strict_integer_C_ceiling':str(C_integer),'widths':{method:{key:str(ends(obj['values'][key])[1]-ends(obj['values'][key])[0]) for key in ('raw_N','raw_I','N','I_H','C')} for method,obj in (('arb512',Aout),('iv180',Iout))},'files':dict(sorted(files.items())),'seconds':time.monotonic()-start,'scope':'All quotient coefficients and global coefficient L1 bound; algebraic divisibility is proved in PROOF, never inferred from zero containment. No stationary profile or finite L2 residual norm.'}
(E/'checks.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:out[k] for k in ('utc','status','counts','suggested_strict_integer_C_ceiling','seconds')}));print(json.dumps({k:b['display'] for k,b in Aout['values'].items() if k in ('N','I_H','C','B','J_b')}))

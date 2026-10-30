from pathlib import Path
from datetime import datetime,timezone
import importlib.util,json,hashlib,sys,time
from flint import fmpq as Q
sys.set_int_max_str_digits(0)
B=Path(__file__).resolve().parents[1];R=B.parent;helper=R/'weak_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('compact_tail_polar',helper);M=importlib.util.module_from_spec(spec);spec.loader.exec_module(M)
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
start=time.monotonic();rows=[]
for name,src in [('007',R/'taylor_projection/source/canonical007.json'),('013',R/'new_successor_weak/data/013/canonical.json'),('014',R/'new_successor_weak/data/014/canonical.json')]:
 state=json.loads(src.read_text());c,delta,rho,stream=M.fields(state)
 assert all(((i-j)*delta/2).denominator!=1 for i in range(1,17) for j in range(1,i))
 lower=[];first=None
 for ell in range(1,9):
  a=ell*delta/2
  rr={n:-a*p(Q(1))-p.derivative()(Q(1)) for (j,n),p in rho.items() if j+1==ell}
  ss={m:-a*p(Q(1))-p.derivative()(Q(1)) for (j,m),p in stream.items() if j+1==ell}
  rr={n:q for n,q in rr.items() if q};ss={m:q for m,q in ss.items() if q}
  if rr:
   first=ell;break
  assert not ss
  lower.append(ell)
 assert first is not None
 e=1-first*delta-2;gamma=1/c;assert e>gamma-4 and c*e-1!=0
 residual={str(n):str((c*e-1)*q) for n,q in rr.items()}
 row={'candidate':name,'canonical_sha256':sha(src),'c_exact':str(c),'delta_exact':str(delta),'first_density_descendant_branch':first,'lower_density_and_stream_descendants_zero':lower,'exponent_exact':str(e),'exterior_threshold_exact':str(gamma-4),'strict_exponent_gap_exact':str(e-(gamma-4)),'density_coefficients_exact':{str(n):str(q) for n,q in rr.items()},'residual_coefficients_exact':residual,'different_branch_nonresonance':True,'compact_correction_obstruction':True}
 rows.append(row);print(name,'first descendant',first,'exponent',float(e),'gap',float(e-gamma+4),'nonzero modes',len(rr),flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'inputs':{str(p):sha(p) for p in [helper,B/'PROOF.md',Path(__file__)]},'rows':rows,'elapsed_seconds':time.monotonic()-start,'status':'Exact coefficient checks passed; general exterior proof and candidate application await independent Opus review'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print('DONE',out['utc'],'seconds',out['elapsed_seconds'],flush=True)

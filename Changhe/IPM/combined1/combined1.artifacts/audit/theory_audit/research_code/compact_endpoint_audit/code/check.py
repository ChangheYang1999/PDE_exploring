from pathlib import Path
from collections import defaultdict
from datetime import datetime,timezone
import hashlib,json,sys,time
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0);ctx.prec=512
B=Path(__file__).resolve().parents[1];R=B.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ar=lambda q:arb(q.numerator)/q.denominator
def put(d,n,v):
 if n<0:n,v=-n,-v
 if n and v:
  d[n]=d.get(n,Q(0))+v
  if not d[n]:del d[n]
def density(pot,d):
 out={}
 for n,A in pot.items():
  put(out,n+1,-A*(d*d-n*n)*(d-2-n)/2)
  put(out,n-1,+A*(d*d-n*n)*(d-2+n)/2)
 return out
def enc(d):return {str(k):str(v) for k,v in sorted(d.items())}
start=time.monotonic();peer=json.loads((B/'source/T2_result.json').read_text())['C'];rows=[]
for name in ['007','013','014']:
 src=R/'taylor_projection/source/canonical007.json' if name=='007' else R/f'new_successor_weak/data/{name}/canonical.json'
 data=json.loads(src.read_text());c=Q(data['cl']);assert c==Q(4076476460239181,2251799813685248)
 gamma=1/c;delta=1-gamma;p=(3+gamma)/2
 assert all(((ell-1)*delta/2).denominator!=1 for ell in range(2,17))
 pot=[defaultdict(lambda:Q(0)),defaultdict(lambda:Q(0))]
 for (j,m,k),value in zip(data['order'],data['coefficients'],strict=True):
  if j==0:
   a=Q(value);pot[0][2*m]+=a;pot[1][2*m]+=a*(p-k)*(p-k-1)/2
 T0=density(pot[0],3+gamma);T2=density(pot[1],gamma-1)
 F={n:-4*c*v for n,v in T2.items()};P={}
 for n,v in T0.items():
  put(P,n+2,v*(gamma+n)/2);put(P,n-2,v*(gamma-n)/2)
 dot=lambda x,y:sum((v*y.get(n,Q(0)) for n,v in x.items()),Q(0))
 lam=dot(F,P)/dot(P,P);res={n:F.get(n,Q(0))-lam*P.get(n,Q(0)) for n in set(F)|set(P)};res={n:v for n,v in res.items() if v}
 assert res and peer[name]['R2_proportional'] is False
 n0=min(P);det=next((n,F.get(n0,Q(0))*P.get(n,Q(0))-F.get(n,Q(0))*P[n0]) for n in sorted(set(F)|set(P)) if F.get(n0,Q(0))*P.get(n,Q(0))-F.get(n,Q(0))*P[n0])
 norms={'F_norm':(arb.pi()*ar(dot(F,F))).sqrt(),'P_norm':(arb.pi()*ar(dot(P,P))).sqrt(),'relative_residual':ar(dot(res,res)/dot(F,F)).sqrt(),'lambda':ar(lam)}
 fields={'F_norm':'R2_F12_norm','P_norm':'R2_dipole_norm','relative_residual':'R2_rel_residual','lambda':'R2_lambda_float'}
 for own,their in fields.items():assert abs(float(norms[own])/peer[name][their]-1)<1e-12
 exact={'candidate':name,'source':str(src),'source_sha256':sha(src),'c':str(c),'Theta0':enc(T0),'Theta12':enc(T2),'F12':enc(F),'P':enc(P),'lambda':str(lam),'projection_residual':enc(res),'nonzero_determinant':{'modes':[n0,det[0]],'value':str(det[1])}}
 dst=B/f'data/{name}_endpoint.json'
 with dst.open('x') as f:json.dump(exact,f,indent=2);f.write('\n')
 rows.append({'candidate':name,'exact_data_sha256':sha(dst),'nonproportional':True,'nonzero_witness_modes':[n0,det[0]],**{k:v.str(100) for k,v in norms.items()},'all_peer_float_comparisons_pass':True})
 print(name,{k:v.str(20) for k,v in norms.items()},flush=True)
out={'utc':datetime.now(timezone.utc).isoformat(),'rows':rows,'proof_sha256':sha(B/'PROOF.md'),'code_sha256':sha(Path(__file__)),'peer_result_sha256':sha(B/'source/T2_result.json'),'elapsed_seconds':time.monotonic()-start,'verdict':'CONFIRMED exact endpoint constraint and independent candidate coefficient test'}
with (B/'verification/result.json').open('x') as f:json.dump(out,f,indent=2);f.write('\n')
print(out['utc'],out['elapsed_seconds'],flush=True)

from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
import json,sys,hashlib,time,importlib.util
from flint import fmpq as Q,arb,ctx
sys.set_int_max_str_digits(0)
ROOT=Path(__file__).resolve().parents[1]
helper=ROOT.parent/'localized_probe_audit/code/reproduce.py'
spec=importlib.util.spec_from_file_location('large_weak_polar',helper);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T,W,Z=m.T,m.W,m.ZERO
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
@lru_cache(None)
def beta0(b,M):
 b=Q(b);assert b>-1 and M>=0
 return (m.ar(b+1).lgamma()+arb(M+1).lgamma()-m.ar(b+M+2).lgamma()).exp()
def integral(P,b,M):
 val=beta0(str(b),M);out=arb(0)
 for j,p in enumerate(P(W)):
  out+=m.ar(p)*val
  val*=m.ar((b+j+1)/(b+j+M+2))
 return out
def maximum(j,b):
 if j==0:return arb(1)
 return m.ar(Q(j)/(j+b))**j*m.ar(b/(j+b))**m.ar(b)
def run():
 start=time.monotonic();ctx.prec=2048
 src=ROOT/'data/state131_canonical.json';peerpath=ROOT/'source/N4_state131_scale_scan_2048.json';velpath=ROOT/'source/velocity_results.json'
 peer=json.loads(peerpath.read_text());assert peer['source_sha256']==sha(src)
 vc={Q(r['a']):Q(r['C']) for r in json.loads(velpath.read_text())['rows'] if r['all_checks_pass']}
 c,delta,rho,stream=m.fields(json.loads(src.read_text()));bg,_=m.square_groups(stream,delta,2);cg,_=m.square_groups(rho,delta,1)
 out={'utc':datetime.now(timezone.utc).isoformat(),'precision_bits':ctx.prec,'candidate':'state131','source_sha256':sha(src),'peer_sha256':sha(peerpath),'velocity_certificate_sha256':sha(velpath),'code_sha256':sha(__file__),'helper_sha256':sha(helper),'proof_sha256':sha(ROOT/'PROOF.md'),'method':'independent polar weak equation with log-gamma beta integrals','rows':[]}
 pairs={}
 for ref in peer['rows']:
  a=Q(ref['a']);k=ref['k'];CU=m.ar(vc[a]);assert vc[a]==Q(ref['C_U'])
  lk=3*c+1+2*c*k*W-4*c*T;gk=1+2*k*W+4*T
  if k not in pairs:
   linear=-arb.pi()/2*sum((integral(R*lk,(j+1)*delta/2-1,k+1) for (j,n),R in rho.items() if n==1),arb(0))
   ng={};hk=1+2*k*W-4*T
   for (j,nm),S in stream.items():
    DS=m.td(S,(j+1)*delta/2,2)
    for (i,n),R in rho.items():
     if abs(n-nm)!=1:continue
     sig=1 if n>nm else -1
     ng[i+j]=ng.get(i+j,Z)+R*(sig*nm*S*hk-DS)
   nonlinear=arb.pi()/4*sum((integral(V,(j+2)*delta/2-1,k+1) for j,V in ng.items()),arb(0))
   pairs[k]=linear+nonlinear
  pair=pairs[k];I=abs(pair);assert I>0
  A2=arb.pi()/2*integral(lk*lk,1-a,2*k+1)
  B2=arb.pi()/2*sum((integral(V*gk*gk,1+(j+2)*delta/2-a,2*k+1) for j,V in bg.items()),arb(0))
  C2=arb.pi()/2*sum((integral(V,1+(j+2)*delta/2-a,2*k+1) for j,V in cg.items()),arb(0))
  assert A2>0 and B2>0 and C2>0
  A,B,C=A2.sqrt(),B2.sqrt(),C2.sqrt();D=A+B+CU*C
  H=arb(1) if k==0 and a<=Q(3,2) else maximum(k,2-a)+2*k*maximum(k,3-a)+4*maximum(k+1,2-a)
  radius=2*I/(D+(D*D+4*CU*H*I).sqrt());assert radius>0
  vals={'pairing':pair,'A':A,'B_upper':B,'C_upper':C,'D':D,'gradient_sup_upper':H,'weighted_L2_radius_lower':radius}
  comparisons={key:bool(v.overlaps(arb(ref[key]))) for key,v in vals.items()};assert all(comparisons.values()),(a,k,comparisons)
  out['rows'].append({'a':str(a),'k':k,'C_U':str(vc[a]),**{key:v.str(100) for key,v in vals.items()},'comparisons':comparisons})
  out['elapsed_seconds']=time.monotonic()-start
  (ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
 print('All',len(out['rows']),'rows agree; seconds',out['elapsed_seconds'],flush=True)
 for a in vc:
  rows=[r for r in out['rows'] if Q(r['a'])==a]
  if rows:
   best=max(rows,key=lambda r:arb(r['weighted_L2_radius_lower']).lower());print('a',a,'k',best['k'],'radius',best['weighted_L2_radius_lower'],flush=True)
if __name__=='__main__':run()

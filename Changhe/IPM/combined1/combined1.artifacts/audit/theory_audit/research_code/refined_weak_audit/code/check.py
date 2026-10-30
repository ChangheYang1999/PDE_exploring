from pathlib import Path
from datetime import datetime,timezone
from functools import lru_cache
from fractions import Fraction
import json,hashlib,time,importlib.util
from flint import fmpq as Q,arb,ctx
ROOT=Path(__file__).resolve().parents[1]
path=ROOT.parent/'large_scale_weak_audit/code/check.py'
spec=importlib.util.spec_from_file_location('loggamma_weak',path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
T,W,Z=m.T,m.W,m.Z
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
start=time.monotonic();ctx.prec=2048
claims=json.loads((ROOT/'data/claims.json').read_text());prepared={};out={'utc':datetime.now(timezone.utc).isoformat(),'code_sha256':sha(__file__),'helper_sha256':sha(path),'proof_sha256':sha(ROOT/'PROOF.md'),'peer_review_sha256':sha(ROOT/'source/T2_REVIEW.md'),'claims_sha256':sha(ROOT/'data/claims.json'),'precision_bits':ctx.prec,'rows':[]}
for claim in claims:
 name=claim['candidate'];a=Q(claim['a']);k=claim['k'];src=ROOT/'data'/f'{name}_canonical.json'
 if name not in prepared:
  c,delta,rho,stream=m.m.fields(json.loads(src.read_text()));bg,_=m.m.square_groups(stream,delta,2);cg,_=m.m.square_groups(rho,delta,1)
  prepared[name]=(c,delta,rho,stream,bg,cg)
 c,delta,rho,stream,bg,cg=prepared[name];CU=m.m.ar(Q(2) if a==1 else Q(808233,500000))
 lk=3*c+1+2*c*k*W-4*c*T;gk=1+2*k*W+4*T
 linear=-arb.pi()/2*sum((m.integral(R*lk,(j+1)*delta/2-1,k+1) for (j,n),R in rho.items() if n==1),arb(0));ng={};hk=1+2*k*W-4*T
 for (j,nm),S in stream.items():
  DS=m.m.td(S,(j+1)*delta/2,2)
  for (i,n),R in rho.items():
   if abs(n-nm)==1:ng[i+j]=ng.get(i+j,Z)+R*((1 if n>nm else -1)*nm*S*hk-DS)
 pair=linear+arb.pi()/4*sum((m.integral(V,(j+2)*delta/2-1,k+1) for j,V in ng.items()),arb(0));I=abs(pair);assert I>0
 A2=arb.pi()/2*m.integral(lk*lk,1-a,2*k+1)
 B2=arb.pi()/2*sum((m.integral(V*gk*gk,1+(j+2)*delta/2-a,2*k+1) for j,V in bg.items()),arb(0))
 C2=arb.pi()/2*sum((m.integral(V,1+(j+2)*delta/2-a,2*k+1) for j,V in cg.items()),arb(0));assert A2>0 and B2>0 and C2>0
 A,B,C=A2.sqrt(),B2.sqrt(),C2.sqrt();D=A+B+CU*C;H=arb(1) if k==0 else m.maximum(k,2-a)+2*k*m.maximum(k,3-a)+4*m.maximum(k+1,2-a)
 radius=2*I/(D+(D*D+4*CU*H*I).sqrt());assert radius>m.m.ar(Q(str(Fraction(claim['strict_lower']))))
 vals={'pairing':pair,'A':A,'B_upper':B,'C_upper':C,'D':D,'gradient_sup_upper':H,'weighted_L2_radius_lower':radius}
 out['rows'].append({**claim,'source_sha256':sha(src),**{key:v.str(100) for key,v in vals.items()},'strict_lower_confirmed':True});out['elapsed_seconds']=time.monotonic()-start
 (ROOT/'verification/results.json').write_text(json.dumps(out,indent=2)+'\n')
 print(name,a,k,radius.str(35),'seconds',out['elapsed_seconds'],flush=True)

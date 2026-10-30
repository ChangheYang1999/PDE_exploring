from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import fmpq as Q,fmpq_poly as P,arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'weak_probe_audit/code'))
from reproduce import fields,ar
ctx.prec=1024
start=time.monotonic();src=ROOT/'data/state131.json';c,delta,rho,stream=fields(json.loads(src.read_text()))
U=P([1,-1]);Z=P([]);ryp={};up={}
for (j,n),v in rho.items():ryp[j]=ryp.get(j,Z)+n*v
for (j,n),v in stream.items():up[j]=up.get(j,Z)-n*v
ryp={j:v(U) for j,v in ryp.items()};up={j:v(U) for j,v in up.items()}
def at(x):
 u=1/(1+x*x);powers={j:ar(u)**ar((j+1)*delta/2) for j in set(ryp)|set(up)}
 ry=sum((powers[j]*ar(v(u)) for j,v in ryp.items()),arb(0))
 ux=ar(x)*sum((powers[j]*ar(v(u)) for j,v in up.items()),arb(0))
 return ry,ux
specs=[('6/5','1/4','3/2',-2),('13/10','1','5',0),('7/5','4','23',2),('3/2','16','135',4),('31/20','4096',None,12),('8/5','4096',str(2**24),12)]
rows=[];tested=0
for sa,sR,sx,end in specs:
 a,R=Q(sa),Q(sR)
 xs=[Q(sx)] if sx else [Q(k)*Q(2)**e/16 for e in range(12,29) for k in range(16,32)]
 for x in xs:
  ry,ux=at(x);tested+=1
  z=ar(c*x*x)+ar(x)*ux;theta=(abs(ry)-ry)/2;drift=ar(a)*z/ar(R*R+x*x);excess=drift+theta-ar(c+1)
  if z>0 and excess>0:
   row={'a':str(a),'R_endpoint':str(R),'point':[str(x),'0'],'rho_y':ry.str(95),'U1':ux.str(95),'V_dot_X':z.str(95),'weight_drift':drift.str(95),'theta':theta.str(95),'excess':excess.str(95),'covered_dyadic_exponents':list(range(-4,end+1)),'all_positive_R_at_most_endpoint':True};rows.append(row)
   print(sa,sR,'x',x,'excess',excess.str(25),'covered',len(row['covered_dyadic_exponents']),flush=True);break
 else:raise AssertionError(('No endpoint witness',sa,sR))
assert sum(len(r['covered_dyadic_exponents']) for r in rows)==58
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(),'source_sha256':sha(src),'proof_sha256':sha(ROOT/'PROOF.md'),'code_sha256':sha(Path(__file__)),'helper_sha256':sha(ROOT.parent/'weak_probe_audit/code/reproduce.py'),'precision_bits':ctx.prec,'number_of_tested_points':tested,'rows':rows,'elapsed_seconds':time.monotonic()-start}
(ROOT/'verification/endpoints_1024.json').write_text(json.dumps(out,indent=2)+'\n');print('complete',out['elapsed_seconds'],flush=True)

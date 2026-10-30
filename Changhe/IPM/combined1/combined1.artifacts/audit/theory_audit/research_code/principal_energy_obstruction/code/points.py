from pathlib import Path
from datetime import datetime,timezone
import sys,json,time,hashlib
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT.parent/'weak_probe_audit/code'))
from reproduce import fields,rat,ar
ctx.prec=1024
start=time.monotonic();src=ROOT/'data/state131.json';c,delta,rho,stream=fields(json.loads(src.read_text()))
rows=[]
for aa,rr,xx in [('6/5','1/8','1'),('6/5','1/4','3/2'),('13/10','1/2','21/8'),('13/10','1','5'),('7/5','2','11'),('7/5','4','23'),('3/2','16','135')]:
 a,R,x=map(rat,[aa,rr,xx]);r2=x*x;t=r2/(1+r2);u=1/(1+r2)
 power={j:ar(u)**ar((j+1)*delta/2) for j,n in rho}
 ry=sum((power[j]*n*ar(v(t)) for (j,n),v in rho.items()),arb(0))
 ur=-ar(x)*sum((power[j]*n*ar(v(t)) for (j,n),v in stream.items()),arb(0))
 b=ar(a)*(ar(c*r2)+ar(x)*ur)/ar(R*R+r2)
 theta=(abs(ry)-ry)/2;lam=b+theta;excess=lam-ar(c+1)
 assert excess>0
 rows.append({'a':str(a),'R':str(R),'point':[str(x),'0'],'rho_x':'0','rho_y':ry.str(90),'U1':ur.str(90),'U2':'0',
              'weight_drift':b.str(90),'theta_X':theta.str(90),'lambda':lam.str(90),'excess_over_c_plus_one':excess.str(90),
              'strict_energy_obstruction':True})
 print(a,R,x,excess.str(24),flush=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':'state131','c':str(c),'precision_bits':ctx.prec,
     'source_sha256':sha(src),'code_sha256':sha(Path(__file__)),'helper_sha256':sha(ROOT.parent/'weak_probe_audit/code/reproduce.py'),
     'proof_sha256':sha(ROOT/'PROOF.md'),'rows':rows,'elapsed_seconds':time.monotonic()-start,
     'status':'T4 validated point computations; independent cross-lane reproduction pending'}
(ROOT/'verification/points.json').write_text(json.dumps(out,indent=2)+'\n')
print('seconds',out['elapsed_seconds'])

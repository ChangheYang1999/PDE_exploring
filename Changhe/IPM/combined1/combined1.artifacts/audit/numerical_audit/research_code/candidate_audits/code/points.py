"""Exact rational-point audit for a frozen candidate."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
import json,sys,time
from flint import arb,ctx
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/point_witness/code'))
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
from cartesian import CartesianJet
from radial import Radial
BASE=ROOT/'research/candidate_audits'
def run(name,x='3/7',y='3/16'):
 ctx.prec=1024;start=time.monotonic();p=BASE/f'data/{name}/canonical.json'
 model=Radial(p);f=CartesianJet(p,x,y).fields();other=model.evaluate(x,y)
 checks={k:bool(v.overlaps(other[k])) for k,v in f.items() if k in other};assert all(checks.values())
 F=abs(f['residual']);V=f['velocity_norm'];D=f['gradient_norm'];rows=[]
 balls=[('A2-Db',arb(1)/262144,arb(1)/65536),('FW-T-TB-rebal-v1',arb(1)/65536,arb(3)/32768),
        ('FW-T-TB-sharp-v1',arb(1)/8192,arb(43)/50000),('T4-019-no-H',arb(1)/131072,arb(1)/16384),
        ('T4-graded-rational-box-1',arb(1)/50000,((arb(1)/5000)**2+2*(arb(1)/3000000)**2+(arb(1)/50000000)**2).sqrt())]
 for label,s,r in balls:
  C0=1/(4*arb.pi()*(1+s)).sqrt();C1=1/(8*arb.pi()*s*(1+s)).sqrt()
  A=C1*V+C0*(1+D);B=C0*C1;upper=r*A+B*r*r;gap=F-upper
  root=2*F/(A+(A*A+4*B*F).sqrt())
  rows.append({'framework':label,'s':s.str(50),'radius':r.str(50),'necessary_upper':upper.str(75),'gap':gap.str(75),'strict_positive_gap':bool(gap>0),'necessary_H2s_radius_lower':root.str(75)})
  print(label,'gap',gap.str(25),flush=True)
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'canonical_sha256':sha256(p.read_bytes()).hexdigest(),
      'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':ctx.prec,'point':[x,y],
      'fields':{k:v.str(80) for k,v in f.items()},'radial_fourier_overlap':checks,'ball_exclusions':rows,'elapsed_seconds':time.monotonic()-start}
 (BASE/f'verification/{name}_point.json').write_text(json.dumps(out,indent=2)+'\n')
 print('F',f['residual'].str(35),'seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':run(*sys.argv[1:])

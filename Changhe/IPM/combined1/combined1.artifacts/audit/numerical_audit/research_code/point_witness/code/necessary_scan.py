"""Finite rational-point lower bounds for the necessary H^(2+s) correction size."""
from pathlib import Path
from datetime import datetime,timezone
from hashlib import sha256
from fractions import Fraction as Q
import json,sys,time
from flint import arb,arb_poly,acb,ctx,fmpq_poly
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT/'research/radial_fourier/code'))
sys.path.insert(0,str(ROOT/'research/background_points/code'))
from radial import Radial,ar
from cartesian import CartesianJet
from signed_scan import source

def run(name):
 ctx.prec=512;start=time.monotonic();p=source(name);model=Radial(p);U=fmpq_poly([1,-1]);funcs={}
 for key in ('rho','u1','u2','rho_x','rho_y'):
  A,d,kind=model.fields[key]
  funcs[key]=([(j,n,arb_poly([ar(v) for v in P]),arb_poly([ar(v) for v in P(U)])) for (j,n),P in A.items()],d,kind)
 maxn=max(n for A,d,k in funcs.values() for j,n,P,P1 in A)
 points=set()
 for i in range(-4,7):
  for multiplier in (Q(1),Q(3,2)):
   scale=Q(2)**i*multiplier;points.add((Q(0),scale))
   for slope in (Q(1,8),Q(1,4),Q(1,2),Q(1),Q(2),Q(4),Q(8)):points.add((scale,scale*slope))
 ss=(Q(1,2**18),Q(1,2**17),Q(1,2**16),Q(5,2**18),Q(1,2**13))
 rows=[];best={}
 for x,y in sorted(points):
  xa=arb(x.numerator)/x.denominator;ya=arb(y.numerator)/y.denominator;r2=xa*xa+ya*ya;r=r2.sqrt();R=1+r2;t=r2/R;u=1/R
  z=acb(xa/r,ya/r);powers=[acb(1)]
  for n in range(maxn):powers.append(powers[-1]*z)
  rp={j:R**ar(exp) for j,exp in model.p.items()};rd={d:r**(-d) for d in (3,4)};v={}
  for key,(A,d,kind) in funcs.items():
   v[key]=sum((rp[j]*rd[d]*(P(t) if t<arb('0.5') else P1(u))*(powers[n].real if kind=='c' else powers[n].imag) for j,n,P,P1 in A),arb(0))
  vx=ar(model.c)*xa+v['u1'];vy=ar(model.c)*ya+v['u2'];F=vx*v['rho_x']+vy*v['rho_y']-v['rho']
  V=(vx*vx+vy*vy).sqrt();g=(v['rho_x']**2+v['rho_y']**2).sqrt();symmetry=x==0 and y>=Q(1,2)
  row={'point':[str(x),str(y)],'F':F.str(65),'velocity_norm':V.str(65),'gradient_norm':g.str(65),'axis_symmetry':symmetry,'required':{}}
  for s in ss:
   sa=arb(s.numerator)/s.denominator;C0=1/(4*arb.pi()*(1+sa)).sqrt();C1=1/((16 if symmetry else 8)*arb.pi()*sa*(1+sa)).sqrt()
   A=C1*V+C0*(1+g);B=C0*C1;root=2*abs(F)/(A+(A*A+4*B*abs(F)).sqrt())
   row['required'][str(s)]=root.str(60)
   if str(s) not in best or root>arb(best[str(s)]['required'][str(s)]):best[str(s)]=row
  rows.append(row)
 for row in best.values():
  jet=CartesianJet(p,*row['point']);jf=jet.fields()
  assert jf['residual'].overlaps(arb(row['F']))
  assert jf['velocity_norm'].overlaps(arb(row['velocity_norm']))
  assert jf['gradient_norm'].overlaps(arb(row['gradient_norm']))
 out={'utc':datetime.now(timezone.utc).isoformat(timespec='seconds'),'candidate':name,'source_sha256':sha256(p.read_bytes()).hexdigest(),
  'code_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),'precision_bits':ctx.prec,'point_count':len(points),'best':best,'rows':rows,
  'cartesian_best_overlaps':True,'elapsed_seconds':time.monotonic()-start,'scope':'Finite-scan lower bounds only; no claim of spatial optimality.'}
 dest=ROOT/f'research/point_witness/verification/{name}_necessary_scan.json';dest.write_text(json.dumps(out,indent=2)+'\n')
 for s,row in best.items():print(name,s,row['point'],row['required'][s],flush=True)
 print('seconds',time.monotonic()-start,flush=True)
if __name__=='__main__':
 for name in sys.argv[1:]:run(name)
